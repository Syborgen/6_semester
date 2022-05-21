import socket
import threading


def rclient_handle(client_socket, client_address):
    print("Handler start for {}".format(client_address))
    while True:
        try:
            message = client_socket.recv(4096)
        except Exception:
            print("Client isn't available\n")
            break

        message = message.decode()
        if message == "exit":
            client_socket.close()
            print("Client {} was closed".format(client_address))
            break
        print("Receive from client ({}): {}".format(client_address, message))
        message = message.upper()
        print("Server {} send: {}".format(threading.get_ident(), message))
        client_socket.send(message.encode())


print("Start server")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 51000))
server_socket.listen(5)

while True:
    socket, address = server_socket.accept()
    socket.settimeout(60)
    thread = threading.Thread(target=client_handler, args=(socket, address))
    thread.start()
