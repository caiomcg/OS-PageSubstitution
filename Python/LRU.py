from Algorithm import Algorithm #Base class

"""
Author: Caio Marcelo Campoy Guedes
E-Mail: caiomcg@gmail.com

License:

MIT License

Copyright (c) 2016 Caio Marcelo Campoy Guedes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

class LRU(Algorithm):
	"""
	The Least Recently used algortithm class.
	"""
	def refactorStack(self, stack, element):
		"""
		Re-stack the values.

		Check if a value is on the stack or if it is not.
		If it is: Remove the value from the stack and put it at the top.
		If it is not: Put it at the top

		Parameters
		----------
		stack : list
			List representing the stack
		element : int
			The element to be refactored
		"""
		try:
			index = stack.index(element) #Get the element index in the stack.
			del stack[index] #Delete the element from the stack
		except ValueError: #Value may not be found
			pass #if the element was not found, do nothing.

		stack.append(element) #Put the element at the top of the stack
		


	def run(self):
		"""
		Run the algorithm.
		"""
		pageFrames  = Algorithm.preparePageFrame(self) #Get the initialized page frames.
		stack   = list(pageFrames) #A copy of the page frames to be used as the stack.

		for locale in range(0, len(self.pages)): #Iterate through the input list(The pages to swap).
			self.refactorStack(stack, self.pages[locale]) #Refactor the stack
			if self.pages[locale] not in pageFrames: #Check if the current page is on the page frame.
				pageFrames[pageFrames.index(stack[-(self.blocks+1)])] = self.pages[locale] #Take the page and place it at the index of the least Recently Used page.
				self.missingPages = self.missingPages + 1 #Increments the missing page counter.

	def __repr__(self):
		"""
		The representation of the class.

		Returns
		-------
		string
			The amount of missing pages for the algorithm
		"""
		return "LRU " + str(self.missingPages)