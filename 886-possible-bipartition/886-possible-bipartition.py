class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        colors = [-1]*(n+1)
        graph = []
        
        for i in range(n+1):
            graph.append([])
            
        for a , b in dislikes :
            graph[a].append(b)
            graph[b].append(a)
        
        
        for currentVertex in range(n+1):
            
            if colors[currentVertex] == 0 or colors[currentVertex] != -1 :
                continue
                
            if not self.hasEvenCycle(graph , currentVertex , 0 , colors):
                return False
            
        return True
        
            
    def hasEvenCycle(self , graph , currentVertex , currentColor , colors):
        
        if colors[currentVertex] != -1 :
            return colors[currentVertex] == currentColor
        
        colors[currentVertex] = currentColor 
        
        for currentNeigh in graph[currentVertex] :
            
            if not self.hasEvenCycle( graph , currentNeigh , 1-currentColor , colors):
                return False
            
        return True
            
        
        