#Ques-12
def add(a,b):
    c=a+b
    print(f"Sum: {c}")

def sub(a,b):
    c=a-b
    print(f"Sub: {c}")

def prod(a,b):
    c=a*b
    print(f"Prod: {c}")

def div(a,b):
    c=float(a/b)
    print(f"Div: {c}")

a=int(input("Enter number A:"))
b=int(input("Enter number B:"))

while True:
    ch=int(input("1.Addition \n2.Substraction \n3.Multiplication \n4.Division \n5.Exit \nEnter your choice: "))
    if ch==1:
        add(a,b)
    elif ch==2:
        sub(a,b)
    elif ch==3:
        prod(a,b)
    elif ch==4:
        div(a,b)
    else:
        exit()
