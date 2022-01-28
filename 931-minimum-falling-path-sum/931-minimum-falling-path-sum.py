class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        answer = 100000
        memo ={}
        
        for currentcolumn in range(0,n):
            tempans = self.minimumsum(0,currentcolumn,matrix,n,memo)
            answer = min(answer,tempans)
            
        return answer 
    def minimumsum(self,currentrow,currentcolumn,matrix,n,memo) :
        
        if currentrow >= n or currentrow < 0 or currentcolumn >= n or currentcolumn < 0 :
            return 100000
        
        if currentrow == n-1 :
            return matrix[currentrow][currentcolumn]
        
        currentkey = (currentrow,currentcolumn)
        
        if currentkey in memo:
            return memo[currentkey]
        
        
        down = matrix[currentrow][currentcolumn] + self.minimumsum(currentrow +1 ,currentcolumn , matrix,n,memo)
        diagleft = matrix[currentrow][currentcolumn] + self.minimumsum(currentrow +1 ,currentcolumn - 1 , matrix,n,memo)
        diagright = matrix[currentrow][currentcolumn] + self.minimumsum(currentrow +1 ,currentcolumn + 1, matrix,n,memo)
        
        memo[currentkey] = min(down,diagleft,diagright)
        return memo[currentkey]
        
        