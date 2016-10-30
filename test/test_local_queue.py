from asynchronousqueue.local_queue import LocalQueue
import pytest


def test_enqueue():
    """ Expect no exceptions upon enqueue
    """
    lq = LocalQueue()
    lq.enqueue(5)


def test_dequeue():
    """ Should enqueue and be able to get items on dequeue
    """
    lq = LocalQueue()
    lq.enqueue(5)
    assert lq.dequeue() == 5


def test_over_dequeue():
    """ Dequeue more items than have been enqueued should raise an exception
    """
    lq = LocalQueue()
    lq.enqueue(5)
    assert lq.dequeue() == 5
    with pytest.raises(IndexError):
        assert lq.dequeue() == 5


def test_size():
    """ Test that the size is properly reported with adding/removal of elements
    """
    lq = LocalQueue()
    lq.enqueue(4)
    assert lq.size() == 1
    lq.enqueue(3)
    assert lq.size() == 2
    lq.dequeue()
    assert lq.size() == 1
