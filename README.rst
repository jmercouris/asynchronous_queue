Asynchronous Task Execution Library
================================================================================
This library is used for executing several functions in parallel. The execution
start order of the functions is guaranteed. That is, given the functions in a
list: function1, function2, function3. Function1 will start first, function2
second, function3, third, etc. What is not guaranteed is that the functions will
terminate in order, that is, there is no blocking for function start based on the
completion of a previous function.

Requirements
--------------------------------------------------------------------------------
The requirements to run this software are:

- Python 3.4+

Running the Example Code
--------------------------------------------------------------------------------
To run the example code without installing this module, simply navigate to the
project root directory (the directory that contains the README.rst). Then execute
the command `python -m example.main` to run the example as a module.

Running the Tests
--------------------------------------------------------------------------------
To run the tests without installing this module, navigate to the root project
directory and execute `python -m pytest test/`.

High Level Architecture
--------------------------------------------------------------------------------
The AsynchronousQueue class has a LocalQueue object. This object behaves like
any other first in first out queue. We add objects to the queue and consume
them in the order that we added them.

To this LocalQueue we add Task objects.
Task objects are containers that maintain a reference to the function we wish
to execute, and the callback we wish to invoke upon the function completion.

Upon starting, the AsynchronousQueue will begin consuming tasks from the LocalQueue
and launching new threads for every Task. The amount of threads that will
simultaneously be running is bound by a parameter called 'parallelism'.
This parameter will prevent the AsynchronousQueue from launching new task threads
until a thread terminates. The AsynchronousQueue will know
when a thread has terminated because it will be notified by a callback.

Upon the completion of all tasks in the LocalQueue, the AsynchronousQueue will
stop running.

Notes
--------------------------------------------------------------------------------
This Library is built with no external dependencies from the default Python
library. The name AsynchronousQueue was chosen for the library name to avoid
namespace collisions with the default Python Queue module. This module could
be further expanded by allowing for the passing of arguments to the callback
and the function to be executed.

License
--------------------------------------------------------------------------------
This software is licensed under the GNU GPL V3. Which can be found 
`here <https://www.gnu.org/licenses/gpl-3.0.en.html>`_

Version
--------------------------------------------------------------------------------
0.1-alpha
