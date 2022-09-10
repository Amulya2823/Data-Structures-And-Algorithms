class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = collections.defaultdict(list)
        visited = set()
        
        for node,neigh,cost in times :
            edges[node].append((neigh,cost))
            
        priorityQueue = []
        answer = 0
        
        heapq.heappush(priorityQueue,(0 , k))
        
        while priorityQueue :
            currentCost , currentVertex = heapq.heappop(priorityQueue)
            
            if currentVertex in visited:
                continue
                
            visited.add(currentVertex) 
            answer = max(answer , currentCost)
            
            for currentNeigh , currentEdgeCost in edges[currentVertex] :
                if currentNeigh in visited :
                    continue
                    
                heapq.heappush(priorityQueue , (currentCost+currentEdgeCost , currentNeigh))
                
        return answer if len(visited) == n else -1
                
                
                
                
                
            
            
            
        