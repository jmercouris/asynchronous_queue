from asynchronousqueue.asynchronous_queue import AsynchronousQueue as Queue
from asynchronousqueue.task import Task
import time

parallelism = 2
task_count = 5


def function():
    time.sleep(1)
    print('Executed Function')


def callback():
    print('Received Callback')


queue = Queue(parallelism)

for i in range(0, task_count):
    queue.add_task(Task('Task {}'.format(i), function, callback))

queue.start()


while queue.is_running():
    pass


