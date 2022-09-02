class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:\
        
        graph = self.constructGraph(numCourses ,prerequisites)
        inDegree = [0]*numCourses
        
        for currentCourse in range(numCourses):
            for currentNeigh in graph[currentCourse]:
                inDegree[currentNeigh] += 1
                
        queue = []
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
                
        visited = [0]*numCourses
        order = []
        
        while queue :
            currentCourse = queue.pop(0)
            
            if visited[currentCourse]:
                continue 
                
            visited[currentCourse] = True 
            order.append(currentCourse)
            
            for currentNeigh in graph[currentCourse]:
                inDegree[currentNeigh] -= 1
                
                if inDegree[currentNeigh] == 0:
                    queue.append(currentNeigh)
                    
        return len(order) == numCourses
                    
    def constructGraph(Self , n , edges):
        graph = []
        
        for i in range(n):
            graph.append([])
            
        for currentEdges in edges :
            a = currentEdges[0]
            b = currentEdges[1]
                
            graph[b].append(a)
                
        return graph
        
        
        