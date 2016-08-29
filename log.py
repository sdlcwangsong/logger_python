#coding=utf8
import logging
import logging.config

class Log(object):
    def __init__(self, name):
        logging.config.fileConfig("logger.conf")
        self.logger = logging.getLogger(name)
    
    def debug(self, message):
        return self.logger.debug(message)
        
    def info(self, message):
        return self.logger.info(message)
        
    def warning(self, message):
        return self.logger.warning(message)

if __name__=='__main__':   
    
    logger = Log("sWang")
    logger.debug('This is debug message')
    logger.info('This is info message')
    logger.warning('This is warning message')
    