from typing import List


def partition(values: List[int], left: int, right: int) -> int:
	j = left-1
	pivot = values[right]

	for i in range(left, right):
		if values[i] < pivot:
			j += 1
			values[i], values[j] = values[j], values[i]
	j += 1
	values[j], values[right] = values[right], values[j]

	return j

def quick_sort(values: List[int]):
	def _quick_sort(left: int, right: int) -> None:
		if left < right:
			index = partition(values, left, right)
			_quick_sort(left, index-1)
			_quick_sort(index+1, right)

	_quick_sort(0, len(values) -1 )


if __name__ == '__main__':
	from random import randint
	#values = [1, 8, 3, 9, 4, 5, 7]
	values = [7, 6, 5, 4, 3, 2, 1]
	print(values)
	print(quick_sort(values))
	print(values)
