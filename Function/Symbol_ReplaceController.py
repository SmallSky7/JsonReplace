from JsonReplace import JsonReplace
import logging


def Symbol_ReplaceController(json_data, file_path):
    if int(JsonReplace().symbol_path[0]) == 0:
        print(">>>文件名为空，将对文件夹下所有文件对应字段作替换\"\-\"<<<")
        logging.debug(">>>文件名为空，将对文件夹下所有文件对应字段作替换\"\-\"<<<")
        json_data = Symbol_ReplaceFunction(json_data)
        return json_data
    for i in range(0, len(JsonReplace().symbol_path)):
        if file_path == JsonReplace().symbol_path[i]:
            json_data = Symbol_ReplaceFunction(json_data)
        else:
            print(">>>文件路径不统一<<<")
            logging.debug(">>>文件路径不统一<<<")
    return json_data


def Symbol_ReplaceFunction(json_data):
    list_length = len(json_data)
    count = 0

    for i in range(0, list_length):
        for key in JsonReplace().symbol_key:
            if json_data[i][key] == '-':
                count = count + 1
        if count == 0:
            continue
        print("\t>>>找到" + str(count) + "个\'-\'匹配项", end=',')
        logging.debug(">>>找到" + str(count) + "个\'-\'匹配项<<<")
        while (count > 0):
            for key in JsonReplace().symbol_key:
                if json_data[i][key] == '-':
                    json_data[i][key] = '\-'
                    count = count - 1
        if count == 0:
            print("已全部修改<<<")
            logging.debug(">>>已全部修改为" + '\'\-\'<<<')
        else:
            print("剩余" + str(count) + "个没有修改")
            logging.debug(">>>剩余" + str(count) + "个没有修改<<<")
    return json_data
