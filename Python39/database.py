import cx_Oracle
conn_obj = cx_Oracle.connect("hr","manager","localhost:1521/xe")
cur_obj = conn_obj.cursor()

cur_obj.execute("INSERT INTO EMPLOYEE VALUES(104,'GANESH',30000,10)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(105,'RAJESH',32000,20)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(106,'RAKESH',33000,30)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(107,'NARESH',34000,10)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(108,'SATISH',35000,20)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(109,'PRAKASH',36000,30)")
cur_obj.execute("INSERT INTO EMPLOYEE VALUES(110,'SUBHASH',37000,10)")
cur_obj.execute("commit")
print("Records Inserted Successfully")

cur_obj.close()
conn_obj.close()
