import pymysql

class TodoDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1q2w3e', db='shopping_db')
        self.cur = self.db.cursor()
        self.cur.execute("""
            create table IF NOT EXISTS todos (
            todo_index int auto_increment PRIMARY KEY,
            task varchar(100) not null,
            completed varchar(30) default 'false' not null)
                         """)
        print("connect ok")

    def get(self):
        sql = "select * from todos"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def add(self, title):
        sql = "insert into todos(task) values('{0}')".format(title)
        self.cur.execute(sql)
        self.db.commit()

    def completed(self, todo_index):
        sql = f"update todos set completed='true' where todo_index={todo_index}"
        self.cur.execute(sql)
        self.db.commit()

    def remove(self, todo_index):
        sql = f"delete from todos where todo_index={todo_index}"
        self.cur.execute(sql)
        self.db.commit()
