def readModules():
    modules = []
    moduleName = input(
        "\tEnter the first Module name (blank to quit) :").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade:"))
        modules.append(module)
        moduleName = input(
            "\tEnter next module name (blank to quit) :").strip()
    return modules


def add(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name :")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)


def view(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])


def displayModules(modules):
    print("\tName \tGrade")
    for module in modules:
        print(f"\t{ module['name']} \t{ module['grade']}")


students = []

while True:
    print("\nA -> ADD\tV -> VIEW\tQ -> QUIT")
    choise = input("\nMake your choise:  ")
    print(f"You choose {choise}")
    if choise.upper() == 'A':
        add(students)
    elif choise.upper() == 'V':
        view()
    elif choise.upper() == 'Q':
        print("PROGRAM COMPLETED! QUIT!")
        break
    else:
        print("WRONG ENTER! Please try again", end="\n")
