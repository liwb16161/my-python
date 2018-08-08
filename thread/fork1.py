#!/usr/local/bin/python3
# 日志级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG


import os
import translog
import logging as LOG
import time

tl = translog.Log()
log_name = tl.logname(__name__)
LOG.basicConfig(filename=log_name,level=LOG.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置



pid = os.fork()
if pid < 0:
    LOG.info("make process error ")
elif pid == 0:
    LOG.debug("i am new process ")
    pid1 = os.fork()
    if pid1 < 0:
        LOG.info("make process error ")
    elif pid1 == 0:
        LOG.debug("i am new process")
