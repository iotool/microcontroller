import alarm
import time
import math
import board
import storage

UNKNOWN = 0
RESETBUTTON = 1
BOOTBUTTON = 2
WAKEUPTIMER = 3

debug = False
memory_offset = 0
boot_reason = UNKNOWN

def start(iMemOffset):
  global boot_reason, memory_offset
  memory_offset = iMemOffset
  # index of sleep_memory
  iLastHi = memory_offset+0
  iLastLo = memory_offset+1
  iWaitHi = memory_offset+2
  iWaitLo = memory_offset+3
  # restore prior timestamp and periode
  tLast = alarm.sleep_memory[iLastHi]*256+alarm.sleep_memory[iLastLo]
  tWait = alarm.sleep_memory[iWaitHi]*256+alarm.sleep_memory[iWaitLo]
  # current timestamp
  tNow = time.time() % 65536
  # calculate sleep time
  if tLast <= tNow:
    tSleep = tNow-tLast
  else:
    tSleep = tNow+(65536-tLast)
  if debug:
    print("iotool_reboot: init mempos",memory_offset)
    print("iotool_reboot: init now",tNow)
    print("iotool_reboot: init last",tLast)
    print("iotool_reboot: init wait",tWait)
    print("iotool_reboot: init sleep",tSleep)
  # boot reason
  if not alarm.wake_alarm:
    boot_reason = RESETBUTTON
    if debug:
      print("iotool_reboot: init resetbutton")
  elif tSleep < tWait:
    boot_reason = BOOTBUTTON
    if debug:
      print("iotool_reboot: init bootbutton")
  else:
    boot_reason = WAKEUPTIMER
    if debug:
      print("iotool_reboot: init wakeuptimer")

def deepsleep(tSleep):
  # index of sleep_memory
  iLastHi = memory_offset+0
  iLastLo = memory_offset+1
  iWaitHi = memory_offset+2
  iWaitLo = memory_offset+3
  # store last timestamp
  tNow = time.time() % 65536
  tNowLo = tNow % 256
  tNowHi = tNow >> 8
  alarm.sleep_memory[iLastHi] = tNowHi
  alarm.sleep_memory[iLastLo] = tNowLo
  # store sleep periode (8.938 = 10s)
  tWait = math.ceil(tSleep) % 65536
  tWaitLo = tWait % 256
  tWaitHi = tWait >> 8
  alarm.sleep_memory[iWaitHi] = tWaitHi
  alarm.sleep_memory[iWaitLo] = tWaitLo
  # debug
  if debug:
    print("iotool_reboot: exit mempos",memory_offset)
    print("iotool_reboot: exit sleep",tSleep,"s")
    print("iotool_reboot: exit wait",tWait,"s")
  # deep sleep
  aTime = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + tSleep)
  aPin = alarm.pin.PinAlarm(pin=board.BUTTON, value=False, pull=True)
  alarm.exit_and_deep_sleep_until_alarms(aTime, aPin)
