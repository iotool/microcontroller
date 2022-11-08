import board
import digitalio
import analogio
import microcontroller
import time
import math

debug = False
memory_offset = 0

temperature = 0
battery = 0
light = 0
oscillation = 0

def messure():
  global battery, temperature, light, oscillation 
  # --- messure battery 0..100% ---
  pBat = analogio.AnalogIn(board.IO14)
  vBatAvg = 0.0
  n = 4
  for i in range(n):
    time.sleep(0.001)
    vBat = pBat.value
    vBatAvg = vBatAvg + vBat
  pBat.deinit()
  vBatAvg = vBatAvg / n
  battery = (vBatAvg-12500)/50
  # --- messure temperature -20..60C ---
  vTmpAvg = 0.0
  n = 35
  for i in range(n):
    time.sleep(0.001)
    vTmp = microcontroller.cpu.temperature
    vTmpAvg = vTmpAvg + vTmp
  vTmpAvg = vTmpAvg / n
  temperature = vTmpAvg
  # --- messure light 0..100% ---
  # led off for 5ms
  pLed = digitalio.DigitalInOut(board.LED)
  pLed.direction = digitalio.Direction.OUTPUT
  pLed.value = False
  time.sleep(0.005)
  pLed.deinit()
  # pre messure 5 times
  pLed = analogio.AnalogIn(board.LED)
  vLedAvg = 0.0
  vLedMinS = 0.0
  vLedMinN = 0
  vLedMaxS = 0.0
  vLedMaxN = 0
  n = 10
  for i in range(n):
    time.sleep(0.001)
    vLed = pLed.value
  n = 35
  for i in range(n):
    time.sleep(0.001)
    vLed = pLed.value
    vLedAvg = vLedAvg + vLed
    if i >= 5:
      vLedMed = vLedAvg / (i+1)
      if vLed < vLedMed:
        vLedMinN = vLedMinN + 1
        vLedMinS = vLedMinS + vLed
      if vLed > vLedMed:
        vLedMaxN = vLedMaxN + 1
        vLedMaxS = vLedMaxS + vLed
  pLed.deinit()
  vLedAvg = vLedAvg / n
  vLedMin = vLedAvg
  if vLedMinN > 0: vLedMin = vLedMinS / vLedMinN
  vLedMax = vLedAvg
  if vLedMaxN > 0: vLedMax = vLedMaxS / vLedMaxN
  vLedStd = math.sqrt((vLedMax-vLedAvg)*(vLedAvg-vLedMin))
  light = vLedAvg/440
  oscillation = vLedStd/vLedAvg*100
