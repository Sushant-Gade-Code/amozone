import configparser
config=configparser.RawConfigParser()
config.read('.\\Configuration\\config.ini')

class ReadConfig:

    @staticmethod
    def getUrl():
        url=config.get("Common Info","baseUrl")
        return url

    @staticmethod
    def getuserEmail():
        uemail=config.get("Common Info","userEmail")
        return uemail

    @staticmethod
    def getpassWord():
        paasw=config.get("Common Info","passWord")
        return paasw