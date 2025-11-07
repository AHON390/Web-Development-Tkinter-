import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        # Get input values
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        # Date of birth and today's date
        dob = date(year, month, day)
        today = date.today()

        # Calculate age
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        # Show the result
        messagebox.showinfo("Age", f"Your current age is: {age} years")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for date, month, and year.")

# Create main window
root = tk.Tk()
root.title("Age Calculator")

# Create and place labels and entry boxes
tk.Label(root, text="Enter your Date of Birth").grid(row=0, column=1)

tk.Label(root, text="Day").grid(row=1, column=0)
entry_day = tk.Entry(root)
entry_day.grid(row=1, column=1)

tk.Label(root, text="Month").grid(row=2, column=0)
entry_month = tk.Entry(root)
entry_month.grid(row=2, column=1)

tk.Label(root, text="Year").grid(row=3, column=0)
entry_year = tk.Entry(root)
entry_year.grid(row=3, column=1)

# Submit button
tk.Button(root, text="Calculate Age", command=calculate_age).grid(row=4, column=1)

# Start the GUI loop
root.mainloop()
