# Function to allow LLM to run a python file
import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    # Find absolute path of current working directory
    working_directory = os.path.abspath(working_directory)

    # Find absolute path of target directory/file
    file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Validate if full path is within the working directory boundaries
    if (
        os.path.commonpath([working_directory, file_path])
        != working_directory
    ):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # Validate if file path exists
    if not os.path.exists(file_path):
        return f'Error: File "{file_path}" not found.'

    # Check file ends in .py
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    # Ensure args is a list of strings
    args = [] if args is None else [str(a) for a in args]

    # Build up cmd to pass a list of args to subprocess.run()
    cmd = ["python", file_path]
    if args:
        cmd.extend(args)

    # make the llm run
    result = subprocess.run(cmd, timeout=30, capture_output=True, cwd=working_directory, text=True)
    

    print(result)