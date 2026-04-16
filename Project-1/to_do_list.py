import tkinter as tk
from tkinter import messagebox
import os
BG_COLOR = "#f4f6f8"
PRIMARY_COLOR = "#053469"
TEXT_COLOR = "#333333"
DONE_COLOR = "#999999"
FONT = ("Segoe UI", 11)
TITLE_FONT = ("Segoe UI", 18, "bold")
FILE_NAME = "tasks.txt"

def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
        save_tasks()
    else:
        messagebox.showwarning("No Selection", "Select a task to delete.")

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(selected, f"✔ {task}")
        task_listbox.itemconfig(selected, fg=DONE_COLOR)
        save_tasks()

def save_tasks():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for task in file.readlines():
                task = task.strip()
                task_listbox.insert(tk.END, task)
                if task.startswith("✔"):
                    task_listbox.itemconfig(tk.END, fg=DONE_COLOR)

root = tk.Tk()
root.title("To-Do List")
root.geometry("450x550")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="📝 To-Do List",
    font=TITLE_FONT,
    bg=BG_COLOR,
    fg=PRIMARY_COLOR
)
title_label.pack(pady=15)
input_frame = tk.Frame(root, bg=BG_COLOR)
input_frame.pack(pady=10)

task_entry = tk.Entry(
    input_frame,
    width=30,
    font=FONT
)
task_entry.pack(side=tk.LEFT, padx=5)
task_entry.bind("<Return>", add_task)

add_button = tk.Button(
    input_frame,
    text="Add",
    font=FONT,
    bg=PRIMARY_COLOR,
    fg="white",
    width=8,
    command=add_task
)
add_button.pack(side=tk.LEFT)

list_frame = tk.Frame(root, bg=BG_COLOR)
list_frame.pack(pady=15)

task_listbox = tk.Listbox(
    list_frame,
    width=40,
    height=15,
    font=FONT,
    selectbackground=PRIMARY_COLOR,
    activestyle="none"
)
task_listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=10)

done_button = tk.Button(
    button_frame,
    text="Mark Done",
    font=FONT,
    bg="#5cb85c",
    fg="white",
    width=12,
    command=mark_done
)
done_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete",
    font=FONT,
    bg="#d9534f",
    fg="white",
    width=12,
    command=delete_task
)
delete_button.pack(side=tk.LEFT, padx=5)

load_tasks()

root.mainloop()
