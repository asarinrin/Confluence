""" logger(python)のexample

"""

import os
import sys
from logging import getLogger, Logger, StreamHandler, FileHandler, Formatter, Filter, DEBUG, INFO, WARNING, ERROR, CRITICAL, NOTSET
from datetime import datetime

LOGLEVEL = DEBUG
ABSPATH = os.path.abspath(".")

class CustomFilter(Filter):
    """任意に定義することのできるフィルター"""

    def filter(self, record):
        """ファイル名、関数名、行番号が出力されるようにフィルタを設定
        rtype: boolean: Trueで常にフィルターをパス
        """
        record.real_filename = getattr(record,'real_filename',record.filename)
        record.real_funcname = getattr(record,'real_funcname',record.funcName)
        record.real_lineno   = getattr(record,'real_lineno',  record.lineno)
        return True

class Logging():

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Logging, cls).__new__(cls)
            cls._instance.__launch()
        return cls._instance

    def __init__(self):
        self.fmt_default = Formatter("%(asctime)s [%(levelname)s]\t%(real_filename)s - %(real_funcname)s:%(real_lineno)s -> %(message)s", "%Y-%m-%d %H:%M:%S")
        self.fmt_start   = Formatter("%(asctime)s %(message)s", "%Y-%m-%d %H:%M:%S")
        self.greet = "default"

    def create_require(self, logname="default", loglevel=DEBUG, filepath="logs/test.log", fmt_type="default", custom_filter=True):
        """loggerの生成
        
        :param str       logname: loggerの名前
        :param Formatter fmt    : フォーマッターの指定
        :return: loggerを返す
        :rtype : Logging
        """

        logger = getLogger(logname)
        logger.setLevel(loglevel)

        if logger.hasHandlers(): return logger

        fmt = self.fmt_default
        if fmt_type == "start": fmt = self.fmt_start

        sh = StreamHandler(sys.stdout)
        sh.setLevel(loglevel)
        sh.setFormatter(fmt)
        logger.addHandler(sh)

        if filepath is not None:
            fh = FileHandler(filepath)
            fh.setLevel(loglevel)
            fh.setFormatter(fmt)
            logger.addHandler(fh)

        if custom_filter: logger.addFilter(CustomFilter())

        return logger

    def __launch(cls):
        startlogger = getLogger("start-logger")
        logger = getLogger("server-logger")
        logger.setLevel(LOGLEVEL)

        sh = StreamHandler(sys.stdout)
        fh = FileHandler("logs/test.log")
        sh.setLevel(LOGLEVEL)
        fh.setLevel(LOGLEVEL)
        startlogger.addHandler(fh)
        startlogger.addHandler(sh)
        startlogger.critical('\n------------ START LOGGER [{}] ------------'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
