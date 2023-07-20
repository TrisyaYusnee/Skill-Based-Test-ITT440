import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.110.128"
    port = 8888

    client_socket.connect((host, port))

    try:
        quote = client_socket.recv(1024).decode()
        print(f"Received Quote of the Day: {quote}")
    except:
        print("Error receiving quote")

    client_socket.close()

if __name__ == "__main__":
    main()
