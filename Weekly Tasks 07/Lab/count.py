from path import path_to_count


def readNumber():
    with open(path_to_count) as f:
        number = int(f.read())
        return number


# test it
num = readNumber()
print(num)


def writeNumber(number):
    with open(path_to_count, "wt") as f:
        f.write(str(number))


# test it
# writeNumber(3)
