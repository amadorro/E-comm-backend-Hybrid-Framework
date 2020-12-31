import configparser
'''Note: @staticmethod: is a decorator which is bound to
the class and not the object of the class.
'''

# create a variable
config = configparser.RawConfigParser()
# read data from .ini file
config.read('./Configurations/config.ini')

# get .ini variables
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getEmail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

