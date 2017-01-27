import math
from decimal import *

def cube_root(operand):
    '''Return the cube root of x'''
    power = 1 / 3.0
    result = math.pow(operand, power)
    return result

def sci_notation(operand1, operand2):
    '''scientific notation'''
    multiplier = math.pow(10, operand2)
    result = operand1 * multiplier
    return result

def invert_sign(operand):
    '''invert sign of operand'''
    return -operand

def decimal_places(operand1, operand2):
    precision = int(operand2)
    result = round(operand1, precision)
    return result

def rnd(operand1, operand2):
    num_before_dot = len(str(operand1).split('.')[0])
    operand1 = float(operand1)
    operand2 = int(operand2)
    if num_before_dot +1 < operand2:
        num_after_dot = operand2 - num_before_dot
        round_str = '0.'
        for dig in range(num_after_dot -1):
            round_str += '0'
        round_str += '1'
        result= float(Decimal(operand1).quantize(Decimal(round_str), rounding=ROUND_HALF_UP))
    elif num_before_dot == operand2:
        result = int(Decimal(operand1).quantize(Decimal('1'),rounding=ROUND_HALF_UP))
    else:
        a = "%.*e" %(operand2-1, operand1)
        if num_before_dot < operand2:
            result = float(a)
        else:
            f = float(a)
            result = int(f)
    return result
