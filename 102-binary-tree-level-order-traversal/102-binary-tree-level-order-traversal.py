# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = []
        queue.append(root)
        result = []
        
        while len(queue) > 0:
            level = []
            for i in range(len(queue)): 
                currentnode = queue.pop(0)
                level.append(currentnode.val)    
                
                if currentnode.left:
                    queue.append(currentnode.left)
                if currentnode.right:
                    queue.append(currentnode.right)
            result.append(level)
        return result
                
                
                
                
                
        
           
               
            
            
            
            
            
        
       