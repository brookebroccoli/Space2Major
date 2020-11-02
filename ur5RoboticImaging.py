import socket
import time
import numpy as np
import os


def server(HOST_IP, PORT_NUM):
    HOST = HOST_IP    # The remote host, as a string
    PORT = PORT_NUM              # The same port as used by the server
    print("Connecting to socket...\n")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("Socket connected!\n")

def movejp(pose,a=0.1,v=0.5,t=0,r=0):
    script = "movej(p[{},{},{},{},{},{}], a={}, v={}, t={}, r={})"
    script = script.format(pose[0], pose[1], pose[2], pose[3], pose[4], pose[5], a, v, t, r)
    s.send(bytes(script, 'utf-8') + bytes("\n", 'utf-8'))
    time.sleep(0.5)

def movel(position,a=0.1,v=0.5,t=0,r=0):
    script = "movel(p[{},{},{},{},{},{}], a={}, v={}, t={}, r={})"
    script = script.format(pose[0], pose[1], pose[2], pose[3], pose[4], pose[5], a, v, t, r)
    s.send(bytes(script, 'utf-8') + bytes("\n", 'utf-8'))
    time.sleep(0.5)

def movej(angles,a=0.1,v=0.5,t=0,r=0):
    base = angles[0]
    shoulder = angles[1]
    elbow = angles[2]
    w1 = angles[3]
    w2 = angles[4]
    w3 = angles[5]
    script = "movel([{},{},{},{},{},{}], a={}, v={}, t={}, r={})"
    script = script.format(base, shoulder, elbow, w1, w2, w3, a, v, t, r)
    s.send(bytes(script, 'utf-8') + bytes("\n", 'utf-8'))
    time.sleep(0.5)

def movec( p_via, p_to, a=0.5, v=0.1, r=0.1, mode=1):
    script = "movec(p[{},{},{},{},{},{}], p[{},{},{},{},{},{}], a={}, v={}, r={}, mode={})"
    script = script.format(p_via[0], p_via[1], p_via[2], p_via[3], p_via[4], p_via[5], p_to[0], p_to[1], p_to[2], p_to[3], p_to[4], p_to[5],  a, v, r, mode)
    s.send(bytes(script, 'utf-8') + bytes("\n", 'utf-8'))
    time.sleep(0.5)
