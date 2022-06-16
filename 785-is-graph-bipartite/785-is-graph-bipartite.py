class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        colors = [-1]*n
        
        for currentVertex in range (n):
            
            if colors[currentVertex] != -1 :
                continue
                
            if not (self.hasEvenCycle(graph , currentVertex , 0 , colors)):
                return False
            
        return True 
    
    def hasEvenCycle(self ,graph , currentVertex , currentColor , colors):
        
        if colors[currentVertex] != -1:
            return colors[currentVertex] == currentColor
        
        colors[currentVertex] = currentColor
        
        for currentNeighbour in graph[currentVertex]:
            
            if not (self.hasEvenCycle(graph , currentNeighbour , 1-currentColor , colors)):
                return False 
            
        return True
                
                
                
        