#导入pymysql
import pymysql
#封装查询方法
def query(sql):  #这个方法的作用就是我要传入这样的一个sql语句，让它得到对应的结果
    #1、连接MySQL数据库
    db = pymysql.connect(host = "118.24.105.78",user="root",password = "1qaz!QAZ123***123",db = "ljtestdb")  #这个步骤就相当于navicat新建连接并实现打开数据库的操作
    #2、获取对应的查询窗口：游标
    cur = db.cursor()     #就相当于navicat打开查询-新建查询窗口
    #3、执行查询sql语句
    cur.execute(sql)      #就相当于在navicat查询窗口里边写查询语句并执行
    #4、获取所有的结果
    res = cur.fetchall()    #就相当于所有的查询结果放到了res变量里边
    #5、关闭数据库连接
    db.close()
    return res


#测试query方法，即调用它
#if __name__ == "__main__":用在调试代码的时候
if __name__ == "__main__":
    sql = "select * from t_user where id = 248"
    r = query(sql)
    print(r)
