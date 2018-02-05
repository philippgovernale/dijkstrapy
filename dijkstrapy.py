import getchar
import os

import var
import screen
import handler
import readconfig

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

readconfig.load_config()
readconfig.read_argv()

if os.name == 'nt':
    import win10col
    win10col.enable_VT()

screen.draw()
while True:
    var.key = getchar._Getch()()

    if var.key in var.SYS_COMMANDS:
        var.SYS_COMMANDS[var.key]()

# Don't write RCs
    if var.key == '\r':
        continue
#colour
    if var.conf_ansi:
        if var.key.isalpha():
            screen.write_custom(var.key, var.conf_colour_alpha)
        elif var.key in var.ADV_OPERATORS:
		    pass
            # screen.write_custom(var.key, 'red')
        else:
            screen.write(var.key)
    else:
        screen.write(var.key)

    if var.key.isdigit():
        handler.num_handle()
    #this is needed to prevent operators being handled by operator handler during help and recurs functions
    elif var.key.isalpha() or var.key in var.ADV_OPERATORS or var.key =='?':
        handler.character_handler(var.key) #character handler does not check whether there is a number waiting to be pushed to stack
    elif var.key == '.':
        if var.number:
            var.number = var.number+'.'
        else:
            var.number = '.'

    if var.key != '\b':
        var.lastkey = var.key
