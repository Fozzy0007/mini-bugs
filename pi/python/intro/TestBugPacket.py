from BugPacket import BugCommand,BugCommandFactory
from BugPacket import EchoCommand, EchoResponse

from io import BytesIO
from queue import Queue

q = Queue()
echo = EchoCommand("wow")
echo.writeToQueue(q)
print(echo.getDataTuple())


print(echo.getDataBytes())

echo2 = BugCommandFactory.CreateCommand(echo.getDataBytes())

print(echo2.getMessage())

echo3 = BugCommandFactory.CreateFromTuple(echo.getDataTuple())
print(echo3.getMessage())