import RPi.GPIO as GPIO
import time
import random

LED = 8
BUTTON = 36

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def measure():
    time.sleep(random.uniform(1, 4))        # 1~4초 중 아무 때나
    GPIO.output(LED, GPIO.HIGH)
    start_time = time.time()

    pressed = GPIO.wait_for_edge(BUTTON, GPIO.FALLING, timeout=3000)   # 최대 3초 기다림
    GPIO.output(LED, GPIO.LOW)
    if pressed is None:
        return None                         # 시간 초과

    ms = int((time.time() - start_time) * 1000)
    return {"ms": ms}
