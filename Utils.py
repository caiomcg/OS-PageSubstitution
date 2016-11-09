class Utils:
	@staticmethod
	def getData():
		data = []

		while True:
			try:
				data.append(int(raw_input()))
			except EOFError:
				break
			except ValueError:
				continue
		
		return data