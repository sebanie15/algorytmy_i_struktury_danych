# 905
from typing import List


class Solution:

	def sortArrayByParity(self, A: List[int]) -> List[int]:
		result = []
		if 1 <= len(A) <= 5000 and 0 <= min(A) <= 5000:
			result = [n for n in A if n % 2 == 0] + [n for n in A if n % 2 != 0]

		return result


if __name__ == '__main__':
	obj1 = Solution()
	nums = [3, 1, 2, 4]
	print(obj1.sortArrayByParity(nums))
