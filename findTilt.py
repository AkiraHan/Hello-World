# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        if(root == None):
            return result
        result = result + abs(self.subSum(root.left) - self.subSum(root.right))
        result = result + self.findTilt(root.left) + self.findTilt(root.right)
        return result
    
    def subSum(self, root):
        subS = 0
        if(root == None):
            return subS
        subS = root.val + self.subSum(root.left) + self.subSum(root.right)
        return subS
