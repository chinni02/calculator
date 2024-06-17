import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Calculator")

# Set the window size
root.geometry("300x400")

# Create a display widget
display = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="sunken", justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Global variables to store the current input and operation
current_input = ""
operator = ""
operand1 = None

def button_click(value):
    global current_input, operator, operand1

    if value == "C":
        current_input = ""
        operator = ""
        operand1 = None
        display.delete(0, tk.END)
    elif value == "=":
        try:
            if operator and operand1 is not None:
                operand2 = float(current_input)
                if operator == "+":
                    result = operand1 + operand2
                elif operator == "-":
                    result = operand1 - operand2
                elif operator == "*":
                    result = operand1 * operand2
                elif operator == "/":
                    if operand2 != 0:
                        result = operand1 / operand2
                    else:
                        result = "Error"
                display.delete(0, tk.END)
                display.insert(tk.END, result)
                current_input = str(result)
                operator = ""
                operand1 = None
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            current_input = ""
            operator = ""
            operand1 = None
            display.delete(0, tk.END)
    elif value in ["+", "-", "*", "/"]:
        if current_input:
            operand1 = float(current_input)
            operator = value
            current_input = ""
    else:
        current_input += value
        display.delete(0, tk.END)
        display.insert(tk.END, current_input)

# Create calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Add buttons to the calculator
row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
              command=lambda b=button: button_click(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main loop
root.mainloop()

