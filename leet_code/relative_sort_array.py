
# 1122
from collections import deque
from typing import List


class Solution:

	def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
		temp = []
		result = []

		for number in arr1:
			if number not in arr2:
				temp.append(number)
		temp.sort()

		for number in arr2:
			for arg_arr1 in arr1:
				if arg_arr1 == number:
					result.append(arg_arr1)

		return result + temp


if __name__ == '__main__':
	obj1 = Solution()

	arr_1 = [2, 3, 1, 3, 2, 4, 6, 19, 9, 2, 7]
	arr_2 = [2, 1, 4, 3, 9, 6]

	relative_list = obj1.relativeSortArray(arr_1, arr_2)
	print(relative_list)
