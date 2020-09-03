# JsonReplace
##简介
根据Setting.conf文件中的配置修改Json文件中对应的字段的值
##使用
###配置Setting.conf
- path_key=0时，启用绝对地址absolute_path，path_key=1时直接读取path
- date_key中配置要修改的字段，如果Json文件中相应的字段值等于当前日期，会直接修改为"-"
- symbol_para=0时，对value本身就是"-"的不做替换，symbol_para=1时，对value本身就是"-"的替换为"\-"
- DATE标签下配置需要替换特定日期的字段，比如update_date=-1，会替换Json文件中值是当前日期-1的字段
- SYMBOL标签下允许指定字段

###JsonReplace使用
直接执行，执行完允许打开对应目录
