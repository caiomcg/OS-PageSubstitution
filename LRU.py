from Algorithm import Algorithm

class LRU(Algorithm):
	def refactorStack(self, stack, element):
		try:
			index = stack.index(element)
			del stack[index]
		except ValueError:
			pass
		stack.append(element)
		


	def run(self):
		memory  = Algorithm.prepareMemory(self)
		stack   = list(memory)

		for locale in range(0, len(self.pages)):
			self.refactorStack(stack, self.pages[locale])

			if not (self.pages[locale] in memory):
				memory[memory.index(stack[0])] = self.pages[locale]
				self.missingPages = self.missingPages + 1

	def __repr__(self):
		return "LRU " + str(self.missingPages)