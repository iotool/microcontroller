# https://github.com/deckerego/ampule/blob/main/examples/webserver/webpages.py
# https://github.com/deckerego/ampule/blob/main/examples/digitalio/led.py

import time
import wifi
import board
import socketpool
import ampule
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
time.sleep(1.0)
led.value = False

# access point

macap="".join("%02X" % _ for _ in wifi.radio.mac_address_ap)
ssidap="ESP-"+macap[6:12]+" (http://192.168.4.1)"
wifi.radio.start_ap(ssidap, "12345678")
print("AP SSID",ssidap) 
print("AP MAC", ":".join("%02X" % _ for _ in wifi.radio.mac_address_ap))

# webserver

headers = {
	"Content-Type": "application/json; charset=UTF-8",
	"Access-Control-Allow-Origin": '*',
	"Access-Control-Allow-Methods": 'GET, POST',
	"Access-Control-Allow-Headers": 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
}

@ampule.route("/on")
def httpLedOn(request):
	print("/on")
	led.value = True
	return (200, headers, '{"enabled": true}')

@ampule.route("/off")
def httpLedOff(request):
	print("/off")
	led.value = False
	return (200, headers, '{"enabled": false}')

def dataPage():
	content = f"""
	<html><body>
	Test 
	<a href=/on>ON</a> 
	<a href=/off>OFF</a> 
	<a href=/test>TEST</a> 
	<a href=/file/test_htm>file-htm</a> 
	<a href=/file/test_txt>file-txt</a> 
	<a href=/parm?name=test>parm</a> 
	</body></html>
	"""
	return content

def dataFile():
	with open('file_test.htm') as local_file:
		content = local_file.read()
	return content

@ampule.route("/home")
def httpHome(request):
	print("/home")
	return (200, {}, dataPage())

@ampule.route("/test")
def httpTest(request):
	print("/test")
	return (200, {}, dataFile())

@ampule.route("/file/<name>")
def httpFile(request, name):
	fn="file_%s" % name
	ft="text/html"
	if (fn.endswith('txt')):
		ft="text/plain"
		fn=fn[0:-4]+".txt"
	if (fn.endswith('htm')):
		ft="text/html"
		fn=fn[0:-4]+".htm"
	print("/file/%s" % name)
	with open(fn) as local_file:
		fdata = local_file.read()
	return (200, {}, fdata)

@ampule.route("/parm")
def httpParm(request):
	name = request.params["name"]
	print("/parm?name=%s" % name)
	return (200, {}, "Hi there %s!" % name)

pool = socketpool.SocketPool(wifi.radio)
socket = pool.socket()
socket.bind(['0.0.0.0', 80])
socket.listen(1)

print("ESP32-S2-mini webserver")
print("http://192.168.4.1/")
print("http://192.168.4.1/on")
print("http://192.168.4.1/off")
print("http://192.168.4.1/test")
print("http://192.168.4.1/file/test_htm")
print("http://192.168.4.1/parm?name=test")

while True:
	time.sleep(0.1)
	ampule.listen(socket)
