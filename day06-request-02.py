#关联
import requests
from dbtools import query

#登录
u = "http://118.24.105.78:2333/login"
h = {"Content-Type":"application/json"}
d = {"username":"liuyun1","password":"a12345678"}

res = requests.post(url=u,headers=h,json=d)

assert res.status_code == 200
assert res.json()["status"] == 200

sql = "select * from t_user where username = '{}'".format(d["username"])
assert len(query(sql)) !=0
print("用户登录成功")

#取token值
token = res.json()["data"]["token"]

#关联用户退出
u = "http://118.24.105.78:2333/logout"
h = {"Content-Type":"application/json","token":token}

res = requests.get(url=u,headers=h)

assert res.status_code == 200
assert res.json()["status"] == 200
print("用户退出登录成功")