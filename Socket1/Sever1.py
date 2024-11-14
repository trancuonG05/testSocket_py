import socket

HOST = "127.0.0.1" #LOOPBACK
SERVER_PORT = 65432
FORMAT = "utf8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket de mo len va host, khong the truyen du lieu bang socket nay 

s.bind((HOST, SERVER_PORT))
s.listen()

print("SEVER SIDE")
print("Sever:", HOST, SERVER_PORT)
print("Waiting for Client")

conn, addr = s.accept() #Goi ham accept() de khi nao co 1 client nao do ket noi vao thi accept va tra ve 2 gia tri addr va conn
#conn cung la socket, dung de trao doi du lieu that su

print("client add:", addr)
print("conn:", conn.getsockname())

username = conn.recv(1024).decode(FORMAT)
print("username:", username)

input()

