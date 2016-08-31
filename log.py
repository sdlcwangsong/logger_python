#coding=utf8
import logging
import logging.config

class Log(object):
    def __init__(self, name, conf):
        logging.config.fileConfig(conf)
        self.logger = logging.getLogger(name)

    
    
if __name__=='__main__':   
    
    logger = Log("sWang","logger.conf").logger
    logger.debug('This is debug message')
    logger.info('This is info message')
    logger.warning('This is warning message')
    