import tkinter as tk
from tkinter import messagebox
import subprocess

def run_python_script():
    try:
        subprocess.run(["python", "your_script.py"], check=True)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to execute the Python script")

def main():
    root = tk.Tk()
    root.title("Desktop Application")
    root.geometry("300x200")

    icon = tk.PhotoImage(file="icon.png")
    root.iconphoto(True, icon)

    label = tk.Label(root, text="Desktop Application", font=("Arial", 14))
    label.pack(pady=10)

    button = tk.Button(root, text="Run Script", command=run_python_script)
    button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
