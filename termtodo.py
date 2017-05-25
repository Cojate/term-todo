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
    task_list = [["task", "due"]]
    
    while True:
        printTasks(task_list)
        print('\n')

        new_task = getTask()
        task_list.append([new_task.task, new_task.due])
        
        os.system('cls' if os.name == 'nt' else 'clear')
        

if __name__ == "__main__":
    main()