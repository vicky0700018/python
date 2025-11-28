from tkinter import *
import math

root = Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.resizable(False, False)
root.config(bg="#1e1e1e")

# ================== Entry box ===================
equation = StringVar()
entry_box = Entry(root, textvariable=equation, font=("Arial", 20), bg="#252526", fg="white", bd=5, insertbackground="white", justify=RIGHT)
entry_box.grid(row=0, column=0, columnspan=5, pady=15, padx=10, ipady=10)

# ================== Button click event ===================
def press(num):
    current = equation.get()
    equation.set(current + str(num))

def clear():
    equation.set("")

def backspace():
    current = equation.get()
    equation.set(current[:-1])

def equal():
    try:
        expr = equation.get()
        expr = expr.replace("√", "math.sqrt")
        expr = expr.replace("^", "**")
        expr = expr.replace("π", str(math.pi))
        expr = expr.replace("e", str(math.e))
        result = eval(expr, {"math": math, "__builtins__": None}, {})
        equation.set(str(result))
    except Exception:
        equation.set("Error")

# ================== Scientific functions ===================
def sin_func():
    try:
        val = float(equation.get())
        equation.set(str(round(math.sin(math.radians(val)), 8)))
    except:
        equation.set("Error")

def cos_func():
    try:
        val = float(equation.get())
        equation.set(str(round(math.cos(math.radians(val)), 8)))
    except:
        equation.set("Error")

def tan_func():
    try:
        val = float(equation.get())
        equation.set(str(round(math.tan(math.radians(val)), 8)))
    except:
        equation.set("Error")

def log_func():
    try:
        val = float(equation.get())
        equation.set(str(round(math.log10(val), 8)))
    except:
        equation.set("Error")

def ln_func():
    try:
        val = float(equation.get())
        equation.set(str(round(math.log(val), 8)))
    except:
        equation.set("Error")

def sqrt_func():
    try:
        val = float(equation.get())
        equation.set(str(round(math.sqrt(val), 8)))
    except:
        equation.set("Error")

# ================== Button Layout ===================
button_texts = [
    ["C", "⌫", "(", ")", "/"],
    ["7", "8", "9", "*", "√"],
    ["4", "5", "6", "-", "^"],
    ["1", "2", "3", "+", "="],
    ["0", ".", "π", "e", "%"]
]

for r, row in enumerate(button_texts, start=1):
    for c, char in enumerate(row):
        action = None
        if char == "C":
            action = clear
        elif char == "⌫":
            action = backspace
        elif char == "=":
            action = equal
        elif char == "√":
            action = sqrt_func
        else:
            action = lambda ch=char: press(ch)

        Button(root, text=char, width=5, height=2, font=("Arial", 18),
               bg="#2d2d2d", fg="white", command=action, relief="ridge").grid(row=r, column=c, padx=3, pady=3)

# Scientific function buttons
scientific_buttons = [
    ("sin", sin_func),
    ("cos", cos_func),
    ("tan", tan_func),
    ("log", log_func),
    ("ln", ln_func)
]

for i, (text, func) in enumerate(scientific_buttons):
    Button(root, text=text, width=7, height=2, font=("Arial", 14),
           bg="#007acc", fg="white", command=func).grid(row=6, column=i, padx=3, pady=5)

# Developer footer
Label(root, text="Developed by Vicky 🧠", bg="#1e1e1e", fg="#aaaaaa", font=("Arial", 10)).grid(row=7, column=0, columnspan=5, pady=10)

root.mainloop()