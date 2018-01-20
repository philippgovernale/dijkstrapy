What is it?
----------

dijkstrapy is a command line reverse polish notation calculator written in python. The purpose of this tool
is to simulate the experience of an rpn calculator on pc by minimising the number of keys required for input.

Features
-------

  - Full rpn experience
  - Real time input. No need to press enter unneccesarily
  - Supports a wide array of math functions that can be called with short keywords
  - Easily enter constants
  - Manage stacks with builtin commands
  - Extensible. Add your own math functions
  - Inbuilt function help
  - Inbuilt manual
  - configuration file
  - colour output

Upcoming features
-----------------

  - npr and ncr functions

Platform
--------

Tested on GNU/Linux and Microsoft Windows.

Known issues
------------

  - Unexpected results due to floating point behaviour (e.g 1.2+ 2.2 = 4.4000000004). Can be mitigated by turning on decimal option in config
  - Backspace in GNU/Linux does not work
  - Some characters from previous operation show up before printing of result in GNU\Linux

Documentation
-------------

Documentation on the use of this application is available by typing 'man' in the main program

For developers
-------------

Below is a list of the functions that each module contains

- stackop (stack operations) = [two_pop, operate, adv_operate_double, adv_operate_single, adv_operate_none]
- screen (drawing operations)= [clear, draw]
- mathfuncs (additional math functions) = [cube_root]
- sysfuncs (system functions) = [clear_line, delete_stack, drop, help, newline, backspace, quit, inline_help]
- handler (input handling functions) = [num_handle, match_and_operate, operator_handler, character_handler]

Bug reporting
------------

When you find a bug, which you are almost certain of doing, open an issue on Github.

Authors
-------

Philipp Governale

Credits
-------

Danny Yoo

Licensing
---------

Please see the LICENSE file
