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

License
--------------------------------------------------------------------------------
This software is licensed under the GNU GPL V3. Which can be found 
`here <https://www.gnu.org/licenses/gpl-3.0.en.html>`_

Notes
--------------------------------------------------------------------------------
This Library is built with no external dependencies from the default python
library.

Version
--------------------------------------------------------------------------------
0.1-alpha
