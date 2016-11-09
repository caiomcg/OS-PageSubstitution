#!/usr/bin/env python

from Utils import Utils

from FIFO import FIFO
from LRU import LRU
from OTM import OTM

if __name__ == "__main__":
	input = Utils.getData()

	fifo = FIFO(input)
	lru  = LRU(input)
	otm  = OTM(input)

	fifo.run()
	lru.run()
	otm.run()
	
	print(fifo)
	print(lru)
	print(otm)