task=[]

while True:
    print("TO DO LIST")
    print("Choose an option")
    print("1.View task")
    print("2.add a task")
    print("3.delete a task")
    print("4.exit")

    Choice=int(input("choose an option(1-4):"))

    if Choice==1:
        for i in task:
            print(i)

    elif Choice==2:
        Choicee=input("Enter the task")
        task.append(Choicee)
        print(Choicee+" added!")
    elif Choice==3:
        pass
    elif Choice==4:
        pass
    else:
        pass

