import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   #works as a door
ip = "10.1.0.8"
port = 9999

target_ip = (ip,port)
message = input("write your message : ")
encrypt_message = message.encode("ascii")
s.sendto(encrypt_message,target_ip)
data = s.recvfrom(120)
print(data)