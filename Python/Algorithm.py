class Algorithm:
	"""
	Algorithm Class

	Base class for the page substitution algorithms.
	"""
	def __init__(self, input = []):
		"""
		Algorithm Constructor.

		Parameters
		----------
		input : list
			A list containing the the input page swap. 
		"""
		if not input: #If the list is empty throw an exception.
			raise ValueError("The list must not be empty") #throws the exception.
		self.blocks = input[0] #Store the page frames size.
		self.pages = input[1:] #Store the pages to swap.
		self.missingPages = self.blocks #Count the lack of pages.

	def removeChuncks(self, list, start, stop):
		"""
		Remove a piece of a list.

		Parameters
		----------
		list : list
			The list to delete the elements
		start : int
			start point.
		stop : int
			stop point.
		"""
		del list[start:stop] #Delete range

	def preparePageFrame(self):
		"""
		Prepare the page frames.

		Returns
		-------
		list
			The list with initialized Page frames
		"""
		pageFrame = [None] * self.blocks #Create the page frame with elements passed by the user.
		iterator = 0
		for i in range(0, len(self.pages)):
			if self.pages[i] not in pageFrame:
				pageFrame[iterator] = self.pages[i]
				iterator = iterator + 1
				if iterator == self.blocks:
					self.removeChuncks(self.pages, 0, i) #Remove part of the list that is on the page frame
					break

		return pageFrame #Return the list
