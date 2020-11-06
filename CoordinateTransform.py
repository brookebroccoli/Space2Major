#Returns the new pose from a camera determined XYZ position
#must pass in xyz of object from camera and position this object was taken from
def CameraXYZToPose(CameraXYZ, FromPose)
    #fixed vector length from TCP to lens
    TcpToCamera = np.array([0,0,0]) #must measure this

    #declare numpy arrys for vector addition
    CameraToObject = np.array(CameraXYZ)
    BaseToTCP = np.array(FromPose)

    #vector addition, note still must include vector diff from TCP to lens
    NewPose = BaseToPhotoTCP + TcpToCamera + CameraToObject
    return NewPose
