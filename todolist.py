task=[]

while True:
    print("TO DO LIST")
    print("Choose an option")
    print("1.View task")
    print("2.add a task")
    print("3.delete a task")
    print("4.exit")

    Choice=int(input("choose an option(1-4): "))

    if Choice==1:
        for i in task:
            print(i)

    elif Choice==2:
        Choicee=input("Enter the task ")
        task.append(Choicee)
        print(Choicee+" added!")
    elif Choice==3:
        discard=input("Enter the task to be removed: ")
        task.remove(discard)
        print(discard+" removed!")
    elif Choice==4:
        print("Exiting the todo list")
        break
    else:
        print("invalid choice, please choose between 1,2,3 and 4: ")




