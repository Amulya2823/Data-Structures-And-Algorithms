#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        answer = 0
        memo = {}
        
        for currentcolumn in range(0,N):
            tempans = self.maximumpathsum(0,currentcolumn,Matrix,N,memo)
            answer = max(answer,tempans)
            
        return answer
        
    def maximumpathsum(self,currentrow,currentcolumn,Matrix,N,memo) :
        
        if currentrow < 0 or currentrow >= N or currentcolumn < 0 or currentcolumn >= N:
            return 0
        
        if currentrow == N-1 :
            return Matrix[currentrow][currentcolumn]
            
        currentkey = (currentrow,currentcolumn)
        
        if currentkey in memo:
            return memo[currentkey]
            
        downmove = Matrix[currentrow][currentcolumn] + self.maximumpathsum(currentrow + 1,currentcolumn,Matrix,N,memo)
        diagonallyleft = Matrix[currentrow][currentcolumn] + self.maximumpathsum(currentrow + 1,currentcolumn - 1,Matrix,N,memo)
        diagonallyright = Matrix[currentrow][currentcolumn] + self.maximumpathsum(currentrow + 1,currentcolumn + 1,Matrix,N,memo)
        
        memo[currentkey] = max(downmove,diagonallyleft,diagonallyright)
        return memo[currentkey] 
        
       
      
        
         
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends