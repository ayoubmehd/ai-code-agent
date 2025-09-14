import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


def get_arg(index, default):
    try:
        return sys.argv[index]
    except IndexError:
        return default

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
user_prompt = sys.argv[1]
verbose = get_arg(2, '')

messages = [
    types.Content(role='user', parts=[types.Part(text=user_prompt)]),
]

def main():

    print("prompt: ", user_prompt)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )
    if (verbose == '--verbose'):
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
