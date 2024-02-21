# This script prompts the user to input a string,
# removes any spaces from the beginning and end,
# and changes all uppercase letters to lowercase.
# Finally, it displays the length of both the original
# and the processed (normalized) string.

rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()
lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)
print(f"That String normalised is :{normalisedString}")
print(
    f"we reduced the input string from {lenghtOfRawString} to {lenghtOfNormalised} characters")
