# Echo client program
import socket

HOST = "192.168.0.10"   # The remote host
PORT = 30002            # The same port as used by the server

# Connect to the UR5
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Test that the connection is working
s.send ("set_digital_out(2,True)" + "\n")
data = s.recv(1024)
s.close()

print ("Received", repr(data))
