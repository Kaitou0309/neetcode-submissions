# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # base case, if list is empty return none
        if len(lists) == 0:
            return None

        # start from index 1, iterate through each list
        # iteration 1: we get, [List0, Merged(0,1), List2, List3, ...
        # iteration 2: we get, [List0, Merged(0,1), Merged(0,1,2), List3, ...]
        # iteration 3: we get, [List0, Merged(0,1), Merged(0,1,2), Merged(0,1,2,3), ...]
        # iteartion n: we get, [List0, Merged(0,1), Merged(0,1,2), Merged(0,1,2,3), ...,    Merged(1, ..., n)]
        for i in range(1, len(lists)):
            lists[i] = self.mergeList(lists[i - 1], lists[i])

        return lists[-1]

    # merge 2 list into 1 in ascending order
    # returns head of the merged list
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next