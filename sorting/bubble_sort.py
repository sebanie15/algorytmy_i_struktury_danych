
from typing import Any, List
from random import randint
from tqdm import tqdm

def bubble_sort(list_to_sort: List[Any]) -> None:
	n = len(list_to_sort)
	i = 0
	is_swapped = False

	for i in range(n):
		for j in range(0, n-1):
			if list_to_sort[j] > list_to_sort[j+1]:
				swap(list_to_sort, j, j+1)
				# list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]

def bubble_sort_2(values: List[Any]) -> None:
	length = len(values)
	n = 0
	swap_occurred = True

	while n < length and swap_occurred:
		swap_occurred = False
		for index in range(length - 1):
			if values[index] > values[index + 1]:
				values[index], values[index + 1] = values[index + 1], values[index]
				swap_occurred = True

		n += 1

def gt(value1, value2):
	pass


def swap(list, a, b) -> None:
	list[a], list[b] = list[b], list[a]

def generate_random_list(length, start, end):
	return [randint(start, end) for _ in range(length)]

def  generate_order_list(length):
	return list(range(length))

def generate_reversed_list(length):
	return list(reversed(range(length)))


if __name__ == '__main__':
	# list_to_sort = [5,4, 2, 1, 8]
	# print(list_to_sort)
	# bubble_sort(list_to_sort)
	# print(list_to_sort)
	# start = 0
	#end = 10

	length = 10000
	ordered_list = generate_order_list(length)
	reversed_list = generate_reversed_list(length)
	random_list = generate_random_list(length, 0, 10)

	bubble_sort_2(ordered_list)

	print(ordered_list)