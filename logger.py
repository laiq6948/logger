import os
import sys
import time
import logging
from singleton import Singleton


@Singleton  # Using Singleton here because we will output logs to only one path.
class Logger:
    def __init__(self, set_level="INFO",
        name=os.path.split(os.path.splitext(sys.argv[0])[0])[-1],
        log_name=time.strftime("%Y-%m-%d.log", time.localtime()),
        log_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "log"),
        use_console=True):
        """
        :param set_level: Log Level ["NOTSET"|"DEBUG"|"INFO"|"WARNING"|"ERROR"|"CRITICAL"], Default:INFO
        :param name: Log Name, Default: Name of Program
        :param log_name: Log File Name, Default: （Y-M-D.log）
        :param log_path: Log Path, Default: ~/log/
        :param use_console: Flag for handling whether print log on console, Default: True
        """
        if not set_level:
            set_level = self._exec_type()
        self.__logger = logging.getLogger(name)
        self.setLevel(
            getattr(logging, set_level.upper()) if hasattr(logging, set_level.upper()) else logging.INFO)
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler_list = list()
        handler_list.append(logging.FileHandler(os.path.join(log_path, log_name), encoding="utf-8"))
        if use_console:
            handler_list.append(logging.StreamHandler())
        for handler in handler_list:
            handler.setFormatter(formatter)
            self.addHandler(handler)

    def __getattr__(self, item):
        return getattr(self.logger, item)

    @property
    def logger(self):
        return self.__logger

    @logger.setter
    def logger(self, func):
        self.__logger = func

    @staticmethod
    def _exec_type():
        return "DEBUG" if os.environ.get("IPYTHONENABLE") else "INFO"
