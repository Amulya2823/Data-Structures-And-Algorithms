class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        memo ={'2' : 'abc' ,
               '3' : 'def' ,
               '4' : 'ghi' ,
               '5' : 'jkl' ,
               '6' : 'mno' ,
               '7' : 'pqrs' ,
               '8' : 'tuv' ,
               '9' : 'wxyz'}
        
        answer =[]
        
        if len(digits) == 0:
            return answer
                
        self.generateletterCombinations(digits,0,"",answer,memo)
        return answer 
    
    def generateletterCombinations(self,s,currentindex,currentstring,answer,memo):
        
        if currentindex >= len(s):
            answer.append(currentstring)
            return 
        
        currentchar = s[currentindex] 
        mappings= memo[currentchar]
        
        for i in range(len(mappings)):
            self.generateletterCombinations(s,currentindex+1,currentstring + mappings[i],answer,memo)
            
        return   
        
