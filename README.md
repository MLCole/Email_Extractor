# 📧 Email Extractor GUI

A lightweight Python desktop application to **extract email addresses** from any block of text, with easy formatting and one-click clipboard copy.

Built with `tkinter` for the UI and `pyperclip` for clipboard functionality.

Inspired by the need to quickly extract emails from marketing lists, customer exports, or chat logs without messing with Excel or regex tools.


---

## 🚀 Features

- ✅ Extracts all valid email addresses from pasted text
- 🧹 Cleans and deduplicates results (basic regex-based extraction)
- 🔁 Toggle between:
  - Newline-separated format
  - Comma-separated format
- 📋 Copy extracted emails directly to your clipboard
- 🖼️ Simple, scrollable GUI — no terminal needed

---

## 🖥️ Screenshot

<img width="802" height="728" alt="image" src="https://github.com/user-attachments/assets/b9c7e15d-9373-45df-bf9c-5ceca274650f" />

---

## 🔧 Requirements

- Python 3.7+
- Dependencies:
  - `pyperclip` (for clipboard functionality)

Install with:

```bash
pip install pyperclip
````

---

## 📝 How to Use

1. **Run the script**:

   ```bash
   python email_extractor_gui.py
   ```

2. **Paste any text** into the input box.

3. Click **"Extract Emails"** to extract all valid email addresses.

4. Use the **"Format"** button to toggle between newline-separated or comma-separated lists.

5. Click **"Copy to Clipboard"** to grab the list for pasting into emails, spreadsheets, etc.

---

## 📦 Packaging (Optional)

If you want to create a standalone `.exe`:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed email_extractor_gui.py
```

The executable will be in the `dist/` folder.

---

## 📄 License
    MIT License — free to use, modify, and distribute.
