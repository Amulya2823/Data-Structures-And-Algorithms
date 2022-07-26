class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    
        
        result = []
        
        if not nums or len(nums) == 0 or k > len(nums):
            return result 
        
        queue = deque([])
        
        for i in range(len(nums)):
            
            if queue and queue[0][1] <= i-k :   #remove front element if it goes out of size
                queue.popleft()
                
            while queue and queue[-1][0] < nums[i]:  #maintain the elements in descending order
                queue.pop()
                
            queue.append((nums[i] , i))  #push currentNode
            
            if i >= k-1 :                  #include maximum in teh current window
                result.append(queue[0][0])    
                
        return result 
                
         
                
                
                
            
        
        