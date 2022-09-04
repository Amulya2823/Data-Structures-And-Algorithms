class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.maxProfit(nums , 0 , memo)
    
    
    def maxProfit(self, nums ,currentHouse , memo):
        
        if currentHouse >= len(nums):
            return 0
        
        currentKey = currentHouse
        
        if currentKey in memo :
            return memo[currentKey]
        
        rob =  nums[currentHouse] + self.maxProfit(nums , currentHouse+2, memo )
        noRob = self.maxProfit(nums , currentHouse +1, memo )
        
        memo[currentKey] = max(rob , noRob)
        return memo[currentKey]
        