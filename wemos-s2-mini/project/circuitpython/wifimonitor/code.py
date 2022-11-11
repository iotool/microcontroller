import time
import board
import digitalio
import alarm
import wifi
import socketpool
import ssl
import ipaddress
import microcontroller

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = False

try:
  import adafruit_requests
except ImportError:
  print("error library adafruit_requests.py not found!")
  raise

try:
  from iotool_wifimonitor import wifimonitor
except ImportError:
  print("error library iotool_wifimonitor.py not found!")
  raise

print("iotool_wifimonitor")

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

def ledblink():
  led.direction = digitalio.Direction.INPUT
  led.pull = digitalio.Pull.UP
  time.sleep(0.001)
  led.direction = digitalio.Direction.OUTPUT
  led.value = False
  

while True:
  # access point 1..9
  for i in range(10):
    if wifimonitor.get("ap"+str(i)+"_ssid"):
      # connect to access point
      print("wifi connect",i,":",wifimonitor["ap"+str(i)+"_ssid"])
      ap_ssid = wifimonitor["ap"+str(i)+"_ssid"]
      ap_auth = wifimonitor["ap"+str(i)+"_auth"]
      furl = ""
      fcnt = 0
      try:
        wifi.radio.connect(ssid=ap_ssid,password=ap_auth,timeout=20.0)
        print(".. connect ipaddr:", wifi.radio.ipv4_address)
        ledblink()
        # field 1..7
        for f in range(8):
          fval = 0
          # device 1,2,4,8
          for d in range(9):
            if wifimonitor.get("thingspeak_f"+str(f)+str(d)+"_name"):
              ip_name = wifimonitor["thingspeak_f"+str(f)+str(d)+"_name"]
              ip_addr = wifimonitor["thingspeak_f"+str(f)+str(d)+"_addr"]
              ip_v4 = ipaddress.ip_address(ip_addr)
              ip_ping = wifi.radio.ping(ip=ip_v4,timeout=1)
              if not ip_ping is None:
                # device ping successful
                ledblink()
                fval = fval + d
                fcnt = fcnt + 1 
              print(".. ping "+ip_addr+" "+ip_name+" "+str(ip_ping))
          furl = furl + "&field"+str(f)+"="+str(fval)
        # log device at thingspeak
        if fcnt > 0:
          furl = "https://api.thingspeak.com/update?api_key="+wifimonitor["thingspeak_writekey"]+furl
          furl = furl+"&field8="+str(i)
          print(".. request",furl)
          response = requests.get(furl)
          print(".. response",response.text)
          # response.close()
        wifi.radio.stop_station()
        print(".. disconnect")
        # delay quota of thingspeak
        if fcnt > 0:
          print(".. wait")
          time.sleep(20)
      except ConnectionError:
        print(".. not found")
      except RuntimeError:
        print(".. runtime error / reset")
        time.sleep(20)
        microcontroller.reset()
        time.sleep(20)
