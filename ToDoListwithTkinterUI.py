import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.default_fg_color = self['fg']

        self.insert(0, self.placeholder)
        self.bind('<FocusIn>', self._clear_placeholder)
        self.bind('<FocusOut>', self._set_placeholder)
        self._set_placeholder()

    def _clear_placeholder(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self['fg'] = self.default_fg_color

    def _set_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self['fg'] = 'grey'


class ToDoList:
    def __init__(self):
        self.tasks = []

    def view_tasks(self):
        self.read_file()

        if len(self.tasks) == 0:
            return "List is empty"
        else:
            tasks_with_index = [f"{i}: {task}" for i, task in enumerate(self.tasks)]
            return "\n".join(tasks_with_index)

    def add_task(self, task):
        self.read_file()
        now = datetime.now()
        date_time_stamp = now.strftime("%d/%m/%Y %H:%M:%S")
        self.tasks.append(task + " [" + date_time_stamp + "]")
        self.write_file()

    def mark_task_as_completed(self, task_index: int):
        if task_index < len(self.tasks):
            self.tasks[task_index] += " DONE"
            self.write_file()
        else:
            messagebox.showinfo("Error", "Invalid task index")

    def remove_task(self, task_index: int):
        if task_index < len(self.tasks):
            del self.tasks[task_index]
            self.write_file()
        else:
            messagebox.showinfo("Error", "Invalid task index")

    def remove_all_task(self):
        self.tasks = []
        self.write_file()

    def write_file(self):
        with open('tasks.txt', 'w') as f:
            for task in self.tasks:
                f.write(task + '\n')

    def read_file(self):
        with open('tasks.txt', 'r') as file:
            for line in file:
                line = line.strip()
                append = True
                for task in self.tasks:
                    if task == line:
                        append = False
                if append:
                    self.tasks.append(line)


class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ToDo List")

        self.todo_list = ToDoList()

        # self.label = tk.Label(master, text="task index: task [time stamp]")
        # self.label.grid(row=0, column=0, columnspan=3)

        self.text_display = tk.Text(master, height=10, width=50)
        self.text_display.grid(row=1, column=0, columnspan=3)

        self.add_task_entry = PlaceholderEntry(master, placeholder="Enter task")
        self.add_task_entry.grid(row=2, column=0, padx=5, pady=5)

        self.add_task_button = tk.Button(master, text="Add Task", width=16,
                                         bg="lightgreen", command=self.add_task)
        self.add_task_button.grid(row=2, column=1, padx=5, pady=5)

        self.mark_completed_entry = PlaceholderEntry(master, placeholder="Enter task index")
        self.mark_completed_entry.grid(row=3, column=0, padx=5, pady=5)

        self.mark_completed_button = tk.Button(master, text="Mark as Completed", width=16,
                                               bg="lightblue", command=self.mark_as_completed)
        self.mark_completed_button.grid(row=3, column=1, padx=5, pady=5)

        self.remove_task_entry = PlaceholderEntry(master, placeholder="Enter task index")
        self.remove_task_entry.grid(row=4, column=0, padx=5, pady=5)

        self.remove_task_button = tk.Button(master, text="Remove Task", width=16,
                                            bg="red", command=self.remove_task)
        self.remove_task_button.grid(row=4, column=1, padx=5, pady=5)

        self.remove_all_tasks_button = tk.Button(master, text="Empty List",
                                          bg="red", command=self.empty_list)
        self.remove_all_tasks_button.grid(row=5, column=1, padx=5, pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=self.master.destroy)
        self.quit_button.grid(row=5, column=0, columnspan=1, pady=10)

        self.master.minsize(400, 350)

        self.show_tasks()

    def show_tasks(self):
        tasks = self.todo_list.view_tasks()
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, tasks)

    def add_task(self):
        task = self.add_task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.add_task_entry.delete(0, tk.END)
            self.show_tasks()

    def mark_as_completed(self):
        index = self.get_entry_as_int(self.mark_completed_entry)
        self.todo_list.mark_task_as_completed(index)
        self.show_tasks()

    def remove_task(self):
        index = self.get_entry_as_int(self.remove_task_entry)
        self.todo_list.remove_task(index)
        self.show_tasks()

    def empty_list(self):
        self.todo_list.remove_all_task()
        self.show_tasks()

    def get_entry_as_int(self, entry):
        try:
            value = int(entry.get())
            return value
        except ValueError:
            messagebox.showinfo("Error", "Please enter a valid integer")


def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
