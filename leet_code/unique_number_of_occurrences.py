
# 1207
from typing import List


class Solution:

	def uniqueOccurrences(self, arr: List[int]) -> bool:
		numbers = set(arr)
		result = []
		for number in numbers:
			if arr.count(number) in result:
				return False
			result.append(arr.count(number))

		return True


if __name__ == '__main__':
	obj1 = Solution()

	arr = [1,2,2,1,1,3]
	print(obj1.uniqueOccurrences(arr))

	arr = [1,2]
	print(obj1.uniqueOccurrences(arr))

	arr = [-3,0,1,-3,1,1,1,-3,10,0]
	print(obj1.uniqueOccurrences(arr))
