# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return None
        
        runner = head
        
        dummyNode = ListNode(-1)
        dummyNode.next = head
        
        for i in range(n-1):
            runner = runner.next
        
        follower = dummyNode
        
        while runner.next != None:
            runner = runner.next
            follower = follower.next
            
        follower.next = follower.next.next
        return dummyNode.next
        
        
        
            
        
        
        