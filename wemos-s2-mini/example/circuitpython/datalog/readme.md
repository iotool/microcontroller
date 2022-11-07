# datalog sensor value to flash drive

logging mode:
* plugin / power on
* 2 seconds - led off
* 2 seconds - led blink fast / boot don't pressed
* 2 seconds - led on
* log sensor values to flash drive

nologging mode:
* plugin / power on
* 2 seconds - led off
* 2 seconds - led blink fast and boot pressed
* 2 seconds - led blink slow
* log sensor values don't write to flash drive
* download datalog.txt

save mode:
* plugin / power on
* 2 seconds - led off
* fast push/release boot
* code.py editable

## GPIO14 as voltage sensor

For battery-powered sensors, you can detect when the voltage drops below 3.3V.

* GPIO14 changes its ADC value depending on the voltage
* 41100 = 5.00V USB-powered
* 41100 = 4.50V VBUS-battery
* 37500 = 3.20V 3V3-battery
* 34800 = 3.06V 3V3-battery
