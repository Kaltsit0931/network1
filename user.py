import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('h4', 5000))

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        recipient = input("Enter recipient (e.g., h2): ")
        message = input("Enter your message: ")
        full_message = f"To {recipient}: {message} from {client.getsockname()[0]}"
        client.send(full_message.encode('utf-8'))

if __name__ == "__main__":
    main()
