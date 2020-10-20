
# 1351
from typing import List


class Solution:

	def countNegatives(self, grid: List[List[int]]) -> int:
		result = 0

		for list in grid:
			for number in list:
				if number < 0:
					result += 1

		return result


if __name__ == '__main__':
	obj1 = Solution()
	grid1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
	print(obj1.countNegatives(grid1))
	grid2 = [[1,-1],[-1,-1]]
	print(obj1.countNegatives(grid2))
	grid3 = [[-1]]
	print(obj1.countNegatives(grid3))
	grid3 = [[3,2],[1,0]]
	print(obj1.countNegatives(grid3))
