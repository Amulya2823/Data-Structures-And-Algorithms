class DLLNode :
    
    def __init__(self,val,key):
        
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        
        self.head = DLLNode(-1 , -1)
        self.tail = DLLNode(-1 , -1)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        self.head.prev = self.tail
        self.tail.next = self.head
        
        self.size = 0
        self.capacity = capacity
        self.memo = {}
        
        

    def get(self, key: int) -> int:
        
        if key not in self.memo :
            return -1
        
        currentNode = self.memo[key]
        self.deleteNode(currentNode)
        self.addNode(currentNode)
        
        return currentNode.val
        
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.memo:
            currentNode = self.memo[key]
            self.deleteNode(currentNode)
            currentNode.val = value
            self.addNode(currentNode)
            return
            
        
        if self.size == self.capacity :
            self.deleteNodeFromFront()
            
        newNode = DLLNode (value , key)
        self.addNode(newNode)
        
        return 
    
    def addNode(self,  newNode):
        newNode.next = self.tail
        tempNode = self.tail.prev
        self.tail.prev = newNode
        newNode.prev = tempNode
        tempNode.next = newNode
        
        self.size += 1
        self.memo[newNode.key] = newNode
        
        return 
    
    def deleteNodeFromFront(self)  :
        tempNode = self.head.next 
        self.head.next = self.head.next.next
        tempNode.next.prev = self.head 
        
        tempNode.next = None
        tempNode.prev = None
        
        self.size -= 1
        del self.memo[tempNode.key]
        
        return 
    
    def deleteNode(self , currentNode):
        tempNode = currentNode.prev
        currentNode.next.prev = tempNode
        tempNode.next = currentNode.next
        
        currentNode.next = None
        currentNode.prev = None
        
        self.size -= 1
        del self.memo[currentNode.key]
        
        return 
        
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)