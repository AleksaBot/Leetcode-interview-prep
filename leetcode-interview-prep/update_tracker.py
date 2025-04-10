import csv
from datetime import date

# === Prompt for Details ===
problem_name = input("Problem Name (e.g. Two Sum): ").strip()
leetcode_number = input("LeetCode Problem Number (e.g. 1): ").strip()
topic = input("Topic (e.g. Arrays, Trees): ").strip().replace(" ", "")
difficulty = input("Difficulty (Easy/Medium/Hard): ").strip().capitalize()
status = "✅ Complete"
notes = input("Any notes? (optional): ").strip()

# === Construct Row ===
today = date.today().isoformat()
row = [
    today,
    f"{problem_name}",
    topic,
    difficulty,
    status,
    notes
]

# === Append to CSV ===
csv_path = "progress_tracker.csv"

try:
    with open(csv_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)
        print("✅ Tracker updated successfully!")
except FileNotFoundError:
    print("❗ Tracker file not found. Make sure you're in the right folder.")
