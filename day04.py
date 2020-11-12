import time
#循环语句range(数字):就差不多是个序列生成器
#就比如说range(10)：可以生成一个元组（0，1，2，3，4，5，6，7，8，9）


# for i in range(10):  #就把序列理解成元组就行
#     print(i)

#通过下标遍历元组数组
#这样就可以实现去除数组a中所有的值了，即使这个a的长度是变化的都没关系（元组也是类似的）
# a = [1,2,3,4,5,6,7,8,"hh"]
# b = len(a)
# for i in range(b):
#     print(a[i])

#break 关键字终止所有的循环，continue跳过本次循环，开始下一次循环

#打印九九乘法表  \t空格,对齐列表中的各列  \n换行
#print()方法中的end函数：用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}x{}={}\t'.format(j,i,j*i),end = " ")
#     print("")

#while循环
#while 条件语句:
# a = 1
# b = 2
# while a<b:
#     print("a < b")
#     a = a+1   #如果没有这个条件，这个循环会一直执行成死循环了

#while模拟红绿灯显示
#假设一共60s，绿灯30s，黄灯5s，红灯25s
# time= 60
# while True:   #死循环，表示红绿灯一直打印
#     #差一个东西来让红绿灯转起来，每次去增加一个数
#     for i in range(1,61):
#     #判断60s内的状态
#         if i < 31:
#             print("绿灯")
#         elif i < 36:
#             print("黄灯")
#         elif i < 61:
#             print("红灯")
#     break
# #这样运行下来会发现所有的红绿黄灯很快就打印完了，我们需要涉及到一个等待的东西
# #即python的包：python已经帮我们写好了的代码，直接拿来用即可，比如我们这块就涉及到一个time包
"""
主要分为以下几类包：
自带包：例如time、unittest、math等（直接使用，第三方包就必须要去下载）
自定义包：步骤：1、新建一个文件夹 2、在这个文件夹里新建文件取名__init__.py(两根下划线)，这样这个文件夹就变成一个包了，这样之后我们就可以在这个包里创建一些
东西，然后从别的包里引用它，引用方法：from 包名.py文件名 import 变量/方法/类
第三方包：一些大佬写的，如果我们需要取用的话，就会涉及到要去下载它，会用到工具pip/pip3
pip/pip3(用来管理第三方包的):   以管理员身份运行命令：
1、pip3 -V（查看版本号，验证这个工具能不能用）
2、pip3 list（查看所有第三方包）    
3、pip3 install 包名（例如装pymysql（python操作数据库的）：pip3 install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple）-i的意思是从国内去下载
4、安装requests（接口自动化测试）：pip3 install requests -i https://pypi.tuna.tsinghua.edu.cn/simple 
5、安装selenium（web自动化测试）：pip3 install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple
6、安装pytesy（第三方测试框架）：pip3 install pytest -i https://pypi.tuna.tsinghua.edu.cn/simple
源：可以加速下载：-i https://pypi.tuna.tsinghua.edu.cn/simple

卸载命令：pip3 uninstall 包名（这个就不用加源了）
使用方法：1、导入包：import 包名
2、方法2：from 包名 import 内容（例如：from selenium import webdriver）
"""

# while True: 
#     for i in range(1,61):
#     #判断60s内的状态
#         if i < 31:
#             print("绿灯")
#         elif i < 36:
#             print("黄灯")
#         elif i < 61:
#             print("红灯")
#         time.sleep(1)  #用time包里边的方法，注意这个1，就是每一秒打印一次，以后经常会用到的

#引用自定义包
# from wuyanzu.c import sudaqiang
# print(sudaqiang)

#自定义包的作用——封装：重复使用代码，可以使用方法或者类封装，对于python来说，使用方法更方便

#方法：模板/工具,直接调用就可以实现复用
#定义def 方法名(可选参数):，返回值可写可不写，参数可写可不写，但是一旦填写参数，调用方法的时候要去传参，且参数顺序传递
#方法可以不要返回值，如果需要方法给答复，那就需要返回值，否则就不需要，没有返回值，方法的结果为空None
#调用方法时，一定要注意参数一一对应
#方法取名时，多个单词中间用下划线隔开，不像Java，Java时驼峰式命名

def add(a,b):
    sum = a + b
    return sum  #方法不去调用是不会执行的 

# a = 1 + 1
# b = 2 + 2
a = add(1,1)
print(a)

#定义减法
def jianfa(a,b):
    return a-b


c=jianfa(2,1)
print(c)