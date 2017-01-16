import var
import screen
import sys

def two_pop():
    a = var.stack.pop()
    b = var.stack.pop()
    return (a, b)

def operate(operator):
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
    # var.number is not none if the user has entered a digit before the command
    if var.number is not None:
        var.stack.append(float(var.number))
    try:
        a = two_pop()
    except:
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
            var.stack.append(function(a[1], a[0]))
    finally:
        screen.draw()

def adv_operate_single(function):
    if var.number is not None:
        var.stack.append(float(var.number))
    try:
        a = var.stack.pop()
    except:
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
            var.stack.append(function(a))
    finally:
        screen.draw()

def adv_operate_none(function):
    var.stack.append(function)
    screen.draw()
