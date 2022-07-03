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
                
        for key , occurance in memo.items():
            
            if len(answer) < k:
                heapq.heappush(answer , [occurance , key])
                
            else:
                heapq.heappushpop(answer, [occurance , key])
                
        return [key for occurance ,key in answer]
                              
                        
        
        
        
        