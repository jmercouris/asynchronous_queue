class AsynchronousQueue(object):
    """Documentation for Queue
    
    """
    def __init__(self, parallelism):
        super(AsynchronousQueue, self).__init__()
        self.local_queue = LocalQueue()
        self.parallelism = parallelism
    
    def start(self):
        while(self.local_queue.size() > 0):
            self.local_queue.dequeue().execute()
    
    def size(self):
        return self.local_queue.size()
    
    def is_running(self):
        pass
    
    def in_flight(self):
        pass
    
    def add_task(self, task):
        self.local_queue.enqueue(task)
    
    def add_callback(self, callback):
        self.callback = callback


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


class Task(object):
    """Documentation for Task
    
    """
    def __init__(self, function, callback):
        super(Task, self).__init__()
        self.function = function
        self.callback = callback
    
    def execute(self):
        self.function()
        self.callback()
