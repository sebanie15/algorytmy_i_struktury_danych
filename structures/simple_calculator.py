"""
Stos –Zadanie wykorzystujacestos : Zajęcia
•Częstym błedem w programowaniu jest brakujący lub zbyteczny dodatkowy nawias. Wykorzystując stos możemy napisać
 algorytm do weryfikacji czy wyrażenie zawiera poprawnie zapisane nawiasy.
•Wyrażenie ”((()))” jest poprawne. “(()” jest niepoprawne.
•W jaki sposób za pomocą stosu możemy rozwiązać ten problem?
•Jeżeli znak jest lewym nawiasem, dodaj go na stos w przeciwnym wypadku sprawdź czy na stosie znajduje się lewy nawias;
 jeżeli tak to usuń go i czytaj kolejny znak; jeżeli nie zwróć False.
 Wykonuj to dla wszystkich znaków w napisie. Sprawdź na końcu czy stos jest pusty. Dla“(()” zostanie na nim jeden
 element.
 Jeżeli pusty to zwróć True, jeżeli nie to False.
•Wersja dla ambitniejszych: Napis złożony z trzech rodzajów nawiasów {[( np: “{{[()]}}”
•Wersja dla ambitnych: Napis może składać się z białych znaków, liczb i operatorów matematycznych np:
    ”12   + (2 * 3) / 17 +     [2 + [2 * 2]]”.
    Dalej interesują nas tylko nawiasy. Należy wymyśleć sposób do wyciągania kolejnych nawiasów pomijając inne znaki.
"""

# ad.1
from math import sin, cos

from structures.queues import Stack
import structures.functions

LEFT_PARENTHESIS = {'(': '(', '{': '{', '[': '['}
RIGHT_PARENTHESIS = {')': '(', '}': '{', ']': '['}

OPERATORS = {
	'(': 0,
	'{': 0,
	'[': 0,
	'+': 1,
	'-': 1,
	')': 1,
	'}': 1,
	']': 1,
	'*': 2,
	'/': 2,
	'%': 2,
	'^': 3
}


class CalcBase:

	def __init__(self):
		self._operations = {
			'+': self.sum,
			'-': self.sub,
			'*': self.mul,
			'/': self.div,
			'%': self.mod,
			'^': self.pow
		}

		self._operators = Stack()
		self._onp = []
		self._operation = ''

	@staticmethod
	def is_valid_brackets_count(value: str) -> bool:
		"""	checks that the parentheses are written in the correct order and number the function is sensitive to
		different types of parentheses

		Args:
			value: str
		Returns:
			True: '()' or '[]' or '{}' etc.
			False: '(()' or '[]]' or '{{}' or '(]' or '{)' etc.
		"""
		stack = Stack[str]()

		for char in value:
			if char in LEFT_PARENTHESIS:
				stack.push(char)
			elif char in RIGHT_PARENTHESIS and stack:
				if stack.front() == RIGHT_PARENTHESIS[char]:
					stack.pop()
				else:
					return False

		return not stack

	@staticmethod
	def is_valid_brackets_count2(value: str) -> bool:
		"""	checks that the parentheses are written in the correct order and number the function is sensitive to
		different types of parentheses

		Args:
			value: str
		Returns:
			True: '()' or '[]' or '{}' etc.
			False: '(()' or '[]]' or '{{}' or '(]' or '{)' etc.
		"""
		stack = []

		for char in value:
			if char in LEFT_PARENTHESIS:
				stack.append(char)
			elif char in RIGHT_PARENTHESIS and stack:
				if stack[-1] == RIGHT_PARENTHESIS[char]:
					stack.pop()
				else:
					return False
			else:
				return False

		return not stack

	def operator_has_lower_priority(self, char: str) -> bool:
		return OPERATORS[self._operators.front()] >= OPERATORS[char]

	@staticmethod
	def is_left_parenthesis(char: str) -> bool:
		return char in LEFT_PARENTHESIS

	@staticmethod
	def is_right_parenthesis(char: str) -> bool:
		return char in RIGHT_PARENTHESIS

	@staticmethod
	def is_an_operator(char: str) -> bool:
		return char in OPERATORS

	@staticmethod
	def is_comma(char: str) -> bool:
		return char == '.'

	@property
	def previous_operator(self) -> str:
		return self._operators.front()

	def pop_operator(self) -> str:
		return self._operators.pop()

	@property
	def onp(self) -> str:
		return ' '.join(self._onp)

	@onp.setter
	def onp(self, onp: str) -> None:
		if self.is_valid_onp(onp):
			self._onp = onp.split(' ')

	@property
	def calculation(self) -> str:
		return self._operation

	@calculation.setter
	def calculation(self, operation: str) -> None:
		self._operation = operation.rstrip()
		self._onp = self.infix_notation_to_onp(self._operation).split(' ')

	def infix_notation_to_onp(self, infix_expresion: str = '') -> str:
		"""Algorytm konwersji z notacji infiksowej do ONP

		Edsger Dijkstra wymyślił algorytm nazywany „stacją rozrządową”, ponieważ jest w działaniu bardzo podobny do
		kolejowej stacji rozrządowej. Tak jak algorytm liczący wartość wyrażenia ONP, ten także działa na bazie stosu.
		Do konwersji używane są dwie zmienne (typu ciągu znakowego) — wejście oraz wyjście. Jest także stos przechowujący
		operatory niedodane jeszcze do wyjścia. W uproszczeniu, program czyta po kolei każdą literę i wykonuje operację
		zależną od tej litery.

		Szczegóły algorytmu

		1. Póki zostały symbole do przeczytania wykonuj:

		2. Przeczytaj symbol.

			- Jeśli symbol jest liczbą dodaj go do kolejki wyjście.
			- Jeśli symbol jest funkcją włóż go na stos.
			- Jeśli symbol jest znakiem oddzielającym argumenty funkcji (np. przecinek):

				- Dopóki najwyższy element stosu nie jest lewym nawiasem, zdejmij element ze stosu i dodaj go do kolejki
				  wyjście. Jeśli lewy nawias nie został napotkany oznacza to, że znaki oddzielające zostały postawione w
				  złym miejscu lub nawiasy są źle umieszczone.

			- Jeśli symbol jest operatorem, o1, wtedy:

				1) dopóki na górze stosu znajduje się operator, o2 taki, że:

							o1 jest lewostronnie łączny i jego kolejność wykonywania jest mniejsza lub równa kolejności
							wyk. o2,
							lub
							o1 jest prawostronnie łączny i jego kolejność wykonywania jest mniejsza od o2,

					zdejmij o2 ze stosu i dołóż go do kolejki wyjściowej i wykonaj jeszcze raz 1)

				2) włóż o1 na stos operatorów.

			- Jeżeli symbol jest lewym nawiasem to włóż go na stos.
			- Jeżeli symbol jest prawym nawiasem to zdejmuj operatory ze stosu i dokładaj je do kolejki wyjście, dopóki
			  symbol na górze stosu nie jest lewym nawiasem, kiedy dojdziesz do tego miejsca zdejmij lewy nawias ze stosu
			  bez dokładania go do kolejki wyjście. Teraz, jeśli najwyższy element na stosie jest funkcją, także dołóż go do
			  kolejki wyjście. Jeśli stos zostanie opróżniony i nie napotkasz lewego nawiasu, oznacza to, że nawiasy zostały
			  źle umieszczone.

		Jeśli nie ma więcej symboli do przeczytania, zdejmuj wszystkie symbole ze stosu (jeśli jakieś są) i dodawaj je do
		kolejki wyjścia. (Powinny to być wyłącznie operatory, jeśli natrafisz na jakiś nawias oznacza to, że nawiasy zostały
		 źle umieszczone.)

		Args:
			infix_expresion:

		Returns:
			str:
		"""

		if not self.is_valid_brackets_count(infix_expresion):
			return ''

		infix_expresion = infix_expresion.rstrip()

		found_comma = False
		for char in infix_expresion:
			if char.isdecimal():
				if found_comma:  # liczba
					self._onp[-1] += char
				else:
					self._onp.append(char)
			elif self.is_comma(char):
				found_comma = True
				if self._onp:
					self._onp[-1] += char
				else:
					self._onp.append('0.')
			elif self.is_left_parenthesis(char):  # '('
				found_comma = False
				self._operators.push(char)
			elif self.is_right_parenthesis(char):  # ')' '}' ']'
				found_comma = False
				while self._operators:
					if not self.is_left_parenthesis(self.previous_operator):
						self._onp.append(self._operators.pop())
					if self.is_left_parenthesis(self.previous_operator):
						self._operators.pop()
						break
			elif self.is_an_operator(char):  # operator
				found_comma = False
				while self._operators and self.operator_has_lower_priority(char):
					self._onp.append(self._operators.pop())
				self._operators.push(char)

		while self._operators:
			self._onp.append(self._operators.pop())

		return self.onp

	@staticmethod
	def is_valid_onp(onp: str) -> bool:
		"""method checks if the given ONP string is correct

		Args:
			onp: str (ONP string)
		Returns:
			True: if onp is correct ONP string
		"""
		onp = onp.split(' ')
		counter = 0
		for entry in onp:
			if entry[0].isdecimal():
				counter += 1
			else:
				counter -= 1

		return counter != 0

	@staticmethod
	def sum(a, b) -> float:
		return a + b

	@staticmethod
	def mul(a: float, b: float) -> float:
		return a * b

	@staticmethod
	def div(a: float, b: float) -> [float, str]:
		if b != 0:
			return a / b
		else:
			raise ZeroDivisionError

	@staticmethod
	def mod(a: int, b: int) -> [int, str]:
		if b != 0:
			return a % b
		else:
			return 'ZeroDivisionError'

	@staticmethod
	def pow(a: [int, float], b: float) -> float:
		return a ** b

	@staticmethod
	def sub(a: float, b: float) -> float:
		return a - b

	@staticmethod
	def sin_deg(deg: [int, float]) -> float:
		return sin(deg)

	@staticmethod
	def cos_deg(deg: [int, float]) -> float:
		return cos(deg)

	@staticmethod
	def sin_rad(rad: int) -> float:
		return 0

	def calc(self) -> [float, str]:
		"""
		Returns:
			float: the result of the ONP operation
		"""

		if self.is_valid_brackets_count(self._operation):
			stack = Stack()
			try:
				for entry in self._onp:
					if entry[0].isdecimal():
						stack.push(float(entry))
					else:
						val_1 = float(stack.pop())
						val_2 = float(stack.pop())
						result_value = self._operations[entry](val_2, val_1)
						stack.push(result_value)
			except ZeroDivisionError:
				return 'You\'re trying divide bytes zero'
			else:
				return stack.pop()


if __name__ == '__main__':
	s = "(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))(((){()}[]))"
	calc = CalcBase()
	print(calc.is_valid_brackets_count2(s))

	s = "((())]"
	print(calc.is_valid_brackets_count2(s))

	s = "]"
	print(calc.is_valid_brackets_count2(s))

	print('-' * 40)

	operation = '3 +4*3.2 /((2-1)+2)^2'
	calc.calculation = operation
	result = calc.calc()
	print(f'ONP: {calc.onp}, wynik: calc_onp: {result}  - python: {3 + 4 * 3.2 / ((2 - 1) + 2) ** 2}')

	operation = '3+4*3/(2-1)+2^2'
	calc.calculation = operation
	result = calc.calc()
	print(f'wynik: calc_onp: {result}  - python: {3 + 4 * 3 / (2 - 1) + 2 ** 2}')

	operation = '12 + (2 * 3) / 17 + (2 + 2 * 2))'
	# result = calc.calc_onp(operation)
	# print(f'wynik: calc_onp: {result}  - python: {12 + (2 * 3) / 17 + (2 + 2 * 2)}')

	print(sin(180))
