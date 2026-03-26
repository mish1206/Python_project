#Ques-19
import random
import string

length=int(input("Enter password length: "))
ch=string.ascii_letters + string.digits + string.punctuation
password= ''.join(random.choice(ch) for _ in range(length))
print(f"Generated password: {password}")
