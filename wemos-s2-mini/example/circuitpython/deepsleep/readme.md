# Deep sleep with CircuitPython 7.3.0

* WeMos S2 mini has native support for deep sleep
* no extra resistor or wire is needed
* only consume 58uA @ 4.5Vbus

## execution

* 5.7 Ohm resistor @ 4.11 VBUS
* 140mV = 24.6mA / 84mV = 14.7mA

![](https://raw.githubusercontent.com/iotool/microcontroller/main/wemos-s2-mini/example/circuitpython/deepsleep/deepsleep-a-cpy730-esp32s2.jpg)

## periode

* 1262ms boot @ 38mA 171mW
* 1000ms code @ 26mA 117mW
* 8938ms sleep @ 58uA 261uW

![](https://raw.githubusercontent.com/iotool/microcontroller/main/wemos-s2-mini/example/circuitpython/deepsleep/deepsleep-b-cpy730-esp32s2.jpg)

![](https://raw.githubusercontent.com/iotool/microcontroller/main/wemos-s2-mini/example/circuitpython/deepsleep/deepsleep-c-cpy730-esp32s2.jpg)
