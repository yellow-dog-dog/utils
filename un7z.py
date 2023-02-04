import py7zr

file_path = input("input path:")


def un7z_file():
    i = 0
    while 1:
        try:
            with py7zr.SevenZipFile(file_path, 'r', password=str(i)) as fp:
                fp.extractall(path="./")
                print("password is{}".format(i))
                return 0
        except:
            print(i)
            i += 1


if __name__ == '__main__':
    un7z_file()
