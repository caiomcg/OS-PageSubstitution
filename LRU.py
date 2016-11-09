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
		pageFrames  = Algorithm.prepareMemory(self)
		stack   = list(pageFrames)

		for locale in range(0, len(self.pages)):
			self.refactorStack(stack, self.pages[locale])
			if self.pages[locale] not in pageFrames:
				pageFrames[pageFrames.index(stack[-(self.blocks+1)])] = self.pages[locale]
				self.missingPages = self.missingPages + 1

	def __repr__(self):
		return "LRU " + str(self.missingPages)