# LED as sensor

* you can use the builtin led as a light sensor
* every led produce voltage depend on light level
* for WeMos S2 mini we use adc of GPIO15

## light pattern

* blackness = low average and high oscillations
* darkness = low average and low oscillations
* light = high average and low oscillations
* blinking = high average and high oscillations

![](https://raw.githubusercontent.com/iotool/microcontroller/main/wemos-s2-mini/example/circuitpython/ledsensor/led-as-sensor-wemos-s2-mini-esp32s2.png)

## light sensor

* avg = average kpi
* gap = oscillation kpi
* min = low oscillation
* max = high oscillation

![](https://raw.githubusercontent.com/iotool/microcontroller/main/wemos-s2-mini/example/circuitpython/ledsensor/led-as-sensor2-wemos-s2-mini-esp32s2.png)
