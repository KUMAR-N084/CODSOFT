import tkinter as tk
from tkinter import messagebox
import secrets
import string

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("450x400")
        self.root.configure(bg="#f0f0f0") 

        main_frame = tk.Frame(root, bg="#f0f0f0")
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        title_label = tk.Label(main_frame, text="Secure Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=10)

        length_frame = tk.Frame(main_frame, bg="#f0f0f0")
        length_frame.pack(pady=10)
        tk.Label(length_frame, text="Password Length:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=0, column=0, padx=5)
        self.length_entry = tk.Entry(length_frame, font=("Helvetica", 12), width=10)
        self.length_entry.grid(row=0, column=1, padx=5)

        options_frame = tk.Frame(main_frame, bg="#f0f0f0")
        options_frame.pack(pady=10)
        tk.Label(options_frame, text="Include:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").pack(anchor="w")
        self.include_lower = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="Lowercase letters (a-z)", variable=self.include_lower, font=("Helvetica", 10), bg="#f0f0f0").pack(anchor="w", padx=20)
        self.include_upper = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="Uppercase letters (A-Z)", variable=self.include_upper, font=("Helvetica", 10), bg="#f0f0f0").pack(anchor="w", padx=20)
        self.include_digits = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="Digits (0-9)", variable=self.include_digits, font=("Helvetica", 10), bg="#f0f0f0").pack(anchor="w", padx=20)
        self.include_symbols = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="Special symbols (!@#$%^&*)", variable=self.include_symbols, font=("Helvetica", 10), bg="#f0f0f0").pack(anchor="w", padx=20)

        button_frame = tk.Frame(main_frame, bg="#f0f0f0")
        button_frame.pack(pady=10)
        generate_btn = tk.Button(button_frame, text="Generate Password", command=self.generate_password, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10)
        generate_btn.grid(row=0, column=0, padx=5)
        regenerate_btn = tk.Button(button_frame, text="Regenerate", command=self.generate_password, font=("Helvetica", 12), bg="#2196F3", fg="white", padx=10)
        regenerate_btn.grid(row=0, column=1, padx=5)
        copy_btn = tk.Button(button_frame, text="Copy to Clipboard", command=self.copy_to_clipboard, font=("Helvetica", 12), bg="#FF9800", fg="white", padx=10)
        copy_btn.grid(row=0, column=2, padx=5)

        display_frame = tk.Frame(main_frame, bg="#f0f0f0")
        display_frame.pack(pady=10)
        tk.Label(display_frame, text="Generated Password:", font=("Helvetica", 12), bg="#f0f0f0").pack()
        self.password_display = tk.Entry(display_frame, font=("Courier", 14), state="readonly", width=30, justify="center")
        self.password_display.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1 or length > 100:
                messagebox.showerror("Error", "Length must be between 1 and 100.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for length.")
            return

        chars = ""
        if self.include_lower.get():
            chars += string.ascii_lowercase
        if self.include_upper.get():
            chars += string.ascii_uppercase
        if self.include_digits.get():
            chars += string.digits
        if self.include_symbols.get():
            chars += string.punctuation

        if not chars:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        password = ''.join(secrets.choice(chars) for _ in range(length))
        self.password_display.config(state="normal")
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)
        self.password_display.config(state="readonly")

    def copy_to_clipboard(self):
        password = self.password_display.get()
        if not password:
            messagebox.showwarning("Warning", "No password to copy. Generate one first!")
            return
        if CLIPBOARD_AVAILABLE:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Success", "Password copied to clipboard (Tkinter fallback)!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
