# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preIndex = [0]
        memo = {}
        
        for i in range (len(inorder)):
            memo[inorder[i]] = i
            
        return self.constructTree(preorder ,inorder , preIndex , 0 , len(inorder)-1,memo)
    
    def constructTree(self , preorder , inorder , preIndex ,inStart , inEnd , memo):
        
        if inStart > inEnd :
            return None 
        
        currentVal = preorder[preIndex[0]]
        currentNode = TreeNode(currentVal)
        preIndex[0] += 1
        
        i = memo[currentVal]
        
        currentNode.left = self.constructTree(preorder , inorder , preIndex , inStart , i-1 , memo)
        currentNode.right =self.constructTree(preorder , inorder , preIndex , i+1 , inEnd , memo)
        
        return currentNode
        
        
        
        
        