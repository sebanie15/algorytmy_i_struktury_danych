"""
Stos –Zadanie wykorzystujacestos : Zajęcia
•Częstym błedem w programowaniu jest brakujący lub zbyteczny dodatkowy nawias. Wykorzystując stos możemy napisać algorytm do
 weryfikacji czy wyrażenie zawiera poprawnie zapisane nawiasy.
•Wyrażenie ”((()))” jest poprawne. “(()” jest niepoprawne.
•W jaki sposób za pomocą stosu możemy rozwiązać ten problem?
•Jeżeli znak jest lewym nawiasem, dodaj go na stos w przeciwnym wypadku sprawdź czy na stosie znajduje się lewy nawias;
 jeżeli tak to usuń go i czytaj kolejny znak; jeżeli nie zwróć False.
 Wykonuj to dla wszystkich znaków w napisie. Sprawdź na końcu czy stos jest pusty. Dla“(()” zostanie na nim jeden element.
 Jeżeli pusty to zwróć True, jeżeli nie to False.
•Wersja dla ambitniejszych: Napis złożony z trzech rodzajów nawiasów {[( np: “{{[()]}}”
•Wersja dla ambitnych: Napis może składać się z białych znaków, liczb i operatorów matematycznych np:
    ”12   + (2 * 3) / 17 +     [2 + [2 * 2]]”.
    Dalej interesują nas tylko nawiasy. Należy wymyśleć sposób do wyciągania kolejnych nawiasów pomijając inne znaki.
"""

# ad.1

from tqdm import tqdm

LEFT_PARENTHESIS = ['{', '[', '(']
RIGHT_PARENTHESIS = ['}', ']', ')']


def is_valid_parentheses(s: str) -> bool:
	"""	checks that the parentheses are written in the correct order and number

	Args:
		s: str
	Returns:
		True: if s has the correct number of parentheses in the correct order
	"""
	stack = []
	for char in tqdm(s):
		if char in LEFT_PARENTHESIS:
			stack.append(char)
			print(stack)
		elif char in RIGHT_PARENTHESIS:
			if LEFT_PARENTHESIS[RIGHT_PARENTHESIS.index(char)] in stack:
				stack.pop(stack.index(LEFT_PARENTHESIS[RIGHT_PARENTHESIS.index(char)]))
				print(stack)
			else:
				return False

	return not stack


def infix_notation_to_onp(operation: str) -> str:
	operators = {
		'(': 0,
		'+': 1,
		'-': 1,
		')': 1,
		'*': 2,
		'/': 2,
		'%': 2,
		'^': 3
	}
	RIGHT_JOINT_OPERATORS = ['/', '^']

	if not is_valid_parentheses(operation):
		return ''

	s = operation.replace(' ', '').rstrip()

	stack = []
	out = []
	next_operator = ''
	idx = 0
	while idx < len(s):
		if s[idx].isdecimal():
			out.append(s[idx])
			if next_operator != '':
				out.append(next_operator)
				next_operator = ''

		if s[idx] == '(':
			stack.append(s[idx])

		if s[idx] == '+' or s[idx] == '-':
			stack.append(s[idx])

		if s[idx] == ')':
			# TODO: check this condition
			if stack:
				while stack:
					if stack[-1] != '(':
						out.append(stack.pop())
					else:
						break
				stack.pop()

		if s[idx] == '*':
			stack.append(s[idx])

		if s[idx] == '/' and stack:
			if operators[stack[-1]] < 2:
				stack.append(s[idx])
			elif stack[-1] == '*':
				out.append(stack.pop())
				stack.append(s[idx])

		if s[idx] == '/' and not stack:
			stack.append(s[idx])

		if s[idx] == '%' and stack:
			if stack[-1] == '/':
				stack.append(s[idx])
			else:
				out.append(stack.pop())
				stack.append(s[idx])

		if s[idx] == '%' and not stack:
			stack.append('%')

		# TODO: implement exponentiation

		idx += 1

	while stack:
		out.append(stack.pop())

	return ' '.join(out)


def is_valid_onp(onp: str) -> bool:
	"""
	method checks if the given ONP string is correct

	Args:
		onp: str (ONP string)
	Returns:
		True: if onp is correct ONP string
	"""
	s = onp.split(' ')
	counter = 0
	for entry in s:
		if entry.isdecimal():
			counter += 1
		else:
			counter -= 1

	return counter != 0


def calc_onp(onp: str) -> float:
	"""

	Args:
		onp: str - ONP string
	Returns:
		float: the result of the ONP operation
	"""
	def _calc_operation(operation: str, val_1: float, val_2: float) -> float:
		if operation == '+':
			return val_2 + val_1
		elif operation == '-':
			return val_2 - val_1
		elif operation == '*':
			return val_2 * val_1
		elif operation == '/':
			if val_1 != 0:
				return val_2 / val_1
			# TODO: raise exception or something else ;)
		elif operation == '%':
			return val_2 % val_1
		elif operation == '^':
			return val_2 ** val_1
		elif operation == '*':
			return val_2 * val_1

	s = onp.split(' ')
	print(f'from calc: {s}')
	stack = []
	if is_valid_onp(onp):
		for entry in tqdm(s):
			if entry.isdecimal():
				stack.append(float(entry))
			else:
				stack.append(_calc_operation(entry, float(stack.pop()), float(stack.pop())))
		# print(stack, entry)

		return stack.pop()


if __name__ == '__main__':
	# s = "(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))"
	# print(is_valid_stack(s))

	# s = "((())"
	# print(is_valid_stack(s))

	print('-' * 40)
	operation = '3+4*3/(2-1)+2'
	# operation = '3 + 2-1  +2'
	onp = infix_notation_to_onp(operation)
	print(onp)
	result = calc_onp(infix_notation_to_onp(operation))
	print(f'wynik: {result}  - {3 + 4 * 3 / (2 - 1) + 2}')

	# print(infix_notation_to_onp('3 + 5 % 2'))
	print(5 + 5 / 3)
	# onp = '3 4 2 * 1 5 - 2 3 ^ ^ / +'

	print('-' * 40)
	number = '-2'
	print(number.isdigit())
