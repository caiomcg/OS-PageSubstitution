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

import operator #Operator module

class OTM(Algorithm):
	"""
	The Optimum algortithm class.
	"""
	def usedLast(self, elements, queue):
		"""
		Get the last used element index.

		Iterates through a list of elements, find the index of the first occurence of the element located in elements
		and stores the right most index. The code returns the last used element based on the OTM concept.

		Parameters
		----------
		elements : list
			The elements to locate at the queue
		queue : list
			The queue where the elements are mainteined.

		Returns
		-------
		int
			The element used last(The last page used based on the elements list).
    	"""
		value = 0 #auxiliar variable
		counterpart = list(elements) #The counterpartof the elements list used to store the index of each element.

		for x in range(0, len(elements)): #Iterate through the elements
			try:
				counterpart[x] = queue.index(elements[x]) #Fetch the index of the first occurence of an element.
			except ValueError: #Value may not be found.
				return elements[x] #In this case this is the page we want to swap. So, we return it.
		index, value = max(enumerate(counterpart), key=operator.itemgetter(1)) #Find the biggest index among the counterparts.
		return elements[index] #Return the element to be removed from the page frame.
		


	def run(self):
		"""
		Run the algorithm.
		"""
		pageFrames  = Algorithm.preparePageFrame(self) #Get the initialized page frames.

		for locale in range(0, len(self.pages)): #Iterate through the pages to be swapped.
			if self.pages[locale] not in pageFrames: #If the page is not on the page frame.
				lu = self.usedLast(pageFrames, self.pages[locale+1:]) #Get the last used page on the page frame.
				pageFrames[pageFrames.index(lu)] = self.pages[locale] #Update the page frame change the new page with the page to use last.
				
				self.missingPages = self.missingPages + 1 #Increments the missing page counter.

	def __repr__(self):
		"""
		The representation of the class.

		Returns
		-------
		string
			The amount of missing pages for the algorithm
		"""
		return "OTM " + str(self.missingPages)