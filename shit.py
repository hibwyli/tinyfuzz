import ast 
import json
import glob
import importlib.util
import sys
from pathlib import Path 

py_files = glob.glob('./cpython/**/*.py', recursive=True)
py_files = [x for x in py_files if "test" not in  x] 
print(len(py_files))
# We parse shit with ast 

result =  {
    "imports" :[] , 
    "functions" :[] , 
    "classes" : []
}  

def loop(node,current_class=None,current_function=None,filePath=None) : 
 
    if  isinstance(node,ast.ClassDef) : 
        if current_function is not None  : 
            return

        current_class =  {
            "name" :  node.name ,  
            "bases" : [ast.unparse(x) for x in node.bases]  , 
            "functions" :[] 
        }
        result["classes"].append(current_class)  
    elif  isinstance(node,  (ast.FunctionDef,ast.AsyncFunctionDef)) : 
        for x  in  node.args.defaults:  
            print(f"SHIT : {x}") 
        if current_function is not None : 

            return
        #  Make an id for function name

        if current_class:
            qualname = f"{current_class['name']}.{node.name}"
        else:
            qualname = node.name

        current_function =  {
            "name": node.name,
            "qualname": qualname,
            "api_id": (
                filePath,
                qualname
            ),
            "params"  :[x.arg for x in (node.args.posonlyargs + node.args.args + node.args.kwonlyargs) if x.arg !="self"]     , 
            "defaults" : [ 
                ast.unparse(x) for x in node.args.defaults
            ]  , 
            "returns" : [] , 
            "exceptions" : []  
        }
        if current_class : 
            current_class["functions"].append(current_function)
        else : 
            result['functions'].append(current_function)

    elif isinstance(node,ast.Return) and current_function : 
        value = ast.unparse(node.value) if node.value else None
        current_function['returns'].append(value)

    elif isinstance(node,ast.Raise) and current_function : 
        value = ast.unparse(node.exc) if node.exc else "re-raise"
        current_function["exceptions"].append(value)

    elif isinstance(node,ast.ExceptHandler) and current_function : 
        if node.type : 
            current_function['exceptions'].append(
                ast.unparse(node.type)) 

    elif isinstance(node,ast.Import) : 
        result["imports"] += [x.name for x in node.names]

    elif isinstance(node,ast.ImportFrom) : 
        result['imports'].append(node.module) 

    for child in ast.iter_child_nodes(node) : 
        loop(child,current_class,current_function,filePath)

def findTypeAPI(filePath, test=None) :  
    testPath =  "./cpython/Lib/test/test_xdrlib.py"  
    tracerCode = open("tracer.py").read()
    testCode = open(testPath).read()

    current_namespace = globals()
    current_namespace["TRACE_TARGET_FILE"] = str(Path(filePath).resolve())

    module_name = Path(filePath).stem
    spec = importlib.util.spec_from_file_location(module_name, filePath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    exec(tracerCode, current_namespace, current_namespace)
    try:
        exec(testCode, current_namespace, current_namespace)
    except SystemExit:
        pass
    finally:
        sys.settrace(None)

    inputs = current_namespace["input_types"]
    outputs = current_namespace["output_types"]
    return inputs, outputs


def phase1(code,filePath) : 
    code = open(filePath,'r').read()
    result["imports"].clear()
    result["functions"].clear()
    result["classes"].clear()
    # Static extraction  
    res = None 
    tree = ast.parse(code)

    loop(tree,filePath= str(Path(filePath).resolve()))
    print(len(py_files))
    # Dynamic refinement to convert from untyped into type
    # we use test file of that features to find the type of input and output
    #  Run this file with powerful of python tracer to get the type 

    inputType,outputType = findTypeAPI(filePath)

    apis = result["functions"] + [
        method
        for cls in result["classes"]
        for method in cls["functions"]
    ]
    for api in apis:
        api["input_types"] = dict(inputType.get(api["api_id"], {}))
        api["output_types"] = outputType.get(api["api_id"], set())

    # Typed API description
    return result 

def buildChains(apidesc) : 
    data = None
    try :  
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except : 
        pass

    if data : 
        return data

    print(f"We have: {[x['name'] for x in apidesc['functions']]}")
    IMMUTABLE = {
    "int", "float", "complex", "bool",
    "str", "bytes", "tuple", "frozenset", "NoneType"
}

    # L1 fuzzing
    # We find  the input match output between functions

    functions = list(apidesc["functions"])

    methods =   []
    for cls in apidesc["classes"]:
        for method in cls["functions"]:
            method["parent_class"] = cls["name"]
            methods.append(method) 

    all_apis =  functions + methods
    # Call sequence mutation
    chains1 = []
    # Case 1 : B(A_output)
    for source in all_apis:
        for output in source["output_types"]:
            outputs = output[1] if isinstance(output, tuple) else [output]

            for target in all_apis:
                inputs = target["input_types"].values()

                if all(out in inp for out, inp in zip(outputs, inputs)):
                    chains1.append({
                        "source": source["api_id"],
                        "target": target["api_id"],
                    }) 
    # Case 2  : B(other_args, A_output)
    chains2 = []
    for source in all_apis:
        for output in source["output_types"]:
            output_type = output[0] if isinstance(output, tuple) else output

            for target in all_apis:
                for index, input_types in enumerate(target["input_types"].values()):
                    if output_type in input_types:
                        chains2.append({
                            "source": source["api_id"],
                            "target": target["api_id"],
                            "target_arg": index

                        })
    # Case 3 : Mutable arguments like a fucking list
    chains3 = []
    for source in all_apis:
        for arg_index, types in enumerate(source["input_types"].values()):
            for input_type in types:
                if input_type not in IMMUTABLE:
                    for target in all_apis:
                        if target["api_id"] == source["api_id"]:
                            continue

                        for target_index, target_types in enumerate(
                            target["input_types"].values()
                        ):
                            if input_type in target_types:
                                chains3.append({
                                    "source": source["api_id"],
                                    "source_arg": arg_index,
                                    "target": target["api_id"],
                                    "target_arg": target_index,
                                })
                            # mutable
    # Case 4 : shared link  , Class Object shit 

    chain_shared_obj =  []
    for cl in apidesc['classes']: 
        res  = {}
        init_method = ([x  for x in cl['functions'] if x['name'] == '__init__' ] or [None] )[0] 
        nor_methods = ([x  for x in cl['functions'] if x['name'] != '__init__' ] or [None] )

        # link from init -> method
        for  nor in nor_methods :
            if nor is None:
                continue

            if init_method :  
                chain_shared_obj.append({
                    "parent_class" : cl['name'],
                    "source" : init_method['api_id'],
                    "target" : nor['api_id'],
                    })

            # link from method -> method
            for target_method in nor_methods:
                if target_method is None or target_method['api_id'] == nor['api_id']:
                    continue

                chain_shared_obj.append({
                    "parent_class" : cl['name'],
                    "source" : nor['api_id'],
                    "target" : target_method['api_id'],
                    })


    # Combine full chain with matching from with to
    # SLOP ALERT , I dont know dsa sorry guys
    link_groups = (chains1, chains2, chains3, chain_shared_obj)
    outgoing_links = {}
    for case_number, links in enumerate(link_groups, start=1):
        for link in links:
            outgoing_links.setdefault(link["source"], []).append(
                (case_number, link)
            )

    constructors = {}
    for cls in apidesc["classes"]:
        init_method = next(
            (func for func in cls["functions"] if func["name"] == "__init__"),
            None,
        )
        if init_method:
            constructors[cls["name"]] = init_method["api_id"]

    fuzz_input_types = {"bytes", "str", "IO", "BytesIO", "StringIO", "ANY"}
    entrypoints = []
    for api in all_apis:
        observed_input_types = {
            input_type
            for types in api["input_types"].values()
            for input_type in types
        }
        if observed_input_types & fuzz_input_types:
            entrypoints.append(api)

    def edge_signature(case_number, link):
        return (
            case_number,
            link["source"],
            link["target"],
            link.get("source_arg"),
            link.get("target_arg"),
            link.get("parent_class"),
        )

    queue = []
    seen_chains = set()
    for entrypoint in entrypoints:
        parent_class = entrypoint.get("parent_class")
        constructor = constructors.get(parent_class)

        if parent_class and entrypoint["name"] != "__init__":
            constructor_link = next(
                (
                    link
                    for link in chain_shared_obj
                    if link["source"] == constructor
                    and link["target"] == entrypoint["api_id"]
                ),
                None,
            )
            if constructor_link is None:
                continue
            apis = [constructor, entrypoint["api_id"]]
            steps = [(4, constructor_link)]
        else:
            apis = [entrypoint["api_id"]]
            steps = []

        signature = (
            tuple(apis),
            tuple(edge_signature(case, link) for case, link in steps),
        )
        if signature not in seen_chains:
            seen_chains.add(signature)
            queue.append({"apis": apis, "steps": steps})

    max_chain_length = 5
    full_chains = list(queue)
    queue_index = 0
    while queue_index < len(queue):
        chain = queue[queue_index]
        queue_index += 1

        if len(chain["apis"]) >= max_chain_length:
            continue

        current_api = chain["apis"][-1]
        for case_number, link in outgoing_links.get(current_api, []):
            target = link["target"]
            if target in chain["apis"]:
                continue

            new_apis = chain["apis"] + [target]
            new_steps = chain["steps"] + [(case_number, link)]
            signature = (
                tuple(new_apis),
                tuple(
                    edge_signature(case, step_link)
                    for case, step_link in new_steps
                ),
            )
            if signature in seen_chains:
                continue

            seen_chains.add(signature)
            new_chain = {"apis": new_apis, "steps": new_steps}
            full_chains.append(new_chain)
            queue.append(new_chain)

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(full_chains[:1000], f, indent=4)

    return full_chains


def  arg_resolve(chains) : 
    print_chain(chains[99])


    pass

def  print_chain(chain) : 
    print(chain)
    print("=============================================")
    index = 0
    step  = chain['steps'][0]
    OBJ_NAME = "obj"
    inclass = 0 
    for step in chain['steps'] :  
        
        type  = step[0]
        source = step[1]['source'][1]
        #target = step[1]['target'][1]
        if inclass : 
            source =source.replace(source.split(".")[0],OBJ_NAME) 

        print(type)  
        # we have wrong type here , which type should be  ? 
        match type : 
            case 1 :  
                print(f"{source}() -> " )
            case 2 : 
                print(f"{source}() -> "  )
            case 3 : 
                print(f"{source}() -> "  )
            case 4 :
                inclass = 1
                print(f"{OBJ_NAME} = {step[1]['target'][1]} -> ")
            case _   : 
                print(f"WHO ARE YOU ? ")


def phase3() : 
    # L2 fuzzing

    pass



code = """
class Calculator:
    def divide(self, a: int, b=1) -> float:
        if b == 0:
            raise ValueError("b cannot be zero")

        try:
            return a / b
        except TypeError:
            return  0


def greet(name="world"):
    return "Hello " + name
""" 
 
filePath = "./cpython/Lib/xdrlib.py"
#testPath =  "./cpython/Lib/test/test_colorsys.py"


#print(code)
apidesc =     phase1(code,filePath)
full_chains = buildChains(apidesc)
args = arg_resolve(full_chains) 


