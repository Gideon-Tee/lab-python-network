'''
This server code listens for a connection from a client
It then sends a file (an image in this case, 'dodge-challenger.jpg') to the client upon request

'''


import socket

# Server Configuration
HOST = '127.0.0.1'
PORT = 65432
FILE_PATH = "dodge-challenger.jpg"


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)  # Listen for one client
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            request = conn.recv(1024).decode('utf-8')  # Receive client request
            if request == "GET_FILE":
                print("Client requested the file.")
                try:
                    with open(FILE_PATH, "rb") as file:
                        file_data = file.read()
                        conn.sendall(file_data)  # Send the image to the client
                        print("File sent successfully.")
                except FileNotFoundError:
                    print("File not found.")
                    conn.sendall(b"ERROR: File not found.")
            else:
                print("Invalid request received.")
                conn.sendall(b"ERROR: Invalid request.")


if __name__ == "__main__":
    start_server()
