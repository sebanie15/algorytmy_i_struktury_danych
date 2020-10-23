# 1403
from typing import List


class Solution:

	def minSubsequence(self, nums: List[int]) -> List[int]:

		numbers = sorted(nums)
		result = []
		while sum(result) <= sum(numbers):
			result.append(numbers.pop())

		return result


if __name__ == '__main__':
	obj1 = Solution()

	nums = [4, 3, 10, 9, 8]
	print(obj1.minSubsequence(nums))

	nums = [4, 4, 7, 6, 7]
	print(obj1.minSubsequence(nums))
