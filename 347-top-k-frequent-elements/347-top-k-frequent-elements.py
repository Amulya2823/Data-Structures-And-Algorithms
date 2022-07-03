import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        answer = []
        memo = {}
        
        for i in nums :
            if i not in memo:
                memo[i] = 1
            else:
                memo[i] += 1
                
        for key , value in memo.items():
            
            if len(answer) < k:
                heapq.heappush(answer , [value , key])
                
            else:
                heapq.heappushpop(answer , [value,key])
                
        return [key for value,key in answer]
                              
                        
        
        
        
        