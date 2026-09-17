from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/숫자") 
def 디비에 저장하는 함수():
    디비 불러서 값 저장시키기
    return / 주소 다시 부름


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
