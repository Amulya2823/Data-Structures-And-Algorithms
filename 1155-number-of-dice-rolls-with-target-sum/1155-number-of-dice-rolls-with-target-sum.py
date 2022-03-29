class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        return self.diceRolls(n , k , target , {})
    
    def diceRolls(self , dices , faces , target , memo) :
        
        if dices == 0 and target == 0 :
            return 1
        
        if dices == 0 or target <= 0 :
            return 0
        
        currentKey = ( dices , target)
        
        if currentKey in memo :
            return memo[currentKey]
        
        answer = 0
        
        
        for i in range (1 , faces + 1) :
            tempAns = self.diceRolls(dices -1 , faces , target - i , memo)
            answer = (answer % 1000000007 + tempAns % 1000000007 ) % 1000000007 
            
            
        memo[currentKey] = answer 
        return memo[currentKey]
            
        
            
        
            
            
            
        
        