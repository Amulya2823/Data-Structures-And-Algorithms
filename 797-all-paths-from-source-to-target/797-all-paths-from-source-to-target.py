class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        answer = []
        n = len(graph)
        visited = [False]*n
        
        self.sourceToTarget(graph , 0 , visited , n , [] ,answer)
        return answer 
    
    def sourceToTarget(self,graph , currentNode , visited , n , currentPath , answer ):
        
        if currentNode == n-1 :
            currentPath.append(currentNode)
            answer.append(currentPath[:])
            currentPath.pop()
            return 
        
        
        if visited[currentNode] == True :
            return 
        
        visited[currentNode] = True
        currentPath.append(currentNode)
        
            
        for neighbour in graph[currentNode] :
            self.sourceToTarget(graph , neighbour , visited , n , currentPath , answer)
            
       
        visited[currentNode] = False 
        currentPath.pop() 
        return 
        
            
            
            
                
                
                
                
                
                
            
            
            
            
            
            
            
            
    
    
        
        
        
