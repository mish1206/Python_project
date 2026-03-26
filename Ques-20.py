#Ques-20
def todo():
    tasks=[]
    while True:
        print("\n1.Add 2. View 3. Delete 4. Exit")
        choice=input("Choose: ")
        if choice=='1':
            task=input("Enter task: ")
            tasks.append(task)
        elif choice == '2':
            for i, t in enumerate(tasks):
                print(i, t)
        elif choice=='3':
            i=int(input("Enter index to delete: "))
            if 0<i< len(tasks):
                tasks.pop(i)
        elif choice=='4':
             break

todo()
