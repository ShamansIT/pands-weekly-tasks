# Weekly Task 4
# Created by Serhii Spitsyn

import random

# init variables
enter_number = int(input("Please enter any positive number: "))
list_numbers = [int(enter_number)]

# check number is valid
if enter_number <= 0:
    print("Wrong enter number! ERROR!")
else:
    # operation with number: even /2, odd *3+1
    while enter_number != 1:
        if enter_number % 2 == 0:
            enter_number /= 2
        else:
            enter_number = (enter_number*3)+1
        list_numbers.append(int(enter_number))
    print(list_numbers)
