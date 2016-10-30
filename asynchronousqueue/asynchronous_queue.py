import threading
from asynchronousqueue.local_queue import LocalQueue


class AsynchronousQueue(object):
    """Documentation for Queue
    
    """
    def __init__(self, parallelism):
        """Constructor to create an AsynchronousQueue object
        
        :param parallelism: Maximum amount of simultaneous threads permitted
        """
        
        super(AsynchronousQueue, self).__init__()
        self.local_queue = LocalQueue()
        self.parallelism = parallelism
        self.running_thread_count = 0
        self.callback = None
        self.running = False
    
    def start(self):
        """Begin the consumption of tasks added to the queue
        """
        
        self.running = True
        
        # If we can launch more threads, and we have tasks to consume, launch threads
        while(self.running_thread_count < self.parallelism and self.local_queue.size() > 0):
            self.launch_task()
    
    def size(self):
        """How many tasks in local_queue have not been launched into threads
        for execution
        
        :returns: How many tasks have yet to be launched into execution threads
        :rtype: Integer
        """
        
        return self.local_queue.size()
    
    def is_running(self):
        """Returns the running variable which signals whether the queue is still running
        
        :returns: Boolean of whether the queue have running tasks
        :rtype: Boolean
        """
        
        return self.running
    
    def in_flight(self):
        """This function returns how many running_thread_count there are, which also indicates
        exactly how many tasks are executing
        
        :returns: How many tasks are currently executing
        :rtype: Integer
        """
        
        return self.running_thread_count
    
    def add_task(self, task):
        """Add a task to the task queue
        
        :param task: The task object
        """
        
        task.notify_queue = self.task_notify
        self.local_queue.enqueue(task)
    
    def add_callback(self, callback):
        """Add a callback to be invoked upon the execution of all tasks
        
        :param callback: The function to be invoked upon all task execution
        """
        
        self.callback = callback
    
    def task_notify(self):
        """Every task upon completion notifies the queue by calling this function.
        This function therefore checks whether new tasks can be launched
        """
        
        self.running_thread_count -= 1
        
        while(self.running_thread_count < self.parallelism and self.local_queue.size() > 0):
            self.launch_task()
        
        if (self.local_queue.size() == 0):
            self.running = False
            if(self.callback is not None):
                self.callback()
    
    def launch_task(self):
        """This function creates a new thread to execute the next task from the queue
        """
        
        self.running_thread_count += 1
        
        task = self.local_queue.dequeue()
        try:
            threading.Thread(target=task.execute).start()
        except Exception as e:
            print(e)
