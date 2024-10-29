# The function to calculate the focal length
def cal_focal(distance, h_pic, h_real):
# one distance is required to calculate the focal length once (calibration)
    """
    Parameters
    ------------------
    distance : the distance from the camera to the objekt in mm
    h_pic : the height of the object in pixel
    h_real : the height of the object in mm

    Returns
    ------------------
    returns the focal length of the used camera in pixel
    """
    return distance * (h_pic / h_real)

# The function calculates the distance between the camera and the objekt
def cal_distance(h_pic, h_real, focal):
    """
    Parameters
    ------------------
    h_pic : the height of the object in pixel
    h_real : the height of the object in mm
    focal : the focal length of the camera in mm

    Returns
    ------------------
    returns the distance from the camera to the objekt in mm
    """
    return focal * (h_real / h_pic)





