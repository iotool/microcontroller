import time
import alarm
import board
import digitalio
import analogio
import microcontroller
import math
import iotool_reboot

print("Wemos-S2-mini")

# boot reason
iotoolReboot = iotool_reboot.IotoolReboot(0)

# boot 
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

if iotoolReboot.bootreason == iotool_reboot.RESETBUTTON:
  # led blinking fast 2500ms
  i=25
  while i>0:
    i=i-1
    led.value = True
    time.sleep(0.05)
    led.value = False
    time.sleep(0.05)
elif iotoolReboot.bootreason == iotool_reboot.BOOTBUTTON:
  # led on 2500ms
  led.value = True
  time.sleep(2.4)
  led.value = False
  time.sleep(0.1)
elif iotoolReboot.bootreason == iotool_reboot.WAKEUPTIMER:
  # led on 10ms
  led.value = True
  time.sleep(0.01)
  led.value = False
  time.sleep(0.1)
led.deinit()

# deep sleep
iotoolReboot.deepsleep(8.938)
