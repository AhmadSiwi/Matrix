class Matrix():
	"""docstring for Matrix"""
	def __init__(self, string_input):
		self.string_matrix = string_input[1:-1]
		self.raws = self.string_matrix.split(';')
		self.elements = []
		for raw in self.raws:
			a_raw = raw.split(' ')
			self.elements.append(a_raw)

	def add(self, other_matrix):
		summition = '['
		for i, raw in enumerate(self.elements):
			for j, element in enumerate(raw):
				x = int(element) + int(other_matrix.elements[i][j])
				summition += str(x)
				summition += ' '
			summition = summition[:-1]
			summition += ';'
		summition = summition[:-1]
		summition += ']'
		return summition

	def subract(self, other_matrix):
		subraction = '['
		for i, raw in enumerate(self.elements):
			for j, element in enumerate(raw):
				x = int(element) - int(other_matrix.elements[i][j])
				subraction += str(x)
				subraction += ' '
			subraction = subraction[:-1]
			subraction += ';'
		subraction = subraction[:-1]
		subraction += ']'
		return subraction

	def multiply(self, other_matrix):
		multiplication = '['
		for i, raw in enumerate(self.elements):
			for j, element in enumerate(other_matrix.elements[0]):
				x = 0
				for k, ele in enumerate(raw):
					multi = int(self.elements[i][k]) * int(other_matrix.elements[k][j])
					x += multi
				multiplication += str(x)
				multiplication += ' '
			multiplication = multiplication[:-1]
			multiplication += ';'
		multiplication = multiplication[:-1]
		multiplication += ']'
		return multiplication

	def power(self, power_no):
		power_result = self.multiplication(self)
		for i in range(1, power_no):
			power_result = power_result.multiplication(self)
		return power_result

	def transpose(self):
		transposion = '['
		for i, raw in enumerate(self.elements):
			for j, element in enumerate(raw):
				transposion = transposion + self.elements[j][i] +' '
			transposion = transposion[:-1] + ';'
		transposion = transposion[:-1] + ']'
		return transposion