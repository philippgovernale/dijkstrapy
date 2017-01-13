import var
import screen

import time

def two_pop():
    a = var.stack.pop()
    b = var.stack.pop()
    return (a, b)

def operate(operator):
    if var.number is not None:
        var.stack.append(var.number)
    try:
        a = two_pop()
    except:
        screen.write("\nTwo numbers required in the stack to complete operation")
        raw_input()
        screen.clear()
    else:
        applied = var.OPERATORS[operator](a[1],a[0])
        var.stack.append(applied)
        screen.draw()

def adv_operate_double(function):
    if var.number is not None:
        var.stack.append(var.number)
    try:
        a = two_pop()
    except:
        screen.write("\nTwo numbers required in the stack to complete operation")
        raw_input()
        screen.clear()
    else:
        var.stack.append(function(a[1], a[0]))
    finally:
        screen.draw()

def adv_operate_single(function):
    if var.number is not None:
        var.stack.append(var.number)
    try:
        a = var.stack.pop()
    except:
        screen.write("\nOne number required in the stack to complete operation")
        raw_input()
        screen.clear()
    else:
        var.stack.append(function(a))
    finally:
        screen.draw()

def adv_operate_none(function):
    var.stack.append(function)
    screen.draw()
