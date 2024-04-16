import time

print("21st Century To-DO List Application")


def display_menu():
    menus = ["Add Task", "View Tasks", "Mark as Done", "Exit"]
    print("Main Menu")
    num = 1
    for menu in menus:
        print(num, ":", menu)
        num += 1


def add_task():
    task_title = input("Enter task title: ")
    if task_title:
        task_status = "pending"
        tasks[task_title] = task_status
    else:
        print("Enter a valid task")
        add_task()


def view_tasks():
    print("Your Tasks and Status Pair(s):")
    for i in tasks:
        print(f"{i}:\t{tasks[i]}")


def mark_done():
    print("Your Tasks and Status Pair(s):")
    for i in tasks:
        print(f"{i}:\t{tasks[i]}")
    task_to_mark_done = input("Choose task to mark as done: ")
    if task_to_mark_done == i:
        tasks[i] = 'Done'
    else:
        print("wtf")



def exit_app():
    print("Exiting App and Deleting Tasks...")
    time.sleep(3)

try:
    running = True
    while running:
        display_menu()
        choice = int(input("Choose a number from the menu: "))
        tasks = {
            "Wake Up": "done",
        }
        if choice == 1:
            on = True
            while on:
                add_task()
                view_tasks()
                add_more = input("Add another Task?(Y/N)").lower()
                if add_more == "y":
                    pass
                elif add_more == "n":
                    print("Tasks added Successfully")
                    view_tasks()
                    on = False
                    print("Going to main menu")
                    time.sleep(3)
                else:
                    pass
        elif choice == 2:
            view_tasks()
            print("Going to Main menu")
            time.sleep(3)
        elif choice == 3:
            mark_done()
            view_tasks()
            print("Off to HOMEPAGE")
            time.sleep(3)
        elif choice == 4:
            exit_app()
            running = False
except TypeError:
    print("Invalid Type")
except KeyboardInterrupt:
    print("Exiting")