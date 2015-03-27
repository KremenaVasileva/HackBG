import sys


def cat2():
    if len(sys.argv[1]) > 1:
        for i in range(1, len(sys.argv)):
            filename = sys.argv[i]
            text_file = open(filename, "r")
            text = text_file.read()
            text_file.close()
            print (text, "\n")
    else:
        print("Give me a file to read!")


if __name__ == '__main__':
    print(cat2())
