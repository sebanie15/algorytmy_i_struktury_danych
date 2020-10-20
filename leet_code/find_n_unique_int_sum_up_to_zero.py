
# 1304
from typing import List


class Solution:
	def sumZero(self, n: int) -> List[int]:
		result =[]

		if n % 2 == 0:
			for i in range(1, n//2 + 1):
				result.append(i)
				result.append(-i)
		else:
			result.append(0)
			for i in range(1, n//2 + 1):
				result.append(i)
				result.append(-i)

		return result


if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.sumZero(3))
	print(obj1.sumZero(1))
	print(obj1.sumZero(5))
