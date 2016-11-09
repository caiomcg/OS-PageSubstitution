#!/usr/bin/env python

from fifo import FIFO

def getData():
	data = []
	while True:
		try:
			data.append(int(raw_input()))
		except EOFError:
			break
		except ValueError:
			continue
	return data

if __name__ == "__main__":
	fifo = FIFO(getData())
	fifo.run()

	print(fifo)