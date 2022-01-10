"""
TEST SCRIPT
IT can be usefult to send specific signals to the parallel port to test the 
proper functioning of triggered equipment.
"""

from psychopy import parallel
import time

pPort = parallel.ParallelPort(address = '0xD010')
# pPort.setData(int("00000000",2))

for _ in range(1):
    pPort.setData(int("00001000",2))
    time.sleep(0.1)
    pPort.setData(int("00000001",2))
    time.sleep(1)
