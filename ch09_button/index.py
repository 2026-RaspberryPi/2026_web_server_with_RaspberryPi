from flask import Flask, render_template, jsonify
import model.button
import sensor.button


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/start", methods=["POST"])
def start():
    result = sensor.button.measure()          # 1회 측정
    if result is None:
        return jsonify({"message": "time over!"}), 400
    model.button.add(result["ms"])            # 저장
    return jsonify(result)                    # {"ms": 312}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
