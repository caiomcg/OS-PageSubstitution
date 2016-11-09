#!/usr/bin/env python

from Utils import Utils

from FIFO import FIFO
from LRU import LRU

if __name__ == "__main__":
	input = Utils.getData()

	fifo = FIFO(input)
	lru  = LRU(input)

	fifo.run()
	lru.run()
	
	fifo.result("FIFO ")
	lru.result("LRU ")