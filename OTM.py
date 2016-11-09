from Algorithm import Algorithm

import operator

class OTM(Algorithm):
	def leastUsed(self, elements, queue):
		value = 0
		counterpart = list(elements)

		for x in range(0, len(elements)):
			try:
				counterpart[x] = queue.index(elements[x])
			except ValueError:
				return elements[x]
		index, value = max(enumerate(counterpart), key=operator.itemgetter(1))
		return elements[index]
		


	def run(self):
		pageFrames  = Algorithm.prepareMemory(self)
		unique  = list(set(self.pages))

		for locale in range(0, len(self.pages)):
			if self.pages[locale] not in pageFrames:
				lu = self.leastUsed(pageFrames, self.pages[locale+1:])
				pageFrames[pageFrames.index(lu)] = self.pages[locale]
				
				self.missingPages = self.missingPages + 1

	def __repr__(self):
		return "OTM " + str(self.missingPages)