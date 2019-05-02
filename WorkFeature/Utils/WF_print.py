# -*- coding: utf-8 -*-
from WorkFeature.Utils.WF_Utils import print_msg


def print_point(point, msg=""):
    """ Print x,y and z of a point:vector.
    """
    if point.__class__.__name__ != "Vector":
        print_msg("Not a Vector to print !")
        return

    print_msg(str(msg) + " " +
              "x =" + str(point.x) + ", "
              "y =" + str(point.y) + ", "
              "z =" + str(point.z))
    return


def print_segment(segment, msg=""):
    """ Print x,y and z of 2 points:segment.
    """
    point1 = segment[0]
    point2 = segment[1]
    if point1.__class__.__name__ != "Vector":
        print_msg("Not a Vector to print !")
        return
    if point2.__class__.__name__ != "Vector":
        print_msg("Not a Vector to print !")
        return
    print_msg(str(msg) +
              "x1 =" + str(point1.x) + ", "
              "y1 =" + str(point1.y) + ", "
              "z1 =" + str(point1.z) + ", "
              "x2 =" + str(point2.x) + ", "
              "y2 =" + str(point2.y) + ", "
              "z2 =" + str(point2.z))
    return
