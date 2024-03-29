from conection import get_connection

@get_connection
def create_table_students(cur):
    cur.execute("""
        create table if not exists students
        (
            student_id int primary key,
            first_name varchar(64) NOT NULL,
            last_name varchar(64) NOT NULL,
            pater_name varchar(64) NOT NULL,
            gender varchar(1) NOT NULL,
            phone_number varchar(16) NOT NULL
            
        )
    """)

@get_connection
def create_table_teachers(cur):
    cur.execute("""
        create table if not exists teachers
        (
            teacher_id int primary key,
            first_name varchar(64) NOT NULL,
            last_name varchar(64) NOT NULL,
            pater_name varchar(64) NOT NULL,
            gender varchar(1) NOT NULL,
            phone_number varchar(16) NOT NULL
            
        )
    """)

@get_connection
def create_table_subject(cur):
    cur.execute("""
        create table if not exists subjects
        (
            subject_id int primary key,
            name varchar(128) NOT NULL,
            fk_teacher_id int REFERENCES teachers(teacher_id)
            
        )
    """)

@get_connection
def create_table_schedule(cur):
    cur.execute("""
        create table if not exists schedule
        (
            schedule_id int primary key,
            day varchar(15) NOT NULL,
            fk_subject_id int REFERENCES subjects(subject_id)
            
        )
    """)

@get_connection
def create_table_marks(cur):
    cur.execute("""
        create table if not exists schedule
        (
            mark_id int primary key,
            fk_student_id int REFERENCES students(students_id),
            fk_subject_id int REFERENCES subjects(subject_id)
        )
    """)
    



@get_connection
def create_all_tables(cur=None):
    create_table_students(cur)
    create_table_teachers(cur)
    create_table_subject(cur)
    create_table_schedule(cur)
    create_table_marks(cur)

