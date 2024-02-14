# This program reads in a students percentage
# and prints out the corresponding grade

percentage = float(input("Enter the percentage: "))

# check and print condition
if percentage <= 40:
    print("Fail")
elif percentage > 40 and percentage < 50:
    print("Pass")
elif percentage >= 50 and percentage < 60:
    print("Merit 2")
elif percentage >= 60 and percentage < 70:
    print("Merit 1")
elif percentage >= 70 and percentage <= 100:
    print("Distinction")
else:
    print("Wrong input! Please enter a number between 0 and 100")
