
import socket
import threading


nickname=input('Enter your nickname: ')
disconnect_msg="disconnect"
HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())

ADDR=(SERVER, PORT)

FORMAT='utf-8'

SOCKETCLIENT=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SOCKETCLIENT.connect(ADDR)
def receive():
    while True:
        try:
            firstmsg=SOCKETCLIENT.recv(2048).decode(FORMAT)
            if firstmsg=='Enter your nickname: ':
                SOCKETCLIENT.send(nickname.encode(FORMAT))
            else:
                print(firstmsg)
        except:
            print('Error happened')
            SOCKETCLIENT.close()
            break
        
        

def send():
    while True:
        usermsg=input()
        msg_len=len(f'{nickname}: {usermsg}')
        send_len=str(msg_len).encode(FORMAT)
        SOCKETCLIENT.send(send_len)
        # message=f'{nickname}: {usermsg}'
        SOCKETCLIENT.send(f'{nickname}: {usermsg}'.encode(FORMAT))
    
    


recievethread=threading.Thread(target=receive)
recievethread.start()
typemsgthread=threading.Thread(target=send)
typemsgthread.start()

        


