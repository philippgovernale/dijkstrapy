import var
import screen
import sys
from decimal import Decimal, getcontext
import operator

def two_pop():
    a = var.stack.pop()
    b = var.stack.pop()
    return (float(a), float(b))

def append_rogue():
    '''appends number to stack if it is not already there'''
    if var.number is not None:
        if var.conf_decimal:
            var.stack.append(Decimal(var.number))
        else:
            var.stack.append(float(var.number))

# the operate functions should not be calling draw.

def adv_operate_double(function):
    # var.number is not none if the user has entered a digit before the command
    append_rogue()
    try:
        a = two_pop()
    except IndexError:
        screen.write("\nTwo numbers required in the stack to complete operation")
        raw_input()
        screen.clear()
    else:
        try:
            result = function(a[1], a[0])
        except ValueError:
            screen.write("\n%r does not accept decimal input. Please enter integer values" %(function))
            raw_input()
            screen.clear()
        except OverflowError:
            screen.write("\nOverflow. Please choose numbers that leads to a result that is smaller than %r"%(sys.float_info))
            raw_input()
            screen.clear()
        else:
            var.stack.append(result)

def adv_operate_single(function):
    append_rogue()
    try:
        a = var.stack.pop()
    except IndexError:
        screen.write("\nOne number required in the stack to complete operation")
        raw_input()
        screen.clear()
    else:
        try:
            result = function(a)
        except ValueError:
            screen.write("\n%r does not accept decimal input. Please enter integer values" %(function))
            raw_input()
            screen.clear()
        except OverflowError:
            screen.write("\nOverflow. Please choose numbers that leads to a result that is smaller than %r"%(sys.float_info))
            raw_input()
            screen.clear()
        else:
            var.stack.append(result)

def adv_operate_none(function):
    if var.conf_decimal:
        var.stack.append(Decimal(function))
    else:
        var.stack.append(function)
    screen.draw()
