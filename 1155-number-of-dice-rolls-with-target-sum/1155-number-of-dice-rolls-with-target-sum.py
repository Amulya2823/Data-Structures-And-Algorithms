class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        return self.totalways(n,k,target,{})
    
    def totalways(self,dices,faces,target,memo):
        
        if dices == 0 and target!= 0 :
            return 0
        
        if dices == 0 and target == 0:
            return 1
        
        currentkey = (dices,target)
        
        if currentkey in memo:
            return memo[currentkey]
        
        answer = 0
        
        for i in range(1,faces + 1):
            tempans = self.totalways(dices - 1,faces, target - i,memo)
            answer = (answer % 1000000007 + tempans % 1000000007) % 1000000007
            
        memo[currentkey] = answer
        return memo[currentkey]
            
        
        
        
     
    
    
        