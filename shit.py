import ast 
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
            "methods" :[] 
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
            current_class["methods"].append(current_function)
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
    testPath =  "./cpython/Lib/test/test_quopri.py"  
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
        for method in cls["methods"]
    ]
    for api in apis:
        api["input_types"] = dict(inputType.get(api["api_id"], {}))
        api["output_types"] = outputType.get(api["api_id"], set())

    # Typed API description
    return result 

def phase2(apidesc) : 
    print(f"We have: {[x['name'] for x in apidesc['functions']]}")
    IMMUTABLE = {
    "int", "float", "complex", "bool",
    "str", "bytes", "tuple", "frozenset", "NoneType"
}

    # L1 fuzzing
    # We find  the input match output between functions

    # Call sequence mutation
    chains1 = []
    # Case 1 : B(A_output)
    for source in apidesc["functions"]:
        for output in source["output_types"]:
            outputs = output[1] if isinstance(output, tuple) else [output]

            for target in apidesc["functions"]:
                inputs = target["input_types"].values()

                if all(out in inp for out, inp in zip(outputs, inputs)):
                    chains1.append({"source" : source['name'],"target":target["name"]}) 
    # Case 2  : B(other_args, A_output)
    chains2 = []
    for source in apidesc["functions"]:
        for output in source["output_types"]:
            output_type = output[0] if isinstance(output, tuple) else output

            for target in apidesc["functions"]:
                for index, input_types in enumerate(target["input_types"].values()):
                    if output_type in input_types:
                        chains2.append({
                            "source": source["name"],
                            "target": target["name"],
                            "target_arg": index

                        })
    # Case 3 : Mutable arguments like a fucking list
    chains3 = []
    for source in apidesc["functions"]:
        for arg_index, types in enumerate(source["input_types"].values()):
            for input_type in types:
                if input_type not in IMMUTABLE:
                    for target in apidesc["functions"]:
                        if target["api_id"] == source["api_id"]:
                            continue

                        for target_index, target_types in enumerate(
                            target["input_types"].values()
                        ):
                            if input_type in target_types:
                                chains3.append({
                                    "source": source["name"],
                                    "source_arg": arg_index,
                                    "target": target["name"],
                                    "target_arg": target_index,
                                })
                            # mutable
    # Case 4 : shared link  , Class Object shit 
    print(apidesc['classes'])



#    print(chains3)

    pass

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
 
filePath = "./cpython/Lib/quopri.py"
#testPath =  "./cpython/Lib/test/test_colorsys.py"


#print(code)
apidesc =     phase1(code,filePath)
phase2(apidesc)

