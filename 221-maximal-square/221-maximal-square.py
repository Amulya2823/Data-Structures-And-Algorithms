class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        memo = {}
        area = 0
        
        for currentRow in range(m):
            for currentCol in range(n):
                
                if matrix[currentRow][currentCol] == '1':
                    side = self.maximumSize(matrix , currentRow,currentCol , m , n , memo)
                    area = max(area , side*side)
                    
        return area
                    
        
    def maximumSize(self , matrix , currentRow , currentCol , m , n , memo):
        
        if currentRow < 0 or currentRow >= m or currentCol < 0 or currentCol >= n or matrix[currentRow][currentCol] == '0':
            return 0
        
        currentKey = (currentRow , currentCol)
        
        if currentKey in memo :
            return memo[currentKey]
        
        rightSide = 1 + self.maximumSize(matrix , currentRow , currentCol + 1, m , n , memo)
        downSide =  1 + self.maximumSize(matrix , currentRow + 1 , currentCol , m , n,memo)
        rightDiag = 1 + self.maximumSize(matrix , currentRow + 1 , currentCol + 1 , m ,n,memo)
        
        memo[currentKey] = min(rightSide , min(downSide , rightDiag))
        return memo[currentKey]
                    
                    
                    
        