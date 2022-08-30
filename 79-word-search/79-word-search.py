class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        
        for currentRow in range(m):
            for currentCol in range(n):
                
                if board[currentRow][currentCol] == word[0] and self.wordSearch(board , currentRow , currentCol , 0, word ,m , n):
                    return True 
                
        return False
    
    def wordSearch(self , board , currentRow , currentCol , currentIndex , word , m , n):
        
        if currentIndex >= len(word):
            return True
        
        if currentRow < 0 or currentRow >= m or currentCol < 0 or currentCol >= n or board[currentRow][currentCol] != word[currentIndex] :
            return False 
        
        temp = board[currentRow][currentCol]
        board[currentRow][currentCol] = '.'
        
        found = self.wordSearch(board , currentRow +1, currentCol , currentIndex+1 , word , m , n) or self.wordSearch(board , currentRow -1, currentCol , currentIndex+1 , word , m , n) or self.wordSearch(board , currentRow , currentCol+1 , currentIndex +1, word , m , n)or self.wordSearch(board , currentRow , currentCol-1, currentIndex +1, word , m , n)
        
        board[currentRow][currentCol] = temp #after interating through all possible cond , change them to original
        return found
        
        
                    
        
        
        