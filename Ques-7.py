#Ques-7
n=int(input("Enter the number of terms: "))
a=0
b=1
next_n=0
print(f"Fibonacci series upto {n} terms: ")
for i in range(1,n):
    if i==1:
        print(a)
    if i==2:
        print(b)
    next_n=a+b
    a=b
    b=next_n
    print(next_n)
