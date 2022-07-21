# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None: #nodes can be 0
            return None
        
        fastPtr = head
        slowPtr = head
        
        while fastPtr.next != None and fastPtr.next.next != None :
            
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
            
            if fastPtr == slowPtr :
                return True
            
        return False
            
        
        
        
        
        