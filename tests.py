from functions.get_files_info import get_files_info


if __name__ == "__main__":
    # 1) current directory
    print("Result for current directory:")
    result = get_files_info("calculator", ".")
    # print each line, indented by one space
    for line in result.splitlines():
        print(f" {line}")

    # 2) pkg directory
    print("Result for 'pkg' directory:")
    result = get_files_info("calculator", "pkg")

    for line in result.splitlines():
        print(f" {line}")

    # 3) bin directory
    print("Result for '/bin' directory:")
    result = get_files_info("calculator", "/bin")

    for line in result.splitlines():
        print(f" {line}")

    # 4) ../ directory
    print("Result for '../' directory:")
    result = get_files_info("calculator", "../")

    for line in result.splitlines():
        print(f" {line}")