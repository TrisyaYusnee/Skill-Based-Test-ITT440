import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.110.128"
    port = 8080

    client_socket.connect((host, port))

    try:
        pressure = float(input("Enter pressure value in bar: "))
        client_socket.sendall(str(pressure).encode())

        response = client_socket.recv(1024).decode()
        atmosphere_standard = float(response)

        print(f"Pressure in atmosphere-standard: {atmosphere_standard} atm")
    except ValueError:
        print("Invalid input. Please provide a valid pressure value in bar.")

    client_socket.close()

if __name__ == "__main__":
    main()
