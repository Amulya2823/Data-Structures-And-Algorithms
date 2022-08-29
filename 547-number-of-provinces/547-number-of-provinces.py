class Solution:
    def findCircleNum(self, graph: List[List[int]]) -> int:
        
        n = len(graph)
        
        answer = 0
        visited = [0]*n
        
        for currentCity in range(n):
            
            if visited[currentCity] ==  False:
                self.depthFirstSearch(graph , n , currentCity , visited)
                answer += 1
                
        return answer 
        
    def depthFirstSearch(self , graph , n , currentCity , visited):
        
        if visited[currentCity] :
            return 
        
        visited[currentCity] = True
        neighbours = graph[currentCity]
        
        for i in range(n):
            if neighbours[i] == 1:
                self.depthFirstSearch(graph , n , i , visited)
                
        return 
        