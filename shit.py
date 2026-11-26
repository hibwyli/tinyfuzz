import ast 
import pickle 

import string 
import random
import sys
import json
import glob
import importlib.util
from re import findall
import sys
from pathlib import Path
from types import resolve_bases 

py_files = glob.glob('./cpython/**/*.py', recursive=True)
py_files = [x for x in py_files if "test" not in  x] 
print(len(py_files))
# We parse shit with ast 
all_apis = None

result =  {
    "imports" :[] , 
    "functions" :[] , 
    "classes" : []
}  

IMMUTABLE = {
    "int", "float", "complex", "bool",
    "str", "bytes", "tuple", "frozenset", "NoneType" , "BytesIO"
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
    testPath =  "./cpython/Lib/test/test_ipaddress.py"  
    cpython_lib = str(Path(testPath).resolve().parents[1])
    if cpython_lib not in sys.path:
        sys.path.append(cpython_lib)
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
    original_argv = sys.argv
    sys.argv = [sys.argv[0]]
    try: 
        exec(testCode, current_namespace, current_namespace)
    except SystemExit:
        pass
    finally:
        sys.settrace(None)
        sys.argv = original_argv

    inputs = current_namespace["input_types"]
    outputs = current_namespace["output_types"]
    values = current_namespace["arg_values"]
    return inputs, outputs, values


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

    inputType, outputType, argValues = findTypeAPI(filePath)

    apis = result["functions"] + [
        method
        for cls in result["classes"]
        for method in cls["functions"]
    ]
    for api in apis:
        api["input_types"] = dict(inputType.get(api["api_id"], {}))
        api["output_types"] = outputType.get(api["api_id"], set())
        api["input_values"] = dict(argValues.get(api["api_id"], {}))

    # Typed API description
    return result 

def buildChains(apidesc) : 
    global all_apis  

    functions = list(apidesc["functions"])

    methods =   []
    for cls in apidesc["classes"]:
        for method in cls["functions"]:
            method["parent_class"] = cls["name"]
            methods.append(method) 

    all_apis =  functions + methods

    data = None
    print('WTF : ' , sys.argv)
    if   len(sys.argv) > 1 and sys.argv[1] == "SHIT"  : 
        try :  
            with open("data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except : 
            pass

    if data : 
        return data

    print(f"We have: {[x['name'] for x in apidesc['functions']]}")
    # L1 fuzzing

    # We find  the input match output between functions

    # Call sequence mutation
    chains1 = []
    # Case 1 : B(A_output)
    for source in all_apis:
        for output in source["output_types"]:
            outputs = output[1] if isinstance(output, tuple) else [output]

            for target in all_apis:

                inputs = list(target["input_types"].values())
                if len(outputs) == len(inputs) and all(out in inp for out, inp in zip(outputs, inputs)):
                    chains1.append({
                        "source": source["api_id"],
                        "target": target["api_id"],
                        "unpack_return": isinstance(output, tuple),
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

    fuzz_input_types = {
        "bytes", "str", "IO", "BytesIO", "StringIO", "ANY",
        "int", "float", "bool",
    }
    fuzz_points = []
    for api in all_apis:
        for arg_index, arg_name in enumerate(api["params"]):
            for input_type in api["input_types"].get(arg_name, set()):
                if input_type in fuzz_input_types:
                    fuzz_points.append({
                        "api": api,
                        "arg_index": arg_index,
                        "arg_name": arg_name,
                        "input_type": input_type,
                    })

    def edge_signature(case_number, link):
        return (
            case_number,
            link["source"],
            link["target"],
            link.get("source_arg"),
            link.get("target_arg"),
            link.get("parent_class"),
            link.get("unpack_return"),
        )

    queue = []
    seen_chains = set()
    max_chains = 1000
    for fuzz_point in fuzz_points:
        if len(queue) >= max_chains:
            break

        entrypoint = fuzz_point["api"]
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
            fuzz_point["arg_index"],
            fuzz_point["input_type"],
            tuple(edge_signature(case, link) for case, link in steps),
        )
        if signature not in seen_chains:
            seen_chains.add(signature)
            queue.append({
                "apis": apis,
                "steps": steps,
                "fuzz_point": {
                    "api_id": entrypoint["api_id"],
                    "arg_index": fuzz_point["arg_index"],
                    "arg_name": fuzz_point["arg_name"],
                    "input_type": fuzz_point["input_type"],
                },
            })

    max_chain_length = 5
    full_chains = list(queue)
    queue_index = 0
    while queue_index < len(queue) and len(full_chains) < max_chains:
        chain = queue[queue_index]
        queue_index += 1

        if len(chain["apis"]) >= max_chain_length:
            continue

        current_api = chain["apis"][-1]
        for case_number, link in outgoing_links.get(current_api, []):
            if len(full_chains) >= max_chains:
                break

            target = link["target"]
            if target in chain["apis"]:
                continue

            new_apis = chain["apis"] + [target]
            new_steps = chain["steps"] + [(case_number, link)]
            signature = (
                tuple(new_apis),
                chain["fuzz_point"]["arg_index"],
                chain["fuzz_point"]["input_type"],
                tuple(
                    edge_signature(case, step_link)
                    for case, step_link in new_steps
                ),
            )
            if signature in seen_chains:
                continue

            seen_chains.add(signature)
            new_chain = {
                "apis": new_apis,
                "steps": new_steps,
                "fuzz_point": chain["fuzz_point"],
            }
            full_chains.append(new_chain)
            queue.append(new_chain)

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(full_chains[:1000], f, indent=4)
    return full_chains


def  arg_resolve(args) : 
    # What problem this solving ? 

    # remove dup
    return []

def random_value(type_name):
    if type_name == "bool":
        return random.choice([True, False])

    if type_name == "int":
        return random.randint(-1000, 1000)

    if type_name == "float":
        return random.uniform(-1000, 1000)

    if type_name == "str":
        return "".join(
            random.choices(string.printable, k=random.randint(0, 32))
        )

    if type_name == "bytes":
        return random.randbytes(random.randint(0, 32))

    if type_name == "NoneType":
        return None

    if type_name == "list":
        element_type = random.choice(["bool", "int", "float", "str", "bytes"])
        return [
            random_value(element_type)
            for _ in range(random.randint(1, 5))
        ]

    if type_name == "tuple":
        element_type = random.choice(["bool", "int", "float", "str", "bytes"])
        return tuple(
            random_value(element_type)
            for _ in range(random.randint(1, 5))
        )

    if type_name == "dict":
        key_type = random.choice(["bool", "int", "float", "str", "bytes"])
        value_type = random.choice(["bool", "int", "float", "str", "bytes"])
        return {
            random_value(key_type): random_value(value_type)
        }

    if type_name == "set":
        return set()

    return None

def  findEmtpyArgs(chains) : 
    #for chain in chains : 

        #if len(chain['steps']) == 3  : 
        #    print(chains.index(chain))
        #    exit()

# We check this chain only , later will loop all
    for  chain in chains : 
        # Find fuzzing point first
        #chain = chains[866]
        fuzzPoint = chain['fuzz_point']
        apis = chain['apis'] 

        #print(f"{len(chain['steps'])} steps , fuzz point at  : { fuzzPoint}")
        paramsPerStep = []
        for api in apis : 
            paramsPerStep.append([x for x in all_apis if x["api_id"] == tuple(api)][0]['params'])

        # Get provided input from chain
        provided_args  = set()
        for type , link in  chain['steps'] : 
            #print(f"Case {type} {link}")
            match type : 
                case 1:
                    provided_args.add((tuple(link["target"]), "ALL"))
                case  2 :
                    provided_args.add((tuple(link["target"]),link["target_arg"]))
                case  3:
                    provided_args.add((tuple(link["target"]),link["target_arg"]))
                case _ : 
                    pass

        #print(f"Provided  args   :  {provided_args}")
        unresolveArgs = []

        for api, params in zip(apis, paramsPerStep): 
            # This look up consume so large flops  ,  which is better way ? 
            api_desc = next(x for x in all_apis if x["api_id"] == tuple(api))
            default_start = len(params) - len(api_desc["defaults"])

            #print("API DESC : " , api_desc)
            for index, param in enumerate(params):
                # remove fuzz point 
                if (
                    tuple(api) == tuple(fuzzPoint["api_id"])
                    and index == fuzzPoint["arg_index"]
                ):
                    continue
                # Remove  provided args
                if (
                    (tuple(api), "ALL") in provided_args
                    or (tuple(api), index) in provided_args
                ):
                   continue
                # Use default 
                has_default = index >= default_start
                if has_default: 
                    continue

                # remove dependency supplied point
                unresolveArgs.append({
                    "api_id": tuple(api),
                    "arg_index": index,
                    "arg_name": param,
                })

        #if len(unresolveArgs) > 0 : 
            #print("Unresolved : " , unresolveArgs)
            #print("FOUND IT at index :  " , chains.index(chain))
            #exit(0)


        # Resolve args here
        #print("Provided args : " , provided_args)
        #print("Unresolved args: ",  unresolveArgs) 

        # Store object 
        object_pool = chain.setdefault("object_pool", {})
        constructor_failed = False

        for arg in unresolveArgs:
            api_desc = next(x for x in all_apis if x["api_id"] == tuple(arg["api_id"]))
            observed = api_desc.get("input_values", {}).get(arg["arg_name"], [])
            if observed and random.random() < 0.5:
                arg["value"] = random.choice(observed)
                arg["input_type"] = arg["value"].__class__.__name__
                continue

            input_types = api_desc["input_types"].get(arg["arg_name"], set())

            library_classes = {cl["name"] for cl in apidesc["classes"]}
            if input_types:
                library_candidates = input_types & library_classes
                selected_type = (
                    next(iter(library_candidates))
                    if library_candidates
                    else random.choice(tuple(input_types))
                )
            else:
                fallback_types = {
                    "bool", "int", "float", "str", "bytes", "NoneType",
                    "list", "tuple", "dict", "set",
                } | library_classes
                selected_type = random.choice(tuple(fallback_types))

            if selected_type in library_classes:
                if selected_type in object_pool : 
                    # Reuse object
                    arg["input_type"] = selected_type
                    arg["value"] = object_pool[selected_type]
                    continue 
                    


                # We find the shit have 2 steps : 
                print("FOUND IT at index :  " , chains.index(chain))
                print("TYPE : " , selected_type)
                print("STEPS  : " , len(chain['steps']))
                print("Chain :" ,  chain)
                # exit(0)  
                #  LIbrary type , have object previous -> reuse  else call constructor  
                # So we need a way to detect if the previous chain have a object right ? 
                # Basically when the first chain will also meet a class and call constructor
                # Just create a handle type here

                # Now construct the object
                class_desc = next(
                    cl for cl in apidesc["classes"]
                    if cl["name"] == selected_type
                )

                constructor = next(
                    fn for fn in class_desc["functions"]
                    if fn["name"] == "__init__"
                )
                constructor_values = []
                default_start = (len(constructor['params']) - len(constructor['defaults'])) 
                for index, param_name in enumerate(constructor['params'])  :
                    if index >= default_start:
                        continue

                    possible_types = constructor["input_types"].get(
                        param_name, set()
                    )

                    if (
                        selected_type in {
                            "IPv4Address", "IPv6Address",
                            "IPv4Interface", "IPv6Interface",
                            "IPv4Network", "IPv6Network",
                        }
                        and param_name == "address"
                        and "int" in possible_types
                    ):
                        constructor_values.append(random.randint(0, 5))
                    else:
                        param_type = random.choice(tuple(possible_types))
                        constructor_values.append(random_value(param_type))


                module_name = Path(arg["api_id"][0]).stem
                module = sys.modules[module_name]
                class_object = getattr(module, selected_type)
                try:
                    obj = class_object(*constructor_values)
                except Exception as error:
                    chain["valid"] = False
                    chain["failure"] = {
                        "stage": "constructor",
                        "type": selected_type,
                        "error": repr(error),
                    }
                    constructor_failed = True
                    break

                object_pool[selected_type] = obj
                arg["value"] = obj
                arg["input_type"] = selected_type
                continue
            else : 
                arg["input_type"] = selected_type
                arg["value"] = random_value(selected_type)

        if constructor_failed:
            print("\nInvalid chain : ", chain["failure"])
            continue

        chain["valid"] = True
        chain["resolved_args"] = unresolveArgs
        print("\nResolved chain : " , chain)


def chain_to_source(chain, module_name):
    resolved_args = chain.get("resolved_args", [])
    fuzz_point = chain["fuzz_point"]
    tree = ast.Module(
        body=[ast.Import(names=[ast.alias(name=module_name)])],
        type_ignores=[],
    )
    argument_counter = 0
    result_counter = 0
    receiver_counter = 0
    receivers = {}

    def get_api(api_id):
        return next(
            api for api in all_apis
            if tuple(api["api_id"]) == tuple(api_id)
        )

    def build_args(api_id):
        args = {
            arg["arg_index"]: ast.Constant(value=arg["value"])
            for arg in resolved_args
            if tuple(arg["api_id"]) == tuple(api_id)
        }
        if tuple(fuzz_point["api_id"]) == tuple(api_id):
            args[fuzz_point["arg_index"]] = ast.Name(
                id="fuzz_input",
                ctx=ast.Load(),
            )
        return args

    def materialize_args(args):
        nonlocal argument_counter
        for index in sorted(args):
            if isinstance(args[index], ast.Name):
                continue
            variable_name = f"arg{argument_counter}"
            argument_counter += 1
            tree.body.append(
                ast.Assign(
                    targets=[ast.Name(id=variable_name, ctx=ast.Store())],
                    value=args[index],
                )
            )
            args[index] = ast.Name(id=variable_name, ctx=ast.Load())

    def get_receiver(parent_class):
        nonlocal receiver_counter
        if parent_class in receivers:
            return receivers[parent_class]

        variable_name = f"obj{receiver_counter}"
        receiver_counter += 1
        if parent_class in chain.get("object_pool", {}):
            value = ast.Constant(value=chain["object_pool"][parent_class])
        else:
            value = ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id=module_name, ctx=ast.Load()),
                    attr=parent_class,
                    ctx=ast.Load(),
                ),
                args=[],
                keywords=[],
            )
        tree.body.append(
            ast.Assign(
                targets=[ast.Name(id=variable_name, ctx=ast.Store())],
                value=value,
            )
        )
        receivers[parent_class] = variable_name
        return variable_name

    first_api = chain["apis"][0]
    current_args = build_args(first_api)
    materialize_args(current_args)
    first_args = [current_args[index] for index in sorted(current_args)]

    if first_api[1].endswith(".__init__"):
        current_result = "obj0"
        current_receiver = current_result
        receiver_counter = 1
        receivers[first_api[1].rsplit(".", 1)[0]] = current_receiver
        first_func = ast.Attribute(
            value=ast.Name(id=module_name, ctx=ast.Load()),
            attr=first_api[1].rsplit(".", 1)[0],
            ctx=ast.Load(),
        )
    else:
        current_result = "result0"
        current_receiver = None
        result_counter = 1
        first_func = ast.Attribute(
            value=ast.Name(id=module_name, ctx=ast.Load()),
            attr=first_api[1],
            ctx=ast.Load(),
        )

    tree.body.append(
        ast.Assign(
            targets=[ast.Name(id=current_result, ctx=ast.Store())],
            value=ast.Call(func=first_func, args=first_args, keywords=[]),
        )
    )

    for case_type, link in chain["steps"]:
        target = link["target"]
        target_desc = get_api(target)

        if case_type == 1:
            source_result = ast.Name(id=current_result, ctx=ast.Load())
            if link.get("unpack_return", False):
                call_args = [ast.Starred(value=source_result, ctx=ast.Load())]
                target_args = {
                    index: ast.Subscript(
                        value=ast.Name(id=current_result, ctx=ast.Load()),
                        slice=ast.Constant(value=index),
                        ctx=ast.Load(),
                    )
                    for index in range(len(target_desc["params"]))
                }
            else:
                call_args = [source_result]
                target_args = {0: source_result}
        else:
            target_args = build_args(target)
            if case_type == 2:
                target_args[link["target_arg"]] = ast.Name(
                    id=current_result,
                    ctx=ast.Load(),
                )
            elif case_type == 3:
                target_args[link["target_arg"]] = current_args[link["source_arg"]]
            elif case_type != 4:
                raise ValueError(f"Unknown chain case: {case_type}")
            materialize_args(target_args)
            call_args = [target_args[index] for index in sorted(target_args)]

        target_parent = target_desc.get("parent_class")
        if case_type == 4 or target_parent:
            receiver = current_receiver
            if receiver is None or case_type != 4:
                receiver = get_receiver(target_parent or link["parent_class"])
            target_func = ast.Attribute(
                value=ast.Name(id=receiver, ctx=ast.Load()),
                attr=target[1].rsplit(".", 1)[-1],
                ctx=ast.Load(),
            )
            current_receiver = receiver
        else:
            target_func = ast.Attribute(
                value=ast.Name(id=module_name, ctx=ast.Load()),
                attr=target[1].rsplit(".", 1)[-1],
                ctx=ast.Load(),
            )
            current_receiver = None

        result_name = f"result{result_counter}"
        result_counter += 1
        tree.body.append(
            ast.Assign(
                targets=[ast.Name(id=result_name, ctx=ast.Store())],
                value=ast.Call(func=target_func, args=call_args, keywords=[]),
            )
        )
        current_result = result_name
        current_args = target_args

    return ast.unparse(ast.fix_missing_locations(tree))


def write_harnesses(chains, module_name, output_path="harness.py"):
    harnesses = []
    for index, chain in enumerate(chains):
        try:
            source = chain_to_source(chain, module_name)
        except Exception as error:
            source = f"# Could not generate chain {index}: {error!r}"
        harnesses.append(f"# Chain {index}\n{source}")

    Path(output_path).write_text("\n\n===\n\n".join(harnesses))



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

filePath = "./cpython/Lib/ipaddress.py"
#testPath =  "./cpython/Lib/test/test_colorsys.py"


#print(code)
apidesc =     phase1(code,filePath)
with open('apisec.json','wb') as f  : 
    f.write(pickle.dumps(apidesc))
print(apidesc['imports']) 
full_chains = buildChains(apidesc)
args = findEmtpyArgs(full_chains) 
write_harnesses(full_chains, Path(filePath).stem)


# Get the longest chains ? 

max_index = max(
    range(len(full_chains)),
    key=lambda i: len(full_chains[i].get("steps", []))
)

print("Max index:", max_index)
print("Max steps:", len(full_chains[max_index].get("steps", [])))
print(f"testing chain : " , pickle.dumps(full_chains[max_index]))
