
# 1356
from typing import List


class Solution:

	def sortByBits(self, arr: List[int]) -> List[int]:

		def bits_count(entry: int) -> int:
			return bin(entry).count('1')

		result = sorted(arr)
		result.sort(key=bits_count)
		return result


if __name__ == '__main__':
	obj1 = Solution()
	result = obj1.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8])
	print(result)

	obj1 = Solution()
	result = obj1.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1])
	print(result)

	obj1 = Solution()
	result = obj1.sortByBits([10000, 10000])
	print(result)

	obj1 = Solution()
	result = obj1.sortByBits([2, 3, 5, 7, 11, 13, 17, 19])
	print(result)

	obj1 = Solution()
	result = obj1.sortByBits([10, 100, 1000, 10000])
	print(result)
