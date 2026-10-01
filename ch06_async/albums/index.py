from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    res = requests.get(url='https://jsonplaceholder.typicode.com/photos?_limit=5')
    if res.status_code == 200:
        return render_template("index.html", photos = res.json())
    else:
        return res.status_code
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")
