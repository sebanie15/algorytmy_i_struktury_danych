
# 728
from typing import List


class Solution:

	def selfDividingNumbers(self, left: int, right: int) -> List[int]:

		def self_dividing(n: int) -> bool:
			for d in str(n):
				if d == '0' or n % int(d) > 0:
					return False
			return True

		result = []
		if 1 <= left <= right <= 10000:
			for i in range(left, right+1):
				if self_dividing(i):
					result.append(i)

		return result


if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.selfDividingNumbers(1, 22))
