class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.BuyandSell(prices , 0 ,1, {} )
    
    def BuyandSell (self , prices , currentDay , canBuy  , memo ) :
        
        if currentDay >= len(prices)  :
            return 0
        
        currentKey = (currentDay , canBuy  )
        
        if currentKey in memo :
            return memo[currentKey]
    
        
        if canBuy == 1 :
            
            idle = self.BuyandSell(prices , currentDay + 1 , canBuy ,  memo)
            buy = self.BuyandSell(prices , currentDay + 1 , 0 , memo ) - prices[currentDay]
            memo[currentKey] = max(idle , buy)
            return memo[currentKey]
        
        else :
            
            idle = self.BuyandSell(prices , currentDay + 1 , canBuy ,memo)
            sell = self.BuyandSell(prices , currentDay + 1 , 1 , memo) + prices[currentDay]
            memo[currentKey] = max(idle , sell)
            return memo[currentKey]
        
        