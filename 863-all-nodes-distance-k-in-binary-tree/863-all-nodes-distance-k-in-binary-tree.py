# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        memo = {}
        answer = []
        
        self.allParents(None , root , memo)
        
        self.distanceAtK(target , k , memo , answer , [])
        return answer 
    
    def allParents (self ,currentParent , root , memo):
        
        if root == None:
            return 
        
        memo[root] = currentParent
        self.allParents(root, root.left , memo)
        self.allParents(root ,root.right , memo)
        
    def distanceAtK(self , root , k , memo ,answer , visited):
        
        if root == None :
            return 
        
        if root in visited :
            return
        
        visited.append(root)
        
        if k == 0 :
            answer.append(root.val)
            return 
        
        self.distanceAtK(root.left , k-1 , memo , answer , visited)
        self.distanceAtK(root.right , k-1 , memo , answer , visited)
        self.distanceAtK(memo[root] , k-1 , memo , answer , visited)
        
        
        
        
        
        
        
        