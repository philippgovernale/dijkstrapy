import var
import stackop
import sysfuncs
from decimal import Decimal
import screen

def num_handle(): # why not move numbers to stack here as well? Because we don't know whether the number has finished
    '''sets number variable from key'''
    if var.number is None:
        var.number = var.key
    elif var.number:
        var.number = str(var.number) + var.key
    var.tostack = False

def match_and_operate(keyw):
    if keyw in var.operation_single:
        stackop.adv_operate_single(var.ADV_OPERATORS[keyw])
        screen.draw()
    elif keyw in var.operation_double:
        stackop.adv_operate_double(var.ADV_OPERATORS[keyw])
        screen.draw()
    elif keyw in var.operation_none:
        stackop.adv_operate_none(var.MATHS_CONSTANTS[keyw])
        screen.draw()
    elif keyw in var.operation_custom:
        var.ADV_OPERATORS[var.keyword]()

def character_handler(char):
    '''handles all characters (non numbers) and redirects to appropiate control'''
    var.command = True
    # why can comhelp not be regular keyword
    if var.recurs:
        var.recurscommand += char
        try:
            if var.recurscommand[1] == 'a' and var.recurscommand[2] in var.OPERATORS:
                sysfuncs.recursion()
            elif var.recurscommand[1] in var.OPERATORS:
                sysfuncs.recursion()
        except IndexError:
            pass

    elif var.keyword is None:
        var.keyword = var.key
    else:
        var.keyword += char

    if var.keyword in var.ADV_OPERATORS or var.keyword in var.MATHS_CONSTANTS:
        match_and_operate(var.keyword)
        var.keyword = None
        var.number = None
    elif var.keyword[0] == '?' and var.keyword[1:] in var.ADV_OPERATORS:
        sysfuncs.inline_help()
