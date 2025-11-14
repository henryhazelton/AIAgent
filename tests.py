from functions.write_file_content import write_file
from functions.run_python_file import run_python_file


if __name__ == "__main__":
    print("Testing check 'is not a python file'")

    result = run_python_file("calculator", "lorem.txt")

    print(result)

    print("Testing 'file does not exist'")

    result = run_python_file("calculator", "lorem.py")

    print(result)

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
