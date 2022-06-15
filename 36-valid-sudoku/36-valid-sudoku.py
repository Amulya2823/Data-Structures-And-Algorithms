class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for currentrow in range(9)]
        cols = [set() for currentrow in range(9)]
        boxes = [set() for currentRow in range(9)]
        
        
        for currentRow in range (9):
            for currentCol in range (9):

                currentValue = board[currentRow][currentCol]
            
                if currentValue != '.':
                    
                    if currentValue in rows[currentRow] or currentValue in cols[currentCol] :
                        return False
                    
                    rows[currentRow].add(currentValue)
                    cols[currentCol].add(currentValue)
                    
                    
                    index = (currentRow//3)*3+(currentCol//3)
                    if currentValue in boxes[index] :
                        return False
                    
                    boxes[index].add(currentValue)
                    
        return True
                 
                       
                    
                    
                   
                    
                   
                
        