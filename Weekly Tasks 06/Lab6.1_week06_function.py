"""Напишите функцию, которая выводит меню команд, которые мы можем выполнить, т.е. добавить,
просмотреть и выйти. Функция должна возвращать то, что выбрал пользователь.
Проверьте функцию. Нам пока не нужно беспокоиться об обработке ошибок."""


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
    print("\n1-ADD\t2-VIEW\t3-QUIT")
    choise = input("\nMake your choise:  ")
    if choise == '1':
        add()
    elif choise == '2':
        view()
    elif choise == '3':
        print("PROGRAM COMPLETED!")
        break
    else:
        print("WRONG ENTER! Please try again", end="\n")
