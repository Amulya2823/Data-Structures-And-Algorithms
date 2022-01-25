class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        answer = prefixsum = 0
        memo = {}
        
        memo[prefixsum]=1
        
        for i in range(len(nums)):
            
            prefixsum += nums[i]
            
            
            if prefixsum-k in memo:
                answer += memo[prefixsum-k]
            
            if prefixsum in memo:
                memo[prefixsum] += 1
                
            else :
                memo[prefixsum] = 1
            
                
        return answer
        
        
        
    
    