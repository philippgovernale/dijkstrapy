from ConfigParser import ConfigParser
import var

def str2bool(s):
    return s.lower() in ("yes", "1", 'true')

def check_colour(colour):
    if colour.lower() in ['red', 'blue', 'yellow', 'magenta', 'cyan', 'green']:
        return colour
    else:
        return 'yellow'

def load_config():
    cfg = ConfigParser()
    cfg.read('config.ini')

    e_display = cfg.get('Main Configurations', 'display_e')
    var.conf_e_display = str2bool(e_display)

    colour_digit = cfg.get('Colour Configurations', 'colour_digit')
    var.conf_colour_digit = check_colour(colour_digit)
