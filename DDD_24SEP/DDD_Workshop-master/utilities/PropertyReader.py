import configparser

config = configparser.RawConfigParser()

def get_property(group, value):
    config.read("utilities/ConfigFile.properties")
    return str(config.get(group, value))
