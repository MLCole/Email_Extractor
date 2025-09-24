import re
import tkinter as tk
from tkinter import messagebox, scrolledtext
import pyperclip

# Global state for current formatting mode
current_format = "newline"
stored_emails = []

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)

def format_emails(emails, fmt):
    if fmt == "comma":
        return ", ".join(emails)
    return "\n".join(emails)

def on_extract():
    global stored_emails
    input_text = input_box.get("1.0", tk.END)
    stored_emails = extract_emails(input_text)
    update_output()

def update_output():
    result_box.delete("1.0", tk.END)
    if stored_emails:
        formatted = format_emails(stored_emails, current_format)
        result_box.insert(tk.END, formatted)
    else:
        result_box.insert(tk.END, "No email addresses found.")

def toggle_format():
    global current_format
    current_format = "comma" if current_format == "newline" else "newline"
    format_button.config(
        text=f"Format: {'Comma-Separated' if current_format == 'comma' else 'Newline-Separated'}"
    )
    update_output()

def copy_to_clipboard():
    text = result_box.get("1.0", tk.END).strip()
    if text:
        try:
            pyperclip.copy(text)
            messagebox.showinfo("Copied", "Emails copied to clipboard!")
        except pyperclip.PyperclipException:
            messagebox.showerror("Error", "Could not copy to clipboard.")
    else:
        messagebox.showwarning("Empty", "Nothing to copy.")

# GUI Setup
root = tk.Tk()
root.title("Email Extractor")
root.geometry("640x550")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Paste your text here:", font=("Arial", 12)).pack(pady=5)
input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=75, height=10)
input_box.pack(pady=5)

tk.Button(root, text="Extract Emails", command=on_extract, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=8)

format_button = tk.Button(root, text="Format: Newline-Separated", command=toggle_format, bg="#FFC107", fg="black", font=("Arial", 11))
format_button.pack(pady=5)

tk.Label(root, text="Extracted Emails:", font=("Arial", 12)).pack(pady=5)
result_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=75, height=8)
result_box.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white", font=("Arial", 11)).pack(pady=10)

# Run
root.mainloop()
