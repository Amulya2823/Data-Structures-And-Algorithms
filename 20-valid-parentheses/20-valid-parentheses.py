class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        for i in range (len(s)) :
            currentChar = s[i]
            
            if (currentChar == '(' or currentChar == '[' or currentChar == '{') :
                stack.append(currentChar)
                
            else :
                
                    if not stack :
                        return False 
                    
                    elif stack[-1] == '(' and currentChar == ')'  :
                        stack.pop()
                        
                    elif stack[-1] == '[' and currentChar == ']'  :
                        stack.pop()
                        
                    elif stack[-1] == '{' and currentChar == '}'  :
                        stack.pop()
                        
                    else :
                        return False
                    
        return not stack 
                            
                
                
                
            
            
        