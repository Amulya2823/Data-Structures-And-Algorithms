class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if grid[sr][sc] == newColor :
            return grid
        
        self.floodAlgo(grid , sr , sc , grid[sr][sc] , len(grid) , len(grid[0]) , newColor) 
        return grid 
    
    def floodAlgo(self , grid , currentRow , currentCol , color , m , n , newColor):
        
        if currentRow < 0 or currentRow >= m or currentCol < 0 or currentCol >= n or grid[currentRow][currentCol]!= color :
            return 
        
        grid [currentRow][currentCol] = newColor 
        
        #up
        self.floodAlgo(grid , currentRow - 1 , currentCol , color , m , n , newColor)
        
        #down
        self.floodAlgo(grid , currentRow + 1 , currentCol , color , m , n , newColor)
        
        #left
        self.floodAlgo(grid , currentRow , currentCol - 1 , color , m , n , newColor)
        
        #right
        self.floodAlgo(grid , currentRow , currentCol + 1 , color , m , n , newColor)
        
        return 
        