import pandas as pd
import matplotlib.pyplot as plt
import os

EXCEL_FILE = "todo_list.xlsx"

# Load or create Excel file
def load_tasks():

# Save tasks to Excel
def save_tasks(df):
    df.to_excel(EXCEL_FILE, index=False)

# Create a new task
def create_task(df):
    task = input("Enter task description: ")
    priority = input("Enter priority (High/Medium/Low): ")
    new_task = pd.DataFrame([[task, priority, "Pending"]], columns=["Task", "Priority", "Status"])
    df = pd.concat([df, new_task], ignore_index=True)
    save_tasks(df)
    print("Task added successfully.")
    return df

# Main app loop
def main():
    df = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add New Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Show Priority Chart")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        #if choice == '1':
            #df = view_tasks(df)
        elif choice == '2':
            df = create_task(df)
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
