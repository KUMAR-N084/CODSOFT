import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("250x350")

        # Display
        self.display = tk.Entry(root, font=("Arial", 20), justify="right", state="readonly")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Variables for calculation
        self.first_num = None
        self.operation = None
        self.clear_next = False

        # Button layout
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for text, row, col in buttons:
            button = tk.Button(root, text=text, font=("Arial", 15), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Configure grid weights for resizing
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

    def on_button_click(self, text):
        current = self.display.get()

        if text.isdigit():
            if self.clear_next:
                self.display.config(state="normal")
                self.display.delete(0, tk.END)
                self.display.config(state="readonly")
                self.clear_next = False
            self.display.config(state="normal")
            self.display.insert(tk.END, text)
            self.display.config(state="readonly")

        elif text in "+-*/":
            if self.first_num is None and current:
                self.first_num = float(current)
                self.operation = text
                self.clear_next = True

        elif text == "=":
            if self.first_num is not None and self.operation and current:
                try:
                    second_num = float(current)
                    if self.operation == "+":
                        result = self.first_num + second_num
                    elif self.operation == "-":
                        result = self.first_num - second_num
                    elif self.operation == "*":
                        result = self.first_num * second_num
                    elif self.operation == "/":
                        if second_num == 0:
                            messagebox.showerror("Error", "Cannot divide by zero!")
                            return
                        result = self.first_num / second_num
                    self.display.config(state="normal")
                    self.display.delete(0, tk.END)
                    self.display.insert(0, str(result))
                    self.display.config(state="readonly")
                    self.first_num = result  # Allow chaining
                    self.clear_next = True
                except ValueError:
                    messagebox.showerror("Error", "Invalid input!")

        elif text == "C":
            self.display.config(state="normal")
            self.display.delete(0, tk.END)
            self.display.config(state="readonly")
            self.first_num = None
            self.operation = None
            self.clear_next = False

if __name__ == "__main__":
    root = tk.Tk()
    calc = SimpleCalculator(root)
    root.mainloop()
