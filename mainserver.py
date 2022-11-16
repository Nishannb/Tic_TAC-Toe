import socket
import threading



HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())

ADDR=(SERVER, PORT)

FORMAT='utf-8'

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)

    
players=[]
gamenames=[]

def display(command):
    for player in players:
        player.send(command)

def handle_player(player, gamename):
    print(f'New connection: {gamename}')
    game_active=True
    while game_active:
        try:
            command_len=player.recv(HEADER).decode(FORMAT)
            
            
            command_len=int(command_len)
            command=player.recv(command_len)
            display(command)
        except:
            index=players.index(player)
            players.remove(player)
            player.close()
            gamename=gamenames[index]
            display(f'{gamename} left the game'. encode(FORMAT))
            gamenames.remove(gamename)
            # game_active=False
            break
            
    player.close()

def startgame():
    print('Server is ON and listening')
    while True:
        server.listen()
        player, address=server.accept()
        player.send('Enter your gamename: '.encode(FORMAT))
        gamename=player.recv(2048).decode(FORMAT)
        
        gamenames.append(gamename)
        players.append(player)
        display(f'{gamename} joined the game'.encode(FORMAT))
        thread=threading.Thread(target=handle_player, args=(player, gamename))
        thread.start()
        print(f'Active players: {threading.active_count()-1}')
        
        


startgame()





        

