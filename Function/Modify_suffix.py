import os
import sys
import logging


def Modify_suffix(old_suffix, new_suffix, files):
    files_Modified = []
    count = 0

    for file in files:
        portion = os.path.splitext(file)
        if portion[1] == old_suffix:
            count = count + 1
    if count == 0:
        print(">>>该文件夹下没有后缀为" + old_suffix + "的文件<<<")
        logging.debug(">>>该文件夹下没有后缀为.json_bak的文件<<<")
        return files
    while (count > 0):
        for file in files:
            portion = os.path.splitext(file)
            if portion[1] == old_suffix:
                newname = portion[0] + new_suffix
                try:
                    os.rename(file, newname)
                    files_Modified.append(newname)
                    count = count - 1
                except FileExistsError:
                    print(">>>" + newname + "文件已存在,停止执行<<<")
                    logging.debug(">>>" + newname + "文件已存在,停止执行<<<")
                    sys.exit(0)
    if count == 0:
        print(">>>后缀已经修改为" + new_suffix + "<<<")
        logging.debug(">>>后缀已经修改为.json<<<")
        return files_Modified
