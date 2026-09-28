import pymysql

class LED:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='1q2w3e', db='study')
        self.cur = self.conn.cursor() #SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
        self.cur.execute("""
            create table if not exists record_led(
                id int auto_increment primary key,
                status varchar(10) not null,
                date datetime default current_timestamp not null)
        """)
        print("connect ok")

    def get(self):
        self.cur.execute("select * from record_led")
        return self.cur.fetchall()


    def add_status(self, status):
        self.cur.execute("insert into record_led(status) values('{0}')".format(status))
        self.conn.commit()
