# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        self.prevVal=float('-inf')
        return self.isBST(root)
    
    def isBST(self,root):
        if root is None:
            return True
        
        left=self.isBST(root.left)
        if root.val<=self.prevVal:
            return False
        
        self.prevVal=root.val
        right=self.isBST(root.right)
        
        return left and right
