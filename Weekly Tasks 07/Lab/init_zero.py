import os.path
from path import path_to_count


def writeNumber(number):
    with open(path_to_count, "wt") as f:
        f.write(str(number))


def readNumber():
    try:
        with open(path_to_count) as f:
            number = int(f.read())
        return number
    except IOError:
        return 0


if not os.path.isfile(path_to_count):
    print("File does not exist")
    # initialise file here
    writeNumber(0)
