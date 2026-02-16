import ast


def parse_code(code_string):
    """
    Parse Python code and check for both syntax and runtime errors.

    Args:
        code_string (str): Python code to analyze

    Returns:
        dict: Result with success status and error details if any
    """

    # -------- STEP 1: Check Syntax --------
    try:
        tree = ast.parse(code_string)
    except SyntaxError as e:
        return {
            "success": False,
            "error": {
                "type": "Syntax Error",
                "message": str(e),
                "line": e.lineno,
                "offset": e.offset
            }
        }

    # -------- STEP 2: Check Runtime Error --------
    try:
        exec(code_string, {})
    except Exception as e:
        return {
            "success": False,
            "error": {
                "type": "Runtime Error",
                "message": str(e)
            }
        }

    # -------- STEP 3: If Everything Correct --------
    return {
        "success": True,
        "tree": tree,
        "error": None
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
# Testing Block (Runs when file executed)
# -----------------------------

if __name__ == "__main__":

    sample_code = """
def calculate_sum(a, b):
    result = a + b
    if result > 10:
        print("Greater than 10")
    else:
        print("Less than or equal to 10")
    return result

print(calculate_sum(6, 5))
"""

    print(" Checking Code...\n")

    result = parse_code(sample_code)

    if result["success"]:
        print("Code is correct!\n")

        print(" Formatted Code:\n")
        formatted = format_code(sample_code)
        print(formatted)

        print("\n AST Structure:\n")
        print(ast.dump(result["tree"], indent=2))

    else:
        print("Error Found:")
        print(result["error"])
