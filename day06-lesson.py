#requests，注意文件名不能为requests，不然就以为是导的文件了
import requests
from dbtools import query


# url = "http://118.24.105.78:2333/get_title_img"
# res = requests.get(url)  #使用requests去请求get类型的接口
# print(res.text)    #res.text:获取返回值


# #1、构造请求
# u = "http://118.24.105.78:2333/login"      #地址类型字符串
# h = {"Content-Type":"application/json"}     #请求头：字典
# d = {"username":"liuyun1","password":"a12345678"}    #json参数：字典
# #post请求
# res = requests.post(url=u,headers=h,json=d)
# # print(res.text)

# #2、判断结果
# #http状态码：标志着接口的状态   300-重定向
# #结果返回值（结果码）
# assert res.status_code == 200    #断言：assert+条件语句  判断200：只有200的时候接口才是正确的  #预判请求有没有问题
# assert res.json()["status"] == 200    #判断结果码，这个必须要接口状态码200之后
    

# #使用requests注册一个测谈网账号，使用断言判断结果
# #1、构造请求
# u = "http://118.24.105.78:2333/regist"      #地址类型字符串
# h = {"Content-Type":"application/json"}     #请求头：字典
# d = {"username":"zhizhang","password":"a12345678","phone":"18181866333","email":"zz@qq.com"}    
# res = requests.post(url=u,headers=h,json=d)
# # 2、判断结果
# assert res.status_code == 200    
# # assert res.json()["status"] == 200 
# print(res.json()["status"])   


# sql = "select * from t_user where username='{}".format(d[username])
# assert len(query(sql)) !=0
# print("登录成功")

