class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps key -> Node
        
        # Dummy boundaries
        self.left = Node(0, 0)  # LRU end
        self.right = Node(0, 0) # MRU end
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        """Unplugs a node from its current position."""
        # 1. Identify the neighbors
        prev_node = node.prev
        next_node = node.next
        
        # 2. Wire the neighbors to each other, bypassing 'node'
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        """Plugs a node in right before self.right (MRU position)."""
        # 1. Identify where we are inserting (between right's current prev, and right)
        prev_node = self.right.prev
        next_node = self.right
        
        # 2. Wire the neighbors to point inward to the new 'node'
        prev_node.next = node
        next_node.prev = node
        
        # 3. Wire the new 'node' to point outward to its new neighbors
        node.prev = prev_node
        node.next = next_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)  # Unplug from wherever it is
            self.insert(node)  # Move to the MRU spot
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If it already exists, unplug the old version
            self.remove(self.cache[key])
            
        # Create the new node, save it to dict, and plug it into MRU spot
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)
        
        # Evict the LRU if we are over capacity
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)       # Unplug from linked list
            del self.cache[lru_node.key] # Delete from hash map

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)