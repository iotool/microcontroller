import time
import board
import digitalio
import analogio

led = digitalio.DigitalInOut(board.LED)
led.switch_to_input()

while True:
  # detect bright light (e.g. smartphone led)
  if led.value:
    led.switch_to_output()
    led.value=True
    time.sleep(1.5)
    led.value=False
    time.sleep(0.5)
    led.switch_to_input()
  time.sleep(0.1)
