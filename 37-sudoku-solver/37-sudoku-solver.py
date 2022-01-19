class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.SudokuSolver(board,0,0)
        return 
    
    def SudokuSolver(self,board,currentrow,currentcol):
        
        if currentrow == 9:
            return True
        
        if currentcol == 8:
            nextrowpos = currentrow+1
            nextcolpos = 0
            
        else:
            nextrowpos = currentrow
            nextcolpos = currentcol+1
            
        if board[currentrow][currentcol]!='.' :
            return self.SudokuSolver(board,nextrowpos,nextcolpos)
        
        for currentval in range(1 , 10):
            
            if self.isValidCell(board,currentrow,currentcol,currentval):
                board[currentrow][currentcol] = str(currentval)
                
                if self.SudokuSolver(board,nextrowpos,nextcolpos) is True:
                    return True
                    
                board[currentrow][currentcol] = '.'
            
        return False
    
    
    def isValidCell(self,board,currentrow,currentcol,currentval):
        return self.isValidRow(board,currentrow,currentval) and self.isValidCol(board,currentcol,currentval) and self.isValidSubgrid(board,currentrow,currentcol,currentval)
    
    def isValidRow(self,board,currentrow,currentval):
        
        for currentcol in range(9):
            
            if board[currentrow][currentcol] == str(currentval):
                return False
            
        return True
    
    def isValidCol(self,board,currentcol,currentval):
        
        for currentrow in range(9):
            
            if board[currentrow][currentcol] == str(currentval):
                return False
            
        return True
    
    def isValidSubgrid(self,board,currentrow,currentcol,currentval):
        x = 3 * (currentrow//3)
        y = 3 * (currentcol//3)
        
        for i in range(3):
            for j in range(3):
                
                
                if board[x+i][y+j] == str(currentval):
                    return False
                
        return True
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    