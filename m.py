a = "today is sunny"
b = "good day"
#字符串拼接（两种方法:加法直接拼接；使用format方法）
# c = a+b
# print(c)
# print("today is sunny{}".format("good day"))

#字符串方法之find()方法：匹配字符串，匹配成功返回第一个字符串下标,否则返回-1
# index = a.find("day")
# print(index)

#字符串方法之count()方法：统计字符在字符串中出现的次数
# count = a.count("n")
# print(count)

#字符串方法之replace("老字符","新字符")方法
# d = a.replace("sunny","runy")
# print(d)

#字符串方法之len()：获取字符串长度(小心，这里不是点方法了)
lenth = len(a)
print(lenth)