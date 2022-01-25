"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        self.answer = []
        self.preorderTraversal(root)
        return self.answer 
    
    def preorderTraversal(self,root):
        
        if root == None:
            return
        
        self.answer.append(root.val)
        for childNode in root.children:
            self.preorderTraversal(childNode)
                          
    
        