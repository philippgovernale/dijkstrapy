import math
import operator

import mathfuncs
import sysfuncs

stack = []

key = ''

#to stack indicates whether a number should go to the stack. if it is false it should not
tostack = True

number = None
keyword = None
command = False
comhelp = False
lastkey = None
helpcommand = None

SYS_COMMANDS = {'\r':sysfuncs.newline, '\b':sysfuncs.backspace, 'q':sysfuncs.quit, "'":sysfuncs.drop, ';':sysfuncs.clear_line, '?':sysfuncs.inline_help}

OPERATORS = {"+":operator.add ,'-':operator.sub,'*':operator.mul,'/':operator.div}
ADV_OPERATORS = {"pow":math.pow, 'srt':math.sqrt, 'cos':math.cos, 'sin':math.sin, "tan":math.tan, "log":math.log, "epow":math.exp, "tlog":math.log10, "!":math.factorial, "rm":sysfuncs.delete_stack, "nlog":math.log,"ra":math.radians, "deg":math.degrees, "crt":mathfuncs.cube_root, 'help':sysfuncs.help, 'man':sysfuncs.help,";":sysfuncs.clear_line}
MATHS_CONSTANTS = {"pi":math.pi, "eu":math.e}

operation_single = ["srt", "cos", "sin", "tan", "epow", "tlog", "!", "nlog", "ra", "deg", "crt"]
operation_double = ["pow", "log"]
operation_none = ["pi", "eu"]
operation_custom = ["rm", 'help', ';', "man"]
