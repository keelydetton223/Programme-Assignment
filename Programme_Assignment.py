import pandas as pd
import matplotlib.pyplot as plt
import os

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
