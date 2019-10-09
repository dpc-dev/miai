import re
def test_name(user_name):
    '''
    user_name:校验用户名是否合法
    '''
    if re.match("^\S{2,8}$",user_name):
        a = True
    else:
        a = False
    return a
def test_pwd(user_pwd):
    '''
    user_name:校验用户密码是否合法，合法True，非法False
    '''
    if re.match("^\s*?$",user_pwd) or re.match("^[a-z]*?$",user_pwd) or re.match("^[0-9]*?$",user_pwd) or len(user_pwd)>16 or len(user_pwd)<8:
        a=False
    else:
        a = True
    return a
def test_email(user_email):
    '''
    user_email:校验 用户邮箱是否合法
    '''
    if re.match("^.*?@.*?\.([a-z]*?)$",user_email):
        a = True
    else:
        a =False
    return a
def test_phone(user_phone):
    if re.match("^1\d{10}$",user_phone):
        a = True
    else:
        a = False
    return a


