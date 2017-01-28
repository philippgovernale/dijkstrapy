from ConfigParser import ConfigParser
import var

def str2bool(s):
    return s.lower() in ("yes", "1", 'true')

def load_config():
    cfg = ConfigParser()
    cfg.read('config.ini')

    e_display = cfg.get('Main Configurations', 'display_e')
    var.conf_e_display = str2bool(e_display)
