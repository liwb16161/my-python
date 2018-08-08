#!/usr/local/bin/python3

import logging
import os.path
import time


class Log:
    """日志级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
    """
    def __init__(self,level="DEBUG"):
        if level == 'DEBUG':
            self._level = logging.DEBUG
        elif level == 'INFO':
            self._level = logging.INFO
        elif level == 'WARNING':
            self._level = logging.WARNING
        elif level == 'ERROR':
            self._level = logging.ERROR
        elif level == 'CRITICAL':
            self._level = logging.CRITICAL
        else :
            assert "level error"



    def logname(self,transname):
        """输入当前文件名称"""
        rq = time.strftime('%Y%m%d',time.localtime(time.time()))

        log_path = os.path.dirname(os.getcwd()) + '/Log/'
        try:
            os.mkdir(log_path)
        except FileExistsError as e:
            pass
        log_name = log_path + transname + rq +'.log'
        logfile = log_name

        self.log_name = logfile
        return logfile

    def output_message(self,message):
        if self._level == logging.DEBUG:
            logging.debug(message)
        elif self._level == logging.INFO:
            logging.info(message)
        elif self._level == logging.WARNING:
            logging.warning(message)
        elif self._level == logging.ERROR:
            logging.error(message)
        elif self._level == logging.CRITICAL:
            ogging.critical(message)

    def TransLog(self,message):
        # 第一步，创建一个logger
        logger = logging.getLogger()
        logger.setLevel(self._level) #log等级总开关

        # 第二步,创建一个handler,用于写入日志文件
        # rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        # rq = time.strftime('%Y%m%d',time.localtime(time.time()))
        #
        # log_path = os.path.dirname(os.getcwd()) + '/Log/'
        # try:
        #     os.mkdir(log_path)
        # except FileExistsError as e:
        #     pass
        # log_name = log_path + rq +'.log'
        # logfile = log_name
        fh = logging.FileHandler(self.log_name,mode='a') #输出到文件的handler
        fh.setLevel(self._level)

        ch = logging.StreamHandler()  #输出到屏幕上的handler
        ch.setLevel(self._level)
        #第三步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(filename)s[%(lineno)d - %(levelname)s -%(process)d - %(message)s]")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #第四步，将logger添加到handler里面
        logger.addHandler(fh)
        logger.addHandler(ch)

        self.output_message(message)
