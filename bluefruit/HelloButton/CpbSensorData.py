import board
import adafruit_thermistor
import analogio
import digitalio

class CpbSensorData:
    def __init__(self):
        self.buttonA = digitalio.DigitalInOut(board.BUTTON_A)
        self.buttonB = digitalio.DigitalInOut(board.BUTTON_B)
        self.buttonA.switch_to_input(pull=digitalio.Pull.DOWN)
        self.light = analogio.AnalogIn(board.LIGHT)
        self.thermistor = adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 25, 3950)
    def getTemperatureInF(self):
        # we get value in C, convert to F
        temp_f = self.thermistor.temperature * 9 / 5 + 32
        return temp_f
    def getLightReading(self):
        return self.light.value
    def getButtonA(self):
        return self.buttonA.value
    def getButtonB(self):
        return self.buttonB.value
        
