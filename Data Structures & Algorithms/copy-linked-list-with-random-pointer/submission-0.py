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
        
        '''
        [[7,null],     [13,0],[11,4],      [10,2],   [1,0]]
            I             I       I          I         I
        [[7,null,null],[13,null,null],[11,null,null],[10,null,null],[1,null,null]]
        [[7,null],[13,null],[11,null],[10,null],[1,null]]
        key: the current node, but in the original list
        val: be the actual node in the copied list
        '''
        