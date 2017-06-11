import socket

class UDP(object):

    def Server(IPaddress,Port,SendData):
        
        
        udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        serverinfo = (IPaddress,Port)

        udp_server.bind(serverinfo)

        dt , udp_client = udp_server.recvfrom(int(5000))

        udp_server.sendto(SendData.encode("utf-8"),udp_client)

        return dt


    def Client(IPaddress,Port,SendData):


        udp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        serverinfo = (IPaddress,Port)

        udp_client.sendto(SendData.encode("utf-8"),serverinfo)

        dt , udp_server = udp_client.recvfrom(int(5000))


        return dt


"""
https://github.com/Ryu-ji/Deplobox-Modules/blob/0.5/UDP/UDP.py
MIT License

Copyright (c) 2017 Ryu-ji

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""