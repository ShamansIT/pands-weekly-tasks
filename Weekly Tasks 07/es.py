# Weekly Task 7
# Created by Serhii Spitsyn

import os

file_name = input("Please enter file name(best is: moby-dick.txt) -> ")
letter = input("Please enter letter to check -> ")

# Format path
name_strip = "Weekly Tasks 07\\" + file_name.strip()


if name_strip[-4:] != '.txt':  # Check file exicution
    print("Wrong file extention. Not *.txt")
elif os.path.exists(name_strip):  # Check is file exists
    count = 0
    with open(name_strip, 'rt') as f:
        for line in f:  # Read each line
            line_to_count = line  # Count symbol in each line
            count = count + line.count(letter)  # Count symbol
    print(f"Count letter {letter} is {count}")
else:
    print(file_name.strip(), "does not exist! Wrong enter!")
