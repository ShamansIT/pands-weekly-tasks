# program that reads in two numbers and
# outputs the integer answer and remainder

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

# check deviding by zero
if b == 0:
    print("Error! Can not deviding by 0!")
else:
    calculate = int(a//b)
    remainder = a % b
    print("{} divided by {} is {} with remainder {}".format(
        a, b, calculate, remainder))
