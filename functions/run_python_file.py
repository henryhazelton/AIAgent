import os
import subprocess

from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the python file given to the function, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run. The file should be a python file, if not an error message is returned.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional arguments passed into the function call, will be a list of strings",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)


# Function to allow LLM to run a python file
def run_python_file(working_directory, file_path, args=[]):
    try:
        # Store file name
        file_name = file_path

        # Find absolute path of current working directory
        working_directory = os.path.abspath(working_directory)

        # Find absolute path of target directory/file
        file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Validate if full path is within the working directory boundaries
        if os.path.commonpath([working_directory, file_path]) != working_directory:
            return f'Error: Cannot execute "{file_name}" as it is outside the permitted working directory'

        # Validate if file exists
        if not os.path.exists(file_path):
            return f'Error: File "{file_name}" not found.'

        # Check file ends in .py
        if not file_path.endswith(".py"):
            return f'Error: "{file_name}" is not a Python file.'

        # Ensure args is a list of strings
        args = [] if args is None else [str(a) for a in args]

        # Build up cmd to pass a list of args to subprocess.run()
        cmd = ["python", file_path]
        if args:
            cmd.extend(args)

        # make the LLM run
        output = subprocess.run(
            cmd, timeout=30, capture_output=True, cwd=working_directory, text=True
        )

        if output.returncode != 0:
            return f"STDOUT: {output.stdout} STDERR: {output.stderr} Process exited with code {output.returncode}"

        if output.stderr == "" and output.stdout == "":
            return "No output produced."

        return f"STDOUT: {output.stdout} STDERR: {output.stderr}"

    except Exception as e:
        return f"Error executing Python file: {e}"
