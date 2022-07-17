class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = start + (end-start)//2
            
            if nums[mid] == target :
                return True
            
            while start < mid and nums[start] == nums[mid]:
                start += 1
                
            if (nums[start] <= nums[mid]):
                
                if nums[start] <= target and nums[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
                    
            else:
                
                if nums[mid] < target and nums[end] >= target:
                    start = mid+1
                else:
                    end = mid-1
                    
        return False
                
                
                
                 
        
        
        