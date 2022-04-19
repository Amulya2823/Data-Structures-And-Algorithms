class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        memo = [0]*k
        
        for currentVal in arr :
            memo[currentVal % k] += 1
            
        for currentVal in range(k) :
            if currentVal == 0 :
                if ( memo[currentVal] % 2) != 0 :
                    return False
                
            elif (memo[currentVal] != memo[k - currentVal] ):
                return False 
            
        return True
                
                
            
                
            
            
               
            
        
        
        
        
        
        
        
       
        
        
        
                
        

                

        
        
     