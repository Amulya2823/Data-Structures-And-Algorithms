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
        
        
        a = self.lowestCommonAncestor(root.left, p, q)
        b = self.lowestCommonAncestor(root.right, p, q)
        
        if a and not b:
            return a
        
        if not a and b:
            return b
        
        if a and b:
            return root
        
        
        
        
        

        
        
        
        
        
        
        
    
        
        
        
        
        