import RPi.GPIO as GPIO

BUTTON = 36

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # 내부 풀업 저항 사용

print("버튼을 눌러보세요!")
try:
    while True:
        GPIO.wait_for_edge(BUTTON, GPIO.FALLING, bouncetime=200)   # 눌릴 때까지 기다림
        print("눌림!")
except KeyboardInterrupt:
    GPIO.cleanup()
