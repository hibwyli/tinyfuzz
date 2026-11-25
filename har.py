import pickle
import ast 
from pathlib import Path
from ipaddress import IPv4Network

module_path = str(Path(__file__).resolve().parent / "cpython/Lib/ipaddress.py")
constructor = (module_path, "IPv4Interface.__init__")
equals = (module_path, "IPv4Interface.__eq__")
network = (module_path, "ip_network")
interface = (module_path, "ip_interface")
mixed_key = (module_path, "get_mixed_type_key")
address = IPv4Network("0.0.0.1/32")

last_var = None
chain = {
    "apis": [constructor, equals, network, interface, mixed_key],
    "steps": [
        (4, {"source": constructor, "target": equals, "parent_class": "IPv4Interface"}),
        (2, {"source": equals, "target": network, "target_arg": 1}),
        (3, {"source": network, "target": interface, "source_arg": 0, "target_arg": 0}),
        (1, {"source": interface, "target": mixed_key, "unpack_return": False}),
    ],
    "fuzz_point": {
        "api_id": equals,
        "arg_index": 0,
        "arg_name": "other",
        "input_type": "int",
    },
    "object_pool": {"IPv4Network": address},
    "valid": True,
    "resolved_args": [
        {
            "api_id": constructor,
            "arg_index": 0,
            "arg_name": "address",
            "value": "192.0.2.1/24",
            "input_type": "str",
        },
        {
            "api_id": network,
            "arg_index": 0,
            "arg_name": "address",
            "value": address,
            "input_type": "IPv4Network",
        },
    ],
}


moduleName = "ipaddress"
importsList =  ['functools', 're', 'pickle']
importsList.append(moduleName)
# apidesc['imports'] + filename module
  
apisec = None
with open('apisec.json','rb') as f : 
    apisec = pickle.loads(f.read())

steps = chain['steps']
resolved_args = chain['resolved_args']
obj_pool = chain['object_pool']
fuzzPoint = chain['fuzz_point']

 
print(chain)
print("Resolved args :" , resolved_args) 
print("Object pool :" , obj_pool) 
harness =  "" 

tree = ast.Module(body=[], type_ignores=[])

# Build import
for module in importsList:  
    tree.body.append(
        ast.Import(
            names=[ast.alias(name=module, asname=None)]
        )

    )

class_method = apisec['classes']


def value_to_ast(value):
    if value is None or isinstance(value, (bool, int, float, complex, str, bytes)):
        return ast.Constant(value=value)
    if isinstance(value, list):
        return ast.List(
            elts=[value_to_ast(item) for item in value],
            ctx=ast.Load(),
        )
    if isinstance(value, tuple):
        return ast.Tuple(
            elts=[value_to_ast(item) for item in value],
            ctx=ast.Load(),
        )
    if isinstance(value, dict):
        return ast.Dict(
            keys=[value_to_ast(key) for key in value],
            values=[value_to_ast(item) for item in value.values()],
        )
    if isinstance(value, set):
        return ast.Set(elts=[value_to_ast(item) for item in value])

    return ast.Call(
        func=ast.Attribute(
            value=ast.Name(id="pickle", ctx=ast.Load()),
            attr="loads",
            ctx=ast.Load(),
        ),
        args=[ast.Constant(value=pickle.dumps(value))],
        keywords=[],
    )


def build_base_args(api_id):
    args = {}

    for arg in resolved_args:
        if tuple(arg["api_id"]) == tuple(api_id):
            args[arg["arg_index"]] = value_to_ast(arg["value"])

    if tuple(fuzzPoint["api_id"]) == tuple(api_id):
        args[fuzzPoint["arg_index"]] = ast.Name(
            id="fuzz_input",
            ctx=ast.Load(),
        )

    return args


def materialize_args(args, counter):
    for index in sorted(args):
        node = args[index]
        if isinstance(node, ast.Name):
            continue

        variable_name = f"arg{counter}"
        counter += 1
        tree.body.append(
            ast.Assign(
                targets=[ast.Name(id=variable_name, ctx=ast.Store())],
                value=node,
            )
        )
        args[index] = ast.Name(id=variable_name, ctx=ast.Load())

    return counter


def find_api(api_id):
    for api in apisec["functions"]:
        if tuple(api["api_id"]) == tuple(api_id):
            return api

    for cls in apisec["classes"]:
        for api in cls.get("functions", []):
            if tuple(api["api_id"]) == tuple(api_id):
                return api

    raise ValueError(f"Unknown API: {api_id}")


# Generate the first API once. Every step below only generates its target.
first_api = chain["apis"][0]
current_args = build_base_args(first_api)
argument_counter = materialize_args(current_args, 0)
first_args_ast = [current_args[index] for index in sorted(current_args)]

if first_api[1].endswith(".__init__"):
    class_name = first_api[1].rsplit(".", 1)[0]
    current_result_var = "obj0"
    current_receiver_var = current_result_var
    result_counter = 0

    tree.body.append(
        ast.Assign(
            targets=[ast.Name(id=current_result_var, ctx=ast.Store())],
            value=ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id=moduleName, ctx=ast.Load()),
                    attr=class_name,
                    ctx=ast.Load(),
                ),
                args=first_args_ast,
                keywords=[],
            ),
        )
    )
else:
    current_result_var = "result0"
    current_receiver_var = None
    result_counter = 1

    tree.body.append(
        ast.Assign(
            targets=[ast.Name(id=current_result_var, ctx=ast.Store())],
            value=ast.Call(
                func=ast.Attribute(
                    value=ast.Name(id=moduleName, ctx=ast.Load()),
                    attr=first_api[1],
                    ctx=ast.Load(),
                ),
                args=first_args_ast,
                keywords=[],
            ),
        )
    )

last_var = current_result_var

# Maybe we will use AST 
for step in steps : 
    print(step)
    type =  step[0]
    source = step[1]['source']
    target_arg = step[1].get('target_arg')
    parent_class = step[1].get('parent_class') 

    print("Parent  class : " , parent_class)

    api_id = source[0]


    func_name = source[1]


    res = None

    class_method = []
    if parent_class :  
        classes = apisec['classes']
        
    for item in apisec['functions']: 
        if item.get("api_id") == source:
            res =  item 
    if not res  : 
        #print(classes[0])
        results = []

        for cls in apisec['classes']:
                for func in cls.get("functions", []):
                    if func.get("api_id") == source:
                        res = func
                        continue
#    print("Res :  "  , res)

    # Now build the ast body
    target = step[1]['target']
    print(parent_class)

    print(f"Case : {type}")
    # Loop and put those resolved args into those point  . 
    match type: 

        case 1 :
            source_result = ast.Name(id=current_result_var, ctx=ast.Load())
            unpack_return = step[1]["unpack_return"]

            if unpack_return:
                target_args_ast = [
                    ast.Starred(value=source_result, ctx=ast.Load())
                ]
                target_desc = find_api(target)
                target_args = {
                    index: ast.Subscript(
                        value=ast.Name(id=current_result_var, ctx=ast.Load()),
                        slice=ast.Constant(value=index),
                        ctx=ast.Load(),
                    )
                    for index in range(len(target_desc["params"]))
                }
            else:
                target_args_ast = [source_result]
                target_args = {0: source_result}

            target_func = ast.Attribute(
                value=ast.Name(id=moduleName, ctx=ast.Load()),
                attr=target[1].rsplit(".", 1)[-1],
                ctx=ast.Load(),
            )
            result_name = f"result{result_counter}"
            result_counter += 1
            tree.body.append(
                ast.Assign(
                    targets=[ast.Name(id=result_name, ctx=ast.Store())],
                    value=ast.Call(
                        func=target_func,
                        args=target_args_ast,
                        keywords=[],
                    ),
                )
            )

            current_result_var = result_name
            current_receiver_var = None
            current_args = target_args
            last_var = current_result_var
        case 2 :   
            target_args = build_base_args(target)
            target_args[target_arg] = ast.Name(
                id=current_result_var,
                ctx=ast.Load(),
            )
            argument_counter = materialize_args(target_args, argument_counter)
            target_args_ast = [target_args[index] for index in sorted(target_args)]

            target_func = ast.Attribute(
                value=ast.Name(id=moduleName, ctx=ast.Load()),
                attr=target[1].rsplit(".", 1)[-1],
                ctx=ast.Load(),
            )

            result_name = f"result{result_counter}"
            result_counter += 1
            tree.body.append(
                ast.Assign(
                    targets=[ast.Name(id=result_name, ctx=ast.Store())],
                    value=ast.Call(
                        func=target_func,
                        args=target_args_ast,
                        keywords=[],
                    ),
                )
            )

            current_result_var = result_name
            current_receiver_var = None
            current_args = target_args
            last_var = current_result_var
        case 3 :
            source_arg = step[1]["source_arg"]
            if source_arg not in current_args:
                raise ValueError(
                    f"Source argument {source_arg} is unavailable for {source}"
                )

            target_args = build_base_args(target)
            target_args[target_arg] = current_args[source_arg]
            argument_counter = materialize_args(target_args, argument_counter)
            target_args_ast = [target_args[index] for index in sorted(target_args)]

            target_func = ast.Attribute(
                value=ast.Name(id=moduleName, ctx=ast.Load()),
                attr=target[1].rsplit(".", 1)[-1],
                ctx=ast.Load(),
            )
            result_name = f"result{result_counter}"
            result_counter += 1
            tree.body.append(
                ast.Assign(
                    targets=[ast.Name(id=result_name, ctx=ast.Store())],
                    value=ast.Call(
                        func=target_func,
                        args=target_args_ast,
                        keywords=[],
                    ),
                )
            )

            current_result_var = result_name
            current_receiver_var = None
            current_args = target_args
            last_var = current_result_var
        case 4  :
            print("================HANDLE CASE 4 ===========================")
            target_args = build_base_args(target)
            argument_counter = materialize_args(target_args, argument_counter)
            target_args_ast = [target_args[index] for index in sorted(target_args)]
            method_name = target[1].rsplit(".",1)[-1]
            target_func = ast.Attribute(
                value=ast.Name(id=current_receiver_var, ctx=ast.Load()),
                attr=method_name,
                ctx=ast.Load(),
            )

            result_name = f"result{result_counter}"
            result_counter += 1
            tree.body.append(
                ast.Assign(
                    targets=[ast.Name(id=result_name, ctx=ast.Store())],
                    value=ast.Call(
                        func=target_func,
                        args=target_args_ast,
                        keywords=[],
                    ),
                )
                )

            current_result_var = result_name
            current_args = target_args
            last_var = current_result_var
        case _  : 

            print("Who the fuck are you ?")  
            exit(0)




 
 

 

 
    #tree.body.append()




print("=======================================")
ast.fix_missing_locations(tree)
print(ast.unparse(tree))

print("=======================================")
print(apisec['functions'][0])



# print(apisec['classes'])
