import time
import board
import digitalio
import alarm

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

if not alarm.wake_alarm:
  print("first boot")
  alarm.sleep_memory[5] = 1
else:
  n = 1
  print("wakeup after deep sleep")
  alarm.sleep_memory[5] = alarm.sleep_memory[5]+1

n = alarm.sleep_memory[5]
print("rtcmem[5]",alarm.sleep_memory[5])

for i in range(n):
  led.value = True
  time.sleep(0.1)
  led.value = False
  time.sleep(0.4)
time.sleep(1)

# periode 5s = wakeup after 3.938 seconds or if button d0 pressed
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 8.938)
pin_alarm = alarm.pin.PinAlarm(pin=board.BUTTON, value=False, pull=True)
# exit the program, and then deep sleep until the alarm wakes us.
alarm.exit_and_deep_sleep_until_alarms(time_alarm, pin_alarm)
