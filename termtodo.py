import os
import sys
import json

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
        print(index, item['task'])
        index += 1

    while True:
        try:
            remove_number = int(input("Select number to remove: "))
            if remove_number > index - 1:
                continue
            break
        except Exception:
            pass

    del(tasks[remove_number + 1])
    return tasks
    

def printTasks(tasks):
    col_width = max(len(word) for row in tasks for word in row) + 8 # padding
    for row in tasks:
        print("".join(word.ljust(col_width) for word in row.values()))

def onLoad():
    # load database
    with open('test_data_2.txt', 'r') as f:
        read_data = f.read()
    f.close()
    return json.loads(read_data)


def onClose():
    # save data base
    # TODO
    pass


def main():

    task_list = onLoad()
    
    while True:
        printTasks(task_list)
        print(task_list)
        print('\n')

        user_input = input("> ")
        if user_input == 'q':
            sys.exit(0)
        elif user_input == 'a':
            new_task = getTask()
            task_list.append({'task': new_task.task, 'due': new_task.due})
        elif user_input == 'r':
            task_list = removeTask(task_list)
      
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()