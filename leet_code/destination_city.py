
# 1436
from typing import List


class Solution:

	def destCity(self, paths: List[List[str]]) -> str:

		idx = 0
		from_airports = [fly[0] for fly in paths]

		while idx < len(paths):
			if not paths[idx][1] in from_airports:
				return paths[idx][1]
			idx += 1


if __name__ == '__main__':
	obj1 = Solution()
	paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
	paths2 = [["B", "C"], ["D", "B"], ["C", "A"]]
	paths3 = [['A', 'Z']]
	print(obj1.destCity(paths3))
