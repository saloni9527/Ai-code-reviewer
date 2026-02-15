import ast


def parse_code(code_string):
    """
    Parse Python code and check for syntax errors.
    """

    try:
        tree = ast.parse(code_string)

        return {
            "success": True,
            "tree": tree,
            "error": None
        }

    except SyntaxError as e:
        return {
            "success": False,
            "tree": None,
            "error": {
                "message": str(e),
                "line": e.lineno,
                "offset": e.offset
            }
        }


def format_code(code_string):
    """
    Format Python code using AST.
    """

    try:
        tree = ast.parse(code_string)
        formatted_code = ast.unparse(tree)
        return formatted_code

    except Exception:
        return code_string


# -----------------------------
# Testing Block (This makes it runnable)
# -----------------------------

if __name__ == "__main__":

    # Sample user code (you can change this)
    sample_code = """
def add(a,b):
 return a+b

x=10
y=20
print(add(x,y))
"""

    print(" Checking Code...\n")

    result = parse_code(sample_code)

    if result["success"]:
        print("Syntax is correct!\n")

        print("Formatted Code:\n")
        formatted = format_code(sample_code)
        print(formatted)

        print("\n AST Structure:\n")
        print(ast.dump(result["tree"], indent=2))

    else:
        print("Syntax Error Found:")
        print(result["error"])
