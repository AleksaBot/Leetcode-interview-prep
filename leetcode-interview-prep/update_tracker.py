import csv
from datetime import date
import tkinter as tk
from tkinter import messagebox

def submit_entry():
    # Gather inputs
    problem_name = entry_problem_name.get()
    leetcode_number = entry_leetcode_number.get()
    topic = entry_topic.get().replace(" ", "")
    difficulty = entry_difficulty.get().capitalize()
    notes = entry_notes.get()

    if not problem_name or not topic or not difficulty:
        messagebox.showerror("Missing Info", "Please fill out all required fields.")
        return

    today = date.today().isoformat()
    status = "✅ Complete"

    # Append to CSV
    row = [today, problem_name, topic, difficulty, status, notes]
    with open("progress_tracker.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

    messagebox.showinfo("Success", "Tracker updated!")
    clear_fields()

def clear_fields():
    entry_problem_name.delete(0, tk.END)
    entry_leetcode_number.delete(0, tk.END)
    entry_topic.delete(0, tk.END)
    entry_difficulty.delete(0, tk.END)
    entry_notes.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("LeetCode Progress Tracker")

tk.Label(root, text="Problem Name *").grid(row=0, column=0, sticky="e")
tk.Label(root, text="LeetCode #").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Topic *").grid(row=2, column=0, sticky="e")
tk.Label(root, text="Difficulty *").grid(row=3, column=0, sticky="e")
tk.Label(root, text="Notes").grid(row=4, column=0, sticky="e")

entry_problem_name = tk.Entry(root, width=40)
entry_leetcode_number = tk.Entry(root, width=40)
entry_topic = tk.Entry(root, width=40)
entry_difficulty = tk.Entry(root, width=40)
entry_notes = tk.Entry(root, width=40)

entry_problem_name.grid(row=0, column=1)
entry_leetcode_number.grid(row=1, column=1)
entry_topic.grid(row=2, column=1)
entry_difficulty.grid(row=3, column=1)
entry_notes.grid(row=4, column=1)

tk.Button(root, text="Add to Tracker", command=submit_entry).grid(row=5, columnspan=2, pady=10)

root.mainloop()
