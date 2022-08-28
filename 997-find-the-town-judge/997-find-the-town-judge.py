class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        inDegree = [0]*(n+1)
        outDegree = [0]*(n+1)
        
        for currentTrust in trust :
            
            a = currentTrust[0]
            b = currentTrust[1]
            
            inDegree[b] += 1
            outDegree[a] += 1
            
        for currentPeople in range(1,n+1):
            
            if inDegree[currentPeople] == n-1 and outDegree[currentPeople] == 0:
                return currentPeople
            
        return -1
            
        