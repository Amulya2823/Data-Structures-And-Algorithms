class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = start + (end-start)//2
            
            if nums[mid] == target :
                return True
            
            while start < mid and nums[start] == nums[mid]: #checking duplicates
                start += 1
            
            
            if (nums[start] <= nums[mid]):
                
                #sorted array lies in the left,then move left otherwise move right
                if nums[start] <= target and nums[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
                    
            else:
                #sorted array lies in the right,then move right otherwise move left
                if nums[mid] < target and nums[end] >= target:
                    start = mid+1
                else:
                    end = mid-1
                    
        return False
                
                
                
                 
        
        
        