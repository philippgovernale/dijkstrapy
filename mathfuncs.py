import math

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
    return -operand
