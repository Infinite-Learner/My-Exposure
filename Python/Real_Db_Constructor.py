# !/usr/bin/env python
# coding: utf-8
from dataclasses import field

# In[13]:


import mysql.connector

cur = ""


def connection(host_in="", user_in="", password_in=""):
    cnx={
       "host":host_in,
        "user":user_in,
        "password":password_in
    }
    con = mysql.connector.connect(**cnx)
    return con

def create(cur):
    qr = f"CREATE TABLE"
    fields_count = int(input("Enter No of Fields : "))
    Field_Attributes={"Data_type":"",
                                    "Length":"",
                                    "PRIMARY":False,
                                    "UNIQUE":False,
                                    "FOREIGN":False,
                                    "Auto-Increment":False,
                                    "NOT NULL":False,
                                   }
    for i in range(0,fields_count):
        field_name = input("Field_Name : ")
        for j in Field_Attributes:
            Field_Attributes[j] = input(f"Enter {field_name}-->{j} : ")
        print(*Field_Attributes)
def table(cur):
    inp = int(input('''***Table Manupulation***
                    1.CREATE
                    2.INSERT
                    3.DELETE
                    4.UPDATE
                    Enter need : '''))
    if(inp == 1):
       create(cur);


def init(ch, cur):
    if (ch == 1):
        cur.execute("show databases")
        print(cur.fetchall())
        stmt = input("Enter DB_Name : ")
        cur.execute(f"USE {stmt}")
        table(cur);
    elif (ch == 2):
        stmt = input("Enter DB_Name : ")
        cur.execute(f"CREATE DATABASE {stmt}")
        cur.execute(f"USE {stmt}")
        table(cur);


def main(cur):
    ch = int(input('''***Select your choice***
    1.Existing Database
    2.New DataBase
    Enter Your Choice : '''))
    init(ch, cur);


print("Welcome to DB_Controller")
host_in = input("Enter Host name : ")
# port = int(input("Enter Port Number : "))
user_in = input("Enter username : ")
password_in = input("Password : ")
cur = connection(host_in, user_in, password_in)
main(cur.cursor())

# In[ ]:


# In[ ]:

#
# ddl = ['CREATE','ALTER','DROP']
# dml = ['INSERT','DELETE','UPDATE','SELECT']
# con = ['WHERE']
