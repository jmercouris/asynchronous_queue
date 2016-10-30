class Task(object):
    """Documentation for Task
    
    """
    def __init__(self, function, callback):
        super(Task, self).__init__()
        self.function = function
        self.callback = callback
    
    def execute(self):
        print('Executing Task')
        self.function()
        self.callback()
        self.notify_queue()
        

