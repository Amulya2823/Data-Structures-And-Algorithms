class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        answer = self.findAtmost(nums , k)-self.findAtmost(nums , k-1)
        return answer
    
    def findAtmost(self , nums , k) :
        
        memo = {}
        answer = 0
        distinct = 0
        release = 0

        for acquire in range (len(nums)) :
            currentChar = nums[acquire]

            if currentChar in memo :
                memo[currentChar] += 1

            else :
                memo[currentChar] = 1
                distinct += 1

            while (release <= acquire and distinct >k) :
                disChar = nums[release]

                memo[disChar] -= 1

                if memo[disChar] == 0 :
                    del memo[disChar]
                    distinct -= 1
                release += 1
                    
                
            answer +=  acquire - release + 1
                
        return answer  
        