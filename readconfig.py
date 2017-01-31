from ConfigParser import ConfigParser
import var
import sys
import sysfuncs

def str2bool(s):
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

    ansi = cfg.get('Main Configurations', 'ansi')
    var.conf_ansi = str2bool(ansi)

def read_argv():
    arguments = sys.argv[1:]
    for arg in arguments:
        if arg in ['--noansi', '--help', '--sci-not']:
            if arg == '--noansi':
                var.conf_ansi = False
            elif arg == '--help':
                sysfuncs.assist()
            elif arg == '--sci-not':
                var.conf_sci_not = True
        else:
            print arg, "is not a dijkstrapy command. See 'dijkstrapy --help'"
            sys.exit()
