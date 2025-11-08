# Function to allow LLM to run a python file
import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):

    # Find absolute path of current working directory
    path_working_directory = os.path.abspath(working_directory)

    # Find absolute path of target directory/file
    file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # Validate if full path is within the working directory boundaries
    if (
        os.path.commonpath([path_working_directory, file_path])
        != path_working_directory
    ):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # Validate if file path exists
    if not os.path.dirname(file_path):
        return f'Error: File "{file_path}" not found.'
    
    # Check file ends in .py
    if not file_path.endswith(".py"):
        print(file_path)
        return f'Error: "{file_path}" is not a Python file.'
    
    # make the llm run
    subprocess.run(timeout=30, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=file_path, args=args)
    result = subprocess.CompletedProcess

    if result:
        standard_output = f"STDOUT: {result.stdout}"
        standard_error = f"STDERR: {result.stderr}"
        exit_code = f"Process exited with {result.check_returncode()}"

        return standard_output, standard_error, exit_code
    
