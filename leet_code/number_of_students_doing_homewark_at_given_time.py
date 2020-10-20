
# 1450
from typing import List


class Solution:
	def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

		idx = 0
		result = 0

		while idx < len(startTime) and idx < len(endTime):
			if startTime[idx] <= queryTime <= endTime[idx]:
				result += 1
			idx += 1

		return result


if __name__ == '__main__':

	obj1 = Solution()
	startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1]
	endTime = [10,10,10,10,10,10,10,10, 10]

	print(obj1.busyStudent(startTime, endTime, 5))
	print(obj1.busyStudent([4], [4], 4))
