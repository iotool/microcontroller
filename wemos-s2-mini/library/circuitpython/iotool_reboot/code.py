import time
import board
import digitalio
import iotool_reboot

iotool_reboot.debug = True
iotool_reboot.start(5)
print("iotool_reboot.boot_reason: ",iotool_reboot.boot_reason)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

for i in range(iotool_reboot.boot_reason):
  led.value = False
  time.sleep(0.2)
  led.value = True
  time.sleep(0.1)
  led.value = False
  time.sleep(0.2)
time.sleep(1)

iotool_reboot.deepsleep(8.938)
