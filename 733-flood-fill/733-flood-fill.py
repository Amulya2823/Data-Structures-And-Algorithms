class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if grid[sr][sc] == newColor :
            return grid 
        
        m = len(grid)
        n = len(grid[0])
        color = grid[sr][sc]
        
        
        queue = collections.deque()
        queue.append((sr , sc))
        
        while queue :
            currentRow , currentCol = queue.popleft()
            
            
            if currentRow < 0 or currentRow >= m or currentCol < 0 or currentCol >= n or grid[currentRow][currentCol]!= color :
                continue
                
            grid [currentRow][currentCol] =  newColor  
            queue.append((currentRow + 1 , currentCol))
            queue.append((currentRow - 1 , currentCol))
            queue.append((currentRow  , currentCol + 1))
            queue.append((currentRow  , currentCol - 1))
            
        return grid 
            
           
        