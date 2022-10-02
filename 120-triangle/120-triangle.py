class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        return self.minSum(triangle , 0 , 0 , memo)
    
    def minSum(self ,triangle , currentRow , currentCol , memo):
        
        if currentRow == len(triangle)-1:
            return triangle[currentRow][currentCol]
        
        currentKey = (currentRow , currentCol)
        
        if currentKey in memo :
            return memo[currentKey]
        
        
        left = triangle[currentRow][currentCol] + self.minSum(triangle ,currentRow +1 , currentCol , memo)
        right = triangle[currentRow][currentCol] + self.minSum(triangle ,currentRow + 1 , currentCol + 1 , memo)
            
        memo[currentKey] = min(left , right)
        return memo[currentKey]
            
            
            
        
        