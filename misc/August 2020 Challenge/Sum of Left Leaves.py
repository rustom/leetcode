# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def sumLeft(node):
            if not node:
                return
            if (node.left and not node.left.left and not node.left.right):
                self.total += node.left.val
            sumLeft(node.left)
            sumLeft(node.right)
        self.total = 0
        sumLeft(root)
        return self.total