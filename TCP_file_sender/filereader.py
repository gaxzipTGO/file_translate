import json
import socket
import sys

if __name__ == '__main__' :

    if len(sys.argv) == 2 :
        file_data = sys.argv[1]
        IPAdress = input("please input distination IP address")
        file = open(file_data,'r')
        file_byte = file.read().encode()
        
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((IPAdress,9500))
        try :
            client.send(str(len(file_byte)).encode())
            ack = client.recv(1024)
            if ack == b'OK' :
                client.send(file_byte)
                print(client.recv(1024).decode('utf-8'))
        except Exception as e :
            print(str(e))


    