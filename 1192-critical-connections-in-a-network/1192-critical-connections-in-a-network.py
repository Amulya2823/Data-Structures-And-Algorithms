class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = []
        
        for i in range(n):
            graph.append([])
            
        for a,b in connections :
            graph[a].append(b)
            graph[b].append(a)
                
        return self.criticalEdge(n , graph)
       
    def criticalEdge(self , n , graph):
        
        disTime = [-1]*n
        lowTime = [-1]*n
        time = 0
    
        answer = []
        self.tarjansAlgo(0 ,time , -1 ,graph , disTime , lowTime , answer )
        return answer 
    
    def tarjansAlgo(self , currentVertex , time , currentParent ,graph , disTime , lowTime , answer):
        
        disTime[currentVertex] = time
        lowTime[currentVertex] = time
        time += 1
        
        for currentNeigh in graph[currentVertex]:
            
            if currentNeigh == currentParent: #currentNeigh is parent and visited
                continue
                 
            if disTime[currentNeigh] != -1 :   #currentNeigh is visited but not parent
                lowTime[currentVertex] = min(lowTime[currentVertex] , disTime[currentNeigh])
                continue
                
            self.tarjansAlgo(currentNeigh , time , currentVertex ,graph , disTime , lowTime , answer) #currentNeigh is not visited
            
            #after returning
            
            lowTime[currentVertex] = min(lowTime[currentVertex],lowTime[currentNeigh])
            
            if disTime[currentVertex] < lowTime[currentNeigh]:
                answer.append([currentVertex , currentNeigh])
                
        return 
            
                
            
        
        
        
        
                
                
        
        