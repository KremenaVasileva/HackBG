import sys
import os


def duhs():
    if len(sys.argv) == 2:
        try:
            file_path = sys.argv[1]
            total_sum = 0
            for dirpath, dirnames, filenames in os.walk(file_path):
                for name in filenames:
                    path = str(dirpath) + '/' + str(name)
                    total_sum += os.stat(path).st_size
            return total_sum / (1024 * 1024)
        except OSError as error:
            print(error)
    else:
        print("Not enough arguments")


if __name__ == '__main__':
    print(duhs())
