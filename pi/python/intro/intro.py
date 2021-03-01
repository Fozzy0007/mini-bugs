from adafruit_ble import BLERadio
from adafruit_ble.services.nordic import UARTService

import time 

class Echo:
    str=""
    def setString(self, _str):
        self.str = _str
    def getString(self):
        return self.str



echo = Echo()
echo.setString("foo")
prStr = echo.getString()
print(prStr)


ble = BLERadio()


print("scanning")
found = set()
scan_responses = set()
for advertisement in ble.start_scan():
    addr = advertisement.address
    if advertisement.scan_response and addr not in scan_responses:
        scan_responses.add(addr)
    elif not advertisement.scan_response and addr not in found:
        found.add(addr)
    else:
        continue
    # print(addr, advertisement)
    # print("\t" + repr(advertisement))
    # print()
    if advertisement.complete_name == "CIRCUITPYa925":
        uart_connection = ble.connect(advertisement)
        print("hello beetle")
        ble.stop_scan()
        break
# connection = ble.connect("CIRCUITPYa925")
# if ble.connected:
#     print("connected!")

if uart_connection:
    uart = uart_connection[UARTService]
    time.sleep(3)
    if uart.in_waiting:
        data = uart.read(5)
        print(data)
        

    

print ("goodbye!")

