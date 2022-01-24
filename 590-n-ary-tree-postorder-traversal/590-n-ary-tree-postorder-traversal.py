"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        self.answer = []
        self.postorderTraversal(root)
        return self.answer 
    
    def postorderTraversal(self,root):
        
        if root == None :
            return 
        
        for childNode in root.children:
            self.postorderTraversal(childNode)
        self.answer.append(root.val)

        