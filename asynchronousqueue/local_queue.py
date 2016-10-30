class LocalQueue(object):
    """A simple queue implementation using a Python List
    :ivar elements: The elements within the queue
    
    """
    def __init__(self):
        super(LocalQueue, self).__init__()
        self.elements = []
    
    def enqueue(self, element):
        """Add elements to the beginning of the queue
        
        :param element: The element to be added to the queue
        """
        
        self.elements.insert(0, element)
    
    def dequeue(self):
        """Remove elements from the end of the queue
        
        :returns: The next element in the queue
        """
        
        return self.elements.pop()
    
    def size(self):
        """Return the size of the queue
        
        :returns: The size of the Queue
        :rtype: Integer
        """
        
        return len(self.elements)
