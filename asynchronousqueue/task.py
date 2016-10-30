class Task(object):
    """A Task object is a convenient container for a function and an associated
    callback. It stores a couple of useful things:
    
    :ivar identifier: A string identifier that is passed to identify the task
    :ivar function: The function to be executed
    :ivar callback: The callback which will be invoked upon function execution
    
    """
    def __init__(self, identifier, function, callback):
        super(Task, self).__init__()
        self.identifier = identifier
        self.function = function
        self.callback = callback
    
    def execute(self):
        """Execute the function passed in during the task creation, then invoke
        the callback, and finally, notify the queue of the task completion
        """
        
        print('Executing Task: {}'.format(self.identifier))
        self.function()
        self.callback()
        self.notify_queue()
        

