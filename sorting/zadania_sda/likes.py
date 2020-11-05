from typing import List


def likes(names: List[str]) -> str:
	length = len(names)
	if not names:
		return 'nikt tego nie lubi'
	elif length == 1:
		return f'{names[0]} lubi to!'
	elif length == 2:
		return f'{names[0]} i {names[1]} lubią to!'
	elif length == 3:
		return f'{names[0]}, {names[1]} i {names[2]} lubią to!'
	else:
		return f'{names[0]}, {names[1]} i {length - 1} inne osoby lubią to!'

if __name__ == '__main__':
	print(likes([]))  # => "nikt tego nie lubi"
	print(likes(["Piotr"]))  # => "Piotr lubi to!"
	print(likes(["Piotr", "Ania"]))  # => "Piotr i Ania lubią to"
	print(likes(["Piotr", "Ania", "Marek"]))  # => "Piotr, Ania i Marek lubią to"
	print(likes(["Piotr", "Ania", "Marek", "Ola"]))
