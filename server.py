import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
            # Broadcast message to all clients
            for client in clients:
                if client != client_socket:
                    client.send(message.encode('utf-8'))
        except:
            break
    client_socket.close()

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5000))
    server.listen(5)
    print("Server listening on port 5000")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
