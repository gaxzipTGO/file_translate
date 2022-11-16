import json
import socket

if __name__ == '__main__' :
    file_path = input("please input file_input_path")
    file_name = input("please input file_name")
    file_data = input("please input file")
    file = open(file_data,'r')
    file_byte = file.read()
    
    data = {
        "file_data" : file_byte,
        "file_path" : file_path,
        "file_name" : file_name
    }
    jsondata = json.dumps(data)
    jsonfile = {
        "file" :True,
        "data" : data
    }
    
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("169.254.138.194",9500))
    send_byte = json.dumps(jsonfile).encode()
    try :
        client.send(str(len(send_byte)).encode())
        ack = client.recv(1024)
        if ack == b'OK' :
            # print(json.dumps(file_byte).encode())
            print(len(send_byte))
            # while len(send_byte) > 0 :
            client.sendall(send_byte)
                # send_byte = send_byte[1024:]
                # if client.recv(1024) == b'ACK' :
                #     continue
                # else :
                #     raise OSError('send file not succelly')
            print(client.recv(1024).decode('utf-8'))
    except Exception as e :
        print(str(e))


    