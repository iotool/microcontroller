# IotoolReboot

Handle deep sleep and boot reason

bootreason:
* RESETBUTTON ~ reset button was pressed
* BOOTBUTTON ~ boot button was pressed
* WAKEUPTIMER ~ deep sleep timeout reached

tbd:
* time.monotonic() keep on running at usb after fake deep sleep
* time.monotonic() cleared at battery after deep sleep
