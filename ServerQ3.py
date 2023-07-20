import socket

def bar_to_atmosphere(pressure):
    return pressure * 0.986923

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "0.0.0.0"  # Listen on all available interfaces
    port = 8080

    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is listening...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection established with {addr}")

        try:
            data = conn.recv(1024).decode()
            pressure = float(data)
            atmosphere_standard = bar_to_atmosphere(pressure)
            response = str(atmosphere_standard).encode()
            conn.sendall(response)
        except ValueError:
            conn.sendall(b"Invalid input. Please provide a valid pressure value i>

        conn.close()

if __name__ == "__main__":
    main()
