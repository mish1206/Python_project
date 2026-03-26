#Ques-9
ch=int(input("Do you want to enter a string or number? [1/2]"))

if ch==1:
    s=input("Enter your string: ")
    rev=s[::-1]
    if s==rev:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")
                
elif ch==2:
    num=int(input("Enter a number: "))
    ori_num=num
    rev_num=0
    while num!=0:
        r=num%10
        rev_num=rev_num*10+r
        num=num//10
    if ori_num==rev_num:
        print(f"{ori_num} is a palindrome")
    else:
        print(f"{ori_num} is not a palindrome")
else:
    exit()
    
