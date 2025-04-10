import csv
from datetime import date
import tkinter as tk
from tkinter import messagebox

def submit_entry():
<<<<<<< HEAD
    # Gather inputs
    problem_name = entry_problem_name.get()
    leetcode_number = entry_leetcode_number.get()
    topic = entry_topic.get().replace(" ", "")
    difficulty = entry_difficulty.get().capitalize()
    notes = entry_notes.get()

=======
    # Get input values
    problem_name = entry_problem_name.get().strip()
    leetcode_number = entry_leetcode_number.get().strip()
    topic = entry_topic.get().strip().replace(" ", "")
    difficulty = entry_difficulty.get().strip().capitalize()
    notes = entry_notes.get().strip()

    # Validate required fields
>>>>>>> cd9dcdb (Update tracker script)
    if not problem_name or not topic or not difficulty:
        messagebox.showerror("Missing Info", "Please fill out all required fields.")
        return

    today = date.today().isoformat()
<<<<<<< HEAD
    status = "✅ Complete"

    # Append to CSV
    row = [today, problem_name, topic, difficulty, status, notes]
    with open("progress_tracker.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

    messagebox.showinfo("Success", "Tracker updated!")
    clear_fields()
=======
    status = "Complete"
    row = [today, problem_name, topic, difficulty, status, notes]

    # Append to CSV using UTF-8
    try:
        with open("progress_tracker.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)
        messagebox.showinfo("Success", "Tracker updated successfully!")
        clear_fields()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write to file:\n{e}")
>>>>>>> cd9dcdb (Update tracker script)

def clear_fields():
    entry_problem_name.delete(0, tk.END)
    entry_leetcode_number.delete(0, tk.END)
    entry_topic.delete(0, tk.END)
    entry_difficulty.delete(0, tk.END)
    entry_notes.delete(0, tk.END)

<<<<<<< HEAD
# GUI setup
root = tk.Tk()
root.title("LeetCode Progress Tracker")

=======
# GUI layout
root = tk.Tk()
root.title("LeetCode Progress Tracker")

# Labels
>>>>>>> cd9dcdb (Update tracker script)
tk.Label(root, text="Problem Name *").grid(row=0, column=0, sticky="e")
tk.Label(root, text="LeetCode #").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Topic *").grid(row=2, column=0, sticky="e")
tk.Label(root, text="Difficulty *").grid(row=3, column=0, sticky="e")
tk.Label(root, text="Notes").grid(row=4, column=0, sticky="e")

<<<<<<< HEAD
=======
# Entry fields
>>>>>>> cd9dcdb (Update tracker script)
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

<<<<<<< HEAD
tk.Button(root, text="Add to Tracker", command=submit_entry).grid(row=5, columnspan=2, pady=10)

=======
# Submit button
tk.Button(root, text="Add to Tracker", command=submit_entry).grid(row=5, columnspan=2, pady=10)

# Start GUI
>>>>>>> cd9dcdb (Update tracker script)
root.mainloop()
