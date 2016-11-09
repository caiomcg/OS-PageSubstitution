#!/usr/bin/env python

class FIFO:
	def __init__(self, input = []):
		if not input:
			raise ValueError("The list must not be empty")
		self.blocks = input[0]
		self.pages = input[1:]
		self.missingPages = self.blocks

	def removeChuncks(self, list, start, stop):
		del list[start:stop]

	def run(self):
		memory = []
		looper = 0

		for i in range(0, self.blocks):
			memory.append(self.pages[i])

		self.removeChuncks(self.pages, 0, self.blocks)

		for data in self.pages:
			if not (data in memory):
				memory[looper] = data
				self.missingPages = self.missingPages + 1
				looper = looper + 1
			if looper == self.blocks:
				looper = 0



	def __repr__(self):
		return "FIFO " + str(self.missingPages)

	def __str__(self):
		return "FIFO " + str(self.missingPages)


