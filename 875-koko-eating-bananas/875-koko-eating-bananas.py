class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        start = 1
        end = max(piles)
        
        result = end
        
        while start <= end:
            mid = start + (end-start)//2
            
            hours = 0
            
            for pile in piles:
                hours += math.ceil(pile/mid)
                
            if hours <= h :
                result = min(result , mid )
                end = mid-1
                
            else:
                start = mid+1
        
        return result
        