from asynchronousqueue import AsynchronousQueue as Queue
from asynchronousqueue import Task


def function():
    print('Executed Function')


def callback():
    print('Received Callback')

queue = Queue(1)
task = Task(function, callback)

queue.add_task(task)
queue.start()


