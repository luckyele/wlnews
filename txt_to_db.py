'''
1.对文本文件中每一行的内容进行处理
2.保存为数据库文件
3.测试保存是否正确
4.输出新增记录
每天扫更一次，如果数据库中没有，则添加到数据库，并标记为新增。

数据库名称 ahwlmsg

create database ahwlmsg;

数据库表名 daily_msg

CREATE TABLE daily_msg (
   ID INT PRIMARY KEY     NOT NULL,
   URL           CHAR    NOT NULL,
   TITLE         CHAR     NOT NULL,
   CONTENT       CHAR(50),
   FROM_RES      CHAR()
);

数据库表中字段：
id              integer
url             char()
title           char()
content         char
writer          char
clip_img        char
grasp_time      time
publish_time    time       
'''
import sqlite3 
import datetime
import os

def open_table():
    database = "ahwlmsg.db"
    table = "webpages"
    conn = sqlite3.connect(database)
    # print ("\n %s is openned..."%database)
    
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS webpages (  
                    id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    link TEXT,  
                    title TEXT,  
                    content TEXT,  
                    screenshot_path TEXT,  
                    publish_time TEXT  
                    );''')
    # print ("数据表创建成功")
    conn.commit()
    return conn

def close_db(conn):
    conn.close()

def insert(conn):
    cursor = conn.cursor()
    
    content = ""
    screenshot_path = ""
    publish_time = datetime.datetime.now()

    files = get_txtfiles()
    for file in files:
        all_lines = get_lines(file)
        for line in all_lines:
            # print(line)
            if len(line.strip('\n').split('\t')) > 2:
                continue
                #title, link = line.strip('\n').split('\t')
            else:
                title, link = line.strip('\n').split('\t')
            if title != '':
                value = link  
                cursor.execute(f"SELECT * FROM webpages WHERE link = ?", (value,))  
                result = cursor.fetchone()  
                
                # 检查查询结果，如果结果不为空则表示值存在于表中  
                if result:  
                    print(link + " is exists.")
                    continue  
                else:  
                    cursor.execute("insert into webpages (link, title, content, \
                    screenshot_path, publish_time) values (?, ?, ?, ?, ?)",\
                    (link, title, content, screenshot_path, publish_time))
                    conn.commit()
        
def del_all_records(conn):
    print("\n警告：该操作将删除所有记录，请确认(y/n):")
    cursor = conn.cursor()
    if input() == 'y':
        cursor.execute("DELETE FROM webpages")  
        cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'webpages'")
        conn.commit()  

def print_records(conn):
    cursor = conn.cursor()
    records = cursor.execute("select * from webpages")
    for r in records:
        print(r)

def get_lines(filename):
    lines = []
    with open('./txt/' + filename, encoding='utf-8') as f:
        lines = f.readlines()
    # print(lines)
    return lines

def get_txtfiles():
    filenames = []
    for root, dirs, files in os.walk('./txt/'):
        for file in files:
            filenames.append(file)
    # print(filenames)
    return filenames    
            
if __name__ == "__main__":
    c = open_table()
    # del_all_records(c)
    insert(c)
    print_records(c)
    close_db(c)