class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}
        return self.totalWays(coins , 0 , amount , memo)
    
    def totalWays (self , coins , currentIndex , amount , memo):
        
        if amount == 0 :
            return 1
        
        if currentIndex >= len(coins):
            return 0 
        
        currentKey = (currentIndex , amount)
        
        if currentKey in memo :
            return memo[currentKey]
        
        currentCoin = coins[currentIndex]
        
        consider = 0 
        
        if currentCoin <= amount :
            consider = self.totalWays(coins , currentIndex , amount - currentCoin , memo)
            
        notConsider = self.totalWays(coins , currentIndex+1 , amount , memo)
        
        memo[currentKey] = consider + notConsider
        return memo[currentKey]
        
        
        