# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = []
        stack = []
        
        if root == None:
            return []
        
        stack.append(root)
        
        while stack :
            currentNode = stack.pop()
            answer.append(currentNode.val)
            
            if currentNode.left :
                stack.append(currentNode.left)
                
            if currentNode.right :
                stack.append(currentNode.right)
                
        return answer[::-1]