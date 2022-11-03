import time
import board
import digitalio

LED_M1_ON = 0.1
LED_M1_OFF = 0.9
LED_M2_ON = 0.4
LED_M2_OFF = 0.1

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
ledon = LED_M1_ON
ledoff = LED_M1_OFF

btn = digitalio.DigitalInOut(board.BUTTON)
btn.switch_to_input(pull=digitalio.Pull.UP)

print("button")
while True:
	print(btn.value)
	if btn.value:
		ledon = LED_M1_ON
		ledoff = LED_M1_OFF
	else:
		ledon = LED_M2_ON
		ledoff = LED_M2_OFF
	led.value = True
	time.sleep(ledon)
	led.value = False
	time.sleep(ledoff)
