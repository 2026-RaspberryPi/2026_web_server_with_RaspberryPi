from flask import Flask, render_template, redirect, url_for, request
import pymysql

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<num>")
def save_num_get(num):
    '''
        1. numcount 테이블 생성(id, num, insert_at)
        2. pymysql로 연결
        3. 증가 한 수만큼 추가
        4. 연결끊기
        5. db 접속해서 조회
    '''
    conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study')
    cur = conn.cursor()
    cur.execute("insert into numcount(num) values({0})".format(num))
    conn.commit()
    conn.close()

    return redirect(url_for("index"))
    

@app.route("/submit", methods=["POST"])
def save_num_post():
    data = request.get_json()
    print(data.get("value"))
    conn = pymysql.connect(host='localhost', user='root', password='q1w2e3', db='study')
    cur = conn.cursor()
    cur.execute(f"insert into numcount(num) values({data.get("value")})")
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
