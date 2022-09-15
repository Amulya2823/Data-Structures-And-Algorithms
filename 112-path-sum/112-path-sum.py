# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        return self.pathSum(root , target , 0)
    
    def pathSum(self , root , target , currentSum):
    
        if root == None:
            return False
        
        if root.left == None and root.right == None :
            return currentSum + root.val == target
        
        a = self.pathSum(root.left , target ,currentSum + root.val)
        b =self.pathSum(root.right, target ,currentSum + root.val)
        
        return a or b
        
        
        