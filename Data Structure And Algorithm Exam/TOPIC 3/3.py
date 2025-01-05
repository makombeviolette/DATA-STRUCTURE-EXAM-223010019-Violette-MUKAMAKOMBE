import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def remove(self):
        if not self.head:
            return None
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            return removed_data
        current = self.head
        while current.next:
            current = current.next
        removed_data = current.data
        current.prev.next = None
        return removed_data

    def traverse(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

dll = DoublyLinkedList()

def add_update():
    update = entry.get()
    if update:
        dll.append(update)
        entry.delete(0, tk.END)
        update_display()
        messagebox.showinfo(
            "🎉 Update Added",
            f"✨ New update added successfully:\n\n📍 {update}\n\nYour input has been recorded!"
        )
    else:
        messagebox.showwarning(
            "⚠️ Missing Information",
            "Oops! You forgot to enter a bus location or update.\n\n🚨 Please provide details to proceed!"
        )

def remove_update():
    if not dll.head:
        messagebox.showwarning(
            "📋 Empty List",
            "🚫 No updates available to remove.\n\nStart adding updates to manage them here!"
        )
        return
    removed_update = dll.remove()
    update_display()
    messagebox.showinfo(
        "🗑️ Update Removed",
        f"✨ The most recent update has been removed:\n\n📍 {removed_update}\n\nKeep the updates coming!"
    )

def view_updates():
    if not dll.head:
        messagebox.showinfo(
            "ℹ️ No Updates Yet",
            "🕒 The update list is currently empty.\n\nStart adding new updates to see them here!"
        )
        return
    all_updates = dll.traverse()
    updates_message = "\n\n".join([f"📍 {update}" for update in all_updates])
    messagebox.showinfo(
        "📋 All Updates",
        f"🚍 Here are the current bus updates:\n\n{updates_message}\n\nKeep track of the bus easily!"
    )

def update_display():
    updates = dll.traverse()
    display.config(state=tk.NORMAL)
    display.delete(1.0, tk.END)
    for update in updates:
        display.insert(tk.END, f"📍 {update}\n")
    display.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("School Bus Tracking System")
root.geometry("600x700")
root.config(bg="#f0f8ff")

# Title
title = tk.Label(root, text="🚍 School Bus Tracking System", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#4682b4")
title.pack(pady=10)

# Input frame
input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=10)

entry_label = tk.Label(input_frame, text="Enter Location/Event:", font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4")
entry_label.grid(row=0, column=0, padx=5)

entry = tk.Entry(input_frame, width=40, font=("Helvetica", 12))
entry.grid(row=0, column=1, padx=5)

# Buttons
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Update", command=add_update, font=("Helvetica", 12), bg="#4682b4", fg="white", width=15)
add_button.grid(row=0, column=0, padx=10)

remove_button = tk.Button(button_frame, text="Remove Update", command=remove_update, font=("Helvetica", 12), bg="#4682b4", fg="white", width=15)
remove_button.grid(row=0, column=1, padx=10)

view_button = tk.Button(button_frame, text="View Updates", command=view_updates, font=("Helvetica", 12), bg="#4682b4", fg="white", width=15)
view_button.grid(row=0, column=2, padx=10)

# Display updates
display_frame = tk.Frame(root, bg="#f0f8ff")
display_frame.pack(pady=20)

display_label = tk.Label(display_frame, text="📋 Current Updates:", font=("Helvetica", 14), bg="#f0f8ff", fg="#4682b4")
display_label.pack(pady=5)

display = tk.Text(display_frame, height=15, width=50, font=("Courier", 12), state=tk.DISABLED, bg="#e6f2ff", fg="#000080", relief=tk.RIDGE, bd=2)
display.pack()

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Helvetica", 12), bg="#ff6347", fg="white", width=10)
exit_button.pack(pady=20)

root.mainloop()
