class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        matrix =  [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            matrix[i][i] = 0
            
        for currentEdge in edges :
            source = currentEdge[0]
            dest = currentEdge[1]
            cost = currentEdge[2]
            matrix[source][dest] = cost
            matrix[dest][source] = cost
            
        for intermediary in range(n):
            for source in range(n):
                for dest in range(n):
                    
                    if matrix[source][intermediary] != float('inf') and matrix[intermediary][dest] != float('inf') and matrix[source][intermediary]+matrix[intermediary][dest] < matrix[source][dest]  :
                        
                        matrix[source][dest] = matrix[source][intermediary]+matrix[intermediary][dest]
        
        cityCount = 101
        answer = -1
        for currentCity in range(n):
            count = 0
            for currentCityNeigh in range(n):
                
                if currentCity != currentCityNeigh and matrix[currentCity][currentCityNeigh] <= distanceThreshold:
                    count += 1
                    
            if count <= cityCount :
                answer = currentCity
                cityCount = count
            
        return answer 
            
                        
                    
                    
        