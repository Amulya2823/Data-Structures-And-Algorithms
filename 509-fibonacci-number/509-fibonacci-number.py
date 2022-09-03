class Solution:
    def fib(self, n: int) -> int:
        return self.nthFib(n , {})
    
    def nthFib(self , n , memo):
        
        if n == 0 :
            return 0
        
        if n == 1:
            return 1
        
        currentKey = n
        
        if currentKey in memo:
            return memo[currentKey]
        
        a = self.nthFib(n-1 , memo)
        b = self.nthFib(n-2 , memo)
        
        memo[currentKey] = a+b
        return memo[currentKey]
        