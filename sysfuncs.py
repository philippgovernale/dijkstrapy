import var
import screen
import handler

import sys
import time

def clear_line(): # ; command
    var.number = None
    var.command = None
    screen.clear()

def delete_stack(): #rm command
    '''remove stack member x'''
    if var.number is not None:
        var.stack.append(var.number)
    try:
        a = var.stack.pop()
        del var.stack[a]
    except:
        screen.write("\nStack %r does not exist. Cannot remove"%(a))
        raw_input("Press enter to continue...")
    finally:
        screen.draw()

def drop():
    try:
        var.stack.pop()
    except:
        screen.write("\nCannot remove stack")
    finally:
        screen.draw()

def help():
    '''show help manual'''
    screen.clear()
    screen.write('''rPyn Documentation\n
        rPyn is a calculator
        Simple operations:\n
        \t+\t| adds numbers {2}\n
        \t-\t| subtracts numbers {2}\n
        \t*\t| multiplies numbers {2}\n
        \t/\t| divides number {2}\n
        Math functions:\n
    ''')
    for fname in var.ADV_OPERATORS:
        if var.ADV_OPERATORS[fname].__doc__ is not None:
            screen.write('\t\t%s\t| %s\n\n' %(fname, (var.ADV_OPERATORS[fname].__doc__.splitlines()[-1:][0])))
    screen.write('''
        System operations:\n
        \t'\t| drops highest stack member {0}\n
        \trm\t| drops requested member from stack {1}\n
        \thelp\t| opens full documentation\n
        \t?funcname\t| opens documentation for function {1}\n
        \t;\t| clears input (not including stack members) {0}\n
        \tq\t| quit
        ''')
    raw_input("Press enter to exit documentation")
    clear_line()

def newline():
    if var.decimal:
        var.number = handler.add_decimal(var.number, var.decimal_insert)
        var.decimal = False
    if var.number is not None:
        var.stack.append(float(var.number))
        screen.draw()
        var.number = None

def backspace():
    screen.write('\b \b')
    if var.lastkey.isalpha():
        var.keyword = var.keyword[:-1]
        if var.keyword == '':
            var.keyword = None
    elif var.lastkey.isdigit():
        try:
            var.number = int(str(var.number)[:-1])
        except:
            var.number = None
    elif var.lastkey == '.':
        var.decimal = False

def quit():
    sys.exit()

def inline_help():
    var.comhelp = True
    var.helpcommand = '?'
    screen.write('?')
