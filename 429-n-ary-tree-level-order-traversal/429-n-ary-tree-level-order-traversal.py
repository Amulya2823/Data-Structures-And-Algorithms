"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
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
                
                for child in currentnode.children:
                    queue.append(child)
                     
            result.append(level)
        return result
                
      
        