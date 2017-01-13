import msvcrt

import var
import screen
import handler

# CHANGED: Add help
# TODO: exception handling (invalid input, drop func, number of operands)
# TODO: support erasing
# TODO: functions to add possibly: root,
# CHANGED: introduce math functions (sqrt, cos, sin, tan)
# CHANGED: move to float
# CHANGED: allow decimal input
# CHANGED: delete particular stacks

screen.clear()

while True:
    var.key = msvcrt.getch()

    if var.key in var.SYS_COMMANDS:
        var.SYS_COMMANDS[var.key]()
    else:
        screen.write(var.key)

    if var.key.isdigit():
        var.number = handler.num_handle()
    elif var.key in var.OPERATORS:
        handler.operator_handler(var.key)
    elif var.key.isalpha() or var.key in var.ADV_OPERATORS:
        handler.character_handler(var.key)
    elif var.key == '.':
        handler.decimal_handler()

    var.lastkey = var.key
