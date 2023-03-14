#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, N):
        # code here 
        sum = 0
        armstrong = N
        while N :
            lastDigit = N%10
            sum = sum + (lastDigit*lastDigit*lastDigit)
            N = N//10
            
        if sum == armstrong :
            return "Yes"
        else :
            return "No"
           
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends