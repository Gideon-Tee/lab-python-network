import socket
import os


# Client Configuration
HOST = '127.0.0.1'  # Server address
PORT = 65432        # Server port
SAVE_PATH = "received_image.jpg"


def request_file():
    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))  # Connect to the server
            client_socket.sendall(b"GET_FILE")  # Send image request
            print("Request for file sent to the server.")

            # Receive the image data
            with open(SAVE_PATH, "wb") as file:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    file.write(data)

            print(f"Image received and saved to {os.getcwd()}/{SAVE_PATH}")

    except ConnectionRefusedError as e:
        print(f"Couldn't connect to the server\n{e}")


if __name__ == "__main__":
    request_file()
