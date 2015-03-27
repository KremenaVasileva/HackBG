import sys


def sum_numbers():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        file = open(filename, "r")
        contents = file.read().split(" ")
        result = sum([int(x) for x in contents])
        file.close()
        return result
    else:
        print("Give me enough arguments :(")

if __name__ == '__main__':
    print(sum_numbers())
