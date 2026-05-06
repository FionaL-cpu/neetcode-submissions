class Node:
    def __init__(self, key ,val):
        self.key = key
        self.val = val
        self.pre, self.next = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key: node
        
        self.least, self.most = Node(0,0), Node(0,0)
        self.least.next = self.most
        self.most.pre = self.least 

    def remove(self, node):
        preNode = node.pre
        nextNode = node.next
        preNode.next = nextNode 
        nextNode.pre = preNode 


    def insert(self, node):
        preNode, nextNode  = self.most.pre, self.most 
        preNode.next = nextNode.pre = node
        node.next, node.pre = nextNode, preNode
    

    def get(self, key: int) -> int:
        if key in self.cache:
            # least --- most- least
            self.remove(self.cache[key])
            self.insert(self.cache[key]) # add to the most recent used position 
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            # update value 
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #compare cap:
        if len(self.cache)> self.capacity:
            #remove from the list and delete the lru from hashmap
            lru = self.least.next
            self.remove(lru)
            del self.cache[lru.key]

