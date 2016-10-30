from asynchronousqueue.asynchronous_queue import AsynchronousQueue as Queue
from asynchronousqueue.task import Task
import pytest


def function():
    """ Sample Function to be executed as a Task
    """
    pass


def callback():
    """ Sample Function to be executed as a callback
    """
    pass


@pytest.fixture
def aq():
    parallelism = 4  # How many simultaneous threads do we permit
    queue = Queue(parallelism)
    return queue


def test_aq_terminates(aq):
    # Generate a set of Tasks
    task_count = 5  # How many demonstration tasks should we create
    for i in range(0, task_count):
        aq.add_task(Task('Task {}'.format(i), function, callback))
    aq.start()



