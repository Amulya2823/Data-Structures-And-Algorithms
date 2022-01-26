class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        return self.totalways(0,0,m,n,{})
    
    def totalways(self,currentrow,currentcol,m,n,memo):
        
        if currentrow == m-1 and currentcol == n-1:
            return 1
        
        if currentrow > m or currentcol > n:
            return 0
        
        
        currentkey = str(currentrow) + "_" + str(currentcol)
        
         
        if currentkey in memo:
            return memo[currentkey]
        
        
        rightway = self.totalways(currentrow,currentcol+1,m,n,memo)
        downway = self.totalways(currentrow+1,currentcol,m,n,memo)
        
        memo[currentkey] = rightway+downway
        return memo[currentkey]
        
        
        
        
        