
def add():
    print("ADD")
    pass


def view():
    print("VIEW")
    pass


def quit():
    print("QUIT")
    pass


while True:
    print("\nA -> ADD\tV -> VIEW\tQ -> QUIT")
    choise = input("\nMake your choise:  ")
    print(f"You choose {choise}")
    if choise.upper() == 'A':
        add()
    elif choise.upper() == 'V':
        view()
    elif choise.upper() == 'Q':
        print("PROGRAM COMPLETED!")
        break
    else:
        print("WRONG ENTER! Please try again", end="\n")
