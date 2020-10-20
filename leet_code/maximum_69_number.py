class Solution:

	def maximum69Number(self, num: int) -> int:
		s = list(str(num))
		idx = 0
		while idx < len(s):
			if s[idx] == '6':
				s[idx] = '9'
				break
			idx += 1

		return int(''.join(s))

if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.maximum69Number(9669))
	print(obj1.maximum69Number(669))
	print(obj1.maximum69Number(9999))
	print(obj1.maximum69Number(9996))
