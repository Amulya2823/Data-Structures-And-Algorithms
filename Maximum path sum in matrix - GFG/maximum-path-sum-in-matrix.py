#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
       
       answer = 0
       memo = {}
       
       for currentColumn in range(0,N):
           tempans = self.maximumsum(0,currentColumn,Matrix,N,memo)
           answer = max(answer,tempans)
           
       return answer 
        
    def maximumsum(self,currentRow,currentColumn,Matrix,N,memo):
        
        if currentRow >= N or currentRow < 0 or currentColumn >= N or currentColumn <0 :
            return 0
            
        currentkey = (currentRow,currentColumn)  
        
        if currentkey in memo:
            return memo[currentkey]
            
        if currentRow == N-1 :
            return Matrix[currentRow][currentColumn]
            
            
        down = Matrix[currentRow][currentColumn] + self.maximumsum(currentRow+1 , currentColumn,Matrix,N,memo)
        diagleft = Matrix[currentRow][currentColumn] + self.maximumsum(currentRow+1 , currentColumn-1,Matrix,N,memo)
        diagright = Matrix[currentRow][currentColumn] + self.maximumsum(currentRow +1, currentColumn +1,Matrix,N,memo)
        
        memo[currentkey] = max(down,diagleft,diagright)
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