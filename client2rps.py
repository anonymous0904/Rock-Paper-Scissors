import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8888))
    player_number = client_socket.recv(1024).decode()

    print("You are player2")

    choice = input("Enter your choice (rock, paper, scissors): ")
    client_socket.send(choice.encode())
    result = client_socket.recv(1024).decode()
    print(result)
    ms="ceva"
    client_socket.send(ms.encode())
    final=client_socket.recv(1024).decode()

    while final!="final":
        choice = input("Enter your choice (rock, paper, scissors): ")
        client_socket.send(choice.encode())
        result= client_socket.recv(1024).decode()
        print(result)
        client_socket.send(ms.encode())
        final=client_socket.recv(1024).decode()


if __name__ == "__main__":
    main()
