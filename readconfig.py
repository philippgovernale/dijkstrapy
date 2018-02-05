from ConfigParser import ConfigParser
import var
import sys
import sysfuncs
import screen
import sysfuncs
import stackop

def str2bool(s):
    #returns true if argument in defined strings
    return s.lower() in ("yes", "1", 'true')

def check_colour(colour):
    if colour.lower() in ('red', 'blue', 'yellow', 'magenta', 'cyan', 'green','white', 'reset'):
        return colour
    else:
        return 'reset'

def reset_colours():
    if var.conf_colour_reset:
        var.conf_colour_digit_stack_number = 'reset'
        var.conf_colour_digit_stack = 'reset'
        var.conf_colour_alpha = 'reset'
        var.conf_colour_inline_help = 'reset'

def check_precision(precision):
    try:
        prec = int(precision)
        return prec
    except:
        prec = 20
        return prec


def load_config():

    cfg = ConfigParser()
    cfg.read('config.ini')

    sci_not = cfg.get('Main Configurations', 'scientific_notation')
    var.conf_sci_not = str2bool(sci_not)

    colour_digit_stack_number = cfg.get('Colour Configurations', 'colour_digit_stack_number')
    var.conf_colour_digit_stack_number = check_colour(colour_digit_stack_number)

    colour_digit_stack = cfg.get('Colour Configurations', 'colour_digit_stack')
    var.conf_colour_digit_stack = check_colour(colour_digit_stack)

    colour_alpha = cfg.get('Colour Configurations', 'colour_alpha')
    var.conf_colour_alpha = check_colour(colour_alpha)

    colour_inline_help = cfg.get('Colour Configurations', 'colour_inline_help')
    var.conf_colour_inline_help = check_colour(colour_inline_help)

    colour_reset = cfg.get('Main Configurations', 'colour_reset')
    var.conf_colour_reset = str2bool(colour_reset)
    reset_colours()

    decimal = cfg.get('Number Configurations', 'decimal')
    var.conf_decimal = str2bool(decimal)

    decimal_precision = cfg.get('Number Configurations', 'decimal_precision')
    var.conf_decimal_precision = check_precision(decimal_precision)
    sysfuncs.set_precision(var.conf_decimal_precision)

    ansi = cfg.get('Main Configurations', 'ansi')
    var.conf_ansi = str2bool(ansi)

    quit_command = cfg.get('Command shortcuts','quit')
    var.SYS_COMMANDS[quit_command] = sysfuncs.leave

    var.conf_prompt = cfg.get('Main Configurations', 'prompt')

    #read Custom constants
    for opt in cfg.options('Custom Constants'):
        val = cfg.get('Custom Constants',opt)
        var.MATHS_CONSTANTS[opt] = val
        var.operation_none.append(opt)

def read_argv():
    arguments = sys.argv[1:]
    for i,arg in enumerate(arguments):
        if arg in ['--noansi', '--help', '--sci-not']:
            if arg == '--noansi':
                var.conf_ansi = False
            elif arg == '--help':
                sysfuncs.assist()
            elif arg == '--sci-not':
                var.conf_sci_not = True
				
        elif arg.isdigit():
            var.stack.append(float(arg))
        elif arg in var.operation_single:
            stackop.adv_operate_single(var.ADV_OPERATORS[arg])
            if i == (len(arguments) -1):
                print var.stack[0]
                sysfuncs.leave()
        elif arg in var.operation_double:
            stackop.adv_operate_double(var.ADV_OPERATORS[arg])
            if i == (len(arguments) -1):
                print var.stack[0]
                sysfuncs.leave()
        else:
            print arg, "is not a valid argument-mode command. See 'dijkstrapy --help'"
            sys.exit()
