# Echo client program
import socket
import time

# Import all functions from MoveToPose
from UR5Movement import *

HOST = "192.168.0.100"      # The remote host
PORT = 30002                # The same port as used by the server

#ConnectToUR5()
# Connect to the UR5
print "Connecting to UR5"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Test that the connection is working
s.send ("set_digital_out(1,True)" + "\n")
print "Connected to UR5!"

# Need to find these positions in the Lab. These are set positions in m, rad
PhotoPosition = [0.36985, -0.38075, 0.65190, 0.047, 3.1478, 0.015]
ContainerPosition = [0.222167, 0.13817, 0.47490, 2.382, -2.056, 0.018]
#print "Starting MoveToObject Function"
#MoveToPose(PhotoPosition)
#time.sleep(6)

x   = PhotoPosition[0]
y   = PhotoPosition[1]
z   = PhotoPosition[2]
rx  = PhotoPosition[3]
ry  = PhotoPosition[4]
rz  = PhotoPosition[5]

print "UR5 moving to Photo Position"
s.send ("movej(p[0.36985,-0.38075,0.65190,0.047,3.1478,0.015], a=1, v=1)" + "\n")
time.sleep(10)

print "UR5 moving to Container Position"
s.send ("movej(p[0.22640,0.14486,0.27460,3.154,-0.030,0.036], a=1, v=1)" + "\n")
time.sleep(20)


print "Program finish"

# Test that the connection is working
s.send ("set_digital_out(1,False)" + "\n")

print "Closing Connection"
s.close()
print "Main has compiled"
