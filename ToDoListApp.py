
    # Create CLI, display a welcoming message and menu. 

tasks = []

def add_task(new_task):
    global tasks
    task = {
        'task': new_task,
        'complete': False
    }
    if not task in tasks:
        tasks.append(task)
        print(f"\n Task-{task} added to your to-do list.")
    else:
        print(f"\n Task-{new_task} is already on your to-do list ")
         
def view_tasks():
     try:
        for index, task in enumerate(tasks):
            print(f"\n {index + 1}. {task['task']}/ {'Complete'if task['complete'] else 'Incomplete'}")
            if not tasks:
                 return
     except FileNotFoundError:
          print(" \n Tasks are empty. Please add something to view tasks.") 

def task_complete(index):
    try:
        if index > 0 and index <= len(tasks):
            tasks[index]['complete'] = True
        else:
            print("\n Invalid index.")
    except IndexError:
        print("\n Unexpected Index error....")

def task_to_delete():
    view_tasks()
    index_to_delete = input("\n Please enter the number of the item you wish to delete: ")
    try:
        for index in index_to_delete:
            tasks.remove(index)
    except IndexError:
        print("\n Index error! Please try again and select only the number for the item you wish to delete: ")

def display_menu():
    while True:
        print(" \n Welcome to the To-Do List App!")
        print(" \n Menu: ")
        print(" \n 1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Quit")
        try:
            choice = int(input(" \n Please enter the number for the option you would like: "))
            if choice == 1:
                new_task = input(" \n Please enter the task you would like to add: ").lower()
                add_task(new_task)
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                 task_complete()
            elif choice == 4:
                 task_to_delete()
            elif choice == 5:
                break
        except ValueError:
             print(" \n Invalid input. Please enter a number between 1 and 5:  ")

display_menu()
