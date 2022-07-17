class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        
        n = len(nums)
        start = 0
        end = n-1
        
        pivot = -1
        
        while start <= end:
            mid = start + (end-start)//2
            
            if nums[mid] <= x:
                pivot = mid
                start = mid+1
            else:
                end = mid-1
                
        left =  0 if pivot-k<0 else pivot-k
        right = n-1 if pivot+k >= n else pivot+k
        
        while right-left+1 > k:
            
            if abs(nums[left]-x) > abs(nums[right]-x):
                left += 1
                
            else:
                right -=1 
                
        answer = []
        
        for i in range(left,right+1):
            answer.append(nums[i])
            
        return answer 
            
            
        