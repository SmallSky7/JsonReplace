import logging
import re
from JsonReplace import JsonReplace


def Position_strController(json_data):
    list_length = len(json_data)
    count = 0

    for i in range(0, list_length):
        if re.search(JsonReplace().init_date, str(json_data[i].get('position_str'))):
            count = count + 1
    if count == 0:
        return json_data
    print("\t>>>找到" + str(count) + "个" + "position_str匹配项", end=',')
    logging.debug(">>>找到" + str(count) + "个" + "position_str匹配项<<<")
    while (count > 0):
        for i in range(0, list_length):
            if re.search(JsonReplace().init_date, json_data[i].get('position_str')):
                json_data[i]['position_str'] = '-'
                count = count - 1
    if count == 0:
        print("已全部修改<<<")
        logging.debug(">>>已全部修改为" + '\'-\'<<<')
    else:
        print("剩余" + str(count) + "个修改失败<<<")
        logging.debug(">>>剩余" + str(count) + "个修改失败<<<")
    return json_data
