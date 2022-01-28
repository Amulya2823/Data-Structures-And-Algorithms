class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        return self.buyandsell(prices,0,1,1,{})
    
    def buyandsell(self,prices,currentDay,canBuy,transactionCount,memo):
        
        if currentDay >= len (prices) or transactionCount <= 0 :
            return 0
        
        currentkey = (currentDay,canBuy,transactionCount)
        
        if currentkey in memo:
            return memo[currentkey]
        
        if canBuy == 1:
            idle = self.buyandsell(prices,currentDay + 1 ,canBuy ,transactionCount,memo)
            buy = self.buyandsell(prices,currentDay + 1 , 0 ,transactionCount,memo) - prices[currentDay]
            memo[currentkey]  = max(idle,buy)
            return memo[currentkey]
            
        else:
            idle = self.buyandsell(prices,currentDay + 1 ,canBuy ,transactionCount,memo)
            sell = self.buyandsell(prices,currentDay + 1 , 1 ,transactionCount - 1,memo) + prices[currentDay]
            memo[currentkey] =  max(idle,sell)
            return memo[currentkey]
        