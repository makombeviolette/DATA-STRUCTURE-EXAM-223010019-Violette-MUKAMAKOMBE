import tkinter as tk
from tkinter import ttk

def counting_sort_priority(data, max_priority):
    """
    Perform Counting Sort to sort school bus tracking data based on priority.

    Args:
        data (list of dict): A list of dictionaries where each dictionary represents a student's information,
                            including a 'priority' key for sorting.
        max_priority (int): The maximum priority value in the data.

    Returns:
        list of dict: Sorted list of dictionaries by priority.
    """
    # Initialize count array
    count = [0] * (max_priority + 1)

    # Step 1: Count the occurrences of each priority
    for record in data:
        count[record['priority']] += 1

    # Step 2: Calculate cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 3: Sort the data into a new array
    sorted_data = [None] * len(data)
    for record in reversed(data):
        priority = record['priority']
        count[priority] -= 1
        sorted_data[count[priority]] = record

    return sorted_data

def add_student():
    try:
        name = student_name_entry.get().strip()
        priority = int(student_priority_entry.get().strip())
        if not name:
            raise ValueError("Name cannot be empty.")
        students.append({"name": name, "priority": priority})
        student_list_text.insert(tk.END, f"{name}, Priority: {priority}\n")
        student_name_entry.delete(0, tk.END)
        student_priority_entry.delete(0, tk.END)
    except ValueError as e:
        student_list_text.insert(tk.END, f"Error: {e}\n")

def sort_and_display():
    try:
        max_priority_value = int(max_priority_entry.get())
        sorted_students = counting_sort_priority(students, max_priority_value)
        output_text.delete("1.0", tk.END)
        for student in sorted_students:
            output_text.insert(tk.END, f"{student['name']}, Priority: {student['priority']}\n")
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("School Bus Tracking System - Priority Sorting")
root.geometry("600x600")
root.configure(bg="#e6f2ff")

students = []  # List to store student data

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#e6f2ff", foreground="#000000")
style.configure("TButton", font=("Arial", 12), background="#004d99", foreground="#000000")
style.configure("TEntry", font=("Arial", 12))

# Center the frames and widgets
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Input frame
input_frame = ttk.Frame(root, padding="20", relief="ridge", borderwidth=2, style="TFrame")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

input_frame.grid_rowconfigure(5, weight=1)
input_frame.grid_columnconfigure(1, weight=1)

ttk.Label(input_frame, text="Enter Maximum Priority:").grid(row=0, column=0, sticky=tk.E, pady=5, padx=5)
max_priority_entry = ttk.Entry(input_frame, width=15)
max_priority_entry.grid(row=0, column=1, sticky=tk.W, pady=5, padx=5)

ttk.Label(input_frame, text="Enter Student Name:").grid(row=1, column=0, sticky=tk.E, pady=5, padx=5)
student_name_entry = ttk.Entry(input_frame, width=30)
student_name_entry.grid(row=1, column=1, sticky=tk.W, pady=5, padx=5)

ttk.Label(input_frame, text="Enter Student Priority:").grid(row=2, column=0, sticky=tk.E, pady=5, padx=5)
student_priority_entry = ttk.Entry(input_frame, width=15)
student_priority_entry.grid(row=2, column=1, sticky=tk.W, pady=5, padx=5)

add_student_button = ttk.Button(input_frame, text="Add Student", command=add_student)
add_student_button.grid(row=3, column=0, columnspan=2, pady=10)

ttk.Label(input_frame, text="Current Students:").grid(row=4, column=0, sticky=tk.W, pady=5, padx=5)
student_list_text = tk.Text(input_frame, width=50, height=10, font=("Arial", 10), bg="#ffffff", fg="#000000", relief="solid", borderwidth=1)
student_list_text.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=5, padx=5)

sort_button = ttk.Button(input_frame, text="Sort", command=sort_and_display)
sort_button.grid(row=6, column=0, columnspan=2, pady=10)

# Output frame
output_frame = ttk.Frame(root, padding="20", relief="ridge", borderwidth=2, style="TFrame")
output_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

output_frame.grid_rowconfigure(1, weight=1)
output_frame.grid_columnconfigure(0, weight=1)

ttk.Label(output_frame, text="Sorted Students by Priority:").grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)
output_text = tk.Text(output_frame, width=50, height=10, font=("Arial", 10), bg="#ffffff", fg="#000000", relief="solid", borderwidth=1)
output_text.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)

# Run the application
root.mainloop()
