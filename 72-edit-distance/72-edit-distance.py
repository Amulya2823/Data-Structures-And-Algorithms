class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        memo = {}
        return self.minOps(s1 , s2 , 0 , 0 ,len(s1) , len(s2) , memo)
    
    def minOps(self , s1 , s2 , i , j , m , n , memo):
        
        if j >= n :  #if it got exhausted
            return m-i
        
        if i >= m:
            return n-j
        
        currentKey = (i , j)
        
        if currentKey in memo:
            return memo[currentKey]
        
        answer = 10000000
        
        if s1[i] == s2[j]:
            answer = self.minOps(s1 , s2 , i+1 , j+1 , m , n , memo)
            
        else :
            insert = 1+ self.minOps(s1 , s2 , i , j+1 , m , n , memo) 
            delete = 1+self.minOps(s1 , s2 , i+1 , j , m , n , memo)
            replace = 1+ self.minOps(s1 , s2 , i+1 , j+1 , m , n,memo)
            
            answer = min(insert , min(delete , replace))
        
        memo[currentKey] = answer 
        return memo[currentKey]
        