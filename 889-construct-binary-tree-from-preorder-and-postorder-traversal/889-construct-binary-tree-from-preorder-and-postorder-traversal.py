# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not postorder :
            return None
        
        currentNode = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return currentNode
        
        currentIndex = postorder.index(preorder[1])
        
        currentNode.left = self.constructFromPrePost(preorder[1 : currentIndex+2] , postorder[: currentIndex+1])
        currentNode.right =self.constructFromPrePost(preorder[currentIndex+2 :] ,postorder[currentIndex+1 : -1])
        
        return currentNode
        
        