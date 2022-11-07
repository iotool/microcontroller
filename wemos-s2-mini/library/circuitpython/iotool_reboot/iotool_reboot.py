import alarm
import time
import math
import board

RESETBUTTON = 1
BOOTBUTTON = 2
WAKEUPTIMER = 3

class IotoolReboot:

  pLoopHi = 4
  pLoopLo = 5

  def __init__(self, mempos):
    # memory position
    self.pFlagHi = mempos+0
    self.pFlagLo = mempos+1
    self.pLastHi = mempos+2
    self.pLastLo = mempos+3
    self.pLoopHi = mempos+4
    self.pLoopLo = mempos+5
    # sleep time
    tLast = alarm.sleep_memory[self.pLastHi]*256+alarm.sleep_memory[self.pLastLo]
    tLoop = alarm.sleep_memory[self.pLoopHi]*256+alarm.sleep_memory[self.pLoopLo]
    tNow = math.ceil(time.monotonic()*10) % 655536
    tNowLo = tNow % 256
    tNowHi = math.ceil((tNow-tNowLo)/256)
    alarm.sleep_memory[self.pLastHi] = tNowHi
    alarm.sleep_memory[self.pLastLo] = tNowLo
    if tLast <= tNow:
      tSleep = tNow-tLast
    else:
      tSleep = tNow+(655536-tLast)
    # boot reason
    if not alarm.wake_alarm:
      self.bootreason = RESETBUTTON
      print("iotool_reboot: resetbutton")
    elif tSleep < tLoop:
      self.bootreason = BOOTBUTTON
      print("iotool_reboot: bootbutton")
    else:
      self.bootreason = WAKEUPTIMER
      print("iotool_reboot: wakeuptimer")

  @classmethod
  def deepsleep(self, tNext):
    print("iotool_reboot: sleep",tNext,"s")
    # periode 8.938 = 10s
    tLoop = math.ceil(tNext*10) % 655536
    tLoopLo = tLoop % 256
    tLoopHi = math.ceil((tLoop-tLoopLo)/256)
    alarm.sleep_memory[self.pLoopHi] = tLoopHi
    alarm.sleep_memory[self.pLoopLo] = tLoopLo
    # sleep
    aTime = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + tNext)
    aPin = alarm.pin.PinAlarm(pin=board.BUTTON, value=False, pull=True)
    alarm.exit_and_deep_sleep_until_alarms(aTime, aPin)