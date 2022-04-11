class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        first = self.findFirstPos(nums , target) 
        last = self.findLastPos(nums , target) 
        return [first , last]
    
    def findFirstPos(self ,nums , target) :
        
        answer = -1
        start = 0
        end = len(nums)-1
        
        while (start <= end) :
            mid = start + (end - start) // 2
            
            if nums[mid] == target :
                answer = mid 
                end = mid - 1      #for first pos u will move left
                
            elif nums[mid] > target :
                end = mid - 1
                
            else :
                start = mid + 1
                
        return answer 
        
    def findLastPos(self , nums , target):
        
        answer = -1
        start = 0
        end = len(nums)-1
        
        while (start <= end) :
            mid = start + (end - start) // 2
            
            if nums[mid] == target :
                answer = mid 
                start = mid + 1   #for last pos u will move right
                
            elif nums[mid] > target :
                end = mid - 1
                
            else :
                start = mid + 1
            
        return answer 
    
    
   
       

    
    
        