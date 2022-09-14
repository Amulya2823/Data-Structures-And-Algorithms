# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        answer = []
        self.rootToleaf(root,"",answer)
        return answer
    
    def rootToleaf(self,root,currentpath,answer):
        if root == None:
            return 
        
        if root.left == None and root.right == None:
            currentpath += str(root.val)
            answer.append(currentpath)
            return 
        
     
        self.rootToleaf(root.left,currentpath+str(root.val)+ '->',answer)
        self.rootToleaf(root.right,currentpath+str(root.val)+ '->',answer)
        return answer
    
