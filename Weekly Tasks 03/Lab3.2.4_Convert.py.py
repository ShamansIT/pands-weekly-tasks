# Program takes in a float amount of dollars and returns that absolute amount in cent

# Input: floating-point number from user
amount_in_dollars = float(input("Enter the amount in euro: "))
# Conversion
absolute_amount = abs(amount_in_dollars)
amount_in_cents = round(absolute_amount * 100)

# Output: absolute amount in cents
print(f"Absolute amount in cents: {amount_in_cents}")
