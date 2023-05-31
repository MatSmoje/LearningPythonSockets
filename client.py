# This client is designed to connect to manjarin hacklab :]
import socket

HEADERSIZE=15

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.99',2894))


full_msg = ''




while True:
    full_msg = ''
    new_msg = True

    while True:
        msg = s.recv(HEADERSIZE)
        if new_msg:
            print(f"new msg length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("latin1")

        if len(full_msg)-HEADERSIZE == msglen:
            print("FULL MSG RECVD")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''

    print(full_msg)



