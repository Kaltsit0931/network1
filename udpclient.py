import socket
import threading

# Set up UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 8080))  # Listen on all interfaces

def receive_messages():
    while True:
        data, addr = sock.recvfrom(1024)
        if addr != ('client_ip', 8080):
            print(f"Received message: {data.decode()}")

def send_message():
    while True:
        message = input("Enter message to send: ")
        sock.sendto(message.encode(), ('<broadcast>', 8080))  # Send to the broadcast address

if __name__ == '__main__':
    # Start receiving thread
    thread = threading.Thread(target=receive_messages)
    thread.daemon = True
    thread.start()

    # Start sending thread
    send_message()
