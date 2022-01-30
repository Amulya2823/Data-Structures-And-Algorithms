class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subset = []
        powerset = []
        self.subsetgenerator(0,nums,subset,powerset)
        return powerset
    
    def subsetgenerator(self,currentindex,nums,subset,powerset):
    
        if currentindex >= len(nums) :
            powerset.append(subset[:])
            return 
        
        self.subsetgenerator(currentindex+1,nums,subset,powerset)  #nottake
        
        subset.append(nums[currentindex])
        self.subsetgenerator(currentindex+1,nums,subset,powerset)   #take
        subset.pop()
        return 
    
        
    

        