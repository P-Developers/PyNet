import socket

class TCP(object):

    def Server(IPaddress,Port,SendData):

        tmp = None

        tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        serverinfo = (IPaddress,Port)

        tcp_server.bind(serverinfo)

        tcp_server.listen(5)


        tcp_client , acceptor = tcp_server.accept()

        dt = tcp_client.recv(5000)

        tmp = dt

        tcp_client.sendall(SendData)

        return tmp


    def Client(IPaddress,Port,SendData):

        tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        serverinfo = (IPaddress,Port)

        tcp_client.connect(serverinfo)

        tcp_client.sendall(SendData.encode("utf-8"))

        dt = tcp_client.recv(5000)

        return dt




if __name__ == "__main__":
    print(TCP.Client("127.0.0.1",9999,"HELLO"))