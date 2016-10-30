from asynchronousqueue.asynchronous_queue import AsynchronousQueue as Queue
from asynchronousqueue.task import Task
import time

parallelism = 2  # How many simultaneous threads do we permit
task_count = 5  # How many demonstration tasks should we create


def test_is_running():
    queue = Queue(parallelism)
    assert queue.is_running() == False
