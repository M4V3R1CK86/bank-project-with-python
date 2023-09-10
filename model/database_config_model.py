import configparser


class DatabaseConfigModel:
    def __init__(self, config_file='config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_db_config(self):
        return {
            'host': self.config.get('database', 'host'),
            'port': self.config.get('database', 'port'),
            'user': self.config.get('database', 'user'),
            'password': self.config.get('database', 'password')
        }
