from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


if __name__ == "__main__":
    # 1) current directory
    print("Result for current directory:")
    result = get_file_content("calculator", "main.py")
    # print each line, indented by one space
    for line in result.splitlines():
        print(f" {line}")

    # 2) pkg directory
    print("Result for 'pkg' directory:")
    result = get_file_content("calculator", "pkg/calculator.py")

    for line in result.splitlines():
        print(f" {line}")

    # 3) bin directory
    print("Result for '/bin' directory:")
    result = get_file_content("calculator", "/bin/cat")

    for line in result.splitlines():
        print(f" {line}")

    # 4) ../ directory
    print("Result for '../' directory:")
    result = get_file_content("calculator", "pkg/does_not_exist.py")

    for line in result.splitlines():
        print(f" {line}")
