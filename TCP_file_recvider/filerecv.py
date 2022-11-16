import socket 
import sys

if __name__ == "__main__" :
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if len(sys.argv) == 2 :
        file_name = sys.argv[1]
        IPAddress = input('please input your IP address')
        server.bind((IPAddress,9500))
        server.listen(5)

        conn,addr = server.accept()
        file_len = int(conn.recv(1024).decode('utf-8'))
        print(file_len)
        conn.send(b'OK')
        file_byte = b''
        while file_len > 0 :
            file_byte = file_byte + conn.recv(1024)
            file_len -= 1024
            print(file_len)
        file = open(file_name,'w',newline='')
        file.write(file_byte.decode('utf-8'))
    

    
