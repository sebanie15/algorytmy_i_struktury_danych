
# 832
from typing import List


class Solution:

	def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
		result = []

		for entry in A:
			result.append([number ^ 1 for number in entry[::-1]])

		return result


if __name__ == '__main__':
	img = Solution()
	img_array = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
	print(img.flipAndInvertImage(img_array))
