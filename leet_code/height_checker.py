
# 1051
from typing import List


class Solution:

	def heightChecker(self, heights: List[int]) -> int:

		res = sorted(heights)
		idx = 0

		counter = 0
		while idx < len(heights):
			if heights[idx] != res[idx]:
				counter += 1
			idx += 1


		return counter

"""
#while idx < len(res)-1:
		#	if res[idx] > res[idx+1]:
		#		res[idx], res[idx+1] = res[idx+1], res[idx]
		#		counter += 1
		#		flag = True

		#	if idx == len(res) - 2 and flag:
		#		idx = 0
		#		flag = False
		#	else:
		#		idx += 1

"""


if __name__ == '__main__':
	obj1 = Solution()

	heights = [1,1,4,2,1,3]
	print(f'{heights}: {obj1.heightChecker(heights)}')

	heights = [5,1,2,3,4]
	print(f'{heights}: {obj1.heightChecker(heights)}')

	heights = [1,2,3,4,5]
	print(f'{heights}: {obj1.heightChecker(heights)}')