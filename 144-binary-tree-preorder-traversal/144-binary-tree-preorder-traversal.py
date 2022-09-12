# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        self.preOrder(root , answer)
        return answer 
    
    def preOrder(self , root , answer):
        
        if root == None:
            return 
        
        answer.append(root.val)
        self.preOrder(root.left , answer)
        self.preOrder(root.right , answer)
        
        return answer 