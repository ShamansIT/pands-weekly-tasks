FILENAME = "Weekly Tasks 07\Lab\count.txt"


def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number


# test it
num = readNumber()
print(num)


def writeNumber(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))


# test it
writeNumber(3)
