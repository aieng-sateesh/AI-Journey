# Day 23 - To-Do List Manager using OOP

# define task class
class Task:
    def __init__(self, title, description):  # constructor for task
        self.title = title
        self.description = description
        self.status = "Pending"

    def mark_done(self):  # mark task as completed
        self.status = "Done"

    def show_task(self):  # display task info
        print(f'{self.title} - {self.description} | Status: {self.status}')

# define manager class
class ToDoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):  # add new task
        self.tasks.append(task)
        print(f'Task added: {task.title}')

    def show_all_tasks(self):  # show all tasks
        if not self.tasks:
            print('No tasks to show.')
        for task in self.tasks:
            task.show_task()

    def mark_task_done(self, title):  # mark specific task as done
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                print(f'Task marked as done: {title}')
                return
        print('Task not found')

    def delete_task(self, title):  # delete specific task
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f'Task deleted: {title}')
                return
        print('Task not found')

# sample usage
t1 = Task("Buy groceries", "Milk, Bread, Eggs")
t2 = Task("Finish project", "Submit GitHub repo")

todo = ToDoManager()
todo.add_task(t1)
todo.add_task(t2)
todo.show_all_tasks()
todo.mark_task_done("Buy groceries")
todo.delete_task("Finish project")
todo.show_all_tasks()
