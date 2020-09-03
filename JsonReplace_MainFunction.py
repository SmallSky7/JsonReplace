import json
from Function.Symbol_ReplaceController import *
from Function.Position_strController import *
from Function.initdate_ReplaceController import *
from Function.Date_ReplaceController import *
from JsonReplace import JsonReplace

def get_new_json(file_path):
    # 打开json文件
    file = open(file_path, encoding='gbk')
    json_to_python = json.load(file, strict=False)

    # 判断json文件格式
    if 'data' in json_to_python: # Json文件中只有一个data的文件格式
        return json_to_python
    elif "rows" not in json_to_python: # 说明是list格式的
        # 对Json文件中可能本身value就是"-"的场景作处理，参数置为1即开启
        if int(JsonReplace().symbol_para) == 1:
            json_to_python = Symbol_ReplaceController(json_to_python, file_path)
        
        # 对文件中包含当前日期的position_str作替换
        json_to_python = Position_strController(json_to_python)

        # 对Json文件中init_date作处理
        json_to_python = initdate_ReplaceController(json_to_python)

        # 对Json文件中指定date作处理
        for key in JsonReplace().date_key:
            date_value = JsonReplace().config.get("DATE", key)
            for value in date_value.split(','):
                json_to_python = Date_ReplaceController(json_to_python, value)
        
        return json_to_python
    else: # 说明是dict格式的
        json_to_python_rows = json_to_python['rows']  # 导致写入JSON文件后丢失字段的罪魁祸首
        # 对Json文件中可能本身value就是"-"的场景作处理，参数置为1即开启
        if int(JsonReplace().symbol_para) == 1:
            json_to_python_rows = Symbol_ReplaceController(json_to_python_rows, file_path)
        
        # 对文件中包含当前日期的position_str作替换
        json_to_python_rows = Position_strController(json_to_python_rows)

        # 对Json文件中init_date作处理
        json_to_python_rows = initdate_ReplaceController(json_to_python_rows)

        # 对Json文件中指定date作处理
        for key in JsonReplace().date_key:
            date_value = JsonReplace().config.get("DATE", key)
            for value in date_value.split(','):
                json_to_python_rows = Date_ReplaceController(json_to_python_rows, value)
        
        json_to_python['rows'] = json_to_python_rows
        
        return json_to_python


def rewrite_json_file(file_path, json_data):
    with open(file_path, 'w') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    f.close()