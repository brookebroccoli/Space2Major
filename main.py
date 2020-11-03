# Echo client program
import socket
import time

# Import all functions from MoveToObject 
from MoveToObject import *
# Or can be written as
# import MoveToObject as MoveCommand
# Used as MoveCommand.MoveToObject(1,1,1,0,0,0)


HOST = "192.168.0.10"   # The remote host
PORT = 30002            # The same port as used by the server

# For compilation purposes
x = 1
y = 1
z = 1

# Need to find these positions in the Lab. These are set positions
HomePosition        = [x, y, z]
PhotoPosition       = [x, y, z]
ContainerPosition   = [x, y, z]

# Assign home position (we will have to do this in the lab - get base position
# - whatever you desire to be base)
# NB: can just make this the photo positon

RunLoop = 1
count   = 1

while True:
    # First find the photo positon coordinates - manually move
    # Now assign this as the photo position as a POSE (coords + angles)
    # Move the UR5 there - using MoveToObject
    #MoveToObject(PhotoPosition,0,0,0)


    ### Rock finding(rockinvalid[]) (Elle)
    ### Feed in matrix of invalid rock coordianates [x,y,z]
    RockCoordinates     = [x, y, z]


    ### Take the coordinates given by rock finding
    # Move arm to rock coordinates
    #MoveToObject(RockCoordinates,0,0,0)


    ### Linear movement down to get rock


    # Determine if we can pick up rock - by trying to lift it. If the force is
    # bigger then threshold value then leave that rock
    # Save the location of the unliftable rock
    # Else; rock is liftable, call Jacks function to pick up rock


    # Go to container position
    #MoveToObject(ContainerPosition,0,0,0)
    ### Unclamp gripper to drop rock in container

    if count == 9:
        print "Exiting while loop"
        break

    print "Count is up to ", count
    count += 1

print "Main has compiled"
