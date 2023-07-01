import tkinter as tk
from tkinter import filedialog
import os
import re

# Function to calculate time complexity
def calculate_time_complexity(file_path):
    # Read the contents of the C++ file
    with open(file_path, "r") as file:
        code = file.read()

    # Identify the number of loops in the code
    num_loops = code.count("for") + code.count("while") + code.count("do")

    # Identify the number of arithmetic operations in the code
    num_operations = code.count("+") + code.count("-") + code.count("*") + 
code.count("/") + code.count("%")

    # Identify the number of logarithmic operations in the code
    num_logarithms = 0
    for line in code.split("\n"):
        if re.search(r"\b[a-zA-Z]*[ \t]*\([ \t]*[a-zA-Z]*[ \t]*[\/\*][ 
\t]*2[ \t]*\)", line):
            num_logarithms += 1

    # Determine the time complexity based on the number of loops, 
operations and logarithms
    if num_loops == 0:
        if num_operations == 0:
            complexity = "O(1)"
        else:
            complexity = "O(n)"
    elif num_loops == 1:
        if num_operations == 0:
            complexity = "O(n)"
        elif num_operations == 1:
            complexity = "O(n)"
        else:
            complexity = "O(n^2)"
    elif num_loops == 2:
        if num_operations == 0:
            complexity = "O(n^2)"
        elif num_operations == 1:
            complexity = "O(n^2)"
        elif num_operations == 2:
            complexity = "O(n^2)"
        else:
            complexity = "O(n^3)"
    else:
        if num_logarithms > 0:
            complexity = "O(n log n)"
        else:
            complexity = "O(n^k) (k > 3)"

    return complexity

# Function to handle file selection
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("C++ files", 
"*.cpp")])
    if file_path:
        complexity = calculate_time_complexity(file_path)
        result_label.config(text="Time complexity: " + complexity)
    else:
        result_label.config(text="Please select a file.")

# Create GUI window
window = tk.Tk()
window.title("Time Complexity Calculator")

# Create file selection button
file_button = tk.Button(window, text="Select File", command=select_file)
file_button.pack()

# Create button to display time complexity
complexity_button = tk.Button(window, text="Calculate Time Complexity", 
command=select_file)
complexity_button.pack()

# Create label to display result
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()

