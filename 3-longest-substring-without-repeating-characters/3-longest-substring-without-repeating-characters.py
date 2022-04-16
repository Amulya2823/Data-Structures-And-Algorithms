class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        answer = 0
        memo = {}
        
        release = 0 
        
        for acquire in range (len(s)) :
            currentChar = s[acquire]
            
            while release < acquire and currentChar in memo :
                disChar = s[release]
                del memo[disChar]
                release += 1
                
            memo[currentChar] = 1
            answer = max(answer , acquire - release + 1)
            
        return answer 
            
        
        