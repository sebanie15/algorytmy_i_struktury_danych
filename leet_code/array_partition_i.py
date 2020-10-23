
# 561
from typing import List


class Solution:

	def arrayPairSum(self, nums: List[int]) -> int:
		values = sorted(nums)
		result = 0
		n = 0
		if len(values) > 2:
			while n < len(values):
				result += min(values[n], values[n+1])
				n += 2
		else:
			return min(nums)
		return result

if __name__ == '__main__':
	obj1 = Solution()
	arr = [1, 4, 3, 2]
	print(f'arr: {arr} - {obj1.arrayPairSum(arr)}')

	arr = [1, 1, 1, 1]
	print(f'arr: {arr} - {obj1.arrayPairSum(arr)}')

	arr = [1, 1]
	print(f'arr: {arr} - {obj1.arrayPairSum(arr)}')

	arr = [7, 3, 1, 0, 0, 6]
	print(f'arr: {arr} - {obj1.arrayPairSum(arr)}')
