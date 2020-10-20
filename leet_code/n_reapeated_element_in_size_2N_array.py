
# 961
from typing import List


class Solution:

	def repeatedNTimes(self, A: List[int]) -> int:

		if 4 <= len(A) <= 10000 and 0 <= max(A) <= 10000 and len(A) % 2 == 0:
			set_number = set(A)
			for number in set_number:
				if A.count(number) > 1:
					return number


if __name__ == '__main__':
	obj1 = Solution()
	numbers = [1, 2, 3, 3]
	print(obj1.repeatedNTimes(numbers))

	numbers = [2,1,2,5,3,2]
	print(obj1.repeatedNTimes(numbers))

	numbers = [5,1,5,2,5,3,5,4]
	print(obj1.repeatedNTimes(numbers))
