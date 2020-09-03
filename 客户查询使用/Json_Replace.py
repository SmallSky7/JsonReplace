# -*- coding: UTF-8 -*-

import os,sys
import json
import shutil
import time
import re

from hslib.common import logger

log = logger.getlogger()

def Json_Replace(clouddict, uiexpect = None):
    # 获取字典中的值
    abs_path = clouddict['abs_path']
    path = clouddict['path']
    key = clouddict['key']
    value = clouddict['value']
    check_error = check(abs_path, path, key, value)
    if check_error:
        log.info(check_error)
        sys.exit(0)

    # 修改时间格式
    if value == 'init_date':
        value = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    # 复制文件，并将.json_bak修改为.json
    file = str(abs_path) + '\\' + str(path).split('=')[1]
    try:
        portion = os.path.splitext(file)
    except FileNotFoundError:
        log.info('系统没有找到指定路径')
    if portion[1] == '.json':
        file_path = portion[0] + '.json_bak'
        txt_path = portion[0] + '.txt'
        try:
            shutil.copyfile(file_path, file)
            log.info('文件复制成功')
        except FileNotFoundError:
            log.info('没有找到_bak文件,请再执行一遍用例')
            sys.exit(0)
    else:
        log.info('path中文件后缀名请修改为.json')

    # 替换json文件中对应的值
    json_to_python = json.load(open(file, encoding='gbk'), strict=False)

    json_value = str(json_to_python['data'])

    value_split = json_value.split(key)
    for i in range(1, len(value_split)):
        new_value = value_split[i].replace(value_split[i][0:10], str(value))
        value_split[i] = new_value
    new_json = key.join(value_split)
    
    json_to_python['data'] = new_json

    """new_value = json_value.replace(str(key), str(value))
    json_to_python['data'] = new_value"""

    """if re.search(str(key), str(json_to_python['data'])) == None:
        log.info(str(key) + '已全部替换为' + str(value))"""
    
    with open(txt_path, 'w') as ft:
        ft.write(str(json_to_python['data']))
    ft.close()

    with open(file, 'w') as f:
        json.dump(json_to_python, f, indent=4, ensure_ascii=False)
    f.close()


def check(abs_path, path, key, value):
    errormsg = []
    if abs_path ==' ' or abs_path == None:
        errormsg.append('abs_path不能为空')
    if path == ' ' or abs_path == None:
        errormsg.append('path不能为空')
    if re.match('/=', path) == None:
        errormsg.append('path格式无法读取')
    if key == ' ' or key == None:
        errormsg.append('key不能为空')
    if value == ' ' or value == None:
        errormsg.append('value不能为空')
    
    return errormsg