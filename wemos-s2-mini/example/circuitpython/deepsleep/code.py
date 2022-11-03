# boot   38mA  171mW  1200ms - execute bootloader
# code   26mA  117mW  1000ms - execute program or usb-connected
# sleep  58uA  261uW    20s  - deep sleep, if not usb-connected

import time
import board
import digitalio
import alarm

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True
print("on")
time.sleep(0.5)
led.value = False
print("off")
time.sleep(2.5)

# start wakeup after 20 seconds or if button d0 pressed
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 20)
pin_alarm = alarm.pin.PinAlarm(pin=board.BUTTON, value=False, pull=True)
# exit the program, and then deep sleep until the alarm wakes us.
alarm.exit_and_deep_sleep_until_alarms(time_alarm, pin_alarm)
