import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(2)
try:
    client_socket.connect(("localhost", 51000))
except Exception:
    print("Connection error")

while True:
    message = input("-> ")

    if message == "exit" or message == "stop server":
        try:
            client_socket.send(message.encode())
        except Exception:
            pass

        client_socket.close()
        print("Exit")
        break

    message = message.encode()
    try:
        client_socket.send(message)
        message = client_socket.recv(4096)
    except Exception:
        print("Server isn't available")
        print("Exit")
        client_socket.close()
        break

    message = message.decode()
    print("Server answer: {}".format(message))
