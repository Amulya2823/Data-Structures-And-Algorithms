class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        answer = 1
        dp = [1]* n 
        
        for i in range ( 1 , n) :
            for j in range (i):
                
                if nums[i] > nums[j] :
                    dp[i] = max(dp[i] , 1 + dp[j])
                    
            answer = max(answer , dp[i])   
            
            
        return answer     
        
         
     