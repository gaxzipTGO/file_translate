import socket 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",5000))
server.listen(5)

conn,addr = server.accept()
file_len = int(conn.recv(1024).decode('utf-8'))
print(file_len)
conn.send(b'OK')
file = b''
while file_len > 0 :
    file = file + conn.recv(1024)
    file_len -= 1024
    print(file_len)

print(file)
