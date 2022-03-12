class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1] * n # length of LIS with nums[i]
        
        
        answer = 1
        for i in range(1, n):
            for j in range(i):
                
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            answer = max(answer , dp[i])
        return answer 