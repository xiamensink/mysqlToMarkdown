import pymysql
import os

host = "localhost"  # 数据库地址
user = "root"  # 用户名
password = ""  # 密码
database = "iwarehouse"  # 数据库名称

conn = pymysql.connect(host=host, user=user, password=password, database=database, charset="utf8")  # 数据库连接
cursor = conn.cursor()


def createTxt(name, data):
    path = "table_structure"
    if not os.path.exists(path):  ##不存在目录则创建
        os.mkdir(path)

    name = path + "\\" + name
    if not os.path.exists(name):  # 不存在就创建txt
        with open(name, "w") as f:
            f.write(data)

    else:  # 存在就删除文件再创建txt
        os.remove(name)
        with open(name, "w") as f:
            f.write(data)


def creatByTableName(tableName):
    sql = "SHOW  full fields from  " + tableName  # 搜索表结构的sql
    try:
        cursor.execute(sql)  # 执行数据库语句
    except Exception as e:
        print("执行数据库查询语句时发生错误:")
        print(e)
        return 0

    result = cursor.fetchall()
    data = "- " + tableName + "\n\n|字段名|  格式 | 备注 |\n| :------------: | :------------: | :------------: |\n"  # 表头
    for line in result:
        newLine = "|" + line[0] + "|" + line[1] + "|" + line[8] + "|\n"  # 表结构
        data = data + newLine
    createTxt(tableName, data)


def getAllTable(DbName):
    sql = "select table_name from information_schema.tables where table_schema= %s"  # 搜索表结构的sql
    try:
        cursor.execute(sql, DbName)  # 执行数据库语句
        return cursor.fetchall()
    except Exception as e:
        print("执行数据库查询语句时发生错误:")
        print(e)


while 1:
    tableName = input("请输入表名\n如果想转换所有表,请输入all\n退出请输入0:\n")
    if tableName.upper() == "ALL":
        result = getAllTable(database)
        for table in result:
            creatByTableName(table[0])
    elif tableName.upper() == "0":
        break
    else:
        creatByTableName(tableName)
cursor.close()
conn.close()
