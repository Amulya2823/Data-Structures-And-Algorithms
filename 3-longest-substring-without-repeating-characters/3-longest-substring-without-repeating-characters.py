class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        answer = 0
        memo = {}
        
        release = 0 
        
        for acquire in range (len(s)) :
            currentChar = s[acquire]
            
            if currentChar in memo and memo[currentChar] >= release :
                release = memo[currentChar] + 1
           
                
            memo[currentChar] = acquire
            answer = max(answer , acquire - release + 1)
            
        return answer 
            
        
        