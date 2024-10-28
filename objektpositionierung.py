# The function to calculate the focal length
def cal_focal(distance, height_camera, height_object):
# one distance is required to calculate the focal length once (calibration)
    """
    Parameters
    ------------------
    distance : the distance from the camera to the objekt in mm
    height_camera : the height of the camera in mm
    height_object : the height of the object in mm

    Returns
    ------------------
    returns the focal length of the used camera
    """
    return distance * (height_camera / height_object)



