def show_menu():
    print("\n===== MY TASK LIST =====")
    print("1. Add a task")
    print("2. Show tasks")
    print("3. Remove a task")
    print("4. Quit")


tasks = []

while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Write your task: ").strip()

        if task:
            tasks.append(task)
            print("Task saved!")
        else:
            print("Please enter a task.")

    elif choice == "2":
        if not tasks:
            print("Your task list is empty.")
        else:
            print("\nSaved Tasks:")

            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        if not tasks:
            print("There are no tasks to remove.")
            continue

        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")

        try:
            number = int(input("Which task do you want to remove? "))

            if 1 <= number <= len(tasks):
                removed_task = tasks.pop(number - 1)
                print("Removed:", removed_task)
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a number.")

    elif choice == "4":
        print("Thanks for using the To-Do Manager!")
        break

    else:
        print("Please choose an option from 1 to 4.")
