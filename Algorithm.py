class Algorithm:
	def __init__(self, input = []):
		if not input:
			raise ValueError("The list must not be empty")
		self.blocks = input[0]
		self.pages = input[1:]
		self.missingPages = self.blocks

	def removeChuncks(self, list, start, stop):
		del list[start:stop]

	def prepareMemory(self):
		memory = [self.pages[x] for x in range(0, self.blocks)]
		self.removeChuncks(self.pages, 0, self.blocks)
		return memory

	def result(self, algorithm):
		print(algorithm + str(self.missingPages))

