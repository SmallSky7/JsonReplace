import logging
from JsonReplace import JsonReplace


def initdate_ReplaceController(json_date):
    list_length = len(json_date)
    count = 0

    for i in range(0, len(JsonReplace().date)):
        key = JsonReplace().date[i]
        for i in range(0, list_length):
            if json_date[i].get(key) == int(JsonReplace().init_date):
                count = count + 1
        if count == 0:
            continue
        print("\t>>>找到" + str(count) + "个" + key + "匹配项", end=',')
        logging.debug(">>>找到" + str(count) + "个" + key + "匹配项<<<")
        while (count > 0):
            for i in range(0, list_length):
                if json_date[i].get(key) == int(JsonReplace().init_date):
                    json_date[i][key] = '-'
                    count = count - 1
        if count == 0:
            print("已全部修改<<<")
            logging.debug(">>>已全部修改为" + '\'-\'<<<')
        else:
            print("剩余" + str(count) + "个修改失败<<<")
            logging.debug(">>>剩余" + str(count) + "个修改失败<<<")
    return json_date
