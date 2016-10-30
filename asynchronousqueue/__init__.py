import threading
from asynchronousqueue.local_queue import LocalQueue


class AsynchronousQueue(object):
    """Documentation for Queue
    
    """
    def __init__(self, parallelism):
        super(AsynchronousQueue, self).__init__()
        self.local_queue = LocalQueue()
        self.parallelism = parallelism
        self.running_thread_count = 0
        self.callback = None
        self.running = False
    
    def start(self):
        self.running = True  # Change status to Running
        
        while(self.running_thread_count < self.parallelism and self.local_queue.size() > 0):
            self.launch_task()
    
    def size(self):
        return self.local_queue.size()
    
    def is_running(self):
        return self.running
    
    def in_flight(self):
        return self.running_thread_count
    
    def add_task(self, task):
        task.notify_queue = self.task_notify
        self.local_queue.enqueue(task)
    
    def add_callback(self, callback):
        self.callback = callback
    
    def task_notify(self):
        self.running_thread_count -= 1
        
        while(self.running_thread_count < self.parallelism and self.local_queue.size() > 0):
            self.launch_task()
        
        if (self.local_queue.size() == 0):
            self.running = False
            if(self.callback is not None):
                self.callback()
    
    def launch_task(self):
        self.running_thread_count += 1
        task = self.local_queue.dequeue()
        try:
            threading.Thread(target=task.execute).start()
        except Exception as e:
            print(e)
