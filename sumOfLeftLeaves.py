class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        L = []
        self.addLeftToList(root, L, 2)
        return sum(L)
        
    def addLeftToList(self, root, L, subType):
        if(root.left == None and root.right == None):
            if(subType == 1):
                L.append(root.val)
        if(root.left != None):
            self.addLeftToList(root.left, L, 1)
        if(root.right != None):
            self.addLeftToList(root.right, L, 2)
