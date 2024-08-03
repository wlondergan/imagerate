import psycopg2

class Database:
    conn: psycopg2.connection = None
    cur: psycopg2.cursor = None

db: Database = Database()

def connect():
    db.conn = psycopg2.connect("dbname=imagerate, user=postgres, password=secret")
    db.cur = db.conn.cursor()
    
def close():
    db.cur.close()
    db.conn.close()
    