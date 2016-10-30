from asynchronousqueue.task import Task
from asynchronousqueue.asynchronous_queue import AsynchronousQueue


def test_function():
    pass


def test_callback():
    pass


def test_task_creation():
    """ Test that tasks can be created
    """
    Task('Identifier', test_function, test_callback)


def test_task_execution():
    """ Test that tasks can be created and executed
    """
    aq = AsynchronousQueue(1)
    t = Task('Identifier', test_function, test_callback)
    aq.add_task(t)
    t.execute()
