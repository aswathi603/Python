import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self):
        task_name = input("Enter task name: ")
        print("Select deadline (in days from today):")
        print("1. 7 days")
        print("2. 10 days")
        print("3. Custom number of days")
        choice = input("Enter choice (1-3): ")
        
        if choice == '1':
            days = 7
        elif choice == '2':
            days = 10
        elif choice == '3':
            try:
                days = int(input("Enter number of days for deadline: "))
            except ValueError:
                print("Invalid input. Using default 7 days.")
                days = 7
        else:
            print("Invalid choice. Using default 7 days.")
            days = 7
            
        start_date = datetime.date.today()
        deadline = start_date + datetime.timedelta(days=days)
        
        self.tasks.append({
            'name': task_name,
            'start_date': start_date,
            'deadline': deadline,
            'completed': False
        })
        print("Task added successfully!")
    
    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list!")
            return
            
        print("\n=== TODO LIST ===")
        today = datetime.date.today()
        for i, task in enumerate(self.tasks, 1):
            days_left = (task['deadline'] - today).days
            status = "✓" if task['completed'] else "✗"
            
            # Color based on days left
            if days_left <= 2:
                color = Fore.RED
            elif days_left <= 5:
                color = Fore.YELLOW
            else:
                color = Fore.GREEN
                
            print(f"{i}. {task['name']} | Days left: {color}{days_left}{Style.RESET_ALL} | Start: {task['start_date']} | Deadline: {task['deadline']} | Status: {status}")
    
    def mark_complete(self):
        self.display_tasks()
        if not self.tasks:
            return
            
        try:
            task_num = int(input("Enter task number to mark complete: ")) - 1
            if 0 <= task_num < len(self.tasks):
                self.tasks[task_num]['completed'] = True
                print("Task marked as complete!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def run(self):
        while True:
            print("\nMenu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task Complete")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.display_tasks()
            elif choice == '3':
                self.mark_complete()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo = TodoList()
    todo.run()
