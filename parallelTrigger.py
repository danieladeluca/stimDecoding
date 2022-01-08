from psychopy import core, parallel
import time


pPort = parallel.ParallelPort(address = '0xD010')
# pPort.setData(int("00000000",2))

for _ in range(1):
    pPort.setData(int("00001000",2))
    time.sleep(0.1)
    pPort.setData(int("00000001",2))

    time.sleep(1)
