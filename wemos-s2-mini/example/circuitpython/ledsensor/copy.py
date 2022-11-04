#             avg   gap
# blackness  <200  >64
# darkness   <150  <32
# blinking   >200  >200
# dimmed     >500  >32
# full       >500  <16

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
min = 128
avg = 384
max = 768
gap = max-min
rnd = 0

while True:
	val = pin.value/64
	avg = (3*avg+val)/4
	if val<avg:
		min = (min+val)/2
	if val>avg:
		max = (max+val)/2
	gap = max-min
	print(math.ceil(avg), math.ceil(gap))
	time.sleep(0.1)
	# detect blinking light and turn led on
	rnd = rnd+1
	if ((rnd>100) and (math.ceil(avg)>200) and (math.ceil(gap)>200)):
		rnd = 0
		pin.deinit()
		led = digitalio.DigitalInOut(board.LED)
		led.direction = digitalio.Direction.OUTPUT
		led.value = True
		time.sleep(3.0)
		led.deinit()
		pin = analogio.AnalogIn(board.LED)

