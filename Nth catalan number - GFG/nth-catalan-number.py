#User function Template for python3

class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
       
       
       return self.nthCatalan(n,{})
       
    def nthCatalan(self,n,memo) :
        
        
        if n <= 1 :
            return 1 
            
        currentkey = n
        
        if currentkey in memo:
            return memo[currentkey]
            
        catalanNumbers = 0    
        for i in range (0,n) :
            catalanNumbers += self.nthCatalan(i,memo) * self.nthCatalan(n - i - 1,memo)
            
        memo[currentkey] = catalanNumbers   
        return memo[currentkey]
            

            
            
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        
        print(Solution().findCatalan(n))
        
# } Driver Code Ends