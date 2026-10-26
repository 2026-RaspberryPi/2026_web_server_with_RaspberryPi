from flask import Flask, request, render_template, jsonify
from model.dht11 import DHT11
from sensor import dht11

app = Flask(__name__)

dht11_db = DHT11()

@app.route("/")
def home():
  return render_template("index.html")

@app.route('/api/now')
def insertdb():
    temp, hum = dht11.get_now()
    result = dht11_db.add(temp, hum)
    return result

@app.route('/api/record')
def selectAll():
    result = dht11_db.find_all()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
