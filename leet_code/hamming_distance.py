
# 461

class Solution:

	def hammingDistance(self, x: int, y: int) -> int:

		return bin(x^y).count('1')

	def hammingDistance2(self, x: int, y: int) -> int:
		x = x ^ y
		count = 0
		while x > 0:
			if x & 1 == 1:
				count += 1
			x = x >> 1
		return count


if __name__ == '__main__':
	a = 4
	b = 1^4
	# b = b[:-2]
	print(bin(b).count('1'))

	obj1 = Solution()
	print(obj1.hammingDistance(1, 4))
