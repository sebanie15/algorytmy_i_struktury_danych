# 1374

class Solution:
	def generateTheString(self, n: int) -> str:
		result = ''
		if 1 <= n <= 500:
			if n % 2 == 0:
				result = 'a' * (n-1) + 'b'
			else:
				result = 'a' * n

		return result


if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.generateTheString(7))
