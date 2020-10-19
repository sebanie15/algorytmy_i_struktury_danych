
# 680

class Solution:
	def validPalindrome(self, s: str) -> bool:

		if s == s[::-1]: return True

		start, stop = 0, len(s) - 1
		while start < stop:
			if s[start] != s[stop]:
				a = s[:start] + s[start + 1:]
				b = s[:stop] + s[stop + 1:]
				print(a, a[::-1])
				return a == a[::-1] or b == b[::-1]
			else:
				start += 1
				stop -= 1
		return True

if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.validPalindrome('cbbcc'))
	print('abca'[:3], 'abca'[4:])
