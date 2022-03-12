#User function Template for python3
class Solution:
	def maxSumIS(self, nums, n):
		
		answer = 0
		
		dp = [1]*n
		
		for i in range (n) :
		    dp[i] = nums[i]
		    answer = max (answer , dp[i])
		    
		    
		for i in range (1 , n) :
		    for j in range (i) :
		        
		        if nums[i] > nums[j] :
		            dp[i] = max (dp[i] , nums[i] + dp[j])
		            
		    answer = max(answer , dp[i])    
		    
		return answer     
		            
		
		

		
		
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends