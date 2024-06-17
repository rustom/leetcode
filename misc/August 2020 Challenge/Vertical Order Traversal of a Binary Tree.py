# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = []
        
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.helper((0, 0, root))
        xVals = [item[0] for item in self.nodes]
        xVals = sorted(set(xVals))
        result = []
        subList = []
        for x in xVals:
            subList = [item for item in self.nodes if item[0] == x]
            subList.sort(key = lambda x: (-x[1], x[2].val))
            subList = [item[2].val for item in subList]
            result.append(subList)
        return result
        
    def helper(self, item: (int, int, TreeNode)):
        self.nodes.append(item)
        if item[2].left != None:
            self.helper((item[0] - 1, item[1] - 1, item[2].left))
        if item[2].right != None:
            self.helper((item[0] + 1, item[1] - 1, item[2].right))