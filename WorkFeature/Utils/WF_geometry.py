# -*- coding: utf-8 -*-
import Part
import Draft
import FreeCAD as App
from FreeCAD import Base
from WorkFeature.Utils.WF_Utils import print_msg
from WorkFeature.Utils.WF_selection import get_ActiveDocument
from WorkFeature.Utils.WF_print import print_point


def angleBetween(e1, e2):
    """ Return the angle (in degrees) between 2 edges.
    """
    if isinstance(e1, Part.Edge) and isinstance(e2, Part.Edge):
        # Create the Vector for first edge
        v1 = e1.Vertexes[-1].Point
        v2 = e1.Vertexes[0].Point
        ve1 = v1.sub(v2)
        # Create the Vector for second edge
        v3 = e2.Vertexes[-1].Point
        v4 = e2.Vertexes[0].Point
        ve2 = v3.sub(v4)
    elif isinstance(e1, Base.Vector) and isinstance(e2, Base.Vector):
        ve1 = e1
        ve2 = e2
    elif isinstance(e1, Part.Edge) and isinstance(e2, Base.Vector):
        v1 = e1.Vertexes[-1].Point
        v2 = e1.Vertexes[0].Point
        ve1 = v1.sub(v2)
        ve2 = e2
    elif isinstance(e1, Base.Vector) and isinstance(e2, Part.Edge):
        ve1 = e1
        v3 = e2.Vertexes[-1].Point
        v4 = e2.Vertexes[0].Point
        ve2 = v3.sub(v4)
    else:
        return

    angle = ve1.getAngle(ve2)
    import math
    return math.degrees(angle), angle


def minMaxObjectsLimits(objs, info=0):
    """ Return the min and max limits along the 3 Axis for all selected objects.
    """
    xmax = xmin = ymax = ymin = zmax = zmin = 0
    if objs is None:
        print_msg("ERROR: objs=None, leaving minMaxObjectsLimits()")
        return xmax, xmin, ymax, ymin, zmax, zmin

    m_objs = objs
    m_num = len(m_objs)
    if m_num < 1:
        print_msg("ERROR: len(m_objs) <1, leaving minMaxObjectsLimits()")
        return xmax, xmin, ymax, ymin, zmax, zmin

    import sys
    if sys.version < '3.0.0':
        max_val = sys.maxint
        min_val = -sys.maxint - 1
    # for python 3.0 use sys.maxsize
    else:
        max_val = sys.maxsize
        min_val = -sys.maxsize - 1
    xmin = ymin = zmin = max_val
    xmax = ymax = zmax = min_val
    # print_msg(str(xmin))
    # print_msg(str(xmax))
    m_doc = get_ActiveDocument()

    for m_obj in m_objs:
        if hasattr(m_obj, 'TypeId'):
            m_type = m_obj.TypeId
        else:
            m_type = m_obj.Type
        # pm_type = m_obj.TypeId
        if info != 0:
            print_msg("m_obj       : " + str(m_obj))
            # print_msg("m_obj.Type  : " + str(m_obj.Type))
            # print_msg("m_obj.TypeId: " + str(m_obj.TypeId))
            print_msg("m_obj.TypeId: " + str(m_type))

        # if m_obj.TypeId[:6] == "Length":
        if m_type[:6] == "Length":
            if info != 0:
                print_msg("Found a Length object!")
            box = m_obj.Shape.BoundBox
        # elif m_obj.TypeId[:4] == "Mesh":
        elif m_type[:4] == "Mesh":
            if info != 0:
                print_msg("Found a Mesh object!")
            box = m_obj.Mesh.BoundBox
        # elif m_obj.TypeId[:6] == "Points":
        elif m_type[:6] == "Points":
            if info != 0:
                print_msg("Found a Points object!")
            box = m_obj.Points.BoundBox
        # elif m_obj.TypeId[:4] == "Part":
        elif m_type[:4] == "Part":
            if info != 0:
                print_msg("Found a Part object!")
            box = m_obj.Shape.BoundBox
        # elif m_obj.TypeId[:6] == "Sketch":
        elif m_type[:6] == "Sketch":
            if info != 0:
                print_msg("Found a Sketch object!")
            # box = Draft.draftify(m_obj,delete=False).Shape.BoundBox
            m_wire = Draft.draftify(m_obj, delete=False)
            if info != 0:
                print_msg("m_wire = " + str(m_wire))
            if type(m_wire) is list:
                for m_sub_wire in m_wire:
                    if info != 0:
                        print_msg("m_sub_wire = " + str(m_sub_wire))
                    box = m_sub_wire.Shape.BoundBox
                    xmax = max(xmax, box.XMax)
                    xmin = min(xmin, box.XMin)
                    ymax = max(ymax, box.YMax)
                    ymin = min(ymin, box.YMin)
                    zmax = max(zmax, box.ZMax)
                    zmin = min(zmin, box.ZMin)
                    App.getDocument(str(m_doc.Name)).removeObject(str(m_sub_wire.Label))
            else:
                box = m_wire.Shape.BoundBox
                App.getDocument(str(m_doc.Name)).removeObject(str(m_wire.Label))
        else:
            continue
        if info != 0:
            print_msg("box = " + str(box))
        xmax = max(xmax, box.XMax)
        xmin = min(xmin, box.XMin)
        ymax = max(ymax, box.YMax)
        ymin = min(ymin, box.YMin)
        zmax = max(zmax, box.ZMax)
        zmin = min(zmin, box.ZMin)
    if info != 0:
        print_msg("Limits of all objects selected are:")
        print_msg("xmax =" + str(xmax) + ", "
                  "xmin =" + str(xmin) + ", "
                  "ymax =" + str(ymax) + ", "
                  "ymin =" + str(ymin) + ", "
                  "zmax =" + str(zmax) + ", "
                  "zmin =" + str(zmin))
    return xmax, xmin, ymax, ymin, zmax, zmin


def centerObjectsPoint(objs, info=0):
    """ Return the center point of all selected Objects.
    """
    xmax, xmin, ymax, ymin, zmax, zmin = minMaxObjectsLimits(objs, info=info)
    center = App.Vector((xmax + xmin) / 2.0, (ymax + ymin) / 2.0, (zmax + zmin) / 2.0)
    if info != 0:
        print_point(center, "Center of all objects selected is: ")
    return center
