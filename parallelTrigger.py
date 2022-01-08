from psychopy import core, parallel
import time


pPort = parallel.ParallelPort(address = '0xD010')

for _ in range(60):
    pPort.setData(int("00000001",2))
    time.sleep(0.001)
    pPort.setData(int("00000000",2))

    time.sleep(1)
