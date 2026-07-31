#Ques-18
with open("text.txt","w") as f:
    f.write("Hello World! \n")

with open("text.txt","r") as f:
    content=f.read()
    print(content)
