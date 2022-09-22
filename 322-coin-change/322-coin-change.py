class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        answer = self.minCoins(coins , 0 , amount , memo)
        
        if answer == 10001:
            return -1
        return answer
    
    def minCoins (self , coins , currentIndex , amount , memo):
        
        if amount == 0 :
            return 0 
        
        if currentIndex == len(coins):
            return 10001
        
        currentKey = (currentIndex , amount)
        
        if currentKey in memo :
            return memo[currentKey]
        
        currentCoin = coins[currentIndex]
        consider = 10001
        
        if amount >= currentCoin :
            consider = 1 + self.minCoins(coins , currentIndex , amount - currentCoin , memo)
            
        notConsider = self.minCoins(coins , currentIndex+1 , amount , memo)
        
        memo[currentKey] = min(consider , notConsider)
        return memo[currentKey]
        