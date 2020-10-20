
# 1309

SHIFT_CHAR = 96 # ord('a') = 97


class Solution:

	def freqAlphabets(self, s: str) -> str:

		result = []
		idx = 0

		if len(s) == 1:
			return ''.join(chr(int(s[0]) + SHIFT_CHAR))

		while idx < len(s)-2:
			if s[idx+2] == '#':
				result.append(chr(int(s[idx:idx+2]) + SHIFT_CHAR))
				idx += 3
			else:
				result.append(chr(int(s[idx]) + SHIFT_CHAR))
				idx += 1
		if s[-1] != '#':
			result.append(chr(int(s[idx]) + SHIFT_CHAR))
			idx += 1
			if idx < len(s):
				result.append(chr(int(s[idx]) + SHIFT_CHAR))

		return ''.join(result)


if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.freqAlphabets("10#11#12"))
	print(obj1.freqAlphabets("1#"))
	print(obj1.freqAlphabets("26#11#418#5"))
