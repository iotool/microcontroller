# Deep sleep with CircuitPython 7.3.0

* WeMos S2 mini has native support for deep sleep
* no extra resistor or wire is needed
* only consume 58uA @ 4.5Vbus

## execution

* 5.7 Ohm resistor @ 4.11 VBUS
* 24.6mA (140mV) / 14.7mA (84mV) with oszi
* 38mA / 26mA with multimeter

![](https://raw.githubusercontent.com/iotool/microcontroller/main/wemos-s2-mini/example/circuitpython/deepsleep/deepsleep-a-cpy730-esp32s2.jpg)

* phase 1 = 500ms wait (boot-button)
* phase 2 = 768ms init (rf calibration)
* phase 3 = 1000ms code (circuit python)
* phase 4 = 8938ms sleep

## periode

power consumption

* 1262ms boot @ 38mA 171mW
* 1000ms code @ 26mA 117mW
* 8938ms sleep @ 58uA 261uW

average consumption

* 10sec periode = 7.45mA 34mW
* 60sec periode = 1.29mA 5.8mW
* 10min periode = 0.181mA 0.81mW
* 60min periode = 0.079mA 0.35mW

![](https://raw.githubusercontent.com/iotool/microcontroller/main/wemos-s2-mini/example/circuitpython/deepsleep/deepsleep-b-cpy730-esp32s2.jpg)

![](https://raw.githubusercontent.com/iotool/microcontroller/main/wemos-s2-mini/example/circuitpython/deepsleep/deepsleep-c-cpy730-esp32s2.jpg)
