# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = []
        answer = []
        
        if root == None :
            return answer
        
        self.addLeftSubtree(root , stack) #make a call to left subtree
        
        while stack :     # make a call to node
            currentNode = stack.pop()
            answer.append(currentNode.val)
            
            if currentNode.right != None : #add all the left elements of the right subtree
                self.addLeftSubtree(currentNode.right , stack)
                
        return answer
    
    def addLeftSubtree(self , currentNode , stack):  # left child
        stack.append(currentNode)
        
        while currentNode.left != None :
            stack.append(currentNode.left)
            currentNode = currentNode.left
            
        return 
            
            
            
                
                
             
        
        
        
        
        
        
        
        
            
        
        
        