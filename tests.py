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

    # print("Testing check 'is not a python file'")

    # result = run_python_file("calculator", "lorem.txt")

    # print(result)

    # print("Testing 'file does not exist'")

    # result = run_python_file("calculator", "lorem.py")

    # print(result)

    # # 1) current directory
    # print("Result for current directory:")

    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")

    # print(result)

    # # 2) pkg directory
    # print("Result for 'pkg' directory:")
    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")

    # print(result)

    # # 3) bin directory
    # print("Result for '/bin' directory:")
    # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

    # print(result)

    # # 4) ../ directory
    # print("Result for '../' directory:")
    # result = get_file_content("calculator", "pkg/does_not_exist.py")

    # print(result)
