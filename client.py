# This client is designed to connect to manjarin hacklab :]
import socket
import sys
import pickle

port = int(sys.argv[1])

HEADERSIZE=10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.99',port))


full_msg = ''




while True:
    full_msg = b''
    new_msg = True

    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"NewMSGLen: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg
        
        if len(full_msg)-HEADERSIZE == msglen:
            print("FULL MSG RECVD")
            print(full_msg[HEADERSIZE:])

            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b''

    


