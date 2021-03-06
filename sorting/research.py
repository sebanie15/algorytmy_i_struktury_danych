import pathlib
from abc import ABC, abstractmethod
import json
import sys
from random import randint
from typing import Dict, List, Any

from tqdm import tqdm

from sorting.bubble_sort import generate_order_list, generate_reversed_list, generate_random_list

sys.setrecursionlimit(1500)
ORDERED = 'ordered'
RANDOM = 'random'
REVERSED = 'reversed'

BASE = pathlib.Path(__file__).parent.absolute() / 'temp_data'


class SortingAlgorithm(ABC):

	def __init__(self):
		self.comparisons = 0

	def _sort_(self):
		pass

	def gt(self, value_1, value_2) -> bool:
		self.comparisons += 1
		return value_1 > value_2

	def lt(self, value_1, value_2) -> bool:
		self.comparisons += 1
		return value_1 < value_2

	def lte(self, value_1, value_2) -> bool:
		self.comparisons += 1
		return value_1 <= value_2

	def gte(self, value_1, value_2) -> bool:
		self.comparisons += 1
		return value_1 >= value_2

	def eq(self, value_1, value_2) -> bool:
		self.comparisons += 1
		return value_1 == value_2

	@abstractmethod
	def sort(self, values):
		pass


class BubbleSort(SortingAlgorithm):

	def sort(self, values):
		self.comparisons = 0
		length = len(values)
		n = 0
		swap_occurred = True

		while n < length and swap_occurred:
			swap_occurred = False
			for index in range(length - 1):
				if self.gt(values[index], values[index + 1]):
					values[index], values[index + 1] = values[index + 1], values[index]
					swap_occurred = True

			n += 1


class InsertSort(SortingAlgorithm):

	def sort(self, values):
		self.comparisons = 0
		length = len(values)

		for i in range(1, length):

			value = values[i]
			j = i - 1

			while self.gte(j, 0) and self.lt(value, values[j]):
				values[j + 1] = values[j]
				j -= 1
			values[j + 1] = value


class QuickSort(SortingAlgorithm):

	def partition(self, values: List[int], left: int, right: int) -> int:
		pivot_index = randint(left, right)
		values[right], values[pivot_index] = values[pivot_index], values[right]
		pivot = values[right]
		j = left - 1

		for i in range(left, right):
			if self.lt(values[i], pivot):
				j += 1
				values[i], values[j] = values[j], values[i]
		j += 1
		values[j], values[right] = values[right], values[j]
		return j

	def sort(self, values: List[Any]) -> None:
		self.comparisons = 0
		def _quick_sort(left: int, right: int) -> None:
			if self.lt(left, right):
				index = self.partition(values, left, right)
				_quick_sort(left, index - 1)
				_quick_sort(index + 1, right)

		_quick_sort(0, len(values) - 1)


def simulate(algorithm: SortingAlgorithm, max_length: int) -> None:
	"""
	The method allows to simulate the sorting of lists with the given maximum length.
	The data is saved to a .json file.

	Args:
		algorithm: SortingAlgorithm
		max_length: int
	Returns:
		None
	"""
	result = {
		ORDERED: {},
		REVERSED: {},
		RANDOM: {}
	}

	for length in tqdm(range(1, max_length+1)):

		ordered_list = generate_order_list(length)
		reversed_list = generate_reversed_list(length)
		random_list = generate_random_list(length, 0, 10)

		algorithm.sort(ordered_list)
		result[ORDERED][length] = algorithm.comparisons

		algorithm.sort(reversed_list)
		result[REVERSED][length] = algorithm.comparisons

		algorithm.sort(random_list)
		result[RANDOM][length] = algorithm.comparisons

	filename = BASE / f'{algorithm.__class__.__name__}_{max_length}.json'
	save_dict_to_json(filename, result)


def save_dict_to_json(filename: str, dict: Dict) -> None:
	# filename = BASE / f'{algorithm.__class__.__name__}_{max_length}.json'
	with open(filename, 'w') as f:
		json.dump(dict, f, indent=4, sort_keys=True)


if __name__ == '__main__':
	length = 500

	#simulate(BubbleSort(), length)
	#simulate(InsertSort(), length)
	simulate(QuickSort(), length)



