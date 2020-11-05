# 876

# Definition for singly-linked list.
class ListNode:

	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:

	def middleNode(self, head: ListNode) -> ListNode:
		A = [head]
		while A[-1].next:
			A.append(A[-1].next)
		return A[(len(A) // 2)]


if __name__ == '__main__':
	obj1 = Solution()

	head = ListNode()