import socket
import threading
import pygame

HEADER=64
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())

ADDR=(SERVER, PORT)

FORMAT='utf-8'

clients=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clients.connect(ADDR)

nickname=input("Enter your name: ")
def recieve():
     while True:
        try:
            msg=clients.recv(1024).decode(FORMAT)
            if msg=='Enter your gamename: ':
                clients.send(nickname.encode(FORMAT))
                print('You joined the server.')
            
            else:
                print(msg)
        except:
            print('Error happened')
            clients.close()
            break




def send():
    while True:
        typemsg=input()
        msg_len=len(f'{nickname}: {typemsg}')
        send_len=str(msg_len).encode(FORMAT)
        clients.send(send_len)
     
        clients.send(f'{nickname}: {typemsg}'.encode(FORMAT))




recievethread=threading.Thread(target=recieve)
recievethread.start()
typemsgthread=threading.Thread(target=send)
typemsgthread.start()