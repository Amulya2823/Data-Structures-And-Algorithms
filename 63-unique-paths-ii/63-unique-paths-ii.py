class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        return self.totalways(0,0,m,n,obstacleGrid,{})
    
    def totalways(self,currentrow,currentcolumn,m,n,obstacleGrid,memo):
        
        if currentrow >= m or currentcolumn >= n or obstacleGrid[currentrow][currentcolumn] == 1:
            return 0
        
        if currentrow == m-1 and currentcolumn == n-1:
            return 1
        
        currentkey = str(currentrow) + "_" + str(currentcolumn)
        
        if currentkey in memo:
            return memo[currentkey]
            
        
        rightway = self.totalways(currentrow,currentcolumn + 1,m ,n,obstacleGrid,memo)
        downway = self.totalways(currentrow+1,currentcolumn,m,n,obstacleGrid,memo)
        
        memo[currentkey] = rightway + downway
        return memo[currentkey]
    
        
        
        
        