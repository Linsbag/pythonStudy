#导入包,这个第三方包是人家写的，我们要用它，就是去用它的方法，一定要先导入,注意，因为我们要导requests包，所以文件名一定不能取requests，不然就分不清是要导文件还是包了
import requests
from dbtools import query  

# #用url存放接口地址,注意要加引号
# #获取首页轮播图接口地址
# url = "http://118.24.105.78:2333/get_title_img"    #接口地址一定是一个字符串
# h = {"Content-Type":"application/json"}
# #使用requests去请求get类型的接口,最终的返回值就是接口返回的内容了
# res = requests.get(url=url,headers=h)     #就相当于postman里边去填写接口地址
# #获取返回值：res.text
# print(res.text)

#post请求：用户登录接口 （依次从接口文档上填写请求地址、请求头、请求数据）
u = "http://118.24.105.78:2333/login"     #接口地址
h = {"Content-Type":"application/json"}    #请求头：字典格式
d = {"username":"liuyun1","password":"a12345678"}    #请求数据：json格式、字典

res = requests.post(url=u,headers=h,json=d)    #依次传参
# print(res.text)

#判断结果（要判断两个：先接口状态码和后结果返回值）
#状态码：标志着接口的状态:预判接口是否有问题       res.status_code获取状态码
assert res.status_code == 200     #运行这步要把前面的print(res.text)删掉或者注释掉
#结果返回值（结果码）  接口返回的结果是放在res中了，但是它存放的是字符串类型，python中用res.json()将字符串转换为字典类型
assert res.json()["status"] == 200

# #练习：使用requests去注册一个账号，并使用断言判断
# #1、构造请求
# u = "http://118.24.105.78:2333/regist"
# h = {"Content-Type":"application/json"}
# d = {"username":"aqy11111","password":"a123456789","phone":"18022222222","email":"aqy11111@163.com"}
# res = requests.post(url=u,headers=h,json=d)
# print(res.text)
# #2、判断结果
# assert res.status_code == 200
# assert res.json()["status"] == 200


#查询数据库
sql = "select * from t_user where username = '{}'".format(d["username"])
# print(sql)   #从这里就可以看见数据库语句拼接起来了
# r = query(sql)
assert len(query(sql)) != 0
print("登录成功的测试用例通过")