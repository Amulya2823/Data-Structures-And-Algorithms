class Solution:
    def mySqrt(self, x: int) -> int:
        
        start = 0
        end = x
        
        answer = -1
        
        while start<= end:
            mid = start + (end-start)//2
            temp = mid*mid
            
            if temp == x:
                return mid
            
            if temp > x:
                end = mid-1
                
            else:
                answer = mid
                start = mid+1
                
                
        return answer 
                    
            
            
        