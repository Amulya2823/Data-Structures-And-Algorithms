class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        answer = 0
        
        
        for currentRow in range (m):
            for currentCol in range (n):
                if grid[currentRow][currentCol] == '1' :
                    answer += 1
                    self.numberIslands(grid , currentRow , currentCol , m , n)
                    
        return answer
    
    def numberIslands(self , grid , currentRow , currentCol , m , n):
        
        if currentRow < 0 or currentRow >= m or currentCol < 0 or currentCol >= n or grid[currentRow][currentCol] == '0' :
            return 
        
        grid [currentRow][currentCol] = '0'
        
        self.numberIslands(grid , currentRow + 1, currentCol , m , n)
        self.numberIslands(grid , currentRow - 1, currentCol , m , n)
        self.numberIslands(grid , currentRow , currentCol + 1, m , n)
        self.numberIslands(grid , currentRow , currentCol - 1, m , n)
        
        
        return 
    
    
                
        
        