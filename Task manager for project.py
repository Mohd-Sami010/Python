def display_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    task_description = input("Enter task description: ")
    tasks.append({"description": task_description, "completed": False})
    save_tasks_to_file(tasks)  # Save tasks automatically after adding
    print("Task added successfully.")

def view_tasks(tasks):
    print("\n========== Task List ==========")
    if not tasks:
        print("No tasks to display.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "[ ]" if not task["completed"] else "[X]"
            print(f"{index}. {status} {task['description']}")
    print("================================")

def mark_task_as_completed(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to mark as completed: ")) - 1
        tasks[task_index]["completed"] = True
        save_tasks_to_file(tasks)  # Save tasks after marking as completed
        print(f"Task '{tasks[task_index]['description']}' marked as completed.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the number of the task to delete: ")) - 1
        deleted_task = tasks.pop(task_index)
        save_tasks_to_file(tasks)  # Save tasks after deleting
        print(f"Task '{deleted_task['description']}' deleted.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def save_tasks_to_file(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['description']}|{task['completed']}\n")
    print("Tasks saved to 'tasks.txt' successfully.")

def load_tasks_from_file():
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
            print("Exiting Task Manager. Goodbye!")
            save_tasks_to_file(tasks)  # Save tasks before exiting
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Start the Task Manager
task_manager()