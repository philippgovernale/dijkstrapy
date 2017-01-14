import sys
import os

import var

write = sys.stdout.write

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw():
    clear()
    if var.key.isalpha() or var.key in var.OPERATORS:
        write('\b \b')
    for digits in var.stack:
        write("stack %i:  %r\n" %(var.stack.index(digits),digits))
