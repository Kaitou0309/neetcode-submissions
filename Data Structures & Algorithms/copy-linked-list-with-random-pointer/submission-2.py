"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        hash_map = {}

        ptr1 = head

        while ptr1: 
            hash_map[ptr1] = Node(ptr1.val)
            ptr1 = ptr1.next
        
        ptr1 = head 

        while ptr1: 
            copy = hash_map[ptr1]
            copy.next = hash_map.get(ptr1.next)
            copy.random = hash_map.get(ptr1.random)
            ptr1 = ptr1.next

        return hash_map.get(head)