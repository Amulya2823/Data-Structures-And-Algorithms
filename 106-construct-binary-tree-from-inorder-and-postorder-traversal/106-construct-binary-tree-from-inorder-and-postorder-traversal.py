# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        postIndex = [len(postorder)-1] #we will initialize it with last element in postorder
        
        memo = {}
        
        for i in range(len(inorder)):
            memo[inorder[i]] = i
            
        return self.constructTree(inorder , postorder , postIndex , 0 , len(inorder)-1 , memo)
    
    def constructTree(self , inorder , postorder , postIndex , inStart , inEnd , memo):
        
        if inStart > inEnd :
            return None
        
        currentVal = postorder[postIndex[0]]
        currentNode = TreeNode(currentVal)
        postIndex[0] -= 1
        
        i = memo[currentVal]
        
        currentNode.right = self.constructTree(inorder , postorder , postIndex ,i+1 ,inEnd, memo)
        currentNode.left = self.constructTree(inorder , postorder , postIndex , inStart , i-1, memo)
        
        return currentNode
        