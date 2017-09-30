from configparser import ConfigParser

def read(cfg_file, section=None):
    config = ConfigParser()
    config.read(cfg_file)
    return dict(config.items(section))
