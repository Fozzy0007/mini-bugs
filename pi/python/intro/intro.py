from adafruit_ble import BLERadio
from adafruit_ble.services.nordic import UARTService

from BugPacket import BugCommandFactory, EchoCommand, EchoResponse
import time 

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
    if advertisement.complete_name == "CIRCUITPYa925":
        uart_connection = ble.connect(advertisement)
        print("connected to beetle")
        ble.stop_scan()
        break

# we've connected, let's make sure we have a uart connection
if uart_connection:
    uart = uart_connection[UARTService]
    echoSent = False
    while uart_connection.connected:
        if uart.in_waiting:
            # Read the packet
            command = int.from_bytes(uart.read(1), "little")
            length =int.from_bytes(uart.read(1), "little")
            data = uart.read(length)
            tup = (command, length, data)

            # Create the command object
            req = BugCommandFactory.CreateFromTuple(tup)
            # act upon the command object
            if isinstance(req, EchoCommand):
                print("Will echo: " + req.getMessage())
                res = EchoResponse(req.getMessage())
                uart.write(res.getDataBytes())
            elif isinstance(req, EchoResponse):
                print("Response: " + req.getMessage())
                break
        elif not echoSent:
            print("Will send an echo request")
            echo = EchoCommand("Hello Beetle")
            uart.write(echo.getDataBytes())
            echoSent = True
        

    

print ("goodbye!")

