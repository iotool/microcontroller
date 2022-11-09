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

builtin features

* push button as digital input (board.BUTTON)
* blue led as digital output (board.LED)
* blue led as analog light sensor (board.LED)
* temp sensor (microcontroller.cpu.temperature)
* vbat sensor (board.IO14)
* wifi access point / webserver (webapp)
* wifi station / mesh (iot)
* flash memory (filesystem, logging)
* usb hid / storage (keyboard, memory)

## CircuitPython

With CircuitPython you can use MicroPython to develop firmware. 

* pre-installed firmware: CircuitPython 7.3.0 on 2022-05-23
* connect to computer with USB data cable
* mount new drive "CIRCUITPY" with 940KB
* edit firmware file \code.py and optional \boot.py
* flash new firmware release [wemos](https://www.wemos.cc/en/latest/tutorials/s2/get_started_with_circuitpython_s2.html), [circuitpython](https://circuitpython.org/board/lolin_s2_mini/)

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

![](https://raw.githubusercontent.com/iotool/microcontroller/main/wemos-s2-mini/wemos-s2-mini-esp32s2-pinout.jpg)

![](https://github.com/iotool/microcontroller/blob/main/wemos-s2-mini/wemos-s2-mini-v100-a.jpg?raw=true)

```
GND -- |Boot| ------- board.BUTTON ~IO0
GND -- |< -- [2k] --- board.LED    ~IO15
GND -- |RST| +------- EN
             +-[10k]- 3V3
3V3 -- [10k] -------- board.IO18   ~USB
```
![](https://github.com/iotool/microcontroller/blob/main/wemos-s2-mini/wemos-s2-mini-v100-b.jpg?raw=true)

| PIN | IO | D2 | Comment |
| --- | --- | --- | --- |
| 3.3V | 3V3 | 3V3 | VCC |
| 5.0V | VBUS | 5V | VUSB |
| GND | GND | GND | Ground |
| EN | EN | RST| Reset-Button |
| - | 00 | - | Boot-Button |
| 01 | 01 | - |  ADC, Touch, RTC |
| 02 | 02 | - | ADC, Touch, RTC |
| 03 | 03 | A0 | ADC, Touch, RTC |
| 04 | 04 | - | ADC, Touch, RTC |
| 05 | 05 | D0 | ADC, Touch, RTC |
| 06 | 06 | - | ADC, Touch, RTC |
| 07 | 07 | D5 | ADC, Touch, RTC, SCK |
| 08 | 08 | - | ADC, Touch, RTC |
| 09 | 09 | D6 | ADC, Touch, RTC, MISO |
| 10 | 10 | - | ADC, Touch, RTC |
| 11 | 11 | D7 | ADC, Touch, RTC, MOSI |
| 12 | 12 | D8 | ADC, Touch, RTC |
| 13 | 13 | (D8) | ADC, Touch, RTC |
| 14 | 14 | - | ADC, Touch, RTC |
| 15 | 15 | - | ADC, Touch, RTC, LED |
| 16 | 16 | D4 | ADC, Touch, RTC |
| 17 | 17 | - | ADC, Touch, RTC, DAC |
| 18 | 18 | D3 | ADC, Touch, RTC, D3, DAC |
| 21 | 21 | - | ADC, Touch, RTC, XTAL |
| 33 | 33 | D2 | SDA |
| 34 | 34 | - | |
| 35 | 35 | D1 | SCL |
| 36 | 36 | - | |
| 37 | 37 | RX | |
| 38 | 38 | - | |
| 39 | 39 | TX | |
| 40 | 40 | - | |

