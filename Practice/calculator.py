from tkinter import Tk, Entry, Button, StringVar, END, RIGHT, DISABLED, NORMAL

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Simple Calculator")
        root.resizable(False, False)

        self.expression = StringVar()
        self.entry = Entry(root, textvariable=self.expression, font=("Arial", 20), bd=10, relief="ridge", justify=RIGHT)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

        # Buttons layout: list of rows (each row is list of (text, command))
        btn_texts = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="]
        ]

        for r, row in enumerate(btn_texts, start=1):
            for c, char in enumerate(row):
                btn = Button(root, text=char, width=5, height=2, font=("Arial", 18),
                             command=lambda ch=char: self.on_button(ch))
                btn.grid(row=r, column=c, padx=5, pady=5)

        # Allow keyboard input for convenience
        root.bind("<Return>", lambda event: self.on_button("="))
        root.bind("<BackSpace>", lambda event: self.on_button("⌫"))
        for key in "0123456789+-*/.%":
            root.bind(key, lambda event, k=key: self.on_button(k))
        root.bind(".", lambda event: self.on_button("."))
        root.bind("+", lambda event: self.on_button("+"))
        root.bind("-", lambda event: self.on_button("-"))
        root.bind("*", lambda event: self.on_button("*"))
        root.bind("/", lambda event: self.on_button("/"))

    def on_button(self, ch):
        if ch == "C":
            self.expression.set("")
        elif ch == "⌫":
            current = self.expression.get()
            self.expression.set(current[:-1])
        elif ch == "=":
            self.calculate()
        elif ch == "±":
            self.toggle_sign()
        elif ch == "%":
            self.apply_percent()
        else:
            self.expression.set(self.expression.get() + str(ch))

    def calculate(self):
        expr = self.expression.get()
        if not expr:
            return
        try:
            # safe-ish eval: replace the unicode division sign if any, then eval
            expr = expr.replace("×", "*").replace("÷", "/")
            # Evaluate expression
            result = eval(expr, {"__builtins__": None}, {})
            # Format result: if integer-like, show as int
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression.set(str(result))
        except Exception:
            self.expression.set("Error")

    def toggle_sign(self):
        val = self.expression.get()
        if not val:
            return
        try:
            if val.startswith("-"):
                self.expression.set(val[1:])
            else:
                self.expression.set("-" + val)
        except Exception:
            pass

    def apply_percent(self):
        val = self.expression.get()
        if not val:
            return
        try:
            # treat current expression as a number and divide by 100
            num = float(val)
            num = num / 100.0
            # format
            if num.is_integer():
                self.expression.set(str(int(num)))
            else:
                self.expression.set(str(num))
        except Exception:
            self.expression.set("Error")


if __name__ == "__main__":
    root = Tk()
    calc = Calculator(root)
    root.mainloop()