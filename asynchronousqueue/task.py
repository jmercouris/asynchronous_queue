class Task(object):
    """A Task object is a convenient container for a function and an associated
    callback. It stores a couple of useful things:
    
    :ivar identifier: A string identifier that is passed to identify the task
    :ivar function: The function to be executed
    :ivar callback: The callback which will be invoked upon function execution
    
    """
    def __init__(self, identifier, function, callback, *args, **kwargs):
        super(Task, self).__init__()
        self.identifier = identifier
        self.function = function
        self.callback = callback
        self.args = args
        self.kwargs = kwargs
    
    def execute(self):
        """Execute the function passed in during the task creation, then invoke
        the callback, and finally, notify the queue of the task completion
        """
        
        print('Executing Task: {}'.format(self.identifier))
        
        '''In the event of failure, at least notify the queue that it may launch
        a new thread
        '''
        try:
            self.function(*self.args, **self.kwargs)
            self.callback()
        except Exception as e:
            print(e)
        self.notify_queue()
