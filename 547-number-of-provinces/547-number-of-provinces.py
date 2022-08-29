class Solution:
    def findCircleNum(self, graph: List[List[int]]) -> int:
        
        n = len(graph)
        
        answer = 0
        visited = [0]*n
        
        for currentCity in range(n):
            
            if visited[currentCity] ==  False:
                self.breadthFirstSearch(graph , n , currentCity , visited)
                answer += 1
                
        return answer 
        
    def breadthFirstSearch(self , graph , n , currentCity , visited):
        
        queue = []
        queue.append(currentCity)
        
        while queue :
            currentVertex = queue.pop(0)
            
            if visited[currentVertex]:
                continue
            
            visited[currentVertex] = True
            neighbours = graph[currentVertex]
            
            for i in range(n):
                  if neighbours[i] == 1:
                        queue.append(i)


       
        
        
        