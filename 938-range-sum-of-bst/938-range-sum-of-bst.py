# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        answer = []
        
        self.sumofrange(root,low,high,answer)
        return sum(answer)
    
    def sumofrange(self,root,low,high,answer):
        
        if root is None:
            return 
        
        if root.val >= low and root.val <= high :
            answer.append(root.val)
            
            
        self.sumofrange(root.left,low,high,answer)
        self.sumofrange(root.right,low,high,answer)
        
        return 
    
    
    
    
    
    
     
   
        