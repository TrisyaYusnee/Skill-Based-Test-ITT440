import socket
import threading
import random

# List of quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It always seems impossible until it's done. - Nelson Mandela",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
]

def handle_client(client_socket):
    quote = random.choice(quotes).encode()
    client_socket.send(quote)
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "0.0.0.0"
    port = 8888

    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server is listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
