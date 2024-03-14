# Weekly Task 3
# Created by Serhii Spitsyn
# Bank account hide number

# Prompt the user to enter an account number
acc_number = input("Input accoutn number more then 4 digits: ")

# Check if the account number length is greater than 4 and is digit
if len(acc_number) < 4 or not acc_number.isdigit():
    print(f"Error input! Number validation error in number \"{acc_number}\"")
else:
    convert_acc_str = 'x' * (len(acc_number) - 4) + acc_number[-4:]
    print(convert_acc_str)
