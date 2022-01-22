# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root==None:
            return root
   
        
        if root==p or root==q:
            return root
        
        
        leftans = self.lowestCommonAncestor(root.left, p, q)
        rightans = self.lowestCommonAncestor(root.right, p, q)
        
        if leftans and not rightans:
            return leftans
        
        if not leftans and rightans:
            return rightans
        
        if leftans and rightans:
            return root
        
        
        
        
        

        
        
        
        
        
        
        
    
        
        
        
        
        