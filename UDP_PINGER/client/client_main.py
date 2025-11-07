import socket, time
from ..utils.colors import *
server_name = '127.0.0.1'
server_port = 12000
i, n = 0, 5
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)
print(Fore.CYAN + "🔵 Client is starting to send PING requests...\n")
for seq in range(n):
    message = f"PING {seq} {time.time()}"
    start = time.time()
    try:
        client_socket.sendto(message.encode(), (server_name, server_port))
        DATA, SERVER = client_socket.recvfrom(1024)
        end = time.time()
        rtt = round((end - start) * 1000, 2)
        print(Fore.GREEN + f"✅ SERVER : {SERVER} : 📩 {DATA.decode()} : ⏱ RTT : {rtt} ms")
        i = i+1
    except socket.timeout:
        print(Fore.RED + f"❌ The Period expired for request #{seq}\n")
client_socket.close()
print(Fore.CYAN + "🔚 Client socket closed.")
print(Fore.CYAN + "TOTAL SECCUSSFULL : ", i, " / FAILED : ", n-i)