from BugPacket import EchoRequest, EchoResponse, BugCommandFactory
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

from CpbSensorData import CpbSensorData

import time
import board
import neopixel
import adafruit_thermistor


# thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)
# temp_c = thermistor.temperature
# temp_f = thermistor.temperature * 9 / 5 + 32
print(dir(board))
sensors = CpbSensorData()
print("Temperature is: %f F" %(sensors.getTemperatureInF()))
print("Light value is: %f " %(sensors.getLightReading()))
print("ButtonA: %f " % (sensors.getButtonA()))


ble = BLERadio()
uart = UARTService()
advertisement = ProvideServicesAdvertisement(uart)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05)
GREEN = 0x002200
CYAN  = 0x002222
RED   = 0x660000


while True:
    print("Advertising '%s'. . ." %ble.name)
    pixels.fill(CYAN)
    ble.start_advertising(advertisement)
    while not ble.connected:
        pass

    # Now we're connected
    print ("Connected");
    pixels.fill(GREEN)

    connections = ble.connections
    device = connections[0]

    while ble.connected:
        if uart.in_waiting:
            # Read the packet
            command = int.from_bytes(uart.read(1), "little")
            length =int.from_bytes(uart.read(1), "little")
            data = uart.read(length)
            tup = (command, length, data)

            # Create the command object
            req = BugCommandFactory.CreateFromTuple(tup)

            # act upon the command object
            if isinstance(req, EchoRequest):
                print("Requested to echo: " + req.getMessage())
                res = EchoResponse(req.getMessage())
                uart.write(res.getDataBytes())
            elif isinstance(req, EchoResponse):
                print("Response: " + req.getMessage())
        pass

    print("Lost connection")
    pixels.fill(RED)
    time.sleep(2)
