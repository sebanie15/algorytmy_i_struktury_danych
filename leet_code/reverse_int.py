
# 7

class Solution:

	def reverse(self, x: int) -> int:
		"""
		Args:
			x: int
		Returns:
			 int
		"""

		limit = 2147483648

		if x < 0:
			k = -1
		else:
			k = 1

		if abs(x) > limit:
			return 0
		else:
			return int(str(abs(x))[::-1]) * k


if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.reverse(1534236469))
