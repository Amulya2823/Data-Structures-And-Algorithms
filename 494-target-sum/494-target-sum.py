class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        return self.totalWays(nums , 0 , target , {})
    
    def totalWays(self , nums , currentIndex , target, memo) :
        
        if currentIndex == len(nums) and target == 0 :
            return 1
        
        if currentIndex == len(nums) and target is not 0 :
            return 0
        
        currentKey = (currentIndex , target)
        
        if currentKey in memo :
            return memo[currentKey]
        
        
        posSign = self.totalWays(nums , currentIndex+ 1 , target - nums[currentIndex] , memo)
        negSign = self.totalWays(nums , currentIndex+ 1 , target + nums[currentIndex] , memo)
        
        memo[currentKey] = posSign + negSign
        return memo[currentKey]
        
        
        