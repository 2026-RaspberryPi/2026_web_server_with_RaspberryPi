import pymysql


def get_connection():
    return pymysql.connect(host='localhost', user='계정', password='q1w2e3', db='study')


def add(ms):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("insert into record_button(ms) values(%s)", (ms,))
        conn.commit()
    finally:
        conn.close()
