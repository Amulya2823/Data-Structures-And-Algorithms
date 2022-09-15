# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sumToLeft(root , False)
    
    def sumToLeft(self , root , onLeftSide):
        
        if root == None:
            return 0 
        
        if root.left == None and root.right == None:
            return root.val if onLeftSide else 0
        
        leftAns = self.sumToLeft(root.left , True)
        rightAns = self.sumToLeft(root.right , False)
        
        return leftAns + rightAns
        
        
        