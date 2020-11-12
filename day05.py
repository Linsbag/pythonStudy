#复习：遍历字典的时候，i表示每个字典里边的key值
# grade = {"张三":88,"李四":56,"王麻子":90}
# hege = []
# buhege = []
# for i in grade:
#     if grade[i]>=60:
#         hege.append(i)
#     else:
#         buhege.append(i)
# #for循环遍历出了所有的成绩，当然是等for循环遍历完了才打印出名字啊
# print(hege)
# print(buhege)


#方法定义了，不调用是没有用的，调用方法之后，很多都有一个返回值，看返回给谁，倒推回去，然后看到参数，有参数的话就是我们传进去的值

#参数的默认值,传了就取值，否则取默认值   所有的数据类型都可以作为参数传进去
# def add(a,b):   #这个方法在定义的时候参数是没有默认值的
#     return a + b

# def add(a,b = 10):     #这个方法在定义的时候，b参数给了默认值，在方法调用的时候，如果我们传了参数，那就取传来的参数值，否则默认值处理
#     return a + b

# a=add(1,1)
# print(a)

# a=add(1)    #b本身有参数的时候，我们传值的时候可以不传给b，b会取默认值10
# print(a)

#参数可以是任意数据类型，比如这块就是字符串
# def user_login(username,password):
#     if username == "test" and password == "123456":
#         print("登录成功")
#     else:
#         print("登录失败")
        
# user_login("test","123456")


# u = input("请输入账号：")
# p = input("请输入密码：")
# user_login(u,p)

#异常处理   出现异常，代码终止
#如果代码出现错误，不想让他终止   try/except 


#pymysql  使用python连接，并且操作mysql数据库,相当于python的navicat

#步骤：
#2、封装对应的查询

# #导入pymysql
# import pymysql
# #封装查询方法
# def query(sql):
#     #1、连接MySQL数据库
#     db = pymysql.connect(host = "127.0.0.1",user="root",password = "123456",db = "test25")  #实现打开数据库的操作
#     #2、获取对应的查询窗口
#     cur = db.cursor()
#     #3、执行查询sql语句
#     cur.execute(sql)
#     #4、获取所有的结果
#     res = cur.fetchall()
#     #5、关闭数据库连接
#     db.close()
#     return res

# if __name__ == "__main__":
#     sql = "select * from student where id = 1"
#     r = query(sql)
#     print(r)

#模拟接口登陆的完整过程(调接口)
#两个文件在同一模块下相互导入（兄弟关系）
from dbtools import query

u = input("请输入账号：")
p = input("请输入密码：")

sql = "select * from t_pymysql_account where username = '{}' and password = '{}'".format(u,p)
res = query(sql)
if len(res) != 0:
    print("登陆成功")
else:
    print("登录失败")