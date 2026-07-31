#Ques-8
num=int(input("Enter a number: "))
isPrime=1
if num<=1:
    isPrime=0
else:
    for i in range(2,num//2):
        if num%i==0:
            isPrime=0
            break
if isPrime==True:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
