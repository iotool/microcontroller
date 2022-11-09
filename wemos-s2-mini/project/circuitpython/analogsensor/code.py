# Wemos S2 mini - Analog Sensor
# 
# IO18 -- LDR -- IO34  light
# IO17 -- NTC -- IO36  temperature
# IO15 -- 20k -- IO17  voltage

import time
import board
import digitalio
import analogio
import math
import storage

def readTemperature():
  p17s = analogio.AnalogIn(board.IO17)
  p36v = digitalio.DigitalInOut(board.IO36)
  p36v.direction = digitalio.Direction.INPUT
  p36v.pull = digitalio.Pull.UP
  p15g = digitalio.DigitalInOut(board.IO15)
  p15g.direction = digitalio.Direction.INPUT
  p15g.pull = digitalio.Pull.DOWN
  p36v.direction = digitalio.Direction.OUTPUT
  p36v.value = True
  p15g.direction = digitalio.Direction.OUTPUT
  p15g.value = False
  time.sleep(0.01)
  n = 5
  val = 0
  for i in range(n):
    val = val + p17s.value
    time.sleep(0.01)
  v17 = math.ceil(val/n)
  p15g.deinit()
  p36v.deinit()
  p17s.deinit()
  # scaling -40..80 C
  rco  = 20000  # ohm 10040
  t25  = 298.15 # K
  r25  = 10000  # ohm 9970
  beta = 3950   # K 3119
  vu = 3.3-v17/32009*1.60
  vr = (vu/3.3*rco)/(1-vu/3.3)
  vt = 1/(math.log(vr/r25)/beta+1/t25)-273.15
  v17 = vt
  return v17

def readLight():
  save = True
  p18s = analogio.AnalogIn(board.IO18)
  p34g = digitalio.DigitalInOut(board.IO34)
  if save:
    # 165uA use internal pullup resistor
    p34g.direction = digitalio.Direction.INPUT
    p34g.pull = digitalio.Pull.DOWN
  if not save:
    # 330uA don't use internal pullup resistor
    p34g.direction = digitalio.Direction.OUTPUT
    p34g.value = False
  time.sleep(0.01)
  n = 5
  val = 0
  for i in range(n):
    val = val + p18s.value
    time.sleep(0.01)
  v18 = math.ceil(val/n)
  p34g.deinit()
  p18s.deinit()
  # scaling 0..100
  if v18 > 53619:
    v18 = 53619
  if save:
    if v18 < 49990:
      v18 = 49990
    v18 = (53619-v18)/36.29
  if not save:
    v18 = (53619-v18)/536.19
  return v18

def readVoltage():
  p15s = analogio.AnalogIn(board.IO15)
  p36n = digitalio.DigitalInOut(board.IO36)
  p36n.direction = digitalio.Direction.INPUT
  p36n.pull = digitalio.Pull.UP
  p17v = digitalio.DigitalInOut(board.IO17)
  p17v.direction = digitalio.Direction.INPUT
  p17v.pull = digitalio.Pull.UP
  #p17v.direction = digitalio.Direction.OUTPUT
  #p17v.value = True
  time.sleep(0.01)
  n = 5
  val = 0
  for i in range(n):
    val = val + p15s.value
    time.sleep(0.01)
  v15 = math.ceil(val/n)
  p17v.deinit()
  p36n.deinit()
  p15s.deinit()
  # scaling 3.00..3.31 V
  sla = 50429   # adc    52893  50429
  slv = 3.09    # v      3.04   3.09
  sha = 50100   # adc    52784
  shv = 3.31    # v      3.31
  sda = sla-sha #        109
  sdv = shv-slv #        0.27
  vin = shv-sdv/sda*(v15-sha)
  v15 = vin
  return v15

logging = False

if logging:
  try:
    with open("/datalog.txt", "a") as fp:
      fp.write('reset\n')
      fp.flush()
      fp.close()
  except OSError as e:
    print("error log file")

while True:
  vBat = readVoltage()
  vTmp = readTemperature()
  vLgt = readLight()
  print(vBat,vTmp,vLgt)
  led = digitalio.DigitalInOut(board.LED)
  led.direction = digitalio.Direction.OUTPUT
  led.value = False
  if logging:
    try:
      with open("/datalog.txt", "a") as fp:
        fp.write('{0:f} '.format(vBat))
        fp.write('{0:f} '.format(vTmp))
        fp.write('{0:f}\n'.format(vLgt))
        fp.flush()
        fp.close()
    except OSError as e:
      print("error log file")
    time.sleep(5)
  led.deinit()
  time.sleep(0.1)
