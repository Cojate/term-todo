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
    task_due_request = input("Due: ")
    return Task(task_name_request, task_due_request)

def printTask():
    pass

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
    task_list = []
    
    while True:
        # clear terminal print task list
        os.system('cls' if os.name == 'nt' else 'clear')
        print(task_list)
  

        print("task \t due")
        for item in task_list:
            print(item.task, "\t", item.due)

        task_list.append(getTask())

        if task_list[-1].task == 'q' or task_list[-1].due == 'q':
            sys.exit(0)
        

if __name__ == "__main__":
    main()