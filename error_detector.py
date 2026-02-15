import ast


class ErrorFinder(ast.NodeVisitor):
    def __init__(self):
        self.var_created = set()
        self.var_used = set()
        self.given_import = set()
        self.used_import = set()

    def visit_Import(self, node):
        for alias in node.names:
            base_name = alias.name.split(".")[0]
            self.given_import.add(base_name)
        self.generic_visit(node)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.var_created.add(target.id)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.var_used.add(node.id)
        self.generic_visit(node)

    def report(self):
        errors = []

        unused_vars = self.var_created - self.var_used
        for var in unused_vars:
            errors.append(f"Warning: Variable '{var}' is created but never used.")

        unused_imports = self.given_import - self.var_used
        for imp in unused_imports:
            errors.append(f"Warning: Imported module '{imp}' is not used.")

        return errors


# ✅ FUNCTION MUST BE HERE
def detect_errors(code):
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return [f"Syntax Error at line {e.lineno}: {e.msg}"]

    finder = ErrorFinder()
    finder.visit(tree)
    return finder.report()


# ✅ TEST BLOCK MUST BE AT BOTTOM
if __name__ == "__main__":

    sample_code = """
import os
import json

x = 10
y = 20

print(x)
"""

    result = detect_errors(sample_code)

    print("Detected Issues:")
    for r in result:
        print(r)
