# Prompt the user for two money amounts in cents
amount1 = int(input("Enter amount1 (in cent): "))
amount2 = int(input("Enter amount2 (in cent): "))

# Calculate the sum of the two amounts in euro
amountResult = int(amount1+amount2)/100
print("The sum of these is €", amountResult)
