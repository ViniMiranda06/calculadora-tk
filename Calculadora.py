import tkinter as tk

def calculate(operation):
    global expression
    if operation == 'C':
        expression = ""
    elif operation == 'B':
        expression = expression[:-1]
    elif operation == 'Bin':
        try:
            num = int(eval(expression))
            expression = bin(num)[2:]
            label_text.set(expression)

        except:
            label_text.set("error")
            expression = ""
    elif operation == 'Dec':
        try:
            num = int(expression, 2)
            expression = str(num)
            label_text.set(expression)
        except:
            label_text.set("error")
            expression = ""
    else:
        if expression == "" and operation in ['+', '-', '*', '/']:
            return
        expression += operation

    label_text.set(expression)

def evaluate():
    global expression
    try:
        result = str(eval(expression))
        label_text.set(result)
        expression = result
    except:
        label_text.set("error")
        expression = ""


root = tk.Tk()
root.title("Calculadora Tkinter")

expression = ""
label_text = tk.StringVar()


label = tk.Label(root, textvariable =label_text, font=('Arial', 30))
label.grid(row=0, column=0, columnspan=4)

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('C', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('+', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('B', 4, 2), ('*', 4, 3),
    ('/', 5, 0),
    ('Bin', 6, 0), ('Dec', 6, 1)
]

for text, row, col in botoes:
    action = lambda x=text: calculate(x)
    btn = tk.Button(root, text=text, command=action, font=('Arial', 30), width=5, height=2)
    btn.grid(row=row, column=col)

btn_equal = tk.Button(root, text='=', command=evaluate, font=('Arial', 30), width=11, height=2)
btn_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()