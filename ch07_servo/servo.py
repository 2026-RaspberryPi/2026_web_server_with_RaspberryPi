import RPi.GPIO as GPIO
from time import sleep

pin = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
servo = GPIO.PWM(pin, 50) # pin을 PWM 모드 50Hz로 사용

#서보모터는 주파수에 따라 동작하기 때문에
#사용자 편의를 위해 각도(angle)를 듀티사이클(duty)로 변환해 사용한다.
def setAngle(angle):
    duty = 2.5 + 10 * angle / 180
    print(f"degree : {angle} to {duty}(duty)")
    servo.ChangeDutyCycle(duty)

if __name__ == "__main__":
    servo.start(0) # DUTY 가 0이라 서보는 동작하지 않음

    setAngle(0)
    sleep(1)
    setAngle(90)
    sleep(1)
    setAngle(50)
    sleep(1)
    setAngle(120)
    sleep(1)
    setAngle(180)
    sleep(1)

	servo.stop()
	GPIO.cleanup()
