class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        while len(stones) > 1:
            stones.sort()
            
            if stones[-1]>stones[-2]:
                stones[-1] -= stones[-2]
                stones.pop(-2)
                
            else :
                stones.pop(-1)
                stones.pop(-1)
                
        if len(stones) == 1:
            return stones[0]
        
        else :
            return 0
                
        