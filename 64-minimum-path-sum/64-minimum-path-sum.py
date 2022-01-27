class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        return self.totalways(0,0,m,n,grid,{})
    
    def totalways(self,currentrow,currentcolumn,m,n,grid,memo):
        
        if currentrow >= m or currentcolumn >= n :
            return 10000
        
        if currentrow == m-1 and currentcolumn == n-1:
            return grid[currentrow][currentcolumn]
        
        currentkey = str(currentrow) + "_" + str(currentcolumn)
        
        if currentkey in memo:
            return memo[currentkey]
            
        
        rightway = grid[currentrow][currentcolumn] + self.totalways(currentrow,currentcolumn + 1,m ,n,grid,memo)
        downway = grid[currentrow][currentcolumn] + self.totalways(currentrow+1,currentcolumn,m,n,grid,memo)
        
        memo[currentkey] = min(rightway,downway)
        return memo[currentkey]
    