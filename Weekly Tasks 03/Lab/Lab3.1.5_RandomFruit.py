import random

# List of fruits
fruit_choices = ('Apple', 'Orange', 'Banana', 'Pear')

# Generate a random index within the range of available fruits
random_index = random.randint(0, len(fruit_choices) - 1)

# Select a fruit based on the random index
selected_fruit = fruit_choices[random_index]

# Display the selected random fruit
print("A Random Fruit: {}".format(selected_fruit))
