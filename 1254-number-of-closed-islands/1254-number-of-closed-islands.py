class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        answer = 0
        
        for currentCol in range(n):
            
            if grid[0][currentCol] == 0:
                self.dfs(grid , 0 ,currentCol , m , n)
                
            if grid[m-1][currentCol] == 0:
                self.dfs(grid , m-1 ,currentCol , m , n)
                
        for currentRow in range(m):
            
            if grid[currentRow][0] == 0:
                self.dfs(grid , currentRow , 0 ,m ,n)
                
            if grid[currentRow][n-1] == 0:
                self.dfs(grid , currentRow , n-1 , m , n)
                
        for currentRow in range(m):
            for currentCol in range(n):
                
                if grid[currentRow][currentCol] == 0:
                    self.dfs(grid ,currentRow , currentCol, m , n)
                    answer += 1
                    
        return answer
    
    def dfs(self , grid ,currentRow , currentCol , m , n):
        
        if currentRow < 0 or currentRow >= m or currentCol < 0 or currentCol >= n or grid[currentRow][currentCol] == 1 :
            return 
        
        grid[currentRow][currentCol] = 1
        
        self.dfs(grid , currentRow+1 , currentCol , m , n)
        self.dfs(grid , currentRow-1 , currentCol , m , n)
        self.dfs(grid , currentRow , currentCol+1 , m , n)
        self.dfs(grid , currentRow , currentCol -1, m , n)
        
        return 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        