import os

from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a python file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write to. The file should be a python file, if not an error message is returned.",
            ),
            "content": types.Schema(
                type=types.Type.STRING, description="The content to write to the file."
            ),
        },
        required=["file_path"],
    ),
)


def write_file(working_directory, file_path, content):
    try:
        # Find absolute path of current working directory
        path_working_directory = os.path.abspath(working_directory)

        # Find absolute path of target directory/file
        file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Validate if full path is within the working directory boundaries
        if (
            os.path.commonpath([path_working_directory, file_path])
            != path_working_directory
        ):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Validate if file path exists
        parent_path = os.path.dirname(file_path)
        if parent_path:
            os.makedirs(parent_path, exist_ok=True)

        # Write content to file
        with open(file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error trying to write to file '{file_path}': {e}"
