#User function Template for python3

class Solution:
    def minTime (self, arr, n, k):
        totalSum = 0
       
        for i in range (n):
           totalSum += arr[i]
       
        start = 0
        end = totalSum
       
        answer = -1
       
        while (start <= end) :
            mid = start + (end - start)//2
           
            if self.isPossible( arr , n , k , mid ):   #ifthecoditioniscorrect,returntrueelsereturnfalse
               answer = mid 
               end = mid - 1
               
            else :
                start = mid + 1
                
        return answer    
        
        
    def isPossible(self , pages , n , m , boundVal)  :
        studentCount = 1
        currentSum = 0 
        
        
        for currentPage in pages :
            
            if (currentPage > boundVal ):
                return False 
                
            if (currentPage + currentSum <= boundVal)  :
                currentSum += currentPage 
                
            else :
                studentCount += 1
                currentSum = currentPage 
                
                if (studentCount > m ):
                    return False 
        return True             
       

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        k = int(str[0])
        n = int(str[1])
        arr = input().split()
        for itr in range(n):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.minTime(arr,n,k))
# } Driver Code Ends