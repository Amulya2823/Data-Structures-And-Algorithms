# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists :
            return 
        
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists)//2
        left = self.mergeKLists(lists[:mid]) #upto mid
        right = self.mergeKLists(lists[mid:]) #after mid
        
        return self.merge(left,right)
    
    def merge(self,l1,l2):
        
        currentNode = dummyNode = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                currentNode.next = ListNode(l1.val)
                currentNode = currentNode.next
                l1 = l1.next
                
            else:
                currentNode.next = ListNode(l2.val)
                currentNode = currentNode.next
                l2 = l2.next
                
        if l1:
            currentNode.next = l1
            
        else:
            currentNode.next = l2
            
        return dummyNode.next
        