# Connecting to SQLite database

import sqlite3

conn_obj = sqlite3.connect("apec.db")
print("Established Connection with the database")

conn_obj.close()
print("Closed Connection with the database")

-------------------------------------------------
#creating a new table in sqlite
import sqlite3
conn_obj = sqlite3.connect("apec.db")
cur_obj = conn_obj.cursor()

sql = """ CREATE TABLE EMPLOYEE(
 EMP_ID NUMERIC(3),
 EMP_NAME VARCHAR(10),
 SALARY NUMERIC(7,2),
 DEPT_ID NUMERIC(2)) """
cur_obj.execute(sql)
print("Table Created Successfully")

cur_obj.close()
conn_obj.close()

------------------------------------------------
#inserting records into the table

import sqlite3
conn_obj=sqlite3.connect("apec.db")
cur_obj=conn_obj.cursor()


cur_obj.execute("INSERT INTO EMPLOYEE VALUES(101,'A SURESH',230000,10)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(102,'B SURESH',240000,20)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(103,'C SURESH',309999,30)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(104,'D SURESH',390000,10)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(105,'E SURESH',875000,20)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(106,'D SURESH',750000,30)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(107,'E SURESH',550000,10)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(108,'F SURESH',900000,20)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(109,'G SURESH',400000,30)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(110,'F SURESH',500000,10)")
cur_obj.execute("COMMIT")
print("Record Inserte Successfully")
print("Record After Insertion:")
for record in cur_obj:
    print(record)


cur_obj.close()
conn_obj.close()

----------------------------------------------------------

