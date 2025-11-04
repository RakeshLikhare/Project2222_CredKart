import logging                  ##log's generate karne ke liye ye library khud import karna padta hai
import inspect


class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]             ##ye use krne se logs me second number pe ROOT ke jagah Class ka name aata hai
        logger = logging.getLogger(name)
        logfile=logging.FileHandler(".\\Logs\\CredKart_Logs.log")
        logformate =logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s")
        logfile.setFormatter(logformate)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger

### logs ke create hone ke bad uska level kaise hota hai --->imp for interview
##debug
##info
##warning
##error
##critical
## ye hota hai level ese he level batana hai sequence me aage piche nhi chalenga guys


##log ka level jo bhi set kro vha se logs generate hona start hota hai uske niche ke logs level wale logs he logfile me capture hote hai uske upar ke logs ke level ko vo cosider nhi krta hai
