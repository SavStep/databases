from conection import get_connection


def check_field(field):
    alphabet = "абвгдеёжзийклмнопрстуфхчшщьыъэюя"
    if not field:
        return False
    elif field.isdigit():
        print("вы ввели число,а так нельзя")
        return False
    elif all([letter in alphabet for letter in field]):
        print ("Вы ввели английские буквы")
        return False
    return True

@get_connection
def add_student_or_teacher(cur=None):
    first_name = ""
    while not check_field(first_name):
        first_name = input("Введите имя ученика: ")


    last_name = ""
    while not check_field(last_name):
        last_name = input("Введите фамилию ученика: ")



    patern_name = ""
    while not check_field(patern_name):
        patern_name = input("Введите отчество ученика: ")


    gender = ""
    while  gender  not in ["м", "ж"]:
        gender = input("Введите пол ученика(м или ж): ")


    phone_number = ""
    while len(phone_number) < 5:
        phone_number = input("Введите номер телефона без пробела: ")
    
    cur.execute("SELECT COUNT(*) FROM students")
    id = cur.fetchone()[0] + 1 
    try:
        cur.execute("INSERT into students values (%d, '%s', '%s', '%s', '%s', '%s',)"%(
            id, first_name, last_name, patern_name, gender, phone_number
        ))
        print("Успешно дбвален новый ученик")
    except:
        print("Не вышло")

@get_connection
def add_teacher(cur=None):
    first_name = ""
    while not check_field(first_name):
        first_name = input("Введите имя учителя: ").capitalize()
    last_name = ""
    while not check_field(last_name):
        last_name = input("Введите фамилию учителя: ").capitalize()
    pater_name = ""
    while not check_field(pater_name):
        pater_name = input("Введите отчество учителя: ").capitalize()
    
    gender = ""
    while gender not in ["м", "ж"]:
        gender = input("Выберите пол (м/ж): ")
        
    phone_number = ""
    while len(phone_number) < 5 and  not phone_number.isdigit():
        phone_number = input("Введите номер телефона без пробелов: ")
    
    cur.execute("SELECT COUNT(*) FROM teachers")
    id = cur.fetchone()[0] + 1
    try:
        cur.execute("INSERT into teachers values(%d, '%s','%s','%s','%s','%s')"%(
            id, first_name, last_name, pater_name, gender, phone_number
        ))
        print("Успешно добавлен новый преподаватель")
    except:
        print("Что-то не получилось")
 
 
def add_subject(cur=None):
    name = ""
    while not check_field(name):
        name = input('Введите название предмета: ')
    cur.execute('SELECT COUNT(*) FROM subjects')
    id = cur.fetchone()[0] + 1
    try:
        cur.execute("INSERT INTO subjects VALUES (%d, '%s');" % (
            id, name
        ))
        print('Успешно добавлена новая запись!')
    except:
        print('Что-то не получилось')