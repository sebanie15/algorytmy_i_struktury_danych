
# 1299
from typing import List


class Solution:

	def replaceElements(self, arr: List[int]) -> List[int]:
		result = []
		idx = 0
		if 1 <= len(arr) <= 10000 and 1 <= max(arr) <= 100000:
			while idx < len(arr)-1:
				if arr[idx:]:
					result.append(max(arr[idx+1:]))
				idx += 1
			result.append(-1)

		return result


if __name__ == '__main__':
	obj1 = Solution()
	arr = [17, 18, 5, 4, 6, 1]
	print(obj1.replaceElements(arr))
