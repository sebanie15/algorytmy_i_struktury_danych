# 1464
from typing import List


class Solution:
	def maxProduct(self, nums: List[int]) -> int:

		result = 0

		if 2 <= len(nums) <= 500:
			values = nums[:]
			first_value = values.pop(values.index(max(values)))
			second_value = values.pop(values.index(max(values)))
			result = (first_value - 1) * (second_value - 1)

		return result


if __name__ == '__main__':
	obj1 = Solution()
	nums = [3, 8, 4, 2]
	print(obj1.maxProduct(nums))
