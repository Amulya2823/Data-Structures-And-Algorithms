class Solution:
    def numTrees(self, n: int) -> int:
        
        return self.uniquetrees(n,{})
    
    def uniquetrees(self,n,memo):
        
        if n<= 1:
            return 1
        
        
        currentkey = n
        
        if currentkey in memo:
            return memo[currentkey]
        
        values = 0
        for i in range(0,n):
            values += self.uniquetrees(i,memo) * self.uniquetrees(n - i - 1,memo)
            
        memo[currentkey] = values   
        return memo[currentkey]
            
        