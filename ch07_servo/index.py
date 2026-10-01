from flask import Flask, request, render_template, jsonify
import RPi.GPIO as GPIO
from time import sleep

app = Flask(__name__)

pin = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
servo = GPIO.PWM(pin, 50) # pin을 PWM 모드 50Hz로 사용

#서보모터는 주파수에 따라 동작하기 때문에
#사용자 편의를 위해 각도(angle)를 주파수(duty)로 변환해 사용한다.
def set_angle(angle):
    duty = 2.5 + 10 * angle / 180 # duty는 펄스폭을 나타내는 값으로 0~100 사이 값
    print(f"degree : {angle} to {duty}(duty)")
    servo.ChangeDutyCycle(duty)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/api/angle', methods=['POST'])
def control_servo():
    data = request.get_json()
    angle = data.get('angle')  # POST 요청에서 'angle' 값을 가져옴
    if angle is not None:
        set_angle(int(angle))  # 서보 모터 각도 설정
        return jsonify({'message': 'angle set to {}'.format(angle)})
    else:
        return jsonify({'message': 'fail! check your parameter'})


if __name__ == "__main__":
    servo.start(0) # DUTY 가 0이라 서보는 동작하지 않음
    try:
        app.run(host="0.0.0.0")
    except keyboardInterrupt:
        servo.stop()
        GPIO.cleanup()
