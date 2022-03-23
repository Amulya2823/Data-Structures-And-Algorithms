class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
         return self.BuyandSell(prices , 0 ,1, k , {} )
    
    def BuyandSell (self , prices , currentDay , canBuy , transCount , memo ) :
        
        if currentDay >= len(prices) or transCount <= 0 :
            return 0
        
        currentKey = (currentDay , canBuy ,  transCount )
        
        if currentKey in memo :
            return memo[currentKey]
    
        
        if canBuy == 1 :
            
            idle = self.BuyandSell(prices , currentDay + 1 , canBuy , transCount , memo)
            buy = self.BuyandSell(prices , currentDay + 1 , 0 , transCount , memo ) - prices[currentDay]
            memo[currentKey] = max(idle , buy)
            return memo[currentKey]
        
        else :
            
            idle = self.BuyandSell(prices , currentDay + 1 , canBuy , transCount , memo)
            sell = self.BuyandSell(prices , currentDay + 1 , 1 , transCount - 1 , memo) + prices[currentDay]
            memo[currentKey] = max(idle , sell)
            return memo[currentKey]
        
        
        