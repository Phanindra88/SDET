#program to generate student result


students=[]
pass_count=0
fail_count=0


n=int(input("enter how many students:"))
for i in range(n):
    marks={}
    marks["rollno"]=input("enter roll number:")
    marks["name"]=input("enter student name:")
    marks["Tel"]=int(input("enter marks obtained in Telugu:"))
    marks["Eng"]=int(input("enter marks obtained in English:"))
    marks["Mat"]=int(input("enter marks obtained in Maths:"))
    marks["Sci"]=int(input("enter marks obtained in Science:"))
    marks["Soc"]=int(input("enter marks obtained in Social:"))
    marks["tot"] = marks["Tel"] + marks["Eng"] + marks["Mat"] + marks["Sci"] + marks["Soc"]
    marks["avg"] = marks["tot"] / 5
    if marks["Tel"]>=35 and marks["Eng"]>=35 and marks["Mat"]>=35 and marks["Soc"]>=35 and marks["Sci"]>=35:
        marks["result"]="pass"
        pass_count+=1
    else:
        marks["result"]="fail"

        fail_count+=1
    students.append(marks)

      

print("Student Results : ")
print("-------------------------------------------------------------")
print("RollNo Name     Tel  Eng  Mat  Sci  Soc  Total Average  Result")
print("-------------------------------------------------------------")

for stud in students:
    print(" %s  %8
          s   %3d  %3d  %3d  %3d  %3d  %3d  %5.2f    %s"%(stud["rollno"],stud["name"],stud["Tel"],stud["Eng"],stud["Mat"],stud["Sci"],stud["Soc"],stud["tot"],stud["avg"],stud["result"]))

print("-------------------------------------------------------------")
print("No. of Students Attended : ",n)
print("No. of Students Passed : ",pass_count)
print("No. of Students Failed : ",fail_count)
print("-------------------------------------------------------------")
      

