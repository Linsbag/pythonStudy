#if/else,  缩进：看到有冒号，下边的代码肯定是有缩进的（4个空格，tab键，竖线会提示）else可写可不写 
# a = 18
# if a>16:
#     print("成年了")
# else:
#     print("未成年")

# a = int(input("请输入一个年龄："))
# if a<17:
#     print("你好小")19
# else:
#     print("长大了")

#条件语句：==判断两个是数字/字符串是否相等
#连接两个或两个以上的条件：and：同时满足；or：满足一个
# name = input("请输入一个名字：")
# age = int(input("请输入年龄："))
# if name == "智障" and age == 20:
#     print("确实是智障")
# else:
#     print("hh")

#有一个字典{"张三":80,"李四":90}
# user = {"张三":80,"李四":90}
# u1 = user["张三"]
# u2 = user["李四"]     字典的取值有两种方法，一是通过key值直接取，二是通过get("key值")方法
# u1 = user.get("张三")
# u2 = user.get("李四")
# if u1 > u2:
#     print("张三棒")
# else:
#     print("李四棒")

#输入两个人的姓名和成绩，然后输出成绩更好的名字
# u1 = input("请输入名字1:")
# y1 = int(input("请输入名字1的成绩:"))
# u2 = input("请输入名字2:")
# y2 = int(input("请输入名字2成绩:"))
# account = {}
# account[u1] = y1
# account[u2] = y2
# if account[u1] >account[u2]:
#     print("这个兄弟更厉害:{}".format(u1))
# else:
#     print("这个兄弟更厉害:{}".format(u2))


"""
条件语句in：可以判断字符串，元组，列表是否包含
not in 取反
"""
# s1 = "睡王赢了"
# s2 = "懂王不服"
# if "睡王" in s1:
#     print("赢了")
# else:
#     print("输了")

# cj = (85,95,44,66)
# if 85 in cj:
#     print("yes")
# else:
#     print("no")

# cj = [85,95,44,66]
# if 85 in cj:
#     print("yes")
# else:
#     print("no")  

#elif表示在第一个if不满足条件的时候依次执行，也就是在if里边嵌套了，为什么不直接在里边再写一个if呢，这样可以避免代码看起来混论 
# a = int(input("请输入一个年龄："))
# if a > 18:  
#     print ("黄花")
# elif a > 12:
#     print("小黄花")
# elif a > 0:
#     print("小可爱")

"""
for:遍历字符串/元组/字典/数组
遍历即是把所有的值都取出来

"""
#循环字符串
# a = "柠檬树下你和我"
# for i in a:
#     print(i)

#循环元组
# b = ("柠","檬","树")
# for i in b:
#     print(i)

#循环数组
# c = ["柠","檬","树"]
# for i in c:
#     print(i)

#循环字典：元组，数组，字符串的循环取值都是取得元素，字典取得是key值
# d = {"张三":20,"李四":30}
# for i in d:
#     print(i)    #这个i是打印的key值，不是value值
#     print(d[i])   #取出对应的value值，这里的key值是变量

grade = {"张三":80,"李四":90,"王麻子":88,"智障":59}
for i in grade:
    if grade[i] > 60:
        good =[i]
        print(good)
    else:
        bad = [i]
        print(bad)


#grade = {"张三":80,"李四":90,"王麻子":88,"智障":59}，把成绩合格的人分到一个list里，不合格的人分到另一个list里  
# grade = {"张三":80,"李四":90,"王麻子":88,"智障":59}
# good = []
# bad = []
# for i in grade:
#     if grade[i] > 60:
#         good.append(i)
#     else:
#         bad.append(i)
# print(good)
# print(bad)


