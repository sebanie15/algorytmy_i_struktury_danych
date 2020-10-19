
# 125

import re

class Solution:

	def isPalindrome(self, s: str) -> bool:
		pattern = "[a-z0-9]"
		value = re.findall(pattern, s.lower())
		print(value)

		return value == value[::-1]



if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.isPalindrome("a"))
