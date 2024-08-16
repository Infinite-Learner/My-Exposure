#!/usr/bin/env python
# coding: utf-8

# In[13]:


#import mysql.connector
'''def con(host_in="",user_in="",password_in=""):
    mycon = mysql.connector.connect(host=host_in,user=user_in,password=password_in)
    print("Connected Successfully")
    cur = mycon.cursor()
    return cur'''
import sqlite3
def table():
    inp = int(input('''***Table Manupulation***
                    1.CREATE
                    2.INSERT
                    3.DELETE
                    4.UPDATE'''))
    if(inp == 1):
        create();
        
        
def create():
	stmt = ""
	T_Name = input("Enter Table Name : ")
	T_Col = int(input("Enter No of Columns : "))
	qrp=['Name','Data_Type',';.']
	for i in range(0,T_Col):
		qry = input("Enter Field "+i+"Name : ")
'''def init(ch):
    if(ch==1):
        stmt = input("Enter DB_Name : ")
        cur.execute(f"USE DATABASE {stmt}")
        table();
    elif(ch==2):
        stmt = input("Enter DB_Name : ")
        cur.execute(f"CREATE DATABASE {stmt}")
        cur.execute(f"USE {stmt}")
        table();
def main():
    ch = int(input(''''''***Select your choice***
    1.Existing Database
    2.New DataBase
    Enter Your Choice : 
    init(ch);'''
print("Welcome to DB_Controller")
cur=sqlite3.connect("DemoDb.db").cursor()
table()
host_in = input("Enter Host name : ")
#port = int(input("Enter Port Number : "))
user_in = input("Enter username : ")
password_in = input("Password : ")
#cur = con(host_in,user_in,password_in)
main()


# In[ ]:


#main()


# In[ ]:
'''

ddl = ['CREATE','ALTER','DROP']
dml = ['INSERT','DELETE','UPDATE','SELECT']
con = ['WHERE']
'''
