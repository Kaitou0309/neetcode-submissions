# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        prev = None 

        curr = head 

        while curr: 
            
            # save next node so we don't loose the list 
            temp = curr.next 

            # make next node, the last node 
            curr.next = prev 

            # make last node current node 
            prev = curr

            # update current node to be next node 
            curr = temp 


        return prev