
# 852
from typing import List


class Solution:

	def peakIndexInMountainArray(self, arr: List[int]) -> int:
		peak_index = 0
		length = len(arr)
		temp = 0
		idx = 0
		while idx < length-1:
			if arr[idx] < arr[idx+1]:
				peak_index += 1
				# print(arr[idx], arr[idx+1], peak_index)
			if peak_index == 0 or peak_index == length - 1:
				return None

			if arr[idx] > arr[idx+1]:
				temp += 1

			idx += 1

		if peak_index != length-temp-1:
			return None

		return peak_index

		# return arr.index(max(arr))


if __name__ == '__main__':

	obj1 = Solution()

	arr = [0, 1, 0]
	print(obj1.peakIndexInMountainArray(arr))

	arr = [0,2,1,0]
	print(obj1.peakIndexInMountainArray(arr))

	arr = [0,10,5,2]
	print(obj1.peakIndexInMountainArray(arr))

	arr = [3,4,5,1]
	print(obj1.peakIndexInMountainArray(arr))

	arr = [24,69,100,99,79,78,67,36,26,19]
	print(obj1.peakIndexInMountainArray(arr))