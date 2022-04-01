#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, infix):
        
        stack =[]
        
        precedence = {'+' : 1 ,'-' : 1,'*' : 2,'/' : 2,'^' : 3 }
        
        result = ""
        
        for i in range (len(infix)):
            currentChar = infix[i]
            
            if currentChar not in precedence :
                
                if currentChar == '(' :
                    stack.append(currentChar)
                    
                elif currentChar == ')' :
                    while stack!= [] and stack[-1] != '(' :
                        result += stack.pop()
                        
                    if stack !=[] and stack[-1] != '(' :
                        return -1
                    else :
                        stack.pop()
                    
                else :
                    result += currentChar 
                    
            else :
                
                while stack!= [] and stack[-1] != '(' and (precedence[stack[-1]] >= precedence[currentChar] ):
                    result += stack.pop()
                stack.append(currentChar)
            
        #pop all the operators from stack    
        while stack != [] :
            result += stack.pop()
            
        return result
                
                
            
            
       
        
        
        
        
        
        
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends