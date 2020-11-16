import requests
from dbtools import query
#homework
#用户登录-用户新增文章-用户修改文章
#要求：必要的时候做完整的校验

#用户登录
#1、构造请求
u = "http://118.24.105.78:2333/login"
h = {"Content-Type":"application/json"}
d = {"username":"liuyun1","password":"a12345678"}
res = requests.post(url=u,headers=h,json=d)
#2、判断结果
assert res.status_code == 200
assert res.json()["status"] == 200
#3、数据库查询
sql = "select * from t_user where username='{}'".format(d["username"])
assert len(query(sql)) != 0
print("用户登录成功")

#获取登录token值
token = res.json()["data"]["token"]

#用户新增文章
#1、构造请求
u = "http://118.24.105.78:2333/article/new"
h = {"Content-Type":"application/json","token":token}
d = {"title":"接口自动化基础","content":"这就是接口自动化的小基础","tags":"这是测试哟","brief":"这篇文章不需要简介","ximg":"dsfsdf.jpg"}
res = requests.post(url=u,headers=h,json=d)

#2、判断结果
assert res.status_code == 200
assert res.json()["status"] == 200
#3、数据库查询
sql = "select * from t_article where title='{}' and content='{}'and tags='{}'and brief='{}' and ximg='{}'".format(d["title"],d["content"],d["tags"],d["brief"],d["ximg"])
# print(sql)
assert len(query(sql)) != 0
print("用户新增文章成功")

#用户修改文章
#1、构造请求
u = "http://118.24.105.78:2333/article/update"
h = {"Content-Type":"application/json","token":token}
d = {"title":"接口自动化基础","content":"这就是修改后的接口自动化的小基础", "tags":"这是测试哟","brief":"这篇文章不需要简介","ximg":"dsfsdf.jpg","aid":419024}
res = requests.post(url=u,headers=h,json=d)
# print(res.text)
#2、判断结果
assert res.status_code == 200
assert res.json()["status"] == 200
#3、数据库查询
sql = "select * from t_article where title='{}' and content='{}'and tags='{}'and brief='{}' and ximg='{}'".format(d["title"],d["content"],d["tags"],d["brief"],d["ximg"])
assert len(query(sql)) !=0
print("用户修改文章成功")