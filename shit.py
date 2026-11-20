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


def dyinpsect() : 
    pass

def dyrefine(untypedAPI,unit_test_set) : 
    pass
def findTypeAPI(filePath, test=None) :  
    testPath =  "./cpython/Lib/test/test_colorsys.py"  
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
    print(result['functions'])

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

    print(f"inputType  :  {inputType}")
    print(f"outputType  :  {outputType}")

    # Typed API description
    print(result)

    return result

def phase2() : 
    # L1 fuzzing

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

filePath = "./cpython/Lib/colorsys.py"
#testPath =  "./cpython/Lib/test/test_colorsys.py"


#print(code)
phase1(code,filePath)
