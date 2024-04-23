import tkinter as tk

def add_digit(digit):
    current = display.get()
    if current == '0': 
        display.delete(0, tk.END)
    display.insert(tk.END, digit)

def add_operation(operator):
    current = display.get()
    if current[-1] in '+-*/':  
        display.delete(len(current)-1, tk.END)
    display.insert(tk.END, operator)

def clear_display():
    display.delete(0, tk.END)
    display.insert(0, '0')

def calculate():
    try:
        result = eval(display.get())  
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception as e:
        clear_display()
        display.insert(0, "Error")

app = tk.Tk()
app.title("Calculator")

display = tk.Entry(app, width=14, font=("Arial", 24), justify='right')
display.insert(0, '0')
display.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('C', 4, 0), ('=', 4, 2),
]

for (text, row, col) in buttons:
    if text.isdigit() or text == '.':
        action = lambda txt=text: add_digit(txt)
    elif text in '+-*/':
        action = lambda txt=text: add_operation(txt)
    elif text == 'C':
        action = clear_display
    elif text == '=':
        action = calculate
    button = tk.Button(app, text=text, width=5, height=2, font=("Arial", 18), command=action)
    button.grid(row=row, column=col)

app.mainloop()
