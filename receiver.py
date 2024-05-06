import socket #to share a message
S = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #creating a socket
ip = "10.1.0.168"
port = 4545  # 0 ---65636

complete_address = (ip,port)      
S.bind(complete_address)

while True:        #to receive message from all 
    data = S.recvfrom(120)    #buffer size decide
    message = data[0]
    message = message.decode('ascii')
    message = message+"\n"   #to add at last new msg file(append)
    sender_ip = data[1][0]
    filename = sender_ip+".txt"       
    with open(filename,'a+') as file:
        file.write(message)

    reply_mess = "Thank you"
    reply = reply_mess.encode("ascii")
    S.sendto(reply,sender_ip)
    print(data)