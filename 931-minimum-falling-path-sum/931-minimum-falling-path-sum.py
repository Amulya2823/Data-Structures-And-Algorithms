class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        answer = 100000
        memo = {}
        
        for currentCol in range(0 , n ):
            tempAns = self.minimumFalling(matrix , 0 , currentCol , n ,memo )
            answer = min (answer , tempAns)
            
        return answer 
    
    
    def minimumFalling(self , matrix , currentRow , currentCol , n , memo) :
        
        if currentRow < 0 or currentCol >= n or currentCol < 0 or currentCol >= n :
            return 100000
        
        if currentRow == n-1 :
            return matrix[currentRow][currentCol]
        
        currentKey = (currentRow , currentCol)
        
        if currentKey in memo:
            return memo[currentKey]
        
        
        down = matrix[currentRow][currentCol] + self.minimumFalling(matrix ,currentRow + 1 , currentCol , n , memo)
        diagonalleft = matrix[currentRow][currentCol] + self.minimumFalling(matrix ,currentRow +1, currentCol -1 , n , memo)
        diagonalright = matrix[currentRow][currentCol] + self.minimumFalling(matrix ,currentRow +1, currentCol + 1, n , memo)
        
        memo[currentKey] = min(down , diagonalleft,diagonalright)
        return memo[currentKey]
        
        
    

        
        