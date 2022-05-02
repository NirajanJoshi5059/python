import socket

s=socket.socket()#socket(IPv4/IPv6, tcp/udp)

print("Socket Created")

s.bind(('localhost',9999))#we use port number and ip address

s.listen(3)
print("Connecting...")

while True:
    c, addr =s.accept()
    print("Connected ", addr)
    c.send(bytes("Hello welcome to socket testing", 'utc-8'))
    c.close()