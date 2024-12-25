#SUJOY , 2024-12-25 , 12:00 , B.TECH CSE , 2st year , DR.B.C.ROY ENGINEERING COLLEGE , DURGAPUR , WEST BENGAL , INDIA
# To-Do List Manager
# This program allows the user to manage a to-do list by viewing, adding, and removing tasks.
# The tasks are stored in a list, and the user interacts with the program via a text menu.
# The user can view the tasks, add a new task, remove a task, or exit the program.
# The program displays a text menu with options for the user to choose from.
# The user's choice is read as input, and the corresponding action is performed.
# The tasks are stored in a list, and the program provides options to view, add, and remove tasks.

def display_menu():
    print("To-Do List Manager")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks: 
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            add_task(tasks)
        elif choice == 3:
            remove_task(tasks)
        elif choice == 4:
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
