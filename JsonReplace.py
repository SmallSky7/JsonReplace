import logging
import time
import configparser
import os,sys
from JsonReplace_MainFunction import *


class JsonReplace:
    def __init__(self):
        self.init_date = time.strftime("%Y%m%d", time.localtime(time.time()))
        self.config = configparser.ConfigParser()

        if getattr(sys, 'frozen', False):
            self.homepath = os.path.dirname(sys.executable)
        elif __file__:
            self.homepath = os.path.dirname(__file__)

        config_path = os.path.join(self.homepath, 'Setting.conf')

        # 读取Setting.conf文件参数
        self.config.read(config_path, encoding='utf-8')
        self.path_key = self.config['INFO']['path_key']
        self.date = self.config['INFO']['date_key'].split(',')
        self.symbol_para = self.config['INFO']['symbol_para']
        self.absolute_path = self.config['PATH']['absolute_path']
        self.path = self.config['PATH']['path']
        self.date_key = self.config.options('DATE')
        self.symbol_path = self.config['SYMBOL']['symbol_path'].split(',')
        self.symbol_key = self.config['SYMBOL']['symbol_key'].split(',')


if __name__ == "__main__":
    from Function.Modify_suffix import *

    # 配置日志
    log_name = './Log/' + str(JsonReplace().init_date) + '.log'
    if 'Log' not in os.listdir(JsonReplace().homepath):
        os.mkdir('./Log')
    logging.basicConfig(filename=log_name, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug('>>>程序开始运行<<<')

    files_list = []

    if JsonReplace().path_key == '0':  # 启用绝对地址
        file_path = JsonReplace().absolute_path + '\\' + JsonReplace().path
    elif JsonReplace().path_key == '1':  # 不启用绝对地址，直接读path中的路径
        file_path = JsonReplace().path
    else:
        print(">>>无法读取path_key<<<")
        logging.debug(">>>无法读取path_key<<<")
        sys.exit(0)

    try:
        for root, path, files in os.walk(file_path):
            for file in files:
                files_list.append(root + '\\' + file)
    except FileNotFoundError:
        print(">>>系统没有找到指定路径<<<")
        logging.debug(">>>系统没有找到指定路径<<<\n")
        sys.exit(0)

    # 修改文件后缀
    files_Modified = Modify_suffix(".json_bak", ".json", files_list)

    # Json文件字段替换
    for file in files_Modified:
        print("------------------------------------------\n" + file)
        logging.debug('>>>' + file + '<<<')
        try:
            json_data = get_new_json(file)  # 作JSON文件文本替换
            rewrite_json_file(file, json_data)  # 写入新的JSON文件
        except:
            print(">>>程序出现异常<<<")
            logging.debug(">>>程序出现异常<<<")

    print("------------------------------------------")
    a = input(">>>是否需要打开对应的文件夹 y/n<<<\n")
    if a == 'y':
        print(file_path)
        os.system("explorer.exe %s" % file_path)
    if a == 'n':
        sys.exit(0)

    logging.debug('>>>程序结束运行<<<\n')
