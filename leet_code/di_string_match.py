
# 942
from typing import List


class Solution:

	def diStringMatch(self, S: str) -> List[int]:
		result = []
		start = 0
		stop = len(S)

		for char in S:
			if char == 'I':
				result.append(start)
				start += 1
			elif char == 'D':
				result.append(stop)
				stop -= 1
			else:
				result = []
				break
		return result + [start]


if __name__ == '__main__':
	obj1 = Solution()
	command = 'DDI'
	print(obj1.diStringMatch(command))
