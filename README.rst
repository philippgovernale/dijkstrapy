What is it?
----------

rpyn is a command line reverse polish notation calculator written in python. The purpose of this tool
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

Platform
--------

Currently rpyn only supports MICROSOFT WINDOWS due to a dependency of the msvcrt library. I am working on finding
an alternate library with LINUX and MAC OS support.

Known issues
------------

  - functions are not automatically called after backspacing characters
  - decimal point numbers starting with 0 not recognised

Documentation
-------------

Documentation on the use of this application is available by running the typing 'man' in the main program

For developers
-------------

Below is a list of the functions that each module contains

- stackop (stack operations) = [two_pop, operate, adv_operate_double, adv_operate_single, adv_operate_none]
- screen = [clear, draw]
- mathfuncs (additional math functions) = [cube_root]
- sysfuncs (system functions) = [clear_line, delete_stack, drop, help, newline, backspace, quit, inline_help]
- handler (input handling functions) = [num_handle, add_decimal, match_and_operate]

Bug reporting
------------

When you find a bug,

AUTHORS
-------

Philipp Governale

LICENSING
---------

Please see the LICENSE file
