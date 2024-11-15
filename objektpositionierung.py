import math

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
    focal : the focal length of the camera in pixel

    Returns
    ------------------
    returns the distance from the camera to the objekt in mm
    """
    return focal * (h_real / h_pic)

# The function calculates the horizontal and vertical angle between the object and the camera
def cal_angle(x_pic, y_pic, focal):
    """
    Parameters
    -------------------
    x_pic : the x coordinate of the object in pixel
    y_pic : the y coordinate of the object in pixel
    focal : the focal length of the camera in pixel

    Returns
    --------------------
    returns the horizontal and vertical angle of the camera in degrees
    """
    vertical_angle = math.atan(y_pic/focal)
    horizontal_angle = math.atan(x_pic/focal)
    return horizontal_angle, vertical_angle

# The function calculates the position of the Object in the world coordinate system
def cal_position(x_cam_world, y_cam_world, z_cam_world, angle_h, angle_v, d):
    """
    Parameters
    :param x_cam_world: x coordinate of the camera in mm
    :param y_cam_world: y coordinate of the camera in mm
    :param z_cam_world: z coordinate of the camera in mm
    :param angle_h: horizontal angle between the camera and the object in degrees
    :param angle_v: vertical angle between the camera and the object in degrees
    :param d: distance from the camera to the object in mm
    :return: the position of the object in mm
    """
    x_object_world = x_cam_world + d
    y_object_world = y_cam_world + (math.tan(angle_h) * d)
    z_object_world = z_cam_world + (math.tan(angle_v) * d)

    return x_object_world, y_object_world, z_object_world

# open cv



