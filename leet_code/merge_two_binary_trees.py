# 617

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:

	def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
		if not t1:
			return t2
		if not t2:
			return t1
		t1.val += t2.val
		t1.left = self.mergeTrees(t1.left, t2.left)
		t1.right = self.mergeTrees(t1.right, t2.right)
		return t1


if __name__ == '__main__':
	obj1 = Solution()
	t1 = TreeNode(1, left=TreeNode(3, left=TreeNode(5)), right=TreeNode(2))
	t2 = TreeNode(2, left=TreeNode(1, right=TreeNode(4)), right=TreeNode(3, right=(7)))
	obj1.mergeTrees(t1, t2)
	print(t1)