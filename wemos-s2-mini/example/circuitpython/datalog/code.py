import time
import board
import digitalio
import analogio
import storage
import microcontroller

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
btn = digitalio.DigitalInOut(board.BUTTON)
btn.switch_to_input(pull=digitalio.Pull.UP)
log = True

print("press boot to disable logging to file")
i=25
while i>0:
  i=i-1
  if not btn.value:
    log = False
    i=0
  led.value = True
  time.sleep(0.01)
  led.value = False
  time.sleep(0.09)

if not log:
  print("log disabled")
  for i in range(5):
    led.value = True
    time.sleep(0.3)
    led.value = False
    time.sleep(0.2)

if log:
  print("log enabled")
  led.value = True
  time.sleep(2.4)
  led.value = False
  time.sleep(0.1)

led.deinit()
btn.deinit()
i = 0
while True:
  i = i+1
  # led flash
  led = digitalio.DigitalInOut(board.LED)
  led.direction = digitalio.Direction.OUTPUT
  led.value = True
  time.sleep(0.001)
  led.value = False
  led.deinit()
  # messure led
  p15 = analogio.AnalogIn(board.LED)
  v15 = p15.value
  p15.deinit()
  p14 = analogio.AnalogIn(board.IO14)
  v14 = p14.value
  p14.deinit()
  p18 = analogio.AnalogIn(board.IO18)
  v18 = p18.value
  p18.deinit()
  tmp = microcontroller.cpu.temperature
  # display values
  print(i,v14,v15,v18,tmp)
  if log:
    try:
      with open("/datalog.txt", "a") as fp:
        fp.write('{0:d} '.format(i))
        fp.write('{0:d} '.format(v14))
        fp.write('{0:d} '.format(v15))
        fp.write('{0:d} '.format(v18))
        fp.write('{0:f}\n'.format(tmp))
        fp.flush()
        fp.close()
    except OSError as e:
      print("error log file")
  # delay
  led = digitalio.DigitalInOut(board.LED)
  led.direction = digitalio.Direction.OUTPUT
  led.value = False
  time.sleep(5)
  led.deinit()
