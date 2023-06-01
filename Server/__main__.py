import socket
import random
import pickle

HEADERSIZE = 10



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = random.randint(2000,10000)
s.bind(("0.0.0.0", port))

print(f"port: {port}")

s.listen(5)

while True:
    conn, addr = s.accept()
    print(f"Connection from {addr} have been established!")

    d = {1: 'hey', 2: 'there'}
    msg = pickle.dumps(d)

    msg =bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8")+msg
    conn.send(msg)

    #userConnected=f"Connection from {addr} have been established!"
    #conn.sendall(bytes(userConnected, "utf-8"))
