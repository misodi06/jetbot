# calculates the focal length
def cal_focal(distance, height_lens, height_object):
# one distance is required to calculate the focal length once (calibration)
    return distance * (height_lens / height_object)

