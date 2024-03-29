import sqlite3
import datetime
import random
def get_connection(func):
    def wrapper(cur=None,*args,**kwargs):
        with sqlite3.connect("database.db") as conn:
            cur = conn.cursor()
            func(cur)
    return wrapper

def logger(record):
    with open("journal.log", "a", encoding="utf-8") as file:
        file.write(str(datetime.datetime.now())+ " "+ record+ "\n")
@get_connection
def create_table_films(cur=None):
    cur.execute("""
        create  table films
        (
            file_id primary_key,
            title text not null,
            description text
        )
        """)
    
    films = cur.fetchall()
@get_connection
def add_film(cur=None):
    global title, description
    cur.execute("""
               SELECT COUNT(*) FROM films
                """)
    film_id = cur.fetchone()[0] + 1
    cur.execute("""
                SELECT *
                FROM films
                WHERE title='%s'
                """%(title))
    is_film_there = cur.fetchone()
    if is_film_there:
        return None

    cur.execute("""
            insert into films
            values
            (%d,'%s','%s')     
                
                """%(film_id,title,description))
    return True

    
@get_connection
def delete_film(cur=None):
    global title
    try:
        cur.execute("DELETE FROM films WHERE title ='%s'"%(title))
        # cur.execute("SELECT * FROM films")
        # films = cur.fetchal()
        # cur.execute("DELETE * FROM films")
        # for iden, film in enumerate(films, start=1):
        #     film_id, title, description =  film
        #     cur.execute("INSERT INTO film VALUES(%d, '%s', '%s')"%(iden, title, description))
        return True
    except:
        pass
    
@get_connection
def get_film(cur=None):
    cur.execute("SELECT * FROM films")
    films = cur.fetchall()
    return random.choice(films)

title="Мстители: война бесконечности"
description="фильм от марвел"
add_film()
get_film()
    