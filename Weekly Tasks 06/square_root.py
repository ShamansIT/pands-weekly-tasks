import math


def sqrt_fun(num, epsilon=0.0001):
    x_n = num / 2.0  # Initial approximation

    while True:
        # Next approximation according to Newton's formula
        x_next = 0.5*(x_n + num / x_n)
        # resourse: https://en.wikipedia.org/wiki/Newton%27s_method#:~:text=The%20idea%20is%20to%20start,the%20method%20can%20be%20iterated.

        if abs(x_next - x_n) < epsilon:  # Check for convergence
            break
        x_n = x_next
    return x_next


def sqrt_equal_check(num):
    print(f"Math  = {math.sqrt(num)} and sqrt_fun = {sqrt_fun(num)}")
    print(f"Check status: {bool((math.sqrt(num))== (sqrt_fun(num)))}")


while True:
    print("\nCheck sqrt function on!")
    input_number = input("Please enter a positive number: ")
    print("Do you wish change epsilon! Default is 0.0001")
    input_choise = input("Y/N: ")
    if input_choise.upper() == "Y":
        inpup_epsilon = input("Enter new epsilon: ")
        print(
            f"The square root of {input_number} with epsilon {inpup_epsilon} is {sqrt_fun(float(input_number), float(inpup_epsilon))}")
    elif input_choise.upper() == "N":
        print(
            f"The square root of {input_number} is approx. {sqrt_fun(float(input_number))}")
    else:
        print("Wrong input! Don`t do this! Onece you can crush all world with wrong input!")

    print("Do you wish check sqrt_function(F), continue(C) or exit(X)? ")
    input_next_step = ("F / C / X :")
    if input_next_step.upper() == "F":
        sqrt_equal_check(float(input_number))
    elif input_next_step.upper() == "X":
        print("Thank for using our free software!")
        break
    else:
        print("Wrong input! Don`t do this! Onece you can crush all world with wrong input!")
