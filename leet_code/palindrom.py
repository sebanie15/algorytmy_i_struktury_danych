
# 9

class Solution:
	def isPalindrome(self, x: int) -> bool:
		return str(x) == str(x)[::-1]


if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.isPalindrome(120))
