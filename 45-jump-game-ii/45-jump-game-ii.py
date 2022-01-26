class Solution:
    def jump(self, nums: List[int]) -> int:
        
        return self.minways(0,nums,{})
    
    def minways(self,currentindex,nums,memo):
        
        if currentindex >= len(nums)-1 :
            return 0
        
        currentkey = currentindex
        
        if currentkey in memo:
            return memo[currentkey]
        
        
        
        currentjump = nums[currentindex]
        answer = 100001
        
        
        for i in range(1,currentjump+1):
            tempans = 1 + self.minways(currentindex+ i,nums,memo)
            answer = min(answer,tempans)
            
            
        memo[currentkey] = answer    
        return memo[currentkey] 
        
        
        
        
        
     
        
        
        