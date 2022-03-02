class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        answer = 0
        m = len(grid)
        n = len(grid[0])
        
        for currentRow in range(m):
            for currentCol in range(n):
                
                if grid[currentRow][currentCol] == '1' :
                    answer += 1
                    self.numberIslands(grid , currentRow , currentCol , m , n)
                    
        return answer 
    
    def numberIslands(self , grid , currentRow , currentCol , m ,n ):
        queue = collections.deque()
        queue.append((currentRow, currentCol))
        
        
        while queue :
            currentRow,currentCol = queue.popleft()
            
            if currentRow < 0 or currentRow >= m or currentCol < 0 or currentCol >= n or grid[currentRow][currentCol] == '0' :
                continue 
                
            grid[currentRow][currentCol] = '0'
            queue.append((currentRow + 1, currentCol ))
            queue.append((currentRow - 1, currentCol ))
            queue.append((currentRow , currentCol + 1))
            queue.append((currentRow , currentCol - 1))
            
        return 
            
            