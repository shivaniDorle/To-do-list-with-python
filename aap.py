def task():
    tasks = []  # empty list 
    print("___WELCOME TO THE MANAGEMENT APP___")

    total_task = int(input("Enter how many tasks you want to add = "))  # 5
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")  # enter task 3
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int(input("Enter\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit/Stop\n"))
        
        if operation == 1:  # Add a task
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")
        
        elif operation == 2:  # Update a task
            update_val = input("Enter the task name you want to update = ")
            if update_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(update_val)  # find the index of the task to update
                tasks[ind] = up 
                print(f"Task '{update_val}' has been updated to '{up}'.")
            else:
                print(f"Task '{update_val}' not found.")
        
        elif operation == 3:  # Delete a task
            delete_val = input("Enter the task name you want to delete = ")
            if delete_val in tasks:
                tasks.remove(delete_val)
                print(f"Task '{delete_val}' has been successfully deleted.")
            else:
                print(f"Task '{delete_val}' not found.")
        
        elif operation == 4:  # View tasks
            print(f"Current tasks are:\n{tasks}")
        
        elif operation == 5:  # Exit the app
            print("Exiting the app. Goodbye!")
            break
        
        else:
            print("Invalid operation. Please choose a valid option.")

# Run the task management app
task()
