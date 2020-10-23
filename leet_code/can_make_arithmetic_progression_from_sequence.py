
# 1502
from typing import List


class Solution:

	def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

		sorted_arr = sorted(arr)

		if len(sorted_arr) >= 2:
			diff = sorted_arr[0] - sorted_arr[1]
			for i in range(len(sorted_arr)-1):
				if diff != sorted_arr[i] - sorted_arr[i+1]:
					return False

				print(diff)
		else:
			return False

		return True


if __name__ == '__main__':
	obj1 = Solution()

	arr = [3,5,1]
	print(obj1.canMakeArithmeticProgression(arr))
	print('-'*40)
	arr = [1,2,4]
	print(obj1.canMakeArithmeticProgression(arr))