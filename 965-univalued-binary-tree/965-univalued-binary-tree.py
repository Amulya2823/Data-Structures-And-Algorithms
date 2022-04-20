# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.uniValued(root , root.val)
    
    def uniValued(self , root , currentVal) :
        
        if root == None :
            return True 
        
        if root.val != currentVal :
            return False 
        
        leftAns = self.uniValued(root.left , currentVal)
        rightAns = self.uniValued(root.right , currentVal) 
        
        return leftAns and rightAns
        