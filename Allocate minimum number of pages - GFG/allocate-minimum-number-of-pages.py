class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
       
       totalSum = 0
       
       for i in range (N):
           totalSum += A[i]
       
       start = 0
       end = totalSum
       
       answer = -1
       
       while (start <= end) :
           mid = start + (end - start)//2
           
           if self.isPossible( A , N , M , mid ):   #ifthecoditioniscorrect,returntrueelsereturnfalse
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

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends