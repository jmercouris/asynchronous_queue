import _thread
from asynchronousqueue.local_queue import LocalQueue


class AsynchronousQueue(object):
    """Documentation for Queue
    
    """
    def __init__(self, parallelism):
        super(AsynchronousQueue, self).__init__()
        self.local_queue = LocalQueue()
        self.parallelism = parallelism
        self.running = False
    
    def start(self):
        self.running = True  # Change status to Running
        
        while(self.local_queue.size() > 0):
            self.launch_task()
        
        self.running = False  # Execution Complete
    
    def size(self):
        return self.local_queue.size()
    
    def is_running(self):
        return self.running
    
    def in_flight(self):
        pass
    
    def add_task(self, task):
        task.notify_queue = self.task_notify
        self.local_queue.enqueue(task)
    
    def add_callback(self, callback):
        self.callback = callback
    
    def task_notify(self):
        print('Queue Notified Task completed')
    
    def launch_task(self):
        print('Launch task')
        task = self.local_queue.dequeue()
        try:
            _thread.start_new_thread(task.execute, ())
        except Exception as e:
            print(e)



class Task(object):
    """Documentation for Task
    
    """
    def __init__(self, function, callback):
        super(Task, self).__init__()
        self.function = function
        self.callback = callback
    
    def execute(self):
        print('Executing Task')
        self.function()
        self.callback()
        self.notify_queue()
        

