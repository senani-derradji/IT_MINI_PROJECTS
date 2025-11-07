import random, socket
from ..utils.colors import *
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 12000))
print(Fore.CYAN + "🔵 The server is ready to receive UDP messages on port 12000 ....")
while True:
    message, client_address = server_socket.recvfrom(1024)
    print(Fore.YELLOW + f"📩 {client_address} : {message.decode()}")
    if random.random() < 0.1:
        rec_message = message.decode()
        modified_message = "PONG: ".encode() + rec_message.split(" ")[1].encode()
        print(Fore.GREEN + f"✅ Sending modified message to {client_address}: {modified_message.decode()}")
        server_socket.sendto(modified_message, client_address)
    else: print(Fore.RED + f"❌ PACKET LOST from {client_address}")