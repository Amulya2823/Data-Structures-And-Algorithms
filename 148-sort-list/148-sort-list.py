# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        fastPtr = head
        slowPtr = head
        
        while fastPtr.next != None and fastPtr.next.next != None:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next
            
        rightHalf = slowPtr.next
        slowPtr.next = None
        
        leftHalf = head
        
        LeftList = self.sortList(leftHalf)
        RightList = self.sortList(rightHalf)
        
        return self.mergeTwoLists(LeftList , RightList)
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode(-1)
        result = dummyNode
        
        p1 = list1
        p2 = list2
        
        while p1 is not None and p2 is not None:
            
            if p1.val < p2.val:
                newNode = ListNode(p1.val)
                result.next = newNode
                result = result.next
                p1 = p1.next
                
            else:
                newNode = ListNode(p2.val)
                result.next = newNode
                result = result.next
                p2 = p2.next
                
        if p1 is not None:
            result.next = p1
            
        if p2 is not None:
            result.next = p2
        
        return dummyNode.next
                
        
        
    
     