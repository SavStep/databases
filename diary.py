
from add_components import *
from init import create_all_tables


while True:
    print("Меню:")
    print("1 - Инициализировать базу данных")
    print("2 - добавить ученика")
    print("3 - добавить преподавателя")
    print('4 - добавить предмет')
    print("5 - выйти из программы ")
    action = input('ваш выбор: ')
    if action == "1":
        create_all_tables()
    elif action == "2":
        add_student()
    elif action == "3":
        pass
    elif action == "4":
        pass
    elif action == "5":
        pass
    