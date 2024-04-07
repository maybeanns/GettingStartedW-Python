
tasks_list = []

while True:

    print("-------------------------------")
    print("-    Welcome to your List     -")
    print("-    1. View your tasks       -")
    print("-    2. Add a new task        -")
    print("-    3. Delete a task         -")
    print("-    4. Close the App         -")
    print("-------------------------------")
    
    # for error handling potential errors in user inputs
    try:
        choice = int(input("Enter an option: "))
    except ValueError:
        print("Invalid Input! Please try again")
        continue
    
    # using match-case conditional block
    match(choice):
        case 2:
            task_new = input("Please enter your new task:\n")
            tasks_list.append(task_new)
            print("Your task has been added")
        case 1:
            # print(tasks_list)  #we can do this but better is below one
            if tasks_list:
                for index, tasks in enumerate(tasks_list, start=1):
                    print(f"{index}.{tasks}") #using fstring to display index and string at the same time
            else:
                print("Your task list is empty")        
            
        case 3:
            task_del = input("Enter the task you want to delete:\n")
            # if task_del in tasks_list:
            #     tasks_list.remove(task_del)
            #     print("Task has been deleted.")
            # else:
            #     print("Task not found.")    
            if task_del.lower() in (task.lower() for task in tasks_list):
                tasks_list = [task for task in tasks_list if task.lower() != task_del.lower()]
                print("Task has been deleted")
            else:
                print("Task not found!")    
        case 4:
            print("Closing App. Bye!")
            break
        case _:
            print("Error")