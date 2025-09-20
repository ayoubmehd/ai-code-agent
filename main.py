import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import call_function

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
system_propmt="""
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

messages = [
    types.Content(role='user', parts=[types.Part(text=user_prompt)]),
]

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            )
        }
    )
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get file content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read the content from, file should exist in working directory, if not provided an error string will be returned"
            )
        }
    )
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter. if no argument specified run the script anyway",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to execute, file should exist in working directory, must end in .py"
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional arguments to pass to the python script.",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional argument to pass to the python script"
                ),
            ),
        }
    )
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write file content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write to, if file dosn't exist it will be created, if not it's content will be overriten",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be written to the file"
            )
        }
    )
)

available_functions=types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def main():
    is_verbose = verbose == '--verbose'

    if (is_verbose):
        print(f"User prompt: {user_prompt}")

    try:
        for call in range(0, 20):
            if is_verbose:
                print(f"Call: {call}")
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_propmt),
            )


            if (is_verbose):
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
            for candidate in response.candidates:
                if is_verbose:
                    print(f"Candidate: {candidate.content}")
                if candidate:
                    messages.append(
                        candidate.content
                    )

            if response.function_calls: 
                functions_call_result = [call_function(function, is_verbose) for function in response.function_calls]
                for item in functions_call_result:
                    messages.append(item)

                if verbose:
                    response_parts_text = [call.parts[0].function_response.response for call in functions_call_result]
                    response_parts_text = "\n".join([f"-> {response}" for response in response_parts_text])
                    print(response_parts_text)

                if is_verbose:
                    output = [f"Calling function: {call.name}({call.args})" for call in response.function_calls]

                    print("\n".join(output))
                
            elif response.text:
                print(response.text)
                break
    except Exception as e:
        if is_verbose:
            for msg in messages:
                print(f"Message: {msg}")
            print(e)


if __name__ == "__main__":
    main()
