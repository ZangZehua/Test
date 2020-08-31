import csv
import pandas
import pymysql

conn = pymysql.connect('localhost', 'root', '971109', 'myDataBase')
cursor = conn.cursor()
print("MySQL connected successfully!")

with open("d:\\文件\\test.csv", "r") as openfile:
    # 读取csv文件，返回的是迭代类型

    read = csv.reader(openfile)
    for values in read:
        print(values)
        print(values[1], end=" ")
        print(type(values[1]))
        # cursor.execute("insert into myTable values(%s, %d, %d, %d)", values)


print("done!")
