# Task Manager Application

def display_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    # Add a new task to the list
    task_description = input("\nEnter task description: ")
    tasks.append({"description": task_description, "completed": False})
    
    # Save tasks automatically after adding
    save_tasks_to_file(tasks)
    print("Task added successfully.")

    # Ask user to press Enter
    input("\nPress Enter to continue...")

def view_tasks(tasks,x=True):
    # Display the list of tasks
    print("\n========== Task List ==========")
    
    if not tasks:
        print("No tasks to display.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "[ ]" if not task["completed"] else "[X]"
            print(f"{index}. {status} {task['description']}")
    
    print("================================")

    # Ask user to press Enter
    if x:
    	input("Press Enter to continue...")

def mark_task_as_completed(tasks):
    # Mark a task as completed
    view_tasks(tasks,False)
    
    try:
        task_index = int(input("\nEnter the number of the task to mark as completed: ")) - 1
        tasks[task_index]["completed"] = True
        
        # Save tasks after marking as completed
        save_tasks_to_file(tasks)
        print(f"\nTask '{tasks[task_index]['description']}' marked as completed.")
        
        # Ask user to press Enter
        input("\nPress Enter to continue...")
    except (ValueError, IndexError):
        print("\nInvalid task number.")

def delete_task(tasks):
    # Delete a task from the list
    view_tasks(tasks,False)
    
    try:
        task_index = int(input("\nEnter the number of the task to delete: ")) - 1
        deleted_task = tasks.pop(task_index)
        
        # Save tasks after deleting
        save_tasks_to_file(tasks)
        print(f"\nTask '{deleted_task['description']}' deleted.")
        
        # Ask user to press Enter
        input("\nPress Enter to continue...")
    except (ValueError, IndexError):
        print("\nInvalid task number.")

def save_tasks_to_file(tasks):
    # Save tasks to a file
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['description']}|{task['completed']}\n")
    
   # print("\nTasks saved to 'tasks.txt' successfully.")

def load_tasks_from_file():
    # Load tasks from a file
    tasks = []
    
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                description, completed_str = line.strip().split("|")
                completed = completed_str.lower() == 'true'
                tasks.append({"description": description, "completed": completed})
    except FileNotFoundError:
        pass  # Ignore if 'tasks.txt' is not found
    
    return tasks

def task_manager():
    # Main function for the Task Manager
    tasks = load_tasks_from_file()  # Load tasks before starting
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_as_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nExiting Task Manager. Goodbye :)")
            
            # Save tasks before exiting
            save_tasks_to_file(tasks)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    task_manager()