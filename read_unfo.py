from connection import get_connection
 
 
@get_connection
def read_students_table(cur=None):
    cur.execute("SELECT * FROM STUDENTS")
    students = cur.fetchall()
    headers = "№\tИмя\tФамилия\tОтчество\tПол\tНомер телефона"
    print(headers)
    for student in students:
            print(*student, sep="\t")
        
        
@get_connection
def read_teachers_table(cur=None):
    cur.execute("SELECT * FROM teachers")
    teachers = cur.fetchall()
    headers = "№\tИмя\tФамилия\tОтчество\tПол\tНомер телефона"
    print(headers)
    for teacher in teachers:
        print(*teacher, sep="\t")
    
@get_connection
def read_subjects_table(cur=None):
    cur.execute("SELECT subject_id, name FROM subjects")
    subjects = cur.fetchall()
    headers = "№\tНазвание предмета"
    print(headers)
    for subject in subjects:
        print(*subject, sep="\t")
    
@get_connection
def read_student_results(cur=None):
    read_students_table(cur)
    iden = ""
    while not iden.isdigit():
        iden = input("у кого выведем табель умпеваеиости?")
    iden = int(iden)
    try:
        cur.execute ("""
                     SELECT *
                     FROM students
                     WHERE student_id=%s
                     """%(iden))
        
    except:
        print("Нет такого ученика")
        return None
    cur.execute("""
                SELECT first_name, last_name, pater_name, name, AVG(mark)
                FROM marks
                INNER JOIN students ON fk_student_id = students.student_id
                INNER JOIN subjects ON fk_subject_id = subjects.subject_id
                WHERE fk_student_id = %d
                GROUP BY first_name, last_name, pater_name, subjects.name;
                
                """%(iden))
    headers = "Имя\tФамилия\t\tОтчество\tПредмет\t\tСредняя оценка"
    table =  cur.fetchall()
    print(headers)
    for record in table:
        print(*record, sep="\t")
 