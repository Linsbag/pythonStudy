# #元组：混合数据(可以存放任意的数据类型):元组只需要掌握取值就行了
# #元组不可修改
# # a = (1,"zhizhang",True,None)

# #取值：根据下标来取：a[下标]，下标从0开始，最后一个下标可以表示为-1

# #获取元组长度/元素个数:len(元组)
# # print(len(a))

# #列表/数组：list（数组的元素内容为任意数据类型）数组学习crud
# #列表长度和内容可以修改
# b = [1,"2",True,(1,2),["zz",1]]
# #数组取值和元组一样，根据下标来取a[下标]
# #获取列表长度/元素个数
# print(len(b))

# #添加元素：append(),添加在末尾
# # b.append("123")

# #修改:中括号内为下标，等号后为修改好的内容
# # b[0]=100

# #删除：两种方法：del:删除下标为0的元素，第二种，调用方法，注意调用方法只能用在数据类型本身remove(需要删除的内容)
# # del b[0]
# # b.remove(Ture)

# #获取数组中元素的个数b.count(值)
# print(b.count(True))

#数组的排序a.sort(),从小到大排序
# a = [11,22,88,66,33]
# # a.sort()
# # print(a)
# #若想要从大到小排序，加一个参数
# a.sort(reverse=True)
# print(a)

#字典 键值对 key-value 一个键值对是一个元素
a = {"username":"zz","age":18}
print(len(a))
"""
key值可以是数字,但是一般key值用字符串表示，value是任意类型
"""
#取值 通过key值来取 
print(a["username"])
print(a.get("username"))
"""
前者取值元素不存在的时候，下标取值会报错，后者元素不存在时报空类型None
"""

#增加  两种方法  通过下标增加  调用方法
a["sex"] = "女"
print(a)
#若key值存在的时候，那就不是增加了，是修改

a.update({"sex":"男"})
print(a)

#删除
del a["sex"]
print(a)

#清除所有
a.clear()
print(a)

