import  configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class readconfig:

    @staticmethod
    def read_email():
        email = config.get("login details","email_id")
        return email

    @staticmethod
    def read_password():
        password = config.get("login details","password")
        return password