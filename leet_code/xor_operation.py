
# 1486

class Solution:

	def xorOperation(self, n: int, start: int) -> int:
		result = 0
		for i in range(n):
			result ^= start + 2 * i
		return result


if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.xorOperation(10, 5))
