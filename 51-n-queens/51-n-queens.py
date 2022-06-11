class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        answer = []
        board = [["." for i in range (n)]for j in range (n)]

        for i in range (n):
            for j in range (n):
                board[i][j] = '.'
                 
                
        self.nQueens(board , 0 , n , answer)
        return answer
    
    def nQueens(self , board , currentRow , n , answer):
        
        if currentRow == n:        #if you have reached end, u have an answer 
            answer.append(self.constructAnswer(board,n))      
            return 
        
        for currentCol in range (n):
            
            if(self.isValid(board , currentRow , currentCol , n)): #where can you place the queen
                board[currentRow][currentCol] = "Q"
                self.nQueens(board , currentRow + 1 , n , answer)
                board[currentRow][currentCol] = "."            #undo the change
                 
        return 
    
    def constructAnswer(self , board , n):
        
        current = [] 
        
        for i in range (n):          #iterate over row
            currentString = ""
            for j in range (n):         #add as ..Q. 
                currentString += board[i][j]
                
            current.append(currentString)   #add the 4 lines of board
            
        return current
    
    def isValid(self, board , currentRow , currentCol , n):
        return self.isRowValid(board , currentRow , n) and self.isColValid(board , currentCol , n) and self.isDiagonalValid(board , currentRow , currentCol ,n)
    
    
    def isRowValid(self , board ,currentRow , n):
        
        for currentCol in range (n):  #u have to check rows so iterate over columns
            if board[currentRow][currentCol] == "Q":
                return False
            
        return True
    
    def isColValid(self , board , currentCol,n):
        
        for currentRow in range(n):
            if board[currentRow][currentCol] == "Q":
                return False
            
        return True
    
    def isDiagonalValid(self , board , currentRow , currentCol , n):
        
        x = currentRow
        y = currentCol
        
        while x >= 0 and y >= 0:
            
            if board[x][y] == "Q":
                return False
            
            x -= 1
            y -= 1
            
            
        x = currentRow
        y = currentCol
        
        while x >= 0 and y < n:
            
            if board[x][y] == "Q":
                return False
            
            x -= 1
            y += 1
            
        return True
            
      
            
        
            
    
                
    
        
        
            
            
         
            
        
    
    
        
        
        
        
                
                
        