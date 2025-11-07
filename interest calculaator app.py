import tkinter as tk
from tkinter import messagebox

# Function to calculate interests
def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        # Simple Interest Formula
        simple_interest = (principal * rate * time) / 100

        # Compound Interest Formula
        compound_interest = principal * ((1 + rate / 100) ** time) - principal

        # Displaying the results
        label_result.config(text=f"Simple Interest: ₹{simple_interest:.2f}\nCompound Interest: ₹{compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Setting up the GUI
root = tk.Tk()
root.title("Interest Calculator")

# Labels and Entries
tk.Label(root, text="Principal Amount (₹):").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_principal = tk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Rate of Interest (% per annum):").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_rate = tk.Entry(root)
entry_rate.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Time Period (years):").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_time = tk.Entry(root)
entry_time.grid(row=2, column=1, padx=10, pady=5)

# Calculate Button
tk.Button(root, text="Calculate", command=calculate_interest).grid(row=3, columnspan=2, pady=10)

# Result Label
label_result = tk.Label(root, text="", font=('Arial', 12), fg='green')
label_result.grid(row=4, columnspan=2, pady=10)

root.mainloop()
