# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        levels = [-1,-1]
        parents = [-1,-1]
        
        self.cousinsoftree(root,x,y,levels,parents,0,TreeNode(-1))
        
        if (levels[0] == levels[1]) and (parents[0]!= parents[1]):
            return True
        
        return False
    
    def cousinsoftree(self,root,x,y,levels,parents,currentlevel,currentparent):
        
        if root == None:
            return 
        
        if root.val == x:
            levels[0] = currentlevel
            parents[0] = currentparent
            
        if root.val == y:
            levels[1] = currentlevel
            parents[1] = currentparent
            
        self.cousinsoftree(root.left,x,y,levels,parents,currentlevel+1,root)
        self.cousinsoftree(root.right,x,y,levels,parents,currentlevel+1,root)
        
        return
            
            
        
        
        
        
        