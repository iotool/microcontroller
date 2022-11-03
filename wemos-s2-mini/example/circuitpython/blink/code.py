import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("blink")
while True:
	led.value = True
	print("on")
	time.sleep(0.5)
	led.value = False
	print("off")
	time.sleep(0.5)
