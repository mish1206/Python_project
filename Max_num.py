#Ques-4
n=3
l=list()
for i in range(n):
    num=int(input(f"Enter {i} element: "))
    l.append(num)
maxi=l[0]
for i in range(n):
    if maxi<l[i]:
        maxi=l[i]

print(f"Maximum: {maxi}")
