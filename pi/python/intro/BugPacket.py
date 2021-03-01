class BugCommand():
    def __init__(self, command):
        self.command = command
        self.setPayloadLength(0)
    def getDataBytes(self):
        data = bytearray()
        for item in self.getDataTuple():
            data.extend(item)
        return data

    # Private methods
    def getDataTuple(self):
        return (bytearray([self.command]), 
                bytearray([self.payloadLength]), 
                self.getCommandData())
    # @abstractmethod - CircuitPython doesn't support ABC 
    def getCommandData(self):
        pass
    def getCommand(self):
        return self.command
    def setPayloadLength(self, length):
        self.payloadLength = length

        

class BugCommandFactory:
    @staticmethod
    def CreateCommand(data):
        command = data[0]
        length = data[1]
        paramData = data[2:]
        if command == 1:
            echo = EchoCommand.Create(paramData)
        elif command == 2:
            echo = EchoResponse.Create(paramData)
        return echo
    @staticmethod
    def CreateFromTuple(data):
        command = data[0]
        if command == 1:
            echo = EchoCommand.fromByteArray(data[2])
        elif command == 2:
            echo = EchoResponse.fromByteArray(data[2])
        return echo

    
class EchoBase(BugCommand):
    def __init__(self, command, message):
        super().__init__(command)
        self.message = message
        self.setPayloadLength(len(self.message))
    def getCommandData(self):
        encoded = self.message.encode('utf-8')
        data = bytearray(encoded)
        return data
    def getMessage(self):
        return self.message

class EchoCommand(EchoBase):
    def __init__(self, message):
        super().__init__(1, message)
    @staticmethod
    def fromByteArray(bits):
        message = bits.decode('utf-8')
        return EchoCommand(message)


class EchoResponse(EchoBase):
    def __init__(self, message):
        super().__init__(2, message)
    @staticmethod
    def fromByteArray(bits):
        message = bits.decode('utf-8')
        return EchoResponse(message)

