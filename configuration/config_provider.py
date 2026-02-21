import configparser


class ConfigProvider:
    def __init__(self, filename):
        self.config = configparser.ConfigParser()
        self.config.read(filename)

    def get(self, section, key):
        return self.config[section][key]

    def get_int(self, section, key):
        return self.config[section].getint(key)
