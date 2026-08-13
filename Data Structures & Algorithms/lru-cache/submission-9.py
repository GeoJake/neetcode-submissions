class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.front = Node() # MRU
        self.back = Node() # LRU

        self.front.prev = self.back
        self.back.next = self.front

        self.capacity = capacity
        self.cache = {} # map key to Node
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.front.prev, self.front
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            curr = self.cache[key]
            self.remove(curr)
            self.insert(curr)
            return curr.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lruNode = self.back.next
            self.remove(lruNode)
            del(self.cache[lruNode.key])

            
            

        
