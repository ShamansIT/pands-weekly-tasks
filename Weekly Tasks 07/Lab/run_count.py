from path import path_to_count
import os.path


def readNumber():
    with open(path_to_count) as f:
        number = int(f.read())
        return number


def writeNumber(number):
    with open(path_to_count, "wt") as f:
        f.write(str(number))


# main
num = readNumber()
num += 1
print(f"We have run this program {num} times")
writeNumber(num)
