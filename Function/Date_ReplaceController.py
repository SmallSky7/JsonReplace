import logging
import datetime
from JsonReplace import JsonReplace


def Date_ReplaceController(json_date, date_value):
    list_length = len(json_date)
    today_date = datetime.date.today() + datetime.timedelta(days=int(date_value))
    count = 0

    for key in JsonReplace().date_key:
        for i in range(0, list_length):
            if json_date[i].get(key) == int(today_date.strftime("%Y%m%d")):
                count = count + 1
        if count == 0:
            return json_date
        print("\t>>>找到" + str(count) + "个" + key + "匹配项", end=',')
        logging.debug(">>>找到" + str(count) + "个" + key + "匹配项<<<")
        while (count > 0):
            for i in range(0, list_length):
                if json_date[i].get(key) == int(today_date.strftime("%Y%m%d")):
                    json_date[i][key] = '-'
                    count = count - 1
        if count == 0:
            print("已全部修改<<<")
            logging.debug(">>>已全部修改为" + '\'-\'<<<')
        else:
            print("剩余" + str(count) + "个修改失败<<<")
            logging.debug(">>>剩余" + str(count) + "个修改失败<<<")
        return json_date
