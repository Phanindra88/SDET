s1={10,20,30,40,50}
print(s1)
s1.add(60)
print(s1)
s1.add("python")
print(s1)
s1.add((10,20,30))
print(s1)
#s1.add([10,20,30])
s1={10,20,30,40,50,60,70}
print(s1)
print(s1.pop())
print(s1)
print(s1.pop())
print(s1)
s1.remove(30)
print(s1)


A={1,2,3,4,5}
B={3,4,5,6,7}
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))


A={1,2,3,4,5}
B={1,3,5}
C={2,4,6}
print(A.issuperset(B))
print(A.issuperset(C))
print(B.issubset(A))
print(C.issubset(A))



A={1,2,3,4,5}
B={1,3,5}
C={2,4,6}
print(A.isdisjoint(B))
print(A.isdisjoint(C))
print(B.isdisjoint(C))


d1 = dict()
d2 = {}
print(d1)
print(d2)
print(type(d1))
print(type(d2))




emp={"emp_id":101,"emp_name":"suresh","salary":25000.00}
marks={"tel":95,"mat":100,"soc":93,"eng":94}
print(emp)
print(marks)


marks={"tel":95,"mat":100,"soc":93,"eng":94,"Tel":99}
print(marks)


student = {"rollno":101,"name":"Suresh","class":"IX","marks":{"Tel":95,"Mat":100,"Soc":93,"Sci":97,"Eng":93}}
print(student)


marks = {"Tel":95,"Mat":100,"Soc":93,"Sci":97,"Eng":93}
print(marks)
# print("Marks obtained in Telugu : ",marks[0])
print("Marks obtained in Telugu : ",marks["Tel"])


              
                    
H
       
