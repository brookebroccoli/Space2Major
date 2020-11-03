# Echo client program
import socket
import time

HOST = "192.168.0.10"   # The remote host
PORT = 30002            # The same port as used by the server


def ConnectToUR5():
    print "Connecting to UR5"
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.connect((HOST, PORT))
    print "Connected to UR5!"


def MoveToPose(pose,rx,ry,rz):

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

# Rock coords is fed in as [x,y,z] with reference to the cameras position. We
# need to transform this to a coordinate with reference to the UR5 base
def CameraToBaseCoordTransform( VRockCoordinatesCamera ):
    print "CameraToBaseCoordTransform Function"
    # VTcpToCamera = hand measured vector [x,y,z] with TCP as the reference frame
    # VBaseToTcp = [x,y,z]. This has to be received via the get_current_TCP
    #                   pose function. Need to figure out receiving
    # VBaseToCamera = VBaseToTcp + VTcpToCamera

    # Now calculate VBaseToRock
    # RockCoordinatesBase = VBaseToCamera + VRockCoordinatesCamera
