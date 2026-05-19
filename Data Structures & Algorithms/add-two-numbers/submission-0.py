# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carrier = 0 
        
        ptr1 = l1 
        ptr2 = l2 
        dummy = ListNode(0)
        ptr3 = dummy
        while ptr1 or ptr2: 
            v1 = ptr1.val if ptr1 else 0
            v2 = ptr2.val if ptr2 else 0
            
            tot = v1 + v2 + carrier
            
            
            if tot >= 10: 
                carrier = 1
                tot = tot % 10
                ptr3.next = ListNode(tot)
                
                
            else:
                carrier = 0 
                ptr3.next = ListNode(tot)
                
            ptr3 = ptr3.next 
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
        
        if carrier == 1:
            ptr3.next = ListNode(carrier, None)
                
        return dummy.next
            
        '''
        [9,9,9,9,9,9,9]
        [1]
        
        [0,0,0,0,0,0,0,1]
        '''