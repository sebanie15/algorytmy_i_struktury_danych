# 700

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:

	def searchBST(self, root: TreeNode, val: int) -> TreeNode:
		while root and root.val != val:
			if root.val > val:
				root = root.left
			else:
				root = root.right

		return root


if __name__ == '__main__':
	obj1 = Solution()
	t1 = TreeNode(1, left=TreeNode(3, left=TreeNode(5)), right=TreeNode(2))
	t2 = TreeNode(2, left=TreeNode(1, right=TreeNode(4)), right=TreeNode(3, right=(7)))
	print(obj1.searchBST(t1, 2))
	print(t1.right)