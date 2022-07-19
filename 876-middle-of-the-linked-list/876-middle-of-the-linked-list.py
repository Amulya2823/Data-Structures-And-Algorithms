# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        
        fastPtr = head
        slowPtr = head
        
        while fastPtr.next != None and fastPtr.next.next != None :
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
            
        if fastPtr.next != None:
            return slowPtr.next
        
        return slowPtr