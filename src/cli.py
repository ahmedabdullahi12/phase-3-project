# src/cli.py

from helpers import exit_program, create_task, delete_task, show_all_tasks, show_task

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            show_all_tasks()
        elif choice == "4":
            show_task()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a new task")
    print("2. Delete a task")
    print("3. Show all tasks")
    print("4. Show a specific task")

if __name__ == "__main__":
    main()
