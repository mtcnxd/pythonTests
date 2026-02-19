import RPi.GPIO as gpio
import time

ledPin = 18

try:
	gpio.setmode(gpio.BOARD)
	gpio.setup(ledPin, gpio.OUT)

except Exception as e:
	print(f"GPIO Error: {e}")

def blink():
    gpio.output(ledPin, True)
    time.sleep(0.5)
    gpio.output(ledPin, False)
    time.sleep(0.5)

timer=0

while timer < 10:
	print(f"Counter: {timer}")
	timer = timer + 1

	blink()
