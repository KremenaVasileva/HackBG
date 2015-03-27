import sys
from random import randint


def generate_number():
    if len(sys.argv) == 3:
        filename = sys.argv[1]
        file = open(filename, "w")
        contents = []
        n = int(sys.argv[2])
        for i in range(0, n):
            contents.append(str(randint(1, 10)))
        file.write(" ".join(contents))
        file.close()
    else:
        print("Give me enough arguments :(")

if __name__ == '__main__':
    generate_number()
