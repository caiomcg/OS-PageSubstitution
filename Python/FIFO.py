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

class FIFO(Algorithm):
	"""
	The First In, First Out algortithm class.
	"""
	def run(self):
		"""
		Run the algorithm.
    	"""
		looper = 0 #Auxiliar variable that loops through the page frames.

		pageFrames = Algorithm.preparePageFrame(self) #Get the initialized page frames.

		for data in self.pages: #Iterate through the pages to be swapped.
			if data not in pageFrames: #Check if the page is not on the page frame.
				pageFrames[looper] = data #
				self.missingPages = self.missingPages + 1 #Increments the missing page counter.
				looper = looper + 1 #Increments the looper.
			looper = (looper % self.blocks) #Reset the counter if it hits the end of the page frame.

	def __repr__(self):
		"""
		The representation of the class.

		Returns
		-------
		string
			The amount of missing pages for the algorithm
    	"""
		return "FIFO " + str(self.missingPages)