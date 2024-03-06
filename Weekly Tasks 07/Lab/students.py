import json
students = []
path = "Weekly Tasks 07\Lab\\studentData.json)"


def writeDict(data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def readDict():
    with open(path, "r") as file:
        return json.load(file)


def doSave():
    writeDict(students)
    print("students saved")


def doLoad():
    # You will put the call to readDict() here and return the result
    print("In load")
    # For now, let's assume readDict() returns a list of students
    return readDict()


def displayMenu():
    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("type one letter (a/v/s/q):").strip()
    return choice


def doAdd(students):
 # you have code here to add
    print("in adding")


def doView(students):
 # you have code here to view
    print("in viewing")


def doSave(students):
    # you will put the call to save dict here
    print("in save")
# main program
    choice = displayMenu()
    while (choice != 'q'):
     # we could do this with lamda functions
     # I am keeping this basic for the moment
        if choice == 'a':
            doAdd(students)
        elif choice == 'v':
            doView(students)
        elif choice == 's':
            doSave(students)
        elif choice != 'q':
            print("\n\nPlease select either a,v,s or q")
            choice = displayMenu()
