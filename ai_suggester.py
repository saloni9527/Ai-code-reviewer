import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

# Force load .env from project folder
load_dotenv(dotenv_path=".env")

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

model = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=api_key
)

code_string = """
def calculate_sum(a, b):
    result = a + b
    if result > 10:
        print("Greater than 10")
    else:
        print("Less than or equal to 10")
    return result
"""

prompt = PromptTemplate.from_template("""
You are an experienced coding teacher.

Analyze the code and provide:
• errors (if any)
• improvements
• why changes are needed
• time complexity
• space complexity

Code:
{code}
""")

def get_ai_suggestion(code_string):
    formatted_prompt = prompt.format(code=code_string)
    result = model.invoke(formatted_prompt)
    print("\n--- AI Suggestion ---")
    print(result.content)

if __name__ == "__main__":
    get_ai_suggestion(code_string)
