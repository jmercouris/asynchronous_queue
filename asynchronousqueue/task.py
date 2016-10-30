class Task(object):
    """Documentation for Task
    
    """
    def __init__(self, identifier, function, callback):
        super(Task, self).__init__()
        self.identifier = identifier
        self.function = function
        self.callback = callback
    
    def execute(self):
        print('Executing Task: {}'.format(self.identifier))
        self.function()
        self.callback()
        self.notify_queue()
        

