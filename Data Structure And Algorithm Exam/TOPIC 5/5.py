import tkinter as tk
from tkinter import messagebox

# Bus Node class
class BusNode:
    def __init__(self, bus_id):
        self.bus_id = bus_id
        self.left = None
        self.right = None

# Binary Tree for Bus Routes
class BusRouteTree:
    def __init__(self):
        self.root = None
    
    def insert(self, bus_id):
        if self.root is None:
            self.root = BusNode(bus_id)
        else:
            self._insert(self.root, bus_id)
    
    def _insert(self, node, bus_id):
        if bus_id < node.bus_id:
            if node.left is None:
                node.left = BusNode(bus_id)
            else:
                self._insert(node.left, bus_id)
        else:
            if node.right is None:
                node.right = BusNode(bus_id)
            else:
                self._insert(node.right, bus_id)
    
    def display(self):
        return self._inorder_traversal(self.root)
    
    def _inorder_traversal(self, node):
        if node:
            return self._inorder_traversal(node.left) + [node] + self._inorder_traversal(node.right)
        return []

# GUI for School Bus Tracking System
class BusTrackingApp:
    def __init__(self, root):
        self.window = root
        self.window.title("School Bus Tracking System")
        self.window.geometry("600x500")
        self.window.resizable(True, True)  # Allow resizing of the window
        
        self.tree = BusRouteTree()
        
        # Styling for labels and buttons
        self.label_font = ("Arial", 14, "bold")
        self.entry_font = ("Arial", 12)
        self.button_font = ("Arial", 12)
        
        # Bus Information Input Section
        self.label = tk.Label(self.window, text="Enter Bus ID", font=self.label_font)
        self.label.pack(pady=10)
        
        self.bus_id_label = tk.Label(self.window, text="Bus ID (Integer):", font=self.label_font)
        self.bus_id_label.pack(pady=5)
        self.bus_id_entry = tk.Entry(self.window, font=self.entry_font)
        self.bus_id_entry.pack(pady=5)
        
        # Insert Bus Button
        self.insert_button = tk.Button(self.window, text="Insert Bus", command=self.insert_bus, font=self.button_font, bg="#4CAF50", fg="white", width=20, height=2)
        self.insert_button.pack(pady=15)
        
        # Display and Search Section
        self.search_label = tk.Label(self.window, text="Search for Bus by ID:", font=self.label_font)
        self.search_label.pack(pady=10)
        self.search_entry = tk.Entry(self.window, font=self.entry_font)
        self.search_entry.pack(pady=5)
        self.search_button = tk.Button(self.window, text="Search Bus", command=self.search_bus, font=self.button_font, bg="#FF9800", fg="white", width=20, height=2)
        self.search_button.pack(pady=10)
        
        # Clear All Buses Button
        self.clear_button = tk.Button(self.window, text="Clear All Buses", command=self.clear_tree, font=self.button_font, bg="#f44336", fg="white", width=20, height=2)
        self.clear_button.pack(pady=15)
        
        # Display Section for Results
        self.tree_display = tk.Label(self.window, text="Current Bus Information will appear here.", font=("Arial", 12), fg="blue", anchor="w", justify="left", width=70)
        self.tree_display.pack(pady=20)

    def insert_bus(self):
        bus_id = self.bus_id_entry.get()
        
        # Validate the Bus ID input (it should be a valid integer)
        if not bus_id.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid Bus ID (integer).")
            return
        
        # Insert bus and update the display immediately
        self.tree.insert(int(bus_id))
        self.bus_id_entry.delete(0, tk.END)
        
        # Auto update the display with new bus information
        self.update_display()
        
        messagebox.showinfo("Success", f"Bus ID {bus_id} added.")

    def display_buses(self):
        buses = self.tree.display()
        if buses:
            bus_info = "\n".join([f"Bus ID: {bus.bus_id}" for bus in buses])
            self.tree_display.config(text=bus_info)
        else:
            self.tree_display.config(text="No buses in the system yet.")

    def search_bus(self):
        search_id = self.search_entry.get()
        if search_id.isdigit():
            bus_id = int(search_id)
            buses = self.tree.display()
            found_bus = None
            for bus in buses:
                if bus.bus_id == bus_id:
                    found_bus = bus
                    break
            if found_bus:
                self.tree_display.config(text=f"Bus ID {bus_id} found.")
            else:
                self.tree_display.config(text=f"Bus ID {bus_id} not found.")
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid Bus ID.")

    def clear_tree(self):
        self.tree = BusRouteTree()
        self.tree_display.config(text="All buses have been cleared.")

    def update_display(self):
        buses = self.tree.display()
        if buses:
            bus_info = "\n".join([f"Bus ID: {bus.bus_id}" for bus in buses])
            self.tree_display.config(text=bus_info)
        else:
            self.tree_display.config(text="No buses in the system yet.")

# Create the main window for the GUI
root = tk.Tk()

# Instantiate the application
app = BusTrackingApp(root)

# Run the main loop for the GUI
root.mainloop()
