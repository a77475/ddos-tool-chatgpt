import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup

class BruteForceApp:
    def __init__(self, master):
        self.master = master
        master.title("Brute Force Tool - macOS Style")
        master.geometry("400x200")

        self.create_menu()

        self.label_url = ttk.Label(master, text="URL:")
        self.label_url.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_url = ttk.Entry(master)
        self.entry_url.grid(row=1, column=1)

        self.label_username = ttk.Label(master, text="Username:")
        self.label_username.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_username = ttk.Entry(master)
        self.entry_username.grid(row=2, column=1)

        self.label_password = ttk.Label(master, text="Password:")
        self.label_password.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_password = ttk.Entry(master, show="*")
        self.entry_password.grid(row=3, column=1)

        self.button_start = ttk.Button(master, text="Start Brute Force", command=self.start_bruteforce)
        self.button_start.grid(row=4, columnspan=2, pady=10)

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.master.quit)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Help", menu=help_menu)

    def start_bruteforce(self):
        url = self.entry_url.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Perform brute force
        success = self.bruteforce(url, username, password)
        if success:
            messagebox.showinfo("Brute Force Result", "Login successful!")
        else:
            messagebox.showerror("Brute Force Result", "Login failed!")

    def bruteforce(self, url, username, password):
        # Make a POST request with provided username and password
        data = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post(url, data=data)
            # Check if login was successful based on response content
            soup = BeautifulSoup(response.content, "html.parser")
            if "Login successful" in soup.get_text():
                return True
            else:
                return False
        except Exception as e:
            print("Error: ", e)
            messagebox.showerror("Error", f"An error occurred: {e}")
            return False

    def show_about(self):
        messagebox.showinfo("About", "Brute Force Tool\nVersion 1.0\nDeveloped by Your Name")

def main():
    root = tk.Tk()
    app = BruteForceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
