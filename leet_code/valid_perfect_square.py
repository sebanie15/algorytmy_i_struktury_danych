
# 367

class Solution:

	def isPerfectSquare(self, num: int) -> bool:

		min, max = 0, num + 1
		while min < max:
			mid = (min + max) // 2
			if mid * mid == num:
				return True
			if mid * mid > num:
				max = mid
			else:
				min = mid + 1
		return False


if __name__ == '__main__':
	obj1 = Solution()
	print(obj1.isPerfectSquare(36))