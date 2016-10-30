class LocalQueue(object):
    """Documentation for Queue
    
    """
    def __init__(self):
        super(LocalQueue, self).__init__()
        self.elements = []
    
    def enqueue(self, element):
        self.elements.insert(0, element)
    
    def dequeue(self):
        return self.elements.pop()
    
    def size(self):
        return len(self.elements)
