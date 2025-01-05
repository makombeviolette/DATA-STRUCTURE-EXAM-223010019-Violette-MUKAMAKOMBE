import tkinter as tk
from tkinter import ttk

# Tree Node class for School, Bus Routes, and Buses
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

# GUI for School Bus Tracking System with Hierarchical Data
class BusTrackingApp:
    def __init__(self, root):
        self.window = root
        self.window.title("School Bus Tracking System for Parents - Huye High School")
        self.window.geometry("700x600")  # Increased window size
        self.window.resizable(True, True)  # Allow resizing of the window
        
        # Initialize the root school node for Huye High School
        self.school = TreeNode("Huye High School")
        
        # Styling for labels and buttons
        self.label_font = ("Arial", 14, "bold")
        self.entry_font = ("Arial", 12)
        self.button_font = ("Arial", 12)

        # Title label for the top section
        self.label = tk.Label(self.window, text="School Bus Route and Bus Tracking", font=self.label_font, bg="#4CAF50", fg="white")
        self.label.pack(pady=10, fill=tk.X)

        # Parent Location Selection Section
        self.location_label = tk.Label(self.window, text="Select Your Location:", font=self.label_font)
        self.location_label.pack(pady=5)
        self.location_combo = ttk.Combobox(self.window, values=["Buhimba", "Ngoma", "Mbuye"], font=self.entry_font)
        self.location_combo.pack(pady=5)

        # Bus Route Input Section
        self.bus_route_label = tk.Label(self.window, text="Bus Route Name:", font=self.label_font)
        self.bus_route_label.pack(pady=5)
        self.bus_route_entry = tk.Entry(self.window, font=self.entry_font, width=30)
        self.bus_route_entry.pack(pady=5)

        # Bus Input Section
        self.bus_label = tk.Label(self.window, text="Bus Name:", font=self.label_font)
        self.bus_label.pack(pady=5)
        self.bus_entry = tk.Entry(self.window, font=self.entry_font, width=30)
        self.bus_entry.pack(pady=5)
        
        # Insert Bus Route and Bus Button
        self.insert_button = tk.Button(self.window, text="Insert Bus Route and Bus", command=self.insert_bus_route_and_bus, font=self.button_font, bg="#4CAF50", fg="white", width=20, height=2)
        self.insert_button.pack(pady=15)

        # Display Section for Hierarchical Data
        self.tree_label = tk.Label(self.window, text="School Hierarchical View", font=self.label_font, bg="#4CAF50", fg="white")
        self.tree_label.pack(pady=10, fill=tk.X)

        # Treeview widget to display hierarchical data (School -> Routes -> Buses)
        self.treeview = ttk.Treeview(self.window, height=15)
        self.treeview.pack(pady=20, fill=tk.BOTH, expand=True)

        # Initial display of the root (school)
        self.display_hierarchy()

    def insert_bus_route_and_bus(self):
        # Get the Bus Route and Bus names from input fields
        bus_route_name = self.bus_route_entry.get()
        bus_name = self.bus_entry.get()

        if not bus_route_name or not bus_name:
            self.show_error_popup("Input Error", "Please provide both a bus route and bus name.")
            return

        # Create a new bus route node and bus node
        bus_route_node = TreeNode(bus_route_name)
        bus_node = TreeNode(bus_name)

        # Find the correct route (if it exists) or add a new route
        for child in self.school.children:
            if child.name == bus_route_name:
                child.children.append(bus_node)
                break
        else:
            # If the bus route doesn't exist, create a new route and add the bus
            bus_route_node.children.append(bus_node)
            self.school.children.append(bus_route_node)
        
        # Clear input fields
        self.bus_route_entry.delete(0, tk.END)
        self.bus_entry.delete(0, tk.END)

        # Display the updated hierarchy
        self.display_hierarchy()
        
        self.show_success_popup(f"Bus {bus_name} added to route {bus_route_name}.")

    def display_hierarchy(self):
        # Clear the existing tree view
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        
        # Insert the school root
        self.treeview.insert('', 'end', self.school.name, text=self.school.name, open=True)

        # Insert all bus routes and buses
        for route in self.school.children:
            route_id = self.treeview.insert(self.school.name, 'end', route.name, text=route.name)
            for bus in route.children:
                self.treeview.insert(route_id, 'end', bus.name, text=bus.name)

    def show_error_popup(self, title, message):
        # Custom error pop-up window
        error_popup = tk.Toplevel(self.window)
        error_popup.title(title)
        error_popup.geometry("300x150")
        error_popup.configure(bg="#f8d7da")

        # Error message label
        error_label = tk.Label(error_popup, text=message, font=("Arial", 12), bg="#f8d7da", fg="red")
        error_label.pack(pady=20)

        # Close button
        close_button = tk.Button(error_popup, text="Close", command=error_popup.destroy, font=("Arial", 12), bg="#f5c6cb", fg="red")
        close_button.pack(pady=10)

    def show_success_popup(self, message):
        # Custom success pop-up window
        success_popup = tk.Toplevel(self.window)
        success_popup.title("Success")
        success_popup.geometry("300x150")
        success_popup.configure(bg="#d4edda")

        # Success message label
        success_label = tk.Label(success_popup, text=message, font=("Arial", 12), bg="#d4edda", fg="green")
        success_label.pack(pady=20)

        # Close button
        close_button = tk.Button(success_popup, text="Close", command=success_popup.destroy, font=("Arial", 12), bg="#c3e6cb", fg="green")
        close_button.pack(pady=10)

# Create the main window for the GUI
root = tk.Tk()

# Instantiate the application
app = BusTrackingApp(root)

# Run the main loop for the GUI
root.mainloop()
