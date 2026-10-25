import pymysql

class SERVO:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study')
        self.cur = self.conn.cursor() #SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
        self.cur.execute("""
            create table if not exists record_angle(
                id int auto_increment primary key,
                angle int not null,
                date datetime default current_timestamp not null)
        """)
        print("connect ok")


    def get(self):
        self.cur.execute("select * from record_angle")
        return self.cur.fetchall()


    def add(self, angle):
        self.cur.execute("insert into record_angle(angle) values('{0}')".format(angle))
        self.conn.commit()
