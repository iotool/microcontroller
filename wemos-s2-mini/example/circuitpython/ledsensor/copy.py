# blackness  140 -/+ 15
# darkness   140 -/+ 8
# blinking   400 -/+ 150
# dimmed     520 -/+ 25
# full       555 -/+ 4

import time
import board
import digitalio
import analogio
import math

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True
print("on")
time.sleep(0.5)
led.value = False
print("off")
time.sleep(0.5)

led.deinit()
pin = analogio.AnalogIn(board.LED)

while True:
	print(math.ceil(pin.value/64))
	time.sleep(0.1)
