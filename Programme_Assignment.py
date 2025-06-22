import pandas as pd
import matplotlib.pyplot as plt
import os

EXCEL_FILE = "todo_list.xlsx"

# Load or create Excel file
def load_tasks():
    if os.path.exists(EXCEL_FILE):
        return pd.read_excel(EXCEL_FILE)
    else:
        return pd.DataFrame(columns=["Task", "Priority", "Status"])

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

# Read (view) all tasks
def view_tasks(df):
    if df.empty:
        print("No tasks found.")
    else:
        print("\nTo-Do List:")
        print(df.to_string(index=True))
    return df

# Update a task
def update_task(df):
    view_tasks(df)
    try:
        index = int(input("Enter the index of the task to update: "))
        if 0 <= index < len(df):
            print("1. Description")
            print("2. Priority")
            print("3. Status")
            print("4. All")
            item = int(input("Enter which part you'd like to update: "))
            if item == 1:
                df.at[index, "Task"] = input("New description: ")
            elif item == 2:
                df.at[index, "Priority"] = input("New priority: ")
            elif item == 3:
                df.at[index, "Status"] = input("New status (Pending/Done): ")
            elif item == 4:
                df.at[index, "Task"] = input("New description: ")
                df.at[index, "Priority"] = input("New priority: ")
                df.at[index, "Status"] = input("New status (Pending/Done): ")
            else:
                print("Invalid index.")
            save_tasks(df)
            print("Task updated.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a number.")
    return df

# Delete a task
def delete_task(df):
    view_tasks(df)
    try:
        index = int(input("Enter the index of the task to delete: "))
        if 0 <= index < len(df):
            df = df.drop(index).reset_index(drop=True)
            save_tasks(df)
            print("Task deleted.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a number.")
    return df

# Visualize tasks by priority
def show_priority_chart(df):
    if df.empty:
        print("No data to show.")
        return
    priority_counts = df["Priority"].value_counts()
    priority_counts.plot(kind="bar", title="Tasks by Priority", color=['red', 'orange', 'green'])
    plt.xlabel("Priority")
    plt.ylabel("Number of Tasks")
    plt.tight_layout()
    plt.show()

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

        if choice == '1':
            df = view_tasks(df)
        elif choice == '2':
            df = create_task(df)
        elif choice == '3':
            df = update_task(df)
        elif choice == '4':
            df = delete_task(df)
        elif choice == '5':
            show_priority_chart(df)
        elif choice == '6':
            print("Goodluck!!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
