import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x400")
        self.tasks = load_tasks()
        self.selected_task = None

        tk.Label(root, text="Task Description:").pack(pady=5)
        self.desc_entry = tk.Entry(root, width=50)
        self.desc_entry.pack()

        tk.Label(root, text="Due Date (YYYY-MM-DD, optional):").pack(pady=5)
        self.date_entry = tk.Entry(root, width=50)
        self.date_entry.pack()

        tk.Button(root, text="Add Task", command=self.add_task).pack(pady=10)

        tk.Label(root, text="Tasks:").pack()
        self.task_listbox = tk.Listbox(root, width=60, height=10)
        self.task_listbox.pack()
        self.task_listbox.bind('<<ListboxSelect>>', self.on_select)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Mark Complete", command=self.mark_complete).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Edit Task", command=self.edit_task).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Delete Task", command=self.delete_task).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Save Tasks", command=self.save_tasks_gui).grid(row=0, column=3, padx=5)

        self.update_listbox()

    def add_task(self):
        desc = self.desc_entry.get().strip()
        due_date = self.date_entry.get().strip() or None
        if not desc:
            messagebox.showerror("Error", "Task description cannot be empty.")
            return
        task_id = max([t["id"] for t in self.tasks], default=0) + 1
        self.tasks.append({"id": task_id, "description": desc, "completed": False, "due_date": due_date})
        self.desc_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.update_listbox()
        messagebox.showinfo("Success", "Task added!")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in sorted(self.tasks, key=lambda t: (t["completed"], t.get("due_date") or "9999-99-99")):
            status = "[✓]" if task["completed"] else "[ ]"
            due = f" (Due: {task['due_date']})" if task["due_date"] else ""
            self.task_listbox.insert(tk.END, f"{task['id']}. {status} {task['description']}{due}")

    def on_select(self, event):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            task_text = self.task_listbox.get(index)
            task_id = int(task_text.split('.')[0])
            self.selected_task = next((t for t in self.tasks if t["id"] == task_id), None)

    def mark_complete(self):
        if not self.selected_task:
            messagebox.showerror("Error", "Select a task first.")
            return
        self.selected_task["completed"] = True
        self.update_listbox()
        messagebox.showinfo("Success", "Task marked complete!")

    def edit_task(self):
        if not self.selected_task:
            messagebox.showerror("Error", "Select a task first.")
            return
        new_desc = simpledialog.askstring("Edit Task", "New description:", initialvalue=self.selected_task["description"])
        if new_desc:
            self.selected_task["description"] = new_desc
            self.update_listbox()
            messagebox.showinfo("Success", "Task updated!")

    def delete_task(self):
        if not self.selected_task:
            messagebox.showerror("Error", "Select a task first.")
            return
        self.tasks.remove(self.selected_task)
        self.selected_task = None
        self.update_listbox()
        messagebox.showinfo("Success", "Task deleted!")

    def save_tasks_gui(self):
        save_tasks(self.tasks)
        messagebox.showinfo("Success", "Tasks saved!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(app.tasks), root.destroy()))
    root.mainloop()
