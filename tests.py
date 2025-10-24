from functions.write_file_content import write_file


if __name__ == "__main__":
    # 1) current directory
    print("Result for current directory:")

    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")

    print(result)

    # 2) pkg directory
    print("Result for 'pkg' directory:")
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")

    print(result)

    # 3) bin directory
    print("Result for '/bin' directory:")
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

    print(result)

    # # 4) ../ directory
    # print("Result for '../' directory:")
    # result = get_file_content("calculator", "pkg/does_not_exist.py")

    # print(result)
