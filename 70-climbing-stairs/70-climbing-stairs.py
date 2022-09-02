class Solution:
    def climbStairs(self, n: int) -> int:
        return self.numWays(0 , n , {} )
    
    def numWays(self , currentStair , targetStair , memo):
        
        if currentStair == targetStair:
            return 1
        
        if currentStair > targetStair:
            return 0
        
        currentKey = currentStair
        
        if currentKey in memo :
            return memo[currentKey]
        
        oneJump = self.numWays(currentStair+1 , targetStair , memo)
        twoJump = self.numWays(currentStair+2 , targetStair , memo)
        
        memo[currentKey] = oneJump + twoJump
        return memo[currentKey]
            
    
    
    
        