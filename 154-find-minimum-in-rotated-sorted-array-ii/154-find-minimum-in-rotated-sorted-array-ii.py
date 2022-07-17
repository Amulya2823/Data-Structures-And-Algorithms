class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums)-1 
        
        while start < end :
            mid = start + (end-start)//2
            
            #right part is unsorted 
            if nums[mid] > nums[end]:
                start = mid +1 
            
            #left part is unsorted
            elif nums[mid] < nums[end]:
                end = mid 
            
            #when you have mid == end
            else:
                end -= 1
                
        return nums[start]
                
                
                
        