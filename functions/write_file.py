import os
from pathlib import Path
from functions.is_path_in_directory import is_path_in_directory

def write_file(working_directory, file_path, content):

    path = os.path.join(working_directory, file_path)
    working_directory = Path(working_directory).resolve()
    path = Path(path).resolve()
    if not is_path_in_directory(working_directory, path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    try: 
        new_path = Path("/".join(str(path).split('/')[:-1]))
        if not new_path.exists():
            os.makedirs(new_path)

        with open(path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"