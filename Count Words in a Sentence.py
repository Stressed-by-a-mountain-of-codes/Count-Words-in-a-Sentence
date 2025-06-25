import tkinter as tk
from tkinter import messagebox
import pyttsx3
import re
import string

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def count_text(event=None):
    text = entry.get()
    if not text.strip():
        messagebox.showerror("Input Error", "Please enter some text.")
        return

    if remove_punct_var.get():
        text = ''.join(c for c in text if c not in string.punctuation)

    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    char_count = len(text.replace(" ", ""))

    result = f"Words: {word_count} | Characters (no spaces): {char_count}"
    result_label.config(text=result, fg="darkblue")
    speak(f"{word_count} words and {char_count} characters")
    root.after(3000, reset)

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Word & Character Counter")
root.geometry("520x260")
root.resizable(False, False)

tk.Label(root, text="Enter your sentence:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center", width=50)
entry.pack(pady=5)
entry.bind("<Return>", count_text)

remove_punct_var = tk.BooleanVar()
punct_checkbox = tk.Checkbutton(root, text="🧹 Remove punctuation", variable=remove_punct_var, font=("Arial", 10))
punct_checkbox.pack()

tk.Button(root, text="Count", font=("Arial", 12), command=count_text).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=480)
result_label.pack(pady=10)

entry.focus()
root.mainloop()
