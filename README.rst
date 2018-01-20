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
  - Extensible. Add your own math functions (mathfuncs)
  - Inbuilt function help
  - Inbuilt manual
  - Configuration file
  - Colour output

Upcoming features:
-----------------

  - Ability to add user defined constants
  - npr function

Install & Run
-----------------

  For now simply clone and run: python dijstrapy.

  pip support is being developed

Platform
--------

Tested on GNU/Linux and Microsoft Windows.

Known issues
------------

  - Unexpected results due to floating point behaviour (e.g 1.2+ 2.2 = 4.4000000004). Can be mitigated by turning on decimal option in config.ini
  - Backspace in GNU/Linux does not work
  - Some characters from previous operation show up before printing of result in GNU\Linux

Documentation
-------------

Documentation on the use of this application is available by typing 'man' or 'help' in the main program

For developers
-------------

Below is a list of the functions that each module contains

- mathfuncs (additional math functions) = [cube_root, sci_notation, invert_sign, decimal_places, rnd, fract, ncr]
- stackop (stack operations) = [two_pop, operate, append_rogue, adv_operate_double, adv_operate_single, adv_operate_none]
- screen (drawing operations)= [clear, return_custom,  write_custom, draw]
- sysfuncs (system functions) = [clear_line, delete_stack, drop, swap, assist, newline, backspace, leave, catch_inline_help, inline_help, display_version, set_precision]
- handler (input handling functions) = [num_handle, match_and_operate, operator_handler, character_handler]
- readconfig(str2bool, check_colour, reset_colours, check_precision, load_config, read_argv)

Bug reporting && Suggestions
------------

When you find a bug, which you are almost certain of doing, please open an issue on Github.

I welcome any suggestions as I am a newbie

Authors
-------

Philipp Governale

Credits
-------

Danny Yoo

Licensing
---------

Please see the LICENSE file
