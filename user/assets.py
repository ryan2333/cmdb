# encoding: utf-8
'''
返回所有资产信息
【{'sn': '', 'id': '', 'hostname':'', 'ip': '', ...},{},{}】
'''
from dbutils import execute_fetch_sql, execute_commit_sql

def get_list():
    _column = 'id,sn,ip,hostname,os,purchase_date,warranty,vendor,model,idc_id,admin,business,cpu,mem,disk'
    _columns = _column.split(',')
    _sql = 'select {column} from assets where status=0'.format(column=_column)
    print _sql
    _cnt, _rt_list = execute_fetch_sql(_sql)
    print _rt_list
    return [dict(zip(_columns, _line)) for _line in _rt_list]


'''
通过主键返回资产信息
返回None/{}
'''
def get_by_id(aid):
    return None


'''
在创建资产时对信息进行检查
返回None
'''
def validate_create():
    return True, {}


'''
创建资产,更新数据库
返回True/False
'''
def create():
    pass


'''
在修改资产时对信息进行检查
返回True/False, error_msg{}
'''
def validate_update():
    return True, {}


'''
更新资产,更新数据库
返回True/False
'''
def update():
    pass



'''
删除资产,更新数据库
返回True/False
'''
def delete():
    pass


if __name__ == '__main__':
    print get_list()