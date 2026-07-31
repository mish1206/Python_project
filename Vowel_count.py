#Ques-11
s=input("Enter a sentence: ")
count=0
for i in s:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        count+=1
    else:
        continue
print(f"count={count}")
