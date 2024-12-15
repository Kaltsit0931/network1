import socket
import threading

def listen_for_messages(sock):
    while True:
        try:
            message, addr = sock.recvfrom(1024)
            print(f"Received message: {message.decode('utf-8')}")
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind(('', 0))  # Bind to an available port

    # Start a thread to listen for incoming messages
    listener_thread = threading.Thread(target=listen_for_messages, args=(client,))
    listener_thread.start()

    print("Client started. Type your messages below:")
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        client.sendto(message.encode('utf-8'), ('<broadcast>', 5000))

    client.close()

if __name__ == "__main__":
    main()
