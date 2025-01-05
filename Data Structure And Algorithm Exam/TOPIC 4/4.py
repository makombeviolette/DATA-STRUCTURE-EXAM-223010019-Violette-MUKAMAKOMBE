import tkinter as tk
from tkinter import messagebox

# Bus capacity and slots
TOTAL_SEATS = 32
bookings = [None] * TOTAL_SEATS  # None represents an available seat
MAX_PARENT_SLOTS = 31

def book_slot():
    """Book a specific slot for the parent."""
    child_name = entry_name.get()
    seat_number = entry_seat.get()
    if not child_name or not seat_number:
        messagebox.showwarning("Input Missing", "Please enter both child name and seat number.")
        return

    try:
        seat_number = int(seat_number) - 1  # Convert to zero-based index
        if seat_number < 0 or seat_number >= TOTAL_SEATS:
            messagebox.showerror("Invalid Seat", "Seat number must be between 1 and 32.")
            return

        booked_count = sum(1 for seat in bookings if seat is not None)
        if booked_count >= MAX_PARENT_SLOTS:
            messagebox.showerror(
                "Booking Limit Reached",
                "Parents are allowed to book up to 31 slots only."
            )
            return

        if bookings[seat_number] is None:
            bookings[seat_number] = child_name
            update_display()
            entry_name.delete(0, tk.END)
            entry_seat.delete(0, tk.END)
            messagebox.showinfo(
                "Booking Successful",
                f"✅ Seat {seat_number + 1} has been booked for {child_name}.\n\nRemaining slots: {MAX_PARENT_SLOTS - booked_count - 1}"
            )
        else:
            messagebox.showwarning("Seat Occupied", f"Seat {seat_number + 1} is already booked.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Seat number must be a valid integer.")

def cancel_slot():
    """Cancel a specific booking."""
    seat_number = entry_seat.get()
    if not seat_number:
        messagebox.showwarning("Input Missing", "Please enter the seat number to cancel.")
        return

    try:
        seat_number = int(seat_number) - 1  # Convert to zero-based index
        if seat_number < 0 or seat_number >= TOTAL_SEATS:
            messagebox.showerror("Invalid Seat", "Seat number must be between 1 and 32.")
            return

        if bookings[seat_number] is not None:
            child_name = bookings[seat_number]
            bookings[seat_number] = None
            update_display()
            entry_seat.delete(0, tk.END)
            messagebox.showinfo(
                "Cancellation Successful",
                f"❌ Booking for Seat {seat_number + 1} ({child_name}) has been cancelled."
            )
        else:
            messagebox.showwarning("Seat Empty", f"Seat {seat_number + 1} is already empty.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Seat number must be a valid integer.")

def view_slots():
    """View current booking details."""
    booked_list = [
        f"Seat {i + 1}: {name}" for i, name in enumerate(bookings) if name is not None
    ]
    if booked_list:
        messagebox.showinfo(
            "Current Bookings",
            "🚌 Current Seat Bookings:\n\n" + "\n".join(booked_list)
        )
    else:
        messagebox.showinfo("No Bookings", "No seats have been booked yet.")

def update_display():
    """Update the display to show the bus seating chart."""
    display.config(state=tk.NORMAL)
    display.delete(1.0, tk.END)
    for i in range(TOTAL_SEATS):
        seat_status = f"Seat {i + 1}: " + (bookings[i] if bookings[i] else "[Available]")
        display.insert(tk.END, seat_status + "\n")
    display.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("School Bus Tracking System - Seat Booking")
root.geometry("700x700")
root.config(bg="#f0f8ff")

# Title
title = tk.Label(root, text="🚍 School Bus Tracking System", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#4682b4")
title.pack(pady=10)

description = tk.Label(
    root,
    text="Parents can book specific seats for their children on the school bus.\nThe bus has 32 seats, and parents can book up to 31 slots.",
    font=("Helvetica", 12),
    bg="#f0f8ff",
    fg="#4682b4",
    wraplength=600,
    justify="center",
)
description.pack(pady=10)

# Input frame
input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=10)

name_label = tk.Label(input_frame, text="Child's Name:", font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4")
name_label.grid(row=0, column=0, padx=5)

entry_name = tk.Entry(input_frame, width=20, font=("Helvetica", 12))
entry_name.grid(row=0, column=1, padx=5)

seat_label = tk.Label(input_frame, text="Seat Number (1-32):", font=("Helvetica", 12), bg="#f0f8ff", fg="#4682b4")
seat_label.grid(row=1, column=0, padx=5)

entry_seat = tk.Entry(input_frame, width=20, font=("Helvetica", 12))
entry_seat.grid(row=1, column=1, padx=5)

# Buttons
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

book_button = tk.Button(button_frame, text="Book Slot", command=book_slot, font=("Helvetica", 12), bg="#4682b4", fg="white", width=15)
book_button.grid(row=0, column=0, padx=10)

cancel_button = tk.Button(button_frame, text="Cancel Booking", command=cancel_slot, font=("Helvetica", 12), bg="#4682b4", fg="white", width=15)
cancel_button.grid(row=0, column=1, padx=10)

view_button = tk.Button(button_frame, text="View Bookings", command=view_slots, font=("Helvetica", 12), bg="#4682b4", fg="white", width=15)
view_button.grid(row=0, column=2, padx=10)

# Display seating chart
display_frame = tk.Frame(root, bg="#f0f8ff")
display_frame.pack(pady=20)

display_label = tk.Label(display_frame, text="📝 Bus Seat Status:", font=("Helvetica", 14), bg="#f0f8ff", fg="#4682b4")
display_label.pack(pady=5)

display = tk.Text(display_frame, height=20, width=60, font=("Courier", 12), state=tk.DISABLED, bg="#e6f2ff", fg="#000080", relief=tk.RIDGE, bd=2)
display.pack()

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Helvetica", 12), bg="#ff6347", fg="white", width=10)
exit_button.pack(pady=20)

# Initial display update
update_display()

root.mainloop()
