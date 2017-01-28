import getchar
import os

import var
import screen
import handler

# CHANGED: introduce math functions (sqrt, cos, sin, tan)
# CHANGED: move to float
# CHANGED: allow decimal input
# CHANGED: delete particular stacks
# CHANGED: Add help
# CHANGED: Modularised
# CHANGED: support erasing
# CHANGED: support entering negative numbers (\-)
# CHANGED: add scientific notation (E?)
# CHANGED: Added colour code

# TODO: functions to add possibly: root, npr, ncr
# TODO: imaginary number support
# TODO: reorder system functions so that they are in logical order on man page
# TODO: add number history
# TODO: round function
# TODO: settings? (write in scientific notation, turn colours on/off, change command keys) do we need ncurses

screen.clear()

if os.name == 'nt':
    import win10col
    win10col.enable_VT()

while True:
    var.key = getchar._Getch()()

    if var.key in var.SYS_COMMANDS:
        var.SYS_COMMANDS[var.key]()
    # else:
    #     screen.write(var.key)
    if var.comhelp:
        screen.write_custom(var.key, 'cyan')
    elif var.key.isalpha():
        screen.write_custom(var.key, 'green')
    elif var.key in var.ADV_OPERATORS:
        screen.write_custom(var.key, 'red')
    else:
        screen.write(var.key)

    if var.key.isdigit():
        handler.num_handle()
    elif var.key in var.OPERATORS and var.comhelp: #this is needed to stop it from performing operation
         handler.character_handler(var.key)
    elif var.key.isalpha() or var.key in var.ADV_OPERATORS:
        handler.character_handler(var.key)
    elif var.key in var.OPERATORS:
        handler.operator_handler(var.key)
    elif var.key == '.':
        if var.number:
            var.number = var.number+'.'
        else:
            var.number = '.'

    if var.key != '\b':
        var.lastkey = var.key
