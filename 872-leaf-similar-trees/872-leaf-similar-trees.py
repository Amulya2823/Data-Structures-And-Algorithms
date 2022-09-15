# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        leavesOft1 = []
        leavesOft2 = []
        
        self.findLeaves(root1 ,leavesOft1)
        self.findLeaves(root2 ,leavesOft2)
        
        return leavesOft1 == leavesOft2
    
    def findLeaves(self , root , leaves):
        
        if root == None:
            return 
        
        if root.left == None and root.right == None:
            leaves.append(root.val)
            return 
        
        self.findLeaves(root.left , leaves)
        self.findLeaves(root.right , leaves)
        
        return 
        
    
        