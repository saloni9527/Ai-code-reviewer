from code_parse import parse_code
from error_detector import detect_errors

sample_code = """
import os
import json

x = 10
print(x)
"""

print("Parsing Result:")
print(parse_code(sample_code))

print("\nError Detection Result:")
print(detect_errors(sample_code))
