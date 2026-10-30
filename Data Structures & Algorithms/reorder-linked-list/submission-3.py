# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None
        while curr: 
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        l1 = head
        l2 = prev
        while l2:

            l_next = l1.next
            r_next = l2.next
            l1.next = l2
            l2.next = l_next
            l1 = l_next
            l2 = r_next




            


