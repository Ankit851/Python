# Importing Required Modules
import socket as s
import threading as thd
import os

print("\t\t\t\tWelcome to Ankit's ChatApp")
print("\t\t\t\t---------------------")

# Create a Socket and Bind IP and PORT to It
skt = s.socket(s.AF_INET, s.SOCK_DGRAM)
localIP = "192.168.1.2"
skt.bind((localIP, 8081))

# Get Partner's IP to chat with
usrIP = "192.168.1.9"
print()

# Function to Recieve and Print the Message
def recv_msg():
    while True:
        msgRcv = skt.recvfrom(1024)
        if msgRcv[0].decode() == "quit":
            print("Person is Offline!")
            os._exit(1)
        print("\n\t\t\t\t\t\t\t\t\t" + msgRcv[1][0] + ": " + msgRcv[0].decode())


# Function to Send the Message
def send_msg():
    while True:
        data = input().encode()
        msgSent = skt.sendto(data, (usrIP, 8081))
        if data.decode() == "quit":
            os._exit(1)

# Thread for Send Message Function
send_thd = thd.Thread(target=send_msg)

# Threads for Recieve Message Function
rcv_thd = thd.Thread(target=recv_msg)

# Starting Threads
send_thd.start()
rcv_thd.start()
