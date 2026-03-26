#Ques-16
stud_rec=dict()
n=int(input("Enter the no. of Records: "))
for i in range(n):
    name=input("Enter name: ")
    marks=int(input("Enter marks: "))
    stud_rec[name]=marks

print("Student Records: ")
for k,v in stud_rec.items():
    print(f"{k} : {v}")
