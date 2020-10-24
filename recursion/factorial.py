from typing import List

from structures.lists import LinkedList


def factorial(n: int) -> int:
	if n < 2:
		return n
	else:
		return n * factorial(n-1)

def factorial_iter(n: int) -> int:
	result = 1

	for i in range(2, n+1):
		result *= i

	return result

def sum_list_recursively(values: LinkedList[int]) -> int:
	if not values:
		return 0
	else:
		return values[0] + sum_list_recursively(values[1:])


if __name__ == '__main__':
	print(factorial(0))
	print(factorial(1))
	print(factorial(2))
	print(factorial(3))

	print(factorial_iter(3))

	values = [7, 8, 5, 4, 2]

	print(sum_list_recursively(values))