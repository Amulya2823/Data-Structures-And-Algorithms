from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #creating a graph
        n = len(points)
        
        graph = defaultdict(list)
        
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1 , n):
                x2,y2 = points[j]
                dist = abs(x2-x1) + abs(y2-y1)
                graph[i].append([dist,j])
                graph[j].append([dist,i]) 
    
        #prims algorithm 
        
        minCost = 0 
        visited = set()
        
        minHeap = [[0,0]]
        
        while len(visited) < len(points) :
            currentCost , currentVertex = heapq.heappop(minHeap)
            
            if currentVertex in visited:
                continue
            
            minCost += currentCost
            visited.add(currentVertex)
            
            for currentNeighcost , currentNeigh in graph[currentVertex]:
                if currentNeigh not in visited:
                    heapq.heappush(minHeap, [currentNeighcost , currentNeigh])
                
        return minCost
        
        
    
                
                
        
                
                
                
                
                
        