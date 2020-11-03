# Echo client program
import socket
import time

HOST = "192.168.0.10"   # The remote host
PORT = 30002            # The same port as used by the server


def MoveToObject(pose,rx,ry,rz):

    print "Starting MoveToObject Function"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    time.sleep(0.5)

    print "Robot Moves to a point above object"
    s.send ("movej(p[x,y,z,rx,ry,rz], a=0.1, v=0.1)" + "\n")
    time.sleep(10)

    print "Program finish"
    time.sleep(1)
    data = s.recv(1024)
    s.close()
    print ("Received", repr(data))
    print "Status data received from robot"
    print "I have compiled MoveToObject"
