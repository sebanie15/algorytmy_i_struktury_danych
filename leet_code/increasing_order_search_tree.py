# 897


from __future__ import annotations

# Definition for a binary tree node.
from typing import List


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class BST:

	def __init__(self, value: int):
		self.root = TreeNode(value)

	def add_tree_node(self, value, parent: TreeNode):
		# if value < parent.val and not parent.left:
		# 	parent.left = TreeNode(value)
		# else:
		# 	self.add_tree_node(value, parent.left)

		temp = [self.root]
		while temp:
			t_node = temp.pop()
			if value < t_node.val and not t_node.left:
				t_node.left = TreeNode(value)
			else:
				temp.append(t_node.left)

			if value > t_node.val and not t_node.right:
				t_node.right = TreeNode(value)
			else:
				temp.append(t_node.right)


class Solution:

	def increasingBST(self, root: TreeNode) -> TreeNode:

		if not root: return TreeNode()

		treenode_list = [root]
		numbers = []
		while treenode_list:
			node = treenode_list.pop()
			if node.right:
				treenode_list.append(node.right)
			if node.left:
				treenode_list.append(node.left)
			numbers.append(node.val)

		numbers = sorted(numbers)
		# print(numbers)
		result = TreeNode(numbers[0])
		node = result
		for i in range(1, len(numbers)):
			node.right = TreeNode(numbers[i])
			node = node.right

		return result

	def increasingBST2(self, root):
		def inorder(node):
			if node:
				yield from inorder(node.left)
				yield node.val
				yield from inorder(node.right)

		ans = cur = TreeNode()

		for v in inorder(root):
			cur.right = TreeNode(v)
			cur = cur.right
		return ans.right


if __name__ == '__main__':
	obj1 = Solution()

	t1 = TreeNode(
		5,
		left=TreeNode(
			3,
			left=TreeNode(
				2,
				left=TreeNode(1)
			),
			right=TreeNode(4)
		),
		right=TreeNode(
			6,
			right=TreeNode(
				8,
				left=TreeNode(7),
				right=TreeNode(9)
			)
		)
	)

	print(obj1.increasingBST(t1))
