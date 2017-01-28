import getchar

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

# TODO: invalid math input
# TODO: functions to add possibly: root, npr, ncr
# TODO: imaginary number support
# TODO: bugs to fix: function not recognised when backspace characters, float input enter breaks
# TODO: reorder system functions so that they are in logical order on man page
# TODO: introduce colour coding
# TODO: add number history
# TODO: round function
# TODO: settings? (write in scientific notation, turn colours on/off, change command keys) do we need ncurses

screen.clear()

readconfig.load_config()

while True:
    var.key = getchar._Getch()()

    if var.key in var.SYS_COMMANDS:
        var.SYS_COMMANDS[var.key]()
    else:
        screen.write(var.key)

    if var.key.isdigit():
        handler.num_handle()
    elif var.key in var.OPERATORS and var.comhelp:
        handler.character_handler(var.key)
    elif var.key in var.OPERATORS:
        handler.operator_handler(var.key)
    elif var.key.isalpha() or var.key in var.ADV_OPERATORS or var.key in var.OPERATORS:
        handler.character_handler(var.key)
    elif var.key == '.':
        if var.number:
            var.number = var.number+'.'
        else:
            var.number = '.'

    if var.key != '\b':
        var.lastkey = var.key
