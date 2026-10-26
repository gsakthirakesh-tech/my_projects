import tasks

def show_menu():
    print()
    print("------ TODO APPLICATION ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Update Task")
    print("5. Mark Task as Completed")
    print("6. Delete Task")
    print("7. Exit")

def main():
    while True:
        show_menu()
        
        choice_input = input("Enter your choice: ")
        
        try:
            choice = int(choice_input)
        except:
            print("Invalid input! Please type a number from 1 to 7")
            continue
        
        if choice == 1:
            tasks.add_task()
        elif choice == 2:
            tasks.view_tasks()
        elif choice == 3:
            tasks.search_task()
        elif choice == 4:
            tasks.update_task()
        elif choice == 5:
            tasks.complete_task()
        elif choice == 6:
            tasks.delete_task()
        elif choice == 7:
            print("\nExiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a number between 1 and 7.")

if __name__ == "__main__":
    main()