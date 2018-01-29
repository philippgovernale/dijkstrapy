import var
import screen
import sys
import stackop
import pkg_resources
from decimal import Decimal, getcontext

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
    try:
        del var.stack[int(a)]
    except IndexError:
        screen.write("\nStack %r does not exist. Cannot remove\n"%(a))
    finally:
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
        #screen.write('\b \b') # temporary solution

def swap():
    '''swap the last two stack positions'''
    #this function works differently from other two operand functions. Hence stackop func cannot be used
    try:
        a = var.stack.pop()
        b = var.stack.pop()
        var.stack.append(a)
        var.stack.append(b)
    except IndexError:
        screen.write("\nCannot remove stack")
        raw_input("\nPress enter to continue...")
    finally:
        screen.draw()
        #screen.write('\b \b') #temporary solution

def assist():
    '''show help manual'''
    screen.clear()
    #starting newline is temp solution
    screen.write('''\nDijkstrapy Documentation\n
        Dijkstrapy is a reverse polish notation (rpn) calculator that intends to simulate the experience of such a
        calculator on pc.\n
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
        \t'\t| drops highest stack member {1}\n
        \trm\t| drops requested member from stack {1}\n
        \thelp\t| opens full documentation\n
        \t?fnc\t| opens documentation for function {1}\n
        \t;\t| clears input (not including stack members) {0}\n
        \tq\t| quit
        ''')
    raw_input("Press enter to exit documentation")
    clear_line()

def newline():
    if var.number is not None:
        if var.conf_decimal:
            getcontext.prec = 10
            var.stack.append(Decimal(var.number))
        else:
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
    screen.write('\r')
    sys.exit()

def catch_inline_help():
    var.comhelp = True
    var.helpcommand = '?'

def inline_help():
    screen.clear()
    if var.helpcommand[1:] in var.ADV_OPERATORS:
        try:
            screen.write(var.ADV_OPERATORS[var.helpcommand[1:]].__doc__)
        except TypeError:
            screen.write("Missing documentation for: %s"%(var.helpcommand[1:]))
    elif var.helpcommand[1:] in var.OPERATORS:
        try:
            screen.write(var.OPERATORS[var.helpcommand[1:]].__doc__)
        except TypeError:
            screen.write("Missing documentation for: %s"%(var.helpcommand[1:]))
    raw_input('\nPress enter to continue')
    screen.clear()
    var.comhelp = False
    var.helpcommand = None
    var.keyword = None
    var.number = None

def display_version():
    '''displays dijkstrapy version'''
    version_file = open('/data/VERSION')
    version = version_file.read().strip()
    screen.clear()
    screen.write('\b \b'+version+'\n')
    raw_input("Press enter to continue")
    screen.clear()

def set_precision(precision):
    try:
        precis = int(precision)
    except:
        precis = 20
    else:
        getcontext().prec = precis

def catch_recurs():
    var.recurs = True
    var.recurscommand = '@'

def recursion():
    op = var.recurscommand[1]
    screen.write(op)
    if op == 'a' and var.recurscommand[2] in var.OPERATORS:
        screen.write("Got here")
        for i in range(len(var.stack)-1):
            stackop.operate(var.recurscommand[2])
    elif op in var.OPERATORS:
        num = var.stack.pop()
        for n in range(int(num)-1):
            stackop.operate(op)
    screen.draw()
    var.recurs = False
    var.recurscommand = None
