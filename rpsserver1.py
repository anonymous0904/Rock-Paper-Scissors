import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8888))
    server_socket.listen(2)
    print("Waiting for players...")

    player1, addr1 = server_socket.accept()
    print("Player 1 connected")
    player1.send(b'You are Player 1')

    player2, addr2 = server_socket.accept()
    print("Player 2 connected")
    player2.send(b'You are Player 2')

    round_count = 3
    ok=0
    track=0
    final="not"
    while round_count :
        choice1 = player1.recv(1024).decode()
        choice2 = player2.recv(1024).decode()

        if not choice1 or not choice2:
            break

        result = determine_winner(choice1, choice2)
        if result == "It's a tie!":
            tracker = 0
        elif result == "Player 1 wins!" :
            tracker = 1
        elif result=="Player 2 wins!" :
            tracker = -1

        print(f"Player 1 chose {choice1}, Player 2 chose {choice2}. {result}")

        track = track + tracker
        if track == -2 or (track==-1 and round_count==1):
            final="final"
            final_result = "Player 2 wins the game!"
            player1.send(final_result.encode())
            player2.send(final_result.encode())
            ms1=player1.recv(1024).decode()
            ms2=player2.recv(1024).decode()
            player1.send(final.encode())
            player2.send(final.encode())
            ok = 1
            player1.close()
            player2.close()
            server_socket.close()
            break
        elif track == 2 or(track==1 and round_count==1):
            final="final"
            final_result = "Player 1 wins the game!"
            player1.send(final_result.encode())
            player2.send(final_result.encode())
            ms1=player1.recv(1024).decode()
            ms2=player2.recv(1024).decode()
            player1.send(final.encode())
            player2.send(final.encode())
            ok = 1
            player1.close()
            player2.close()
            server_socket.close()
            break
        else:
            player1.send(result.encode())
            player2.send(result.encode())
            ms1=player1.recv(1024).decode()
            ms2=player2.recv(1024).decode()
            player1.send(final.encode())
            player2.send(final.encode())

        round_count = round_count-1

    if track == 0:
        final="final"
        final_result = "It's a tie for the game!"
        player1.send(final_result.encode())
        player2.send(final_result.encode())
        ms1=player1.recv(1024).decode()
        ms2=player2.recv(1024).decode()
        player1.send(final.encode())
        player2.send(final.encode())
    elif track<0 and not ok:
        final_result = "Player 2 wins the game!"
        final="final"
        player1.send(final_result.encode())
        player2.send(final_result.encode())
        ms1=player1.recv(1024).decode()
        ms2=player2.recv(1024).decode()
        player1.send(final.encode())
        player2.send(final.encode())
    elif track>0 and not ok:
        final="final"
        final_result = "Player 1 wins the game!"
        player1.send(final_result.encode())
        player2.send(final_result.encode())
        ms1=player1.recv(1024).decode()
        ms2=player2.recv(1024).decode()
        player1.send(final.encode())
        player2.send(final.encode())


    player1.close()
    player2.close()
    server_socket.close()

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    elif (choice1 == 'rock' and choice2 == 'scissors') or \
         (choice1 == 'paper' and choice2 == 'rock') or \
         (choice1 == 'scissors' and choice2 == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


if __name__ == "__main__":
    main()
