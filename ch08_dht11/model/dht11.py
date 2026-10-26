import pymysql

class DHT11:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study')
        self.cur = self.conn.cursor() #SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
        self.cur.execute("""
            create table if not exists record_dht(
                id int auto_increment primary key,
                humidity int not null,
                temperature int not null,
                created_at datetime default current_timestamp not null)
        """)
        print("connect ok")


    def add(self, temp, hum):
        sql = f"insert into record_dht(temperature, humidity) values('{temp}', '{hum}')"
        self.cur.execute(sql)
        self.conn.commit()
        return [temp, hum]

    def find_all(self):
        sql = "select * from record_dht"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
