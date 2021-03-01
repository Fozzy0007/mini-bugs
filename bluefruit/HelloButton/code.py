from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

import time
import board
import neopixel
# from adafruit_bluefruit_connect.packet import Packet
# from adafruit_bluefruit_connect.button_packet import ButtonPacket

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
    print(connections)
    device = connections[0]

    while ble.connected:
        time.sleep(2)
        uart.write("hello")
        pass
        # if uart.in_waiting:
        #     packet = Packet.from_stream(uart)
        #     if isinstance(packet, ButtonPacket):
        #         if packet.pressed:
        #             if packet.button == ButtonPacket.BUTTON_1:
        #                 # The 1 button was pressed.
        #                 print("1 button pressed!")
        #             elif packet.button == ButtonPacket.UP:
        #                 # The UP button was pressed.
        #                 print("UP button pressed!")

    # If we got here, we lost the connection. Go up to the top and start
    # advertising again and waiting for a connection.

    print("Lost connection")
    pixels.fill(RED)
    time.sleep(2)
