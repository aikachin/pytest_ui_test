import  logging
import time
import os

class Logger(object):

    def __init__(self):

        # 创建一个logger
        self.logger = logging.getLogger()
        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        #log_dir = os.path.abspath('.').split('base_tools')[0]+ '\\logs\\'
        log_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ '\\logs\\'
        log_name = log_dir + rq + '.log'
        fh = logging.FileHandler(log_name,encoding="utf-8",mode="a")

        self.logger.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)
