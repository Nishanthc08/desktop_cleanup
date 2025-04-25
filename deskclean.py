# DeskClean - Desktop Organizer GUI
# Author: Nishanth C
# Description: Sorts desktop files into folders by file type

import os
import shutil
import tkinter as tk
from tkinter import messagebox

# Define your desktop path
DESKTOP_PATH = os.path.expanduser("~/Desktop")

# Map of extensions to folder names
EXTENSION_MAP = {
        'Documents': ['.pdf', '.docx', '.txt', '.odt'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Videos': ['.mp4', 'mkv', '.avi', '.mov'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp', '.java'],
}

def clean_desktop():
    files = [f for f in os.listdir(DESKTOP_PATH) if os.path.isfile(os.path.join(DESKTOP_PATH, f))]
    if not files:
        messagebox.showinfo("DeskClean", "Your desktop is already clean!")
        return

    moved_count = 0

    for file in files:
        filepath = os.path.join(DESKTOP_PATH, file)
        ext = os.path.splitext(file)[1].lower()

        placed = False
        for folder, extensions in EXTENSION_MAP.items():
            if ext in extensions:
                folder_path = os.path.join(DESKTOP_PATH, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(filepath, os.path.join(folder_path, file))
                moved_count += 1
                placed = True
                break

        if not placed:
            misc_path = os.path.join(DESKTOP_PATH, "Misc")
            os.makedirs(misc_path, exist_ok=True)
            shutil.move(filepath, os.path.join(misc_path, file))
            moved_count += 1
    
    messagebox.showinfo("DeskClean", f"Desk cleaned! {moved_count} file(s) sorted.")

# GUI Setup
root = tk.Tk()
root.title("DeskClean")
root.geometry("300x180")
root.resizable(False, False)

title = tk.Label(root, text="DeskClean", font=("Helvetica", 18, "bold"))
title.pack(pady=15)

desc = tk.Label(root, text="Click below to clean your desktop.", font=("Helvetica", 10))
desc.pack()

btn = tk.Button(root, text="Clean My Desk", command=clean_desktop, bg="#3cb371", fg="white", font=("Helvetica", 12, "bold"))
btn.pack(pady=20)

root.mainloop()

