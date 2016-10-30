from asynchronousqueue.local_queue import LocalQueue
import pytest


@pytest.fixture
def lq():
    return LocalQueue()


def test_enqueue(lq):
    """ Expect no exceptions upon enqueue
    """
    lq.enqueue(5)


def test_dequeue(lq):
    """ Should enqueue and be able to get items on dequeue
    """
    lq.enqueue(5)
    assert lq.dequeue() == 5


def test_over_dequeue(lq):
    """ Dequeue more items than have been enqueued should raise an exception
    """
    lq.enqueue(5)
    assert lq.dequeue() == 5
    with pytest.raises(IndexError):
        assert lq.dequeue() == 5


def test_size(lq):
    """ Test that the size is properly reported with adding/removal of elements
    """
    lq.enqueue(4)
    assert lq.size() == 1
    lq.enqueue(3)
    assert lq.size() == 2
    lq.dequeue()
    assert lq.size() == 1
