class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        memo = {}
        
        maxNum = 0
        for i in nums:
            if i > maxNum:
                maxNum = i
                
        frequency = [0]*(maxNum+1)
        
        for i in nums:
            frequency[i] += 1
      
        return self.maxPoints(frequency , nums , 0 , memo)
    
    def maxPoints(self , frequency , nums , currentIndex , memo):
        
        if currentIndex >= len(frequency):
            return 0 
        
        currentKey = currentIndex
        
        if currentKey in memo :
            return memo[currentIndex]
        
        consider = (currentIndex*frequency[currentIndex]) + self.maxPoints(frequency , nums , currentIndex+2 , memo)
        notConsider = self.maxPoints(frequency , nums , currentIndex+1 , memo)
        
        memo[currentKey] = max(consider , notConsider)
        return memo[currentKey]
            
        
        
        
        
        
        
        