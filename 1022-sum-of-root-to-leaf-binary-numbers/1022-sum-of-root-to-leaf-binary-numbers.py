# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        answer = [0]*1
        answer[0] = 0
        
        self.rootToLeaf(root , ""  , answer)
        return answer[0]
    
    def rootToLeaf(self , root , currentPath , answer) :
        
        if root.left is None and root.right is None :
            currentPath += str(root.val)
            answer[0] += int(currentPath , 2)
            return 

        if root.left is not None :
            self.rootToLeaf(root.left , currentPath + str(root.val) , answer)
            
        if root.right is not None :
            self.rootToLeaf(root.right , currentPath + str(root.val) , answer)
            
        return 
        
        
        
        
        
        
        