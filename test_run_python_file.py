from functions.run_python_file import run_python_file


if __name__ == "__main__":
    # Run 1
    print("Run 1")
    result = run_python_file("calculator", "main.py")
    print(result)

    # Run 2
    print("Run 2")
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)

    # Run 3
    print("Run 3")
    result = run_python_file("calculator", "tests.py")
    print(result)

    # Run 4
    print("Run 4")
    result = run_python_file("calculator", "../main.py")
    print(result)

    # Run 5
    print("Run 5")
    result = run_python_file("calculator", "nonexistent.py")
    print(result)

    # Run 6
    print("Run 6")
    result = run_python_file("calculator", "lorem.txt")
    print(result)
