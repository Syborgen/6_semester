import socket

print("Server start")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 51000))
server_socket.listen(1)
message = str()

while True:
    # stop server?
    if message == "stop server":
        server_socket.close()
        print("Server was closed")
        break

    print("Server is waiting client...")
    client_socket, client_address = server_socket.accept()
    client_socket.settimeout(30)
    print("Client have connected with address {}".format(client_address))
    # process for client
    while True:
        try:
            message = client_socket.recv(4096)
        except Exception:
            print("Client isn't available\n")
            break

        message = message.decode()
        if message == "exit":
            client_socket.close()
            break
        print("Receive from client ({}): {}".format(client_address, message))
        print("Server send: {}".format(message))
        client_socket.send(message.encode())
