# 1

from typing import List


class Solution:

	def twoSum(self, nums: List[int], target: int) -> List[int]:
		"""

		Args:
			nums: List[int]
			target: int
		Returns:
			List[int]
		"""
		result = {}
		for i in range(len(nums)):
			if target - nums[i] in result:
				return [result[target - nums[i]], i]
			else:
				result[nums[i]] = i


if __name__ == '__main__':

	input_list = [2, 8, 12, 15]
	ob1 = Solution()
	print(ob1.twoSum(input_list, 10))
