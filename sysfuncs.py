import var
import screen

import sys
import pkg_resources

def clear_line(): # ; command
    '''clear line (not including stacks)'''
    var.number = None
    var.command = None
    var.keyword = None
    screen.clear()

def delete_stack(): #rm command
    '''remove stack member x'''
    if var.number is not None:
        var.stack.append(var.number)
    try:
        a = var.stack.pop()
    except IndexError:
        screen.write("\nNeed a stack to remove\n")
    else:
        try:
            del var.stack[a]
        except IndexError:
            screen.write("\nStack %r does not exist. Cannot remove\n"%(a))
    finally:
        raw_input("Press enter to continue")
        screen.draw()

def drop():
    '''remove last stack'''
    try:
        var.stack.pop()
    except IndexError:
        screen.write("\nCannot remove stack")
        raw_input("\nPress enter to continue...")
    finally:
        screen.draw()

def assist():
    '''show help manual'''
    screen.clear()
    screen.custom_write('Dijkstrapy Documentation', 'underline')
    screen.write('''\n
        Dijkstrapy is a reverse polish notation (rpn) calculator that intends to simulate the experience of such a
        calculator on pc.\n
        Simple operations:\n
        ''')
    screen.write('''
        \t%s\t| adds numbers {2}\n
        \t%s\t| subtracts numbers {2}\n
        \t%s\t| multiplies numbers {2}\n
        \t%s\t| divides number {2}\n
        Math functions:
        '''%(screen.custom_write('+', 'yellow'), screen.custom_write('-', 'yellow'), screen.custom_write('*', 'yellow'), screen.custom_write('/', 'yellow')))
    for fname in var.ADV_OPERATORS:
        if var.ADV_OPERATORS[fname].__doc__ is not None:
            screen.write('\n\t\t%s\t| %s\n' %(screen.custom_write(fname, 'green'), (var.ADV_OPERATORS[fname].__doc__.splitlines()[-1:][0])))
    screen.write('''
        System operations:\n
        \t%s\t| drops highest stack member {0}\n
        \t%s\t| drops requested member from stack {1}\n
        \t%s\t| opens full documentation\n
        \t%s\t| opens documentation for function {1}\n
        \t%s\t| clears input (not including stack members) {0}\n
        \t%s\t| quit
        '''%(screen.custom_write("'", 'cyan'), screen.custom_write('rm', 'cyan'), screen.custom_write('help', 'cyan'), screen.custom_write('?funcname', 'cyan'), screen.custom_write(';', 'cyan'), screen.custom_write('q', 'cyan')))
    raw_input("Press enter to exit documentation")
    clear_line()

def newline():
    if var.number is not None:
        var.stack.append(float(var.number))
        var.number = None
        screen.draw()
    var.leadingzero = False

def backspace():
    screen.write('\b ')
    if var.keyword is not None:
        var.keyword = var.keyword[:-1]
        if var.keyword == '':
            var.keyword = None
    elif var.number is not None:
        var.number = str(var.number)[:-1]
        if var.number == '':
            var.number = None
    elif var.helpcommand is not None:
        var.helpcommand = var.helpcommand[:-1]
        if var.helpcommand == '':
            var.helpcommand = None

def leave():
    sys.exit()

def catch_inline_help():
    var.comhelp = True
    var.helpcommand = '?'

def inline_help():
    screen.clear()
    if var.helpcommand[1:] in var.ADV_OPERATORS:
        screen.write(var.ADV_OPERATORS[var.helpcommand[1:]].__doc__)
    elif var.helpcommand[1:] in var.OPERATORS:
        screen.write(var.OPERATORS[var.helpcommand[1:]].__doc__)
    raw_input('\nPress enter to continue')
    screen.clear()
    var.comhelp = False
    var.helpcommand = None
    var.keyword = None
    var.number = None

def display_version():
    version = pkg_resources.require('dijkstrapy')[0].version
    screen.clear()
    screen.write('\b \b'+version+'\n')
    raw_input("Press enter to continue")
    screen.clear()
