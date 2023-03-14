#User function Template for python3

class Solution:
	def is_palindrome(self, n):
		# Code here
		sum = 0
		palindrome = n #u should store a duplicate beacuse at the end n becomes zero if u compare
		while n > 0 :
		    ld = n%10 
		    sum = sum*10 + ld
		    n = n // 10
		    
		if sum == palindrome :
		    return "Yes"
	    else:
		    return "No"
		        
		  
		        
		  
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends