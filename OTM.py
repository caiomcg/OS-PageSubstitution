from Algorithm import Algorithm

class OTM(Algorithm):
	def run(self):
		memory = Algorithm.prepareMemory(self)
	def __repr__(self):
		return "OTM " + str(self.missingPages)