#User function Template for python3

class Solution:
        # Code here
        
    def findOrder(self,dict, N, K):
        graph = []
        
        for _ in range(K) :
            graph.append([])
        
        for i in range(N-1): 
            s1 , s2 = dict[i] , dict[i+1]
            minLen = min(len(s1) , len(s2))
        
            for j in range(minLen):
                if s1[j] != s2[j] :
                    graph[(ord(s1[j])-ord("a"))].append(ord(s2[j])-ord("a"))
                    break 
                
        ans = []
        inDegree = [0]*K
        
        for currentVertex in graph:
            for currentNeigh in currentVertex:
                inDegree[currentNeigh] += 1
                
        queue = []
        
        for currentVertex in range (len(inDegree)):
            if inDegree[currentVertex] == 0:
                queue.append(currentVertex)
        
        while queue :
            currentVertex = queue.pop(0)
            ans.append(currentVertex) 
            
            for currentNeigh in graph[currentVertex]:
                inDegree[currentNeigh] -= 1
                    
                if inDegree[currentNeigh] == 0:
                    queue.append(currentNeigh)
      
        answer = []
        
        for i in range(len(ans)):
            ch = chr((ord('a')+ ans[i]))
            answer.append(ch)
            
        return answer 
                
    
                
                
        
             
             
        
            
        
        
        
    
  
    
            
            
    
        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends