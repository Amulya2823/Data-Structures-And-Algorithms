class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        start = 1
        end = max(piles)
        
        while start <= end:
            mid = start + (end-start)//2
            
            if self.isPossible(piles , h , mid):
                end = mid-1
            else :
                start = mid+1
                
        return start
    
    def isPossible(self , piles , hours , k):
        
        hoursCount = 0
        
        for pile in piles :
            validHour = pile//k
            hoursCount += validHour 
            
            if pile % k != 0:
                hoursCount += 1
                
        return hoursCount <= hours
         
        