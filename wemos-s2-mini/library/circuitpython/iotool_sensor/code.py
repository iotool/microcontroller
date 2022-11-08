import time
import board
import digitalio
import alarm
import iotool_sensor

iotool_sensor.messure()
print(iotool_sensor.light,iotool_sensor.oscillation,iotool_sensor.battery,iotool_sensor.temperature)
try: 
  with open("/datalog.txt", "a") as fp:
    fp.write('{0:f} '.format(iotool_sensor.light))
    fp.write('{0:f} '.format(iotool_sensor.oscillation))
    fp.write('{0:f} '.format(iotool_sensor.battery))
    fp.write('{0:f}\n'.format(iotool_sensor.temperature))
    fp.flush()
    fp.close()
except OSError as e:
  print("error log file")

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
time.sleep(0.01)
led.value = False
led.deinit()

# restart after 58 seconds
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 58.938)
pin_alarm = alarm.pin.PinAlarm(pin=board.BUTTON, value=False, pull=True)
alarm.exit_and_deep_sleep_until_alarms(time_alarm, pin_alarm)