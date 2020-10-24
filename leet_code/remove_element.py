
# 27
from typing import List


class Solution:

	def removeElement(self, nums: List[int], val: int) -> int:

		while val in nums:
			nums.remove(val)

		return len(nums)


if __name__ == '__main__':
	obj1 = Solution()

	nums = [3,2,2,3]
	print(obj1.removeElement(nums, 3))

	nums = [0,1,2,2,3,0,4,2]
	print(obj1.removeElement(nums, 2))
