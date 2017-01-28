import sys
import os

import var

write = sys.stdout.write

class Colour():
    RESET = '\033[0m'
    RED = '\033[31m'
    BLUE = '\033[34m'
    GREEN = '\033[92m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    STRIKETHROUGH = '\033[9m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def return_custom(text, style):
    selstyle = ''
    if style == 'red':
        selstyle = Colour.RED
    elif style == 'blue':
        selstyle = Colour.BLUE
    elif style == 'yellow':
        selstyle = Colour.YELLOW
    elif style == 'magenta':
        selstyle = Colour.MAGENTA
    elif style == 'cyan':
        selstyle = Colour.CYAN
    elif style == 'green':
        selstyle = Colour.GREEN
    elif style == 'white':
        selstyle == Colour.WHITE
    elif style == 'reset':
        selstyle == Colour.RESET
    elif style == 'bold':
        selstyle == Colour.BOLD
    elif style == 'underline':
        selstyle = Colour.UNDERLINE

    return selstyle+text+Colour.RESET

def write_custom(text, style):
    chars = return_custom(text, style)
    write(chars)

def draw():
    clear()
    # hack for liux problem
    if var.key.isalpha() or var.key in var.OPERATORS:
        write('\b \b')
    for digits in var.stack:
        if var.conf_e_display:
            write("stack %s:  %e\n" %(return_custom(str(var.stack.index(digits)), var.conf_colour_digit_stack_number), digits))
        else:
            write("stack %s:  %s\n" %(return_custom(str(var.stack.index(digits)), var.conf_colour_digit_stack_number),return_custom(str(digits), var.conf_colour_digit_stack)))
