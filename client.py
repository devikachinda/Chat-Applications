import socket
import threading

HOST = '127.0.0.1'  # Server IP
PORT = 65432        # Server port

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # Server closed connection
                print("\n[INFO] Server closed the connection.")
                break
            print(f"\nFriend: {message}\nYou: ", end='', flush=True)
        except:
            # Socket error or client closed
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.daemon = True
    thread.start()

    print("Connected to the server. Start chatting!")
    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            print("[INFO] Closing connection...")
            client_socket.shutdown(socket.SHUT_RDWR)
            client_socket.close()
            break
        try:
            client_socket.send(message.encode('utf-8'))
        except:
            print("[ERROR] Failed to send message. Connection might be closed.")
            break

if __name__ == "__main__":
    start_client()
