
import ast

tree = ast.Module(
    body=[
        ast.Assign(
            targets=[ast.Name(id="x", ctx=ast.Store())],
            value=ast.Constant(value=10)
        ),
        ast.Assign(
            targets=[ast.Name(id="y", ctx=ast.Store())],
            value=ast.Constant(value=20)
        ),
        ast.Expr(
            value=ast.Call(
                func=ast.Name(id="print", ctx=ast.Load()),
                args=[
                    ast.BinOp(
                        left=ast.Name(id="x", ctx=ast.Load()),
                        op=ast.Add(),
                        right=ast.Name(id="y", ctx=ast.Load())
                    )
                ],
                keywords=[]
            )
        )
    ],
    type_ignores=[]
)

tree = ast.fix_missing_locations(tree)


source = ast.unparse(tree)

print(source)