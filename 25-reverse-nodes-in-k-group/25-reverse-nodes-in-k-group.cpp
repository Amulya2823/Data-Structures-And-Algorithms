/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseLL(ListNode* head)
    {
        ListNode *previous = NULL;
        ListNode *current = head;
        while (current!=NULL)
        {
            ListNode * temp = current->next;
            current->next = previous;
            previous = current;
            current = temp;
        }
        return previous;
    }
    ListNode* reverseLLinKGroup(ListNode* head, int k)
    {
        ListNode* current = head;
        int currentlength = 1;
    
        if(head == NULL) 
            return head;
      while(current->next!=NULL and currentlength<k)
      {
          current=current->next;
          currentlength+=1;
      }
        
      if(currentlength<k)
         return head;
        
      ListNode * tempnode = current->next;
      current->next = NULL;
       /*reverse LL */
        
       ListNode * templist = reverseLLinKGroup(tempnode,k);
       ListNode * previous = reverseLL(head);
        
        head->next = templist;
           return previous;
    }
    
    ListNode* reverseKGroup(ListNode* head, int k) {
        return reverseLLinKGroup(head,k);
    }
};