import pickle
import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Not Completed"
                print(f"{index + 1}. {task.description} - {status}")

    def mark_task_as_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.tasks, f)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                self.tasks = pickle.load(f)

def main():
    todo_list = ToDoList()

    filename = "todo_list.pkl"

    # Load tasks from file if it exists
    todo_list.load_from_file(filename)

    while True:
        print("\n==== To-Do List ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Save and Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to mark as done: ")) - 1
            todo_list.mark_task_as_done(index)
        elif choice == '4':
            index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.save_to_file(filename)
            print("To-Do List saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
