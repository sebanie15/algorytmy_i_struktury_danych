# 1370

class Solution:
	def sortString(self, s: str) -> str:

		result = ''
		values = list(s)
		sorted_values_keys = sorted(list(set(s)))

		while values:
			for i in sorted_values_keys:
				if i in values:
					result += values.pop(values.index(i))

			for i in sorted_values_keys[::-1]:
				if i in values:
					result += values.pop(values.index(i))

		return result


if __name__ == '__main__':
	obj1 = Solution()
	s = "aaaabbbbcccc"
	print(obj1.sortString(s))
	s2 = "leetcode"
	print(obj1.sortString(s2))
	s2 = "ggggggg"
	print(obj1.sortString(s2))
	s2 = ""
	print(obj1.sortString(s2))
