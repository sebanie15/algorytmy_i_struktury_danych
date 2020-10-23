
# 977
from typing import List


class Solution:

	def sortedSquares(self, A: List[int]) -> List[int]:
		return sorted([number**2 for number in A])


if __name__ == '__main__':
	obj1 = Solution()

	arr = [-4, -1, 0, 3, 10]
	print(obj1.sortedSquares(arr))

	arr = [-7, -3, 2, 3, 11]
	print(obj1.sortedSquares(arr))