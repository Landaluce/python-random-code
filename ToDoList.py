#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ToDoList:
    def __init__(self):
        self.tasks = []

    def view_tasks(self):
        print()
        if len(self.tasks) == 0:
            print("List is empty")
        for i in range(0, len(self.tasks)):
            print(str(i) + ":", self.tasks[i])
        pass

    def add_task(self, task):
        self.tasks.append(task)
        pass

    def mark_task_as_completed(self, task_index: int):
        self.tasks[task_index] += " DONE"
        pass

    def remove_task(self, task_index: int):
        del self.tasks[task_index]
        pass


def main():
    todo_list = ToDoList()

    while True:
        print("\nToDo List Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo_list.view_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "3":
            index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_task_as_completed(index)
        elif choice == "4":
            index = int(input("Enter the index of the task to remove: "))
            todo_list.remove_task(index)
        elif choice == "5":
            print("Exiting ToDo List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
