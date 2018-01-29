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
recurs = False
recurscommand = None

conf_ansi = True
conf_sci_not = False
conf_decimal = True
conf_decimal_precision = 20

conf_colour_reset = False
conf_colour_digit_stack_number = 'yellow'
conf_colour_digit_stack = 'green'
conf_colour_alpha = 'green'
conf_colour_inline_help = 'cyan'

sys_commands = []

SYS_COMMANDS = {
                '\r':sysfuncs.newline,
                '\b':sysfuncs.backspace,
                'q':sysfuncs.leave,
                ';':sysfuncs.clear_line,
                '?':sysfuncs.catch_inline_help,
                '@':sysfuncs.catch_recurs
                }

OPERATORS = {
             '+':operator.add,
             '-':operator.sub,
             '*':operator.mul,
             '/':operator.div,
             }

ADV_OPERATORS = {
                 '^':math.pow,
                 'srt':math.sqrt,
                 'cos':math.cos,
                 'sin':math.sin,
                 'tan':math.tan,
                 'log':math.log,
                 'epow':math.exp,
                 'tlog':math.log10,
                 '!':math.factorial,
                 'rm':sysfuncs.delete_stack,
                 '#':sysfuncs.swap,
                 'nlog':math.log,
                 'ra':math.radians,
                 'deg':math.degrees,
                 'crt':mathfuncs.cube_root,
                 'help':sysfuncs.assist,
                 'man':sysfuncs.assist,
                 ';':sysfuncs.clear_line,
                 'E':mathfuncs.sci_notation,
                 '$':mathfuncs.invert_sign,
                 'dp':mathfuncs.decimal_places,
                 'rnd':mathfuncs.rnd,
                 'ver':sysfuncs.display_version,
                 '&':mathfuncs.fract,
                 'ncr':mathfuncs.ncr,
                 '\'':sysfuncs.drop,
                 }

MATHS_CONSTANTS = {
                   'pi':math.pi,
                   'eu':math.e
                   }

operation_single = ['srt', 'cos', 'sin', 'tan', 'epow', 'tlog', '!', 'nlog', 'ra', 'deg', 'crt', '$', '&']
operation_double = ['^', 'log', 'E', 'dp', 'rnd', 'ncr']
operation_none = ['pi', 'eu']
operation_custom = ['rm', 'help', ';', 'man', 'ver', '#', '\'']
