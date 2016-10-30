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
    """Create and execute a task queue, just to make sure it completes
    """
    # Generate a set of Tasks
    task_count = 5  # How many demonstration tasks should we create
    for i in range(0, task_count):
        aq.add_task(Task('Task {}'.format(i), function, callback))
    aq.start()
    while(aq.is_running()):
        pass
    assert aq.is_running() is False


def test_aq_is_running(aq):
    """Test whether initialization value of is_running is correct
    """
    assert aq.is_running() is False


def test_aq_size(aq):
    """Test whether size properly reports size and whether items are consumed
    thereby updating the size
    """
    # Generate a set of Tasks
    task_count = 5  # How many demonstration tasks should we create
    for i in range(0, task_count):
        aq.add_task(Task('Task {}'.format(i), function, callback))
    assert aq.size() == 5
    aq.start()
    while(aq.is_running()):
        pass
    assert aq.size() == 0


""" Further Expansion could be achieved using mock, to do assertions on the
callback actually being executed. Additionally, other assertions such as
how many threads are running at any given point in time could be tested.
There are lots of expansions one could do upon the testing, particularly
being that this is a multi-threaded application
"""
