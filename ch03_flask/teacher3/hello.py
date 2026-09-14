from flask import Flask
import config

# __name__ 은 이 파일을 누가 실행했는지 알려주는 값임
# 이 파일을 직접 실행하면 __main__, 다른 파일이 불러오면 파일 이름(hello)이 됨
app = Flask(__name__)


@app.route("/")          # ip 주소 뒤에 붙는 주소
def hello_world():
    return "Hello World!"


@app.route("/hello")
def hello():
    return "hello world"


@app.route("/hi")
def hi():
    return "hi world"

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello, " + name + "!"


if __name__ == "__main__":
    # host="0.0.0.0" 은 누구나 접근할 수 있게 만듦
    app.run(host="0.0.0.0", port=config.PORT, debug=True)
