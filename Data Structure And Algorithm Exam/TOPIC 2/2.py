import tkinter as tk
from tkinter import messagebox

# Stack implementation
stack = []

def push_stack():
    data = entry.get()
    if data:
        stack.append(data)
        entry.delete(0, tk.END)
        update_stack_display()
        messagebox.showinfo("Success", f"'{data}' has been added to the tracking system.")
    else:
        messagebox.showwarning("Input Error", "Please enter the bus location or event to add.")

def pop_stack():
    if stack:
        popped = stack.pop()
        update_stack_display()
        messagebox.showinfo("Entry Removed", f"Last recorded location/event removed: '{popped}'")
    else:
        messagebox.showwarning("Stack Underflow", "No locations or events to remove.")

def update_stack_display():
    stack_display.config(state=tk.NORMAL)
    stack_display.delete(1.0, tk.END)
    stack_display.insert(tk.END, "\n".join(reversed(stack)))
    stack_display.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("School Bus Tracking System")
root.geometry("500x600")
root.config(bg="#f0f8ff")

# Title label
title_label = tk.Label(root, text="School Bus Tracking System", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#4682b4")
title_label.pack(pady=10)

# Description label
description_label = tk.Label(root, text="Track bus locations and events in real-time using the stack mechanism.", font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4", wraplength=400, justify="center")
description_label.pack(pady=5)

# Entry field
entry_frame = tk.Frame(root, bg="#f0f8ff")
entry_frame.pack(pady=10)

entry_label = tk.Label(entry_frame, text="Enter Bus Location/Event:", font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4")
entry_label.grid(row=0, column=0, padx=5)

entry = tk.Entry(entry_frame, width=30, font=("Helvetica", 12))
entry.grid(row=0, column=1, padx=5)

# Buttons
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

push_button = tk.Button(button_frame, text="Add Location/Event", command=push_stack, font=("Helvetica", 12), bg="#4682b4", fg="white", width=18)
push_button.grid(row=0, column=0, padx=10)

pop_button = tk.Button(button_frame, text="Remove Last Entry", command=pop_stack, font=("Helvetica", 12), bg="#4682b4", fg="white", width=18)
pop_button.grid(row=0, column=1, padx=10)

# Stack display
stack_frame = tk.Frame(root, bg="#f0f8ff")
stack_frame.pack(pady=20)

stack_label = tk.Label(stack_frame, text="Recorded Locations/Events:", font=("Helvetica", 14), bg="#f0f8ff", fg="#4682b4")
stack_label.pack(pady=5)

stack_display = tk.Text(stack_frame, height=15, width=40, font=("Courier", 12), state=tk.DISABLED, bg="#e6f2ff", fg="#000080", relief=tk.RIDGE, bd=2)
stack_display.pack()

# Footer
def close_app():
    root.destroy()

footer_frame = tk.Frame(root, bg="#f0f8ff")
footer_frame.pack(pady=20)

exit_button = tk.Button(footer_frame, text="Exit", command=close_app, font=("Helvetica", 12), bg="#ff6347", fg="white", width=10)
exit_button.pack()

# Run the application
root.mainloop()