# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode(-1)
        dummyNode.next = head 
        prev = dummyNode 
        
        
        while head is not None :
            
            if head.next is not None and head.val == head.next.val  :
                
                while head.next is not None and head.val == head.next.val :
                    head = head.next 
                prev.next = head.next 
            
            else :
                 prev = prev.next    
            head = head.next
            
        return dummyNode.next     
                    
                    
        