from matrix import Matrix

first_string = input('Enter your first matrix:\n')
first_matrix = Matrix(first_string)
operator = input('Choose an operator(+,-,*,^,T):\n')

result = ''

if operator == '^':
	power = input("Enter your power:\n")
	result = first_matrix.power(power)
elif operator == 'T':
	result = first_matrix.transpose()
else:
	second_string = input('Enter your second matrix:\n')
	second_matrix = Matrix(second_string)
	if operator == '+':
		result = first_matrix.add(second_matrix)
	if operator == '-':
		result = first_matrix.subtract(second_matrix)
	if operator == '*':
		result = first_matrix.multiply(second_matrix)

print(result)