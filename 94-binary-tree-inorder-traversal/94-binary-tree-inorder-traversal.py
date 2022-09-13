# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        self.inOrder(root , answer)
        return answer 
    
    def inOrder(self , root , answer):
        
        if root == None:
            return 
        
        self.inOrder(root.left , answer)
        answer.append(root.val)
        self.inOrder(root.right, answer)
        
        return answer 
        
        
        
        
        
        