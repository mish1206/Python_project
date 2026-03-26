#Ques-17
s=input("Enter a sentence: ")
count=0
for i in s:
    if i==" " or i==".":
        count+=1
    else:
        continue
print(f"count={count}")
