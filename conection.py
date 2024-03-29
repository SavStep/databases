import psycopg2

def get_connection(func):
    def wrapper(cur=None):
        with psycopg2.connect(database="school", user="postgres", password="postgres", host= "localhost", port=5432) as conn:
            with conn.cursor() as cur:
                func(cur)
    return wrapper
