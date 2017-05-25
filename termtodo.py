import os
import sys

class Task:
    """A class to store information about a task"""
    def __init__(self, task, due):
        self.task = task
        self.due = due

def getTask():
    # Ask user for new task
    task_name_request = input("Task: ")
    if task_name_request == "q":
        sys.exit(0)
    task_due_request = input("Due: ")
    if task_due_request == 'q':
        sys.exit(0)

    return Task(task_name_request, task_due_request)

def removeTask(tasks):
    index = 0
    for item in tasks[1:]:
        print(index, item[0])
        index += 1

    while True:
        try:
            remove_number = int(input("Select number to remove: "))
            if remove_number > index - 1:
                continue
            break
        except:
            pass

    del(tasks[remove_number + 1])
    return tasks
    

def printTasks(tasks):
    col_width = max(len(word) for row in tasks for word in row) + 8 # padding
    for row in tasks:
        print("".join(word.ljust(col_width) for word in row))

def onLoad():
    # load database
    # TODO
    pass

def onClose():
    # save data base
    # TODO
    pass


def main():
    # Ask user for new task
    task_list = [["TASK", "DUE"]]
    
    while True:
        printTasks(task_list)
        print(task_list)
        print('\n')

        user_input = input(">")
        if user_input == 'q':
            sys.exit(0)
        elif user_input == 'a':
            new_task = getTask()
            task_list.append([new_task.task, new_task.due])
        elif user_input == 'r':
            task_list = removeTask(task_list)
                
        
        os.system('cls' if os.name == 'nt' else 'clear')
        

if __name__ == "__main__":
    main()