class AsynchronousQueue(object):
    """Documentation for Queue
    
    """
    def __init__(self, parallelism):
        super(AsynchronousQueue, self).__init__()
        self.local_queue = LocalQueue()
        
        print('Hello World')
    
    def start(self):
        pass
    
    def size(self):
        pass
    
    def is_running(self):
        pass
    
    def in_flight(self):
        pass
    
    def add_task(self):
        pass
    
    def add_callback(self):
        pass


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




