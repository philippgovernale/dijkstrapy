import var
import stackop
import sysfuncs

def num_handle():
    if var.number is None:
        var.number = var.key
    elif var.number:
        var.number = str(var.number) + var.key
    var.tostack = False

def match_and_operate(keyw):
    if keyw in var.operation_single:
        stackop.adv_operate_single(var.ADV_OPERATORS[keyw])
    elif keyw in var.operation_double:
        stackop.adv_operate_double(var.ADV_OPERATORS[keyw])
    elif keyw in var.operation_none:
        stackop.adv_operate_none(var.MATHS_CONSTANTS[keyw])
    elif keyw in var.operation_custom:
        var.ADV_OPERATORS[var.keyword]()

def operator_handler(operator):
    if not var.tostack:
        if var.number is not None:
            var.stack.append(float(var.number))
        var.tostack = True
    stackop.operate(operator)
    var.number = None

def character_handler(char):
    var.command = True
    if var.comhelp:
        var.helpcommand += char
        if var.helpcommand[1:] in var.ADV_OPERATORS or var.helpcommand[1:] in var.OPERATORS:
            sysfuncs.inline_help()
    elif var.keyword is None:
        var.keyword = var.key
        if var.keyword in var.ADV_OPERATORS or var.keyword in var.MATHS_CONSTANTS:
            match_and_operate(var.keyword)
            var.keyword = None
            var.number = None
    else:
        var.keyword += char
        if var.keyword in var.ADV_OPERATORS or var.keyword in var.MATHS_CONSTANTS:
            match_and_operate(var.keyword)
            var.keyword = None
            var.number = None
