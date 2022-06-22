class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        number1,number2,count1 ,count2 = -1,-1,0,0
        
        for i in range(len(nums)):
            if nums[i] == number1:
                count1 += 1
                
            elif nums[i] == number2:
                count2 += 1
                
            elif count1 == 0:
                number1 = nums[i]
                count1 = 1
                
            elif count2 == 0:
                number2 = nums[i]
                count2 = 1
                
            else:
                count1 -= 1
                count2 -= 1
                
        answer =[]
        count1 = 0
        count2 = 0
                
        for i in range(len(nums)):
            
            if nums[i] == number1:
                count1 += 1
                
            elif nums[i] == number2:
                count2 += 1
                
        if count1 > (len(nums)/3):
            answer.append(number1)
                
        if count2 > (len(nums)/3):
            answer.append(number2)
                
        return answer 
                
            
        
        
        