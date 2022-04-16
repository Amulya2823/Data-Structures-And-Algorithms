#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        memo = {}
        answer = -1
        distinct = 0
        release = 0

        for acquire in range (len(s)) :
            currentChar = s[acquire]

            if currentChar in memo :
                memo[currentChar] += 1

            else :
                memo[currentChar] = 1
                distinct += 1

            while (release <= acquire and distinct >k) :
                disChar = s[release]
                release += 1

                memo[disChar] -= 1

                if memo[disChar] == 0 :
                    del memo[disChar]
                    distinct -= 1
                    
            if distinct == k:
                answer = max(answer , acquire - release + 1)
                
        return answer  

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends