from Algorithm import Algorithm

class FIFO(Algorithm):
	def run(self):
		looper = 0

		memory = Algorithm.prepareMemory(self)

		for data in self.pages:
			if not (data in memory):
				memory[looper] = data
				self.missingPages = self.missingPages + 1
				looper = looper + 1
			if looper == self.blocks:
				looper = 0

	def __repr__(self):
		return "FIFO " + str(self.missingPages)