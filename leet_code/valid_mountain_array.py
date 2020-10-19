
# 941

from typing import List


class Solution:

	def validMountainArray(self, A: List[int]) -> bool:
		length = len(A)

		if length >= 3:
			tip_idx = A.index(max(A)) # index with max value
			if tip_idx == 0 or tip_idx == length - 1:
				return False
		else:
			return False

		for i in range(length-1):
			if A[i] == A[i+1]:
				return False
			if i < tip_idx and A[i] > A[i+1]:
				return False
			if i >= tip_idx and A[i] < A[i+1]:
				return False

		return True





if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.validMountainArray([0,1,2,3,4,5,6,7,8,9]))
	print(obj1.validMountainArray([3, 5, 5]))
	print(obj1.validMountainArray([0, 3, 2, 1]))
	print(obj1.validMountainArray([0, 2, 3, 2, 5, 2, 1, 0]))

	for i in range(1, 2):
		print('siema')