import tkinter as tk
from tkinter import messagebox

global root, entry1, entry2, entry3
root, entry1, entry2, entry3 = None, None, None, None

def show_output():
    global generate_button, entry1, entry2, entry3

    input1 = entry1.get()
    input2 = entry2.get()
    input3 = entry3.get()
    print(input1, input2, input3)

    try:
        if input1.isnumeric() and input3.isnumeric() and input2 in ['+', '-', '*', '/'] :
            k = input1 + input2 + input3
            pp = eval(k)
            result_label.config(text=f"Result: {pp}")
        else:
            messagebox.showinfo("Error", "Please provide input1 and input3 as integers, and input2 as one of '*,/,+,-'")
    except ZeroDivisionError:
        messagebox.showinfo("Error", "1 / 0 not permitted")


root = tk.Tk()
root.title("CALC")

# Create and place the widgets
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="INPUT 1").pack(side=tk.LEFT, padx=10)
entry1 = tk.Entry(frame)
entry1.pack(side=tk.LEFT, padx=10)

tk.Label(frame, text="ARITHMETIC").pack(side=tk.LEFT, padx=10)
entry2 = tk.Entry(frame)
entry2.pack(side=tk.LEFT, padx=10)

tk.Label(frame, text="INPUT 2").pack(side=tk.LEFT, padx=10)
entry3 = tk.Entry(frame)
entry3.pack(side=tk.LEFT, padx=10)

generate_button = tk.Button(root, text="Calculate", command=show_output)
generate_button.pack(pady=20)

result_label = tk.Label(root, text="\n", font=("Helvetica", 20),fg='Green')
result_label.pack(pady=20, expand=True)

root.mainloop()
