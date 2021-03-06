import threading
from asynchronousqueue.local_queue import LocalQueue


class AsynchronousQueue(object):
    """The AsynchronousQueue class uses a queue to keep track of tasks that it
    must complete, it launches tasks in a first in first out mode. For every
    task that the AsynchronousQueue class executes, it creates a new thread.
    Upon completion of the task, the AsynchronousQueue is notified via the
    task_notify function. This allows the AsynchronousQueue to keep track of how
    many threads (tasks) have been launched, and how many have been completed.
    This allows the AsynchronousQueue to keep limit the count of parallel
    executing threads to a predefined threshold (var parallelism).
    
    :ivar local_queue: Tasks within the queue
    :ivar parallelism: Number of asynchronous tasks executing
    :ivar running_thread_count: Number of currently executing tasks/threads
    :ivar callback: The callback invoked upon completion of all tasks
    :ivar running: Whether the queue is consuming tasks or not
    """
    
    def __init__(self, parallelism):
        """Constructor to create an AsynchronousQueue object
        
        :param parallelism: Maximum amount of simultaneous threads permitted
        """
        
        super(AsynchronousQueue, self).__init__()
        self.local_queue = LocalQueue()
        self.parallelism = parallelism
        # Check that parallelism is at least 1
        if (self.parallelism < 0):
            raise ValueError('Parallelism must 1 or greater')
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
        """Return how many tasks in local_queue have not been launched into threads
        for execution
        
        :returns: How many tasks have yet to be launched into execution threads
        :rtype: Integer
        """
        
        return self.local_queue.size()
    
    def is_running(self):
        """Return boolean signal of whether the queue is still executing/has tasks to execute
        
        :returns: Boolean of whether the queue have running tasks
        :rtype: Boolean
        """
        
        return self.running
    
    def in_flight(self):
        """Return how many running_thread_count there are, which also indicates
        exactly how many tasks are executing
        
        :returns: How many tasks are currently executing
        :rtype: Integer
        """
        
        return self.running_thread_count
    
    def add_task(self, task):
        """Add a task to the task queue
        
        :param task: The task object
        """
        
        # Add a callback to the queue to notify the queue of task completion
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
        """Create a new thread to execute the next task from the queue
        """
        
        self.running_thread_count += 1
        
        task = self.local_queue.dequeue()
        try:
            threading.Thread(target=task.execute).start()
        except Exception as e:
            print(e)
