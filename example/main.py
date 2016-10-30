from asynchronousqueue.asynchronous_queue import AsynchronousQueue as Queue
from asynchronousqueue.task import Task
import time

parallelism = 2  # How many simultaneous threads do we permit
task_count = 5  # How many demonstration tasks should we create


def function():
    """ Sample Function to be executed as a Task
    """
    
    time.sleep(1)
    print('Executed Function')


def callback():
    """ Sample Function to be executed as a callback
    """
    print('Received Callback')

# Create our AsynchronousQueue
queue = Queue(parallelism)

# Generate a set of Tasks
for i in range(0, task_count):
    queue.add_task(Task('Task {}'.format(i), function, callback))

# Start executing the Tasks
queue.start()

# Wait until all tasks have been Executed
while queue.is_running():
    pass


