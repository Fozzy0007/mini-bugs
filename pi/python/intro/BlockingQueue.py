from queue import Queue
from BugPacket import BugCommand

class BlockingQueue:
    fifo = Queue()
    def AddPacket(self, packet):
        if len(packet) != 3:
            raise Exception("Packet tuple must be 3 in length")
        for item in packet:
            fifo.put(item)
    