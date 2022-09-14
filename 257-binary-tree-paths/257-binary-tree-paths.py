# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    
        answer = []
        
        self.rootToLeaf(root , "" + str(root.val)  , answer)
        return answer
    
    def rootToLeaf(self , root , currentPath , answer) :
        
        if root.left is None and root.right is None :
            answer.append(currentPath)
            return 

        if root.left is not None :
            self.rootToLeaf(root.left , currentPath + "->" + str(root.left.val) , answer)
            
        if root.right is not None :
            self.rootToLeaf(root.right , currentPath + "->" + str(root.right.val) , answer)
            
        return 
        
        