import tkinter as tk
from tkinter import messagebox
from zxcvbn import zxcvbn

# -----------------------------
# Password Analysis Function
# -----------------------------
def analyze_password():
    pwd = password_entry.get()

    if pwd == "":
        messagebox.showerror("Error", "Please enter a password")
        return

    result = zxcvbn(pwd)
    score = result['score']
    crack_time = result['crack_times_display']['offline_fast_hashing_1e10_per_second']

    if score <= 1:
        strength = "VERY WEAK"
    elif score == 2:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    output_label.config(
        text=f"Score: {score}/4\nStrength: {strength}\nCrack Time: {crack_time}"
    )

# -----------------------------
# Wordlist Generator Function
# -----------------------------
def generate_wordlist():
    name = name_entry.get()
    pet = pet_entry.get()
    year = year_entry.get()

    if name == "" or year == "":
        messagebox.showerror("Error", "Name and Birth Year are required")
        return

    words = []
    words.append(name)
    words.append(name + "123")
    words.append(name + year)
    words.append(name + "@123")

    if pet != "":
        words.append(pet)
        words.append(pet + year)

    file = open("wordlist.txt", "w")
    for w in words:
        file.write(w + "\n")
    file.close()

    messagebox.showinfo(
        "Success",
        f"Wordlist saved as wordlist.txt\nTotal passwords generated: {len(words)}"
    )

# -----------------------------
# GUI Window
# -----------------------------
root = tk.Tk()
root.title("Password Strength Analyzer & Wordlist Generator")
root.geometry("450x500")

# -----------------------------
# Password Section
# -----------------------------
tk.Label(root, text="Password Strength Analyzer", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Enter Password:").pack()
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Analyze Password", command=analyze_password).pack(pady=10)

output_label = tk.Label(root, text="", fg="blue")
output_label.pack(pady=10)

# -----------------------------
# Wordlist Section
# -----------------------------
tk.Label(root, text="Wordlist Generator", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Pet Name (optional):").pack()
pet_entry = tk.Entry(root, width=30)
pet_entry.pack()

tk.Label(root, text="Birth Year:").pack()
year_entry = tk.Entry(root, width=30)
year_entry.pack(pady=5)

tk.Button(root, text="Generate Wordlist", command=generate_wordlist).pack(pady=15)

# -----------------------------
# Start GUI
# -----------------------------
root.mainloop()
