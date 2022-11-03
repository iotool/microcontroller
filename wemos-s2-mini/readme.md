# WeMos S2 mini / ESP32-S2 (S2FN4R2)

* ESP32-S2FN4R2 Xtensa® 32-bit LX7 CPU, on-chip, 240MHz, 3V3
* WiFi 2.4GHz IEEE 802.11b/g/n (no Bluetooth!), 150Mbps, 20+40 MHz bandwidth
* 4MB Flash, 2MB PSRAM (Psuedostatic DRAM), 320KB SRAM, 128KB ROM, 16KB SRAM in RTC
* CircuitPython firmware

| Feature | WeMos S2 mini | WeMos D1 mini |
| --- | --- | --- |
| MCU | ESP32-S2 (2019) | ESP8266 (2014) |
| CPU | Xtensa single-core 32-bit LX7 | Xtensa single-core 32-bit L106 | 
| Clock | 240 MHz | 80 MHz |
| SRAM | 320 KB | 160 KB |
| RTC Memory | 16 KB | 512 B |
| WiFi | 2.4 GHz | 2.4 GHz |
| Bluetooth | - | - |
| Features | USB, DAC, ADC, Temp | ADC |
| Low Power | 5uA (58uA) | 20uA |

## CircuitPython

With CircuitPython you can use MicroPython to develop firmware. 

* pre-installed firmware: CircuitPython 7.3.0 on 2022-05-23
* connect to computer with USB data cable
* mount new drive "CIRCUITPY" with 940KB
* edit firmware file \code.py and optional \boot.py

Debug serial output to Putty

* use "zadig-2.7.exe" to install driver "USB Serial (CDC)" at Win7
* set COM-baud to 115200 at windows device manager
* set COM-baud tp 115200 at putty serial connection

Deep Sleep

* 58uA at deep sleep powered by 4.5 VBUS (3x AAA)
* no extra wire or resistor needed
* wakeup by time and/or builtin button D0 
* 80uA average messure 1 second every 60 minutes = 312 days @600mAh
* 180uA average messure 1 second every 10 minutes = 138 days @600mAh
* 1,25mA average messure 1 second every 1 minute = 20 days @600mAh

## Photo

![](https://github.com/iotool/microcontroller/blob/main/wemos-s2-mini/wemos-s2-mini-v100-a.jpg?raw=true)

![](https://github.com/iotool/microcontroller/blob/main/wemos-s2-mini/wemos-s2-mini-v100-b.jpg?raw=true)
