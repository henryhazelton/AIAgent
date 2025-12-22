import os
import config

from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file along with the length of the file and if file is too big truncates the message returned, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read, relative to the working directory. If not provided, returns an error stating cannot read file.",
            )
        },
        required=["file_path"],
    ),
)


# Function to get content of a file
def get_file_content(working_directory, file_path):
    try:
        # Find absolute path of working directory
        absolute_path_working_directory = os.path.abspath(working_directory)

        # Find absolute path of target directory
        absolute_path_target_directory = os.path.abspath(
            os.path.join(working_directory, file_path)
        )

        # Validate if full path is within the working directory boundaries
        if (
            os.path.commonpath(
                [absolute_path_working_directory, absolute_path_target_directory]
            )
            != absolute_path_working_directory
        ):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

        # Validate if file path is a file
        if not os.path.isfile(absolute_path_target_directory):
            return f'Error: "{file_path}" is not a file'

        # Read the file
        with open(absolute_path_target_directory, "r") as f:
            file_content_string = f.read(config.character_limit)

        # Find lenth of file
        file_length = len(file_content_string)

        # Check file length and return message if truncated
        if file_length >= config.character_limit:
            file_content_string_truncated = (
                file_content_string
                + f"[...File '{file_path}' truncated at 10000 characters]"
            )
            return file_content_string_truncated
        else:
            return file_content_string
    except Exception as e:
        return f"Error reading file '{file_path}': {e}"
