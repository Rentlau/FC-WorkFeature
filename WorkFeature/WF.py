# -*- coding: utf-8 -*-

"""
***************************************************************************
*   Thanks to original ideas, codes, and support from:                   *
*   - Javier Martinez Garcia 2014, 2015 for ideas and first WF codes      *
*     for the code on parallelism of two faces, forTour camera code...    *
*   - Jonathan Wiedemann for Gui ideas and for view codes 2014            *
*     and support                                                         *
*   - NormandC for his support                                            *
*   - Yorick for his support and for FlattenWire3Points Macro             *
*   - galou_breizh for macro which creates a circle from 3 selected points*
*   - Eriossoltero for macro Ellipse-Center+2Points                       *
*   - Ulrich Brammer for Geodesic dome code                               *
*   - Wmayer Many Thanks for active help on testing and debbuging         *
*   - Gaël Ecorchard for HighlightDifference Macro                        *
*   - lorenz_l for Beam tool Macro                                        *
*   Special thanks to Mario52 for diverse MACRO codes as FCCamera,        *
*   cutCircle, cutWire, Delta xyz, bounding box ...                       *
*   and other diverse pieces of codes                                     *
*   and all discussions, support, advices, help...merci Mario             *
*   Thanks also to those I forget.                                        *
***************************************************************************
***************************************************************************
*   FreeCAD Work Features / version 2019-01                               *
*   Copyright (c) 2014-2019 <rentlau_64>                                  *
*   Code rewrite by <rentlau_64>                                          *
*   Copyright (c) 2014, 2015 Javier Martinez Garcia                       *
*   Copyright (c) 2013, 2014 Jonathan Wiedemann                           *
*   Copyright (c) 2014, 2015 Mario52                                      *
*   Copyright (c) 2013 galou_breizh                                       *
*   Copyright (c) 2015 Ulrich Brammer <ulrich1a[at]users.sourceforge.net> *
*   Copyright (c) Eriossoltero                                            *
*   Copyright (c) 2015 Gaël Ecorchard                                     *
*                                                                         *
*   This file is a supplement to the FreeCAD CAx development system.      *
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU Lesser General Public License (LGPL)    *
*   as published by the Free Software Foundation; either version 2 of     *
*   the License, or (at your option) any later version.                   *
*   for detail see the COPYING and COPYING.LESSER text files.             *
*                                                                         *
*   This software is distributed in the hope that it will be useful,      *
*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
*   GNU Library General Public License for more details.                  *
*                                                                         *
*   You should have received a copy of the GNU Library General Public     *
*   License along with this macro; if not, write to the Free Software     *
*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
*   USA or see <http://www.gnu.org/licenses/>                             *
***************************************************************************
"""
# First two lines to be able to launch with python
import sys
import os.path

import time
import math
import itertools

import FreeCAD
import FreeCADGui as Gui
from FreeCAD import Base
from pivy.coin import *
from pivy import coin
import Part
import Draft

from PySide import QtCore, QtGui

import WorkFeature.WFGui as WFGui

from WorkFeature.ParCurve.WF_ObjParCurve_2016 import *
from WorkFeature.WF_ObjRot import *

from WorkFeature.Utils.WF_Utils import *
from WorkFeature.Utils.WF_Utils import print_msg
from WorkFeature.Utils.WF_geometry import *
from WorkFeature.Utils.WF_selection import *
from WorkFeature.Utils.WF_print import print_point
from WorkFeature.Utils.WF_translate import _translate


global myRelease
myRelease = "2019_05_01"

####################################################################################
# assume the Icons directory in the same directory as this MACRO file
WF_ICONS_PATH = os.path.dirname(__file__) + "/Icons"

# use "icons" as prefix which we used in the .ui file
QtCore.QDir.addSearchPath("icons", WF_ICONS_PATH)

# LineColor
# red  = 1.0  # 1 = 255
# green = 0.0  #
# blue = 0.0  #
red = (1.00, 0.00, 0.00)
green = (0.00, 0.67, 0.00)
blue = (0.33, 0.00, 1.00)
orange = (1.00, 0.67, 0.00)
flag_for_face = True

# Some Global variables
global myDialog
myDialog = None
global myObject
myObject = None
global centerOfMass
centerOfMass = True
global verbose
verbose = 0
global tolerance
tolerance = 1e-10
global biColor
biColor = 0
global objCopy
objCopy = 0

global sweep_solid
sweep_solid = True
global sweep_frenet
sweep_frenet = True
global sweep_transition
sweep_transition = 2
global imageAxisScale
imageAxisScale = "XY"
global sweep_all
sweep_all = True
global BBox_volum
BBox_volum = False
global BBox_info
BBox_info = False

m_numberLinePart = 2
m_numberLineCut = 2
m_numberPointCutWire = 2
m_numberAxisCutWire = 2
m_numberRandomPoint = 1
m_numberCircleCut = 2
m_numberPlane = 1
m_numberLine = 1
m_numberLine2 = 1
m_numberPoint = 1
m_distanceLinePoint = 0.0
m_distanceRandomPoints = 10.0
m_extensionTwoPointsAxis = 0.0
m_extensionLinePointAxis = 0.0
m_extensionLine = 0.0
m_radiusCircle = 10.0
m_extensionFaceNormal = 0.0
m_extensionPlanePointPlane = 0.0
m_anglePlaneAxisPlane = 0.0
m_lengthPlane = 10.0
m_distPlane = 10.0
m_distLine = 10.0
m_lengthImage = 100.0
m_angleLine = 45.0
m_angleAlignFaces = 0.0
m_angleAlignEdges = 0.0
m_angleAlignMainAxis = 0.0
m_angleRevolve = 360.0
m_distPoint = 10.0
m_diameterCylinder = 2.0
m_lengthCylinder = 20.0
m_lengthCube = 2.0
m_widthCube = 2.0
m_heightCube = 20.0
m_widthPlane = 10.0
m_extensionPlane = 50.0
m_extensionAxis = 50.0
m_attach_point = "Mid"
m_projection_plane = "All"
m_projection_plane2 = "All"
m_letter = "A"

m_cut_selectObjects = []
m_angleCutObject = 0.0
m_thicknessCutObject = 0.0
m_diameterSphere = 10.0
m_diameterDome = 10.0
m_frequencyDome = 2
m_sizeLetter = 2.0

m_callback = None
m_clickForPoint = True
m_clickForAxis = True
m_stack = []
m_set = 'Set'


def verbose_toggled(flag):
    """ Respond to the change of verbose flag.
    """
    global verbose
    verbose = 0
    if flag is True:
        verbose = 1
    print_msg("verbose flag is: " + str(verbose))


def biColor_toggled(flag):
    """ Respond to the change of biColor flag.
    """
    msg = verbose
    global biColor
    biColor = 0
    if flag is True:
        biColor = 1
    if msg != 0:
        print_msg("biColor flag is: " + str(biColor))


def copy_toggled(flag):
    """ Respond to the change of Object copy flag.
    """
    msg = verbose
    global objCopy
    objCopy = 0
    if flag is True:
        objCopy = 1
    if msg != 0:
        print_msg("Object copy flag is: " + str(objCopy))


def init_min_max():
    """ Return min and max values from System.
    min_val, max_val = init_min_max
    """
    import sys
    if sys.version < '3.0.0':
        max_val = sys.maxint
        min_val = -sys.maxint - 1
    # for python 3.0 use sys.maxsize
    else:
        max_val = sys.maxsize
        min_val = -sys.maxsize - 1
    return min_val, max_val


def alignCamera(point1, point2, reverse=False, info=0):
    """ Align the camera along an Axis crossing the 2 points in input.
    reverse=True to exchange points 1 and 2
    """
    # Build vectors difference
    if reverse:
        v = point1.sub(point2)
    else:
        v = point2.sub(point1)
    if info != 0:
        print_msg("Vectors difference is:" + str(v))
    r = App.Rotation(App.Vector(0, 0, 1), v)
    if info != 0:
        print_msg("App.Rotation:" + str(r))
    # App.Rotation.Q: the rotation element as Quaternion
    Gui.ActiveDocument.ActiveView.setCameraOrientation(r.Q)



def get_typefromSelection(objectType="Edge", info=0):
    """ """
    m_num_obj, m_selEx, m_objs, m_objNames = get_InfoObjects(info=0, printError=False)
    m_found = False
    for m_i_o in range(m_num_obj):
        if m_found:
            break
        Sel_i_Object = m_selEx[m_i_o]
        Obj_i_Object = m_objs[m_i_o]
        Name_i_Object = m_objNames[m_i_o]
        if info != 0:
            print("Sel_i_Object = " + str(Sel_i_Object))
            print("Obj_i_Object = " + str(Obj_i_Object))
            print("Name_i_Object = " + str(Name_i_Object))
        SubObjects_Inside = Sel_i_Object.SubObjects
        for n in range(len(SubObjects_Inside)):
            SubObject = SubObjects_Inside[n]
            if info != 0:
                print("SubObject = " + str(SubObject))
                print("SubObject.ShapeType = " + str(SubObject.ShapeType))
            if SubObject.ShapeType == objectType:
                m_found = True
                break
    if m_found:
        return Sel_i_Object, Obj_i_Object, Name_i_Object
    else:
        return None, None, None


def reset_SelectedObjects(Selection, info=0):
    """ Reset the selection changed by Draft.rotate for example
    Selection is the original selection you want to reset. Must be saved before any
    change!
    """
    Gui.Selection.clearSelection()
    for Sel_i_Object in Selection:
        m_DocumentName = Sel_i_Object.DocumentName
        m_ObjectName = Sel_i_Object.ObjectName
        m_Object = Sel_i_Object.Object
        if info != 0:
            print_msg(str(m_Object))
        if len(Sel_i_Object.SubElementNames) == 0:
            if info != 0:
                print_msg(Sel_i_Object.ObjectName)
            Gui.Selection.addSelection(m_Object)
        else:
            for m_SubElementName in Sel_i_Object.SubElementNames:
                if info != 0:
                    m_finalName = str(m_DocumentName) + "." + str(m_ObjectName) + "." + str(m_SubElementName)
                    print_msg(m_finalName)
                Gui.Selection.addSelection(m_Object, str(m_SubElementName))


def get_axesFromSelectedObjects(info=0, printError=True):
    """ Return Selected_Axes as
    list of Edges
    """
    SelectedObjects = get_SelectedObjects(info=info, printError=False)
    Selected_Axes = []

    Number_of_Edges = SelectedObjects[1]
    Number_of_Faces = SelectedObjects[2]
    Number_of_Objects = len(SelectedObjects[6])

    if Number_of_Edges > 0:
        Edge_List = SelectedObjects[4]
        for m_edge in Edge_List:
            Selected_Axes.append(m_edge)

    if Number_of_Faces > 0:
        Face_List = SelectedObjects[5]
        for m_face in Face_List:
            Edge_List = m_face.Edges
            for m_edge in Edge_List:
                Selected_Axes.append(m_edge)

    if Number_of_Objects > 0:
        Object_List = SelectedObjects[6]
        for m_object in Object_List:
            for m_edge in m_object.Shape.Edges:
                Selected_Axes.append(m_edge)

    return Selected_Axes


def get_pointsFromSelectedObjects(info=0, printError=False):
    """ Return Selected_Points as
    list of Vertexes
    """
    SelectedObjects = get_SelectedObjects(info=info, printError=printError)
    Selected_Points = []
    Number_of_Points = SelectedObjects[0]
    Number_of_Edges = SelectedObjects[1]
    Number_of_Faces = SelectedObjects[2]
    Number_of_Objects = len(SelectedObjects[6])

    if Number_of_Points > 0:
        Point_List = SelectedObjects[3]
        for m_point in Point_List:
            Selected_Points.append(m_point)
    if Number_of_Edges > 0:
        Edge_List = SelectedObjects[4]
        for m_edge in Edge_List:
            Selected_Points.append(m_edge.Vertexes[0])
            Selected_Points.append(m_edge.Vertexes[-1])
    if Number_of_Faces > 0:
        Face_List = SelectedObjects[5]
        for m_face in Face_List:
            Edge_List = m_face.Edges
            for m_edge in Edge_List:
                Selected_Points.append(m_edge.Vertexes[0])
                Selected_Points.append(m_edge.Vertexes[-1])

    if Number_of_Objects > 0:
        Object_List = SelectedObjects[6]
        for m_object in Object_List:
            for m_vertex in m_object.Shape.Vertexes:
                Selected_Points.append(m_vertex)

    return Selected_Points


def get_wireListFromObjectName(objName, subSelection=True, msg=1):
    """ Return a list of wires from a selected object.
    objName is the name of the selected object
    subSelection is a flag to say if we want to select from the object:
        Only the wire selected (True) or
        All wires belonging to this object (False)
    """
    if (None in [objName]):
        return None
    m_wires = []
    m_name = objName

    if subSelection:
        if msg != 0:
            print("subSelection is True")
        for o in Gui.Selection.getSelectionEx():
            if msg != 0:
                print("ObjectName selected is: " + str(o.ObjectName))
            if str(o.ObjectName) == str(m_name):
                if msg != 0:
                    print("Found: " + str(m_name))
                for s in o.SubObjects:
                    if msg != 0:
                        print("SubObjects: " + str(s))
                    if hasattr(s, 'Shape'):
                        if msg != 0:
                            print("s.Shape: " + str(s.Shape))
                        if isinstance(s.Shape, Part.Compound):
                            for wire in s.Shape.Wires:
                                m_wires.append(Part.Wire([wire]))
                        if isinstance(s.Shape, Part.Edge) or isinstance(s.Shape, Part.Wire):
                            m_wires.append(Part.Wire([s.Shape]))
                    if hasattr(s, 'ShapeType'):
                        if msg != 0:
                            print("s.ShapeType: " + str(s.ShapeType))
                        if s.ShapeType == 'Edge':
                            m_wires.append(Part.Wire([s]))
                        if s.ShapeType == 'Face':
                            for e in s.Edges:
                                m_wires.append(Part.Wire([e]))
    else:
        if msg != 0:
            print("subSelection is False")
        for o in Gui.Selection.getSelectionEx():
            if msg != 0:
                print("ObjectName selected is: " + str(o.ObjectName))
            if str(o.ObjectName) == str(m_name):
                if msg != 0:
                    print("Found: " + str(m_name))
                if isinstance(o.Object.Shape, Part.Compound):
                    for wire in o.Object.Shape.Wires:
                        m_wires.append(Part.Wire([wire]))
                elif isinstance(o.Object.Shape, Part.Edge) or isinstance(o.Object.Shape, Part.Wire):
                    m_wires.append(Part.Wire([o.Object.Shape]))
                else:
                    m_wires = get_wireListFromObjectName(m_name, True, msg=msg)
                    # m_wires.append(Part.Wire([o.Object.Shape]))
    return m_wires


def get_mainAxesFromSelectedAxes(Selected_Axes, info=0):
    """Return a set of soretd main axes from selected list of axes.
    for new Input Axes: if an already existing axis with same direction exists,
    then the length of the input axis to be stored is only added to the existing one.
    If the input axis has a new direction then the axis with its length are stored.
    The list of axes is then sorted regarding their increasing length and returned.
    The list of points (extrema of axes) is also returned
    """
    m_axes = Selected_Axes
    Number_of_Axes = len(m_axes)
    if info != 0:
        print_msg("Number_of_Axes = " + str(Number_of_Axes))
    if Number_of_Axes >= 1:
        Selected_AxesWithLength = []
        Selected_Points = []
        # Generate list of (Axes, lengthOfAxes)
        for m_axis in m_axes:
            if info != 0:
                print_msg("m_axis.Vertexes[0] = " + str(m_axis.Vertexes[0]))
                print_msg("m_axis.Vertexes[-1] = " + str(m_axis.Vertexes[-1]))
            m_start = m_axis.Vertexes[0].Point
            m_end = m_axis.Vertexes[-1].Point
            m_diff = m_end.sub(m_start)
            # Check if the current m_axis is of Null length
            if abs(m_diff.x) <= tolerance and abs(m_diff.y) <= tolerance and abs(m_diff.z) <= tolerance:
                continue
            Selected_Points.append(m_start)
            Selected_Points.append(m_end)
            # Get the distance between the 2 points
            m_length = distanceBetween(m_start, m_end)
            m_A = (m_axis.Vertexes[-1].Point).sub(m_axis.Vertexes[0].Point).normalize()
            m_B = Base.Vector(0, 0, 0)
            m_dim = len(Selected_AxesWithLength)
            if info != 0:
                print_msg("m_length = " + str(m_length))
                print_msg("len(Selected_AxesWithLength) = " + str(m_dim))

            # Store the first axis with its length
            if m_dim == 0:
                Selected_AxesWithLength.append([m_axis, m_length])
                if info != 0:
                    print_msg("Selected_AxesWithLength = " + str(Selected_AxesWithLength))
            # Else look for existing axes to find if any already exist with the same direction
            else:
                m_found = False
                if info != 0:
                    print_msg("Selected_AxesWithLength = " + str(Selected_AxesWithLength))
                for m_axiswithlength in Selected_AxesWithLength:
                    m_C = (m_axiswithlength[0].Vertexes[-1].Point).sub(m_axiswithlength[0].Vertexes[0].Point).normalize()
                    # Look for colinear vectors
                    if abs((m_A.cross(m_C)).Length) <= 1e-10:
                        m_found = True
                        if info != 0:
                            print_msg("m_found = " + str(m_found))
                        m_axiswithlength[1] += m_length
                # Store the axis with its length in caseof new axis
                if not m_found:
                    Selected_AxesWithLength.append([m_axis, m_length])

        m_new_dim = len(Selected_AxesWithLength)
        if info != 0:
            print_msg("len(Selected_AxesWithLength) = " + str(m_new_dim))
            print_msg("before sort: Selected_AxesWithLength = " + str(Selected_AxesWithLength))
        # Sort stored axes by length
        Selected_AxesWithLength.sort(key=lambda x: x[1])
        if info != 0:
            print_msg("after sort: Selected_AxesWithLength = " + str(Selected_AxesWithLength))

        return Selected_AxesWithLength, Selected_Points

    return None, None


def getType(objs):
    if isinstance(objs, list):
        for obj in objs:
            print(str(type(obj)))


def getEdgeType(edge):
    "returns the type of geom this edge is based on"
    try:
        if isinstance(edge.Curve, Part.Line):
            return "Line"
        elif isinstance(edge.Curve, Part.Circle):
            return "Circle"
        elif isinstance(edge.Curve, Part.BSplineCurve):
            return "BSplineCurve"
        elif isinstance(edge.Curve, Part.BezierCurve):
            return "BezierCurve"
        elif isinstance(edge.Curve, Part.Ellipse):
            return "Ellipse"
        else:
            return "Unknown"
    except Exception as inst:
        print(inst.args)
        return "Unknown"


def getShapeType(subObject):
    try:
        if isinstance(subObject, Part.Edge):
            return "Edge"
        elif isinstance(subObject, Part.Vertex):
            return "Vertex"
        elif isinstance(subObject, Part.Face):
            return "Face"
        elif isinstance(subObject, Part.Wire):
            return "Wire"
        else:
            return "Unknown"
    except Exception as inst:
        print(inst.args)
        return "Unknown"


def definePropOfActiveObj():
    Gui.activeDocument().activeObject().LineColor = (1.00, 0.67, 0.00)
    Gui.activeDocument().activeObject().ShapeColor = (0.33, 1.00, 1.00)
    Gui.activeDocument().activeObject().Transparency = (50)


def addObjectToGrp(obj, grp, info=0):
    m_obj = obj
    m_grp = grp
    # adds object to the group
    m_grp.addObject(m_obj)
    if info != 0:
        print_msg("Object " + str(m_obj) + " added to Group: " + str(m_grp))


def addObjectToGrp2(obj, grp, info=0):
    m_obj = obj
    m_grp = grp
    # adds object to the group
    m_grp.addObject(m_obj)
    m_wire, m_del = Draft.downgrade(m_obj, delete=True)
    m_num = len(m_wire)
    for m_i in range(m_num):
        m_grp.addObject(m_wire[m_i])
        m_face, m_del1 = Draft.upgrade(m_wire[m_i], delete=True)
        m_num = len(m_face)
        for m_i in range(m_num):
            m_grp.addObject(m_face[m_i])


def minMaxVectorsLimits(vertx, info=0):
    """ Return the min and max limits along the 3 Axis for all selected objects.
    """
    xmax = xmin = ymax = ymin = zmax = zmin = 0
    if vertx is None:
        print_msg("ERROR: vertx=None, leaving minMaxVectorsLimits()")
        return xmax, xmin, ymax, ymin, zmax, zmin
    m_vertx = vertx
    m_num = len(m_vertx)
    if m_num < 1:
        print_msg("ERROR: len(m_vertx) <1, leaving minMaxVectorsLimits()")
        return xmax, xmin, ymax, ymin, zmax, zmin

    min_val, max_val = init_min_max()
    xmin = ymin = zmin = max_val
    xmax = ymax = zmax = min_val
    # print_msg(str(xmin))
    # print_msg(str(xmax))
    if info != 0:
        print_msg("Vectors = " + str(m_vertx))
    for m_vert in m_vertx:
        xmax = max(xmax, m_vert.x)
        xmin = min(xmin, m_vert.x)
        ymax = max(ymax, m_vert.y)
        ymin = min(ymin, m_vert.y)
        zmax = max(zmax, m_vert.z)
        zmin = min(zmin, m_vert.z)
    if info != 0:
        print_msg("Limits along the 3 Axis of all vectors selected are:")
        print_msg("xmax =" + str(xmax) + ", "
                  "xmin =" + str(xmin) + ", "
                  "ymax =" + str(ymax) + ", "
                  "ymin =" + str(ymin) + ", "
                  "zmax =" + str(zmax) + ", "
                  "zmin =" + str(zmin))
    return xmax, xmin, ymax, ymin, zmax, zmin


def meanObjects(objs, info=0):
    """ Return the mean of centers of mass of all selected objects.
    """
    mean = App.Vector(0.0, 0.0, 0.0)
    return mean



def baseObjectPoint(obj, info=0):
    """ Return the base point of selected Object.
    """
    placement = App.Placement(obj.Placement)
    base = placement.Base
    # rotation = placement.Rotation
    if info != 0:
        print_point(base, "Base of object selected is:")
    return base


def meanVectorsPoint(vertx, info=0):
    """ Return the mean point of all selected Vectors.
    """
    mean = App.Vector(0.0, 0.0, 0.0)
    m_vertx = vertx
    m_num = len(m_vertx)
    if info != 0:
        print_msg("m_vertx = " + str(m_vertx))
        print_msg("m_num  =  " + str(m_num))
    if m_num < 1:
        print_msg("ERROR: len(m_vertx) <1, meanVectorsPoint()")
        return mean
    m_list = []
    for m_vert in m_vertx:
        m_list.append(m_vert.x)
        m_list.append(m_vert.y)
        m_list.append(m_vert.z)

    import numpy
    V = numpy.array(m_list)
    Vre = V.reshape(m_num, 3)
    C = sum(Vre, 0) / m_num

    if info != 0:
        print_msg("V = " + str(V))
        print_msg("Vre = " + str(Vre))
        print_msg("C = " + str(C))

    mean = App.Vector(C[0], C[1], C[2])
    if info != 0:
        print_point(mean, "Mean of all vectors selected is: ")
    return mean


def centerBBVectorsPoint(vertx, info=0):
    """ Return the center point of the bounding box of all selected Vectors.
    """
    xmax, xmin, ymax, ymin, zmax, zmin = minMaxVectorsLimits(vertx, info=info)

    center = App.Vector((xmax + xmin) / 2.0, (ymax + ymin) / 2.0, (zmax + zmin) / 2.0)

    if info != 0:
        print_point(center, "Center of all vectors selected is: ")
    return center


def centerLinePoints(edge, index, number, info=0):
    """ Return the point at index/number of the Line.
    """
    Vector_A = edge.Vertexes[0].Point
    Vector_B = edge.Vertexes[-1].Point
    distance = Vector_B.sub(Vector_A).Length / 2

    # distance = edge.Length / 2
    if number != 0:
        distance = index * (edge.Length / number)
    # Vector_A = edge.valueAt( distance )
    Vector_A = Vector_A.add(Vector_B.sub(Vector_A).normalize().multiply(distance))
    if info != 0:
        print_point(Vector_A, "Point of line selected is: ")
    return Vector_A


def centerLinePoint(edge, info=0):
    """ Return the center point of the Line.
    """
    # Vector_A=edge.valueAt( 0.0 )
    Vector_A = edge.Vertexes[0].Point
    if info != 0:
        print_point(Vector_A, "Origin of line selected is: ")
    # Vector_B=edge.valueAt( edge.Length )
    Vector_B = edge.Vertexes[-1].Point
    if info != 0:
        print_point(Vector_B, "End of line selected is: ")
    Vector_MidPoint = Vector_B + Vector_A
    center = Vector_MidPoint.multiply(0.5)
    if info != 0:
        print_point(center, "Center of line selected is: ")
    return center


def digitsNumber(v):
    """ Return the number of digit for a given Float or Integer.

    Negative Sign is removed.
    Digits after the decimal sign are removed too.
    """
    try:
        return len(str(abs(int(v))))
    except Exception as inst:
        print(inst.args)
        return 0


def centerCirclePoint(edge, info=0):
    """ Return the center point of the circle.
    """
    center = edge.centerOfCurvatureAt(0.0)
    if info != 0:
        print_point(center, "Center of circle selected is:")
    return center


def distanceBetween(A, B):
    """ Return the distance between 2 points.
    """
    # if isinstance(A,App.Vector) and isinstance(B,App.Vector):
#     try:
#         line = Part.Line(A,B)
#         edge = line.toShape()
#         return edge.Length
#     except Part.OCCError:
#         return 0.0

    X1 = A.x
    Y1 = A.y
    Z1 = A.z

    X2 = B.x
    Y2 = B.y
    Z2 = B.z

    d_X = abs(X1 - X2)
    d_Y = abs(Y1 - Y2)
    d_Z = abs(Z1 - Z2)

    try:
        d = math.sqrt(pow(d_X, 2) + pow(d_Y, 2) + pow(d_Z, 2))
        return d
    except Exception as inst:
        print(inst.args)
        return 0.0


def edgeToVector(edge):
    """ Return a vector from an edge or a Part.line.
    """
    if isinstance(edge, Part.Shape):
        return edge.Vertexes[-1].Point.sub(edge.Vertexes[0].Point)
    elif isinstance(edge, Part.Line):
        return edge.EndPoint.sub(edge.StartPoint)
    else:
        print_msg("Error in edgeToVector(edge): not a good type of input" + str(type(edge)))
        return None


def colinearEdges(edge1, edge2, info=0, tolerance=1e-12):
    """ Return true if 2 edges are colinear.
    """
    if not isinstance(edge1.Curve, Part.Line):
        if info != 0:
            print_msg("colinearEdges: edge1 not instance of Part.Line !")
        return False
    if not isinstance(edge2.Curve, Part.Line):
        if info != 0:
            print_msg("colinearEdges: edge2 not instance of Part.Line !")
        return False
    A = edgeToVector(edge1)
    B = Base.Vector(0, 0, 0)
    C = edgeToVector(edge2)
    return colinearVectors(A, B, C, info=info, tolerance=tolerance)


def colinearVectors(A, B, C, info=0, tolerance=1e-12):
    """ Return true if the 3 points are aligned.
    """
    Vector_1 = B - A
    Vector_2 = C - B
    if info != 0:
        print_point(Vector_1, msg="Vector_1: ")
        print_point(Vector_2, msg="Vector_2: ")
    Vector_3 = Vector_1.cross(Vector_2)
    if info != 0:
        print_point(Vector_3, msg="Vector_1.cross(Vector_2): ")

    if abs(Vector_3.x) <= tolerance and abs(Vector_3.y) <= tolerance and abs(Vector_3.z) <= tolerance:
        if info != 0:
            print_msg("Colinear Vectors !")
        return True
    else:
        if info != 0:
            print_msg("NOT Colinear Vectors !")
        return False
    return


def intersecPoints(shape1, shape2, info=0):
    """ Return the intersection points between 2 shapes
    (Number_of_Points, Intersec_Points)
    or None
    """
    #s1 = shape1.Shape
    #s2 = shape2.Shape
    s1 = shape1
    s2 = shape2
    cs = s1.common(s2)
    sec = s1.section(s2)
    if info != 0:
        print_msg("s1 = " + str(s1))
        print_msg("s2 = " + str(s2))
        print_msg("s1.common(s2) = " + str(cs))
        print_msg("s1.common(s2).ShapeType = " + str(cs.ShapeType))
        print_msg("s1.section(s2) = " + str(sec))
        print_msg("s1.section(s2).Wires = " + str(sec.Wires))
        print_msg("s1.section(s2).Edges = " + str(sec.Edges))
    Intersec_Points = []
    if cs.Vertexes:
        for v in cs.Vertexes:
            Intersec_Points.append(v.Point)
            if info != 0:
                print_point(v.Point, "Intersection point: ")
        Number_of_Points = len(Intersec_Points)
        Intersections = (Number_of_Points, Intersec_Points)
        return Intersections
    else:
        error_msg = "Can't find any intersection point !"
        printError_msg(error_msg)
        return None
    return


def wireDiscretie(wire, numberOfParts=10):
    """ Return a set of points after discretization of the wire.
    """
    wire_points = []

    if hasattr(wire, 'discretize') is not True:
        printError_msg("No discretize function for the wire!")
        return None

    wire_points = wire.discretize(numberOfParts)
    if len(wire_points) <= 2:
        printError_msg("Unable to discretize the wire!")
        return None

    return wire_points


def findNormal(wire, forceDiscretize=False, msg=1):
    """Look for the Normal for wire.
    """
    wire_points = []
    if forceDiscretize:
        if hasattr(wire, 'discretize') is not True:
            printError_msg("No discretize function for the wire!")
            return None
        wire_points = wire.discretize(4)
        if len(wire_points) <= 2:
            printError_msg("Unable to discretize the wire!")
            return None
        m_vect01 = wire_points[1] - wire_points[0]
        m_vect02 = wire_points[2] - wire_points[0]
        wire_normal = m_vect01.cross(m_vect02)
        if msg != 0:
            print_msg("Normal by discretize() !")

    else:
        if len(wire.Edges) != 0:
            wire_normal = wire.Edges[0].tangentAt(0)
            wire_points.append(wire.Vertexes[0].Point)
            if msg != 0:
                print_msg("Normal by Tangent !")
        else:

            if hasattr(wire, 'discretize') is not True:
                printError_msg("No discretize function for the wire!")
                return
            wire_points = wire.discretize(Distance=0.01)
            if len(wire_points) <= 2:
                printError_msg("Unable to discretize the wire!")
                return
            wire_normal = wire_points[1] - wire_points[0]
            if msg != 0:
                print_msg("Normal by discretize() !")

    wire_normal.normalize()
    return wire_normal, wire_points


def getClickedPoint(info):
    global verbose
    msg = verbose
    view = Gui.ActiveDocument.ActiveView
    # down = (info["State"] == "DOWN")
    down = (info["Button"] == "BUTTON1") and (info["State"] == "DOWN")
    pos = info["Position"]
    global m_stack
    global m_callback
    global m_set
    if msg != 0:
        print_msg("down is " + str(down))
    if (down):
        point = view.getPoint(pos[0], pos[1])
        obj = view.getObjectInfo(pos)

#         if msg !=0:
#             print_msg("point is " + str(point))
#             print_msg("obj is " + str(obj))

        if obj is None:
            m_stack.append(point)
        else:
            m_stack.append(App.Vector(obj["x"], obj["y"], obj["z"]))
        if len(m_stack) >= 1:
            name = "Point"
            part = "Part::Feature"
            plot_point(m_stack[-1], part, name, str(m_set))
            print_point(m_stack[-1], "Click point at:")
            #view.removeEventCallback("SoMouseButtonEvent",m_callback)
            # del m_stack[:]


def getClickedNormal(info):
    import Mesh
    msg = 0
    view = Gui.ActiveDocument.ActiveView
    # down = (info["State"] == "DOWN")
    down = (info["Button"] == "BUTTON1") and (info["State"] == "DOWN")
    pos = info["Position"]

    if msg != 0:
        # print_msg("info: " + str(info))
        print_msg("info['Position']: " + str(pos))
    global m_stack
    global m_callback
    global m_extensionFaceNormal
    part = "Part::Feature"
    if (down):
        point = view.getPoint(pos[0], pos[1])
        obj  = view.getObjectInfo(pos)
        if msg != 0:
            print_msg("view.getPoint(pos[0],pos[1]: " + str(point))
            print_msg("view.getObjectInfo(pos): " + str(obj))

        if obj is None:
            printError_msg("No Object selected !")
            view.removeEventCallback("SoMouseButtonEvent", m_callback)
            return None
        else:
            m_sel = Gui.Selection.getSelection()[0]
            if hasattr(m_sel, 'Shape'):
                if len(m_sel.Shape.Faces) > 0:
                    # find the face selected
                    if msg != 0:
                        print_msg(str(obj["Component"]) + " selected !")

                    if len(m_sel.Shape.Faces) == 1:
                        m_face = m_sel.Shape.Faces[0]
                    else:
                        m_face = eval('m_sel.Shape.'+ str(obj["Component"]))
                    m_surf = m_face.Surface
                    m_p = App.Vector(obj["x"], obj["y"], obj["z"])
                    m_uv = m_surf.parameter(m_p)
                    u, v = m_uv[0], m_uv[1]
                    m_p1 = m_face.valueAt(u, v)
                    m_p2 = m_face.normalAt(u, v)
                    if m_extensionFaceNormal == 0.0:
                        m_extensionFaceNormal = 10.0
                    m_p3 = m_p1 + m_p2.normalize().multiply(m_extensionFaceNormal)
                    createFolders('WorkAxis')
                    name = "Normal"
                    plot_axis(m_p1, m_p3, part, name)
                    createFolders('WorkPoints')
                    name = "Point"
                    plot_point(m_p1, part,  name)
                else:
                    printError_msg("No Face selected !")
            else:
                if isinstance(m_sel, Mesh.Feature):
                    print_msg("Mesh selected !")
                    # find the facet selected
                    r = Gui.ActiveDocument.ActiveView.getCameraOrientation()
                    start = r.Axis
                    m_mesh = m_sel.Mesh
                    m_FacetsSel = m_mesh.nearestFacetOnRay((obj["x"], obj["y"], obj["z"]), (start.x, start.y, start.z))
                    if len(m_FacetsSel) == 0:
                        return
                    m_p1 = App.Vector(obj["x"], obj["y"], obj["z"])
                    for idx in m_FacetsSel.keys():
                        m_p2 = App.Vector(m_mesh.Facets[idx].Normal)

                    if m_extensionFaceNormal == 0.0:
                        m_extensionFaceNormal = 10.0
                    m_p3 = m_p1 + m_p2.normalize().multiply(m_extensionFaceNormal)
                    createFolders('WorkAxis')
                    name = "Normal"
                    plot_axis(m_p1, m_p3, part, name)
                    createFolders('WorkPoints')
                    name = "Point"
                    plot_point(m_p1, part,  name)
                else:
                    printError_msg("No Shape available for: " + str(m_sel) + "\nat " + str(App.Vector(obj["x"], obj["y"], obj["z"])))

            view.removeEventCallback("SoMouseButtonEvent", m_callback)


def getClickedTangent(info):
    msg = 0
    view = Gui.ActiveDocument.ActiveView
    # down = (info["State"] == "DOWN")
    down = (info["Button"] == "BUTTON1") and (info["State"] == "DOWN")
    pos = info["Position"]
    if msg != 0:
        print_msg("info['Position']: " + str(pos))
    global m_stack
    global m_callback
    global m_extensionFaceNormal
    part = "Part::Feature"
    if (down):
        point = view.getPoint(pos[0], pos[1])
        obj  = view.getObjectInfo(pos)
        if msg != 0:
            print_msg("view.getPoint(pos[0],pos[1]: " + str(point))
            print_msg("view.getObjectInfo(pos): " + str(obj))
        if obj is None:
            printError_msg("No Object selected !")
            view.removeEventCallback("SoMouseButtonEvent", m_callback)
            return None
        else:
            m_sel = Gui.Selection.getSelection()[0]
            m_face = m_sel.Shape.Faces[0]
            m_surf = m_face.Surface
            m_p = App.Vector(obj["x"], obj["y"], obj["z"])
            m_uv = m_surf.parameter(m_p)
            u, v = m_uv[0], m_uv[1]
            m_p1 = m_face.valueAt(u, v)
            m_p2 = m_face.normalAt(u, v)
            if m_extensionFaceNormal == 0.0:
               m_extensionFaceNormal = 10.
            m_p3 = m_p1 + m_p2.normalize().multiply(m_extensionFaceNormal)
            Plane_Normal = m_p3 - m_p1
            createFolders('WorkPlanes')
            name = "Tangent"
            Plane_User_Name, plane = plot_plane(m_lengthPlane, m_widthPlane, m_p1, Plane_Normal, part, name)
            # createFolders('WorkAxis')
            #name = "Normal"
            # plot_axis(m_p1,m_p3, part, name)
            createFolders('WorkPoints')
            name = "Point"
            plot_point(m_p1, part,  name)
            view.removeEventCallback("SoMouseButtonEvent", m_callback)


def getClickedAxis2(info):
    global verbose
    msg = verbose
    view = Gui.ActiveDocument.ActiveView
    # down = (info["State"] == "DOWN")
    down = (info["Button"] == "BUTTON1") and (info["State"] == "DOWN")
    pos = info["Position"]
    global m_stack
    global m_callback
    if msg != 0:
        print_msg("down is " + str(down))
    if (down):
        point = view.getPoint(pos[0], pos[1])
        obj  = view.getObjectInfo(pos)
        if obj is None:
            m_stack.append(point)
        else:
            m_stack.append(App.Vector(obj["x"], obj["y"], obj["z"]))
        print_point(m_stack[0], "Click point at:")
        if len(m_stack) > 1:
            name = "Line"
            part = "Part::Feature"
            Axis_User_Name, axis = plot_axis(m_stack[-2], m_stack[-1], part, name)
            print_point(m_stack[-1], "Click point at:")


def getClickedAxis(event_cb):
    event = event_cb.getEvent()
    view = Gui.ActiveDocument.ActiveView
    global m_stack
    global m_callback
    if event.getState() == SoMouseButtonEvent.DOWN:
        pos = event.getPosition()
        point = view.getPoint(pos[0], pos[1])
        m_stack.append(point)
        if len(m_stack) == 2:
            name = "Line"
            part = "Part::Feature"
            Axis_User_Name, axis = plot_axis(m_stack[-2], m_stack[-1], part, name)
            view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), m_callback)
            del m_stack[:]


def getClickedPlane2(info):
    view = Gui.ActiveDocument.ActiveView
    # down = (info["State"] == "DOWN")
    down = (info["Button"] == "BUTTON1") and (info["State"] == "DOWN")
    pos = info["Position"]
    global m_stack
    global m_callback
    if (down):
        point = view.getPoint(pos[0], pos[1])
        obj  = view.getObjectInfo(pos)
        if obj is None:
            m_stack.append(point)
        else:
            m_stack.append(App.Vector(obj["x"], obj["y"], obj["z"]))
        if len(m_stack) == 1:
            name = "Plane"
            part = "Part::Feature"
            # return view direction as a vector
            Plane_Normal = Gui.ActiveDocument.ActiveView.getViewDirection()
            # Set the base of the plane at location of mouse click
            Plane_Point = m_stack[-1]
            # Create a Plane
            Plane_User_Name, plane = plot_plane(m_lengthPlane, m_widthPlane, Plane_Point, Plane_Normal, part, name)

            view.removeEventCallback("SoMouseButtonEvent", m_callback)
            del m_stack[:]


def getClickedPlane(event_cb):
    event = event_cb.getEvent()
    view = Gui.ActiveDocument.ActiveView
    global m_stack
    global m_callback
    if event.getState() == SoMouseButtonEvent.DOWN:
        pos  = event.getPosition()
        point = view.getPoint(pos[0], pos[1])
        m_stack.append(point)
        if len(m_stack) == 1:
            name = "Plane"
            part = "Part::Feature"
            # return view direction as a vector
            Plane_Normal = Gui.ActiveDocument.ActiveView.getViewDirection()
            # Set the base of the plane at location of mouse click
            Plane_Point = m_stack[-1]
            # Create a Plane
            Plane_User_Name, plane = plot_plane(m_lengthPlane, m_widthPlane, Plane_Point, Plane_Normal, part, name)

            view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), m_callback)
            del m_stack[:]

# ==============================================================================
# def intersecLineLine(A, B, C, D, info=0):
#     """ Return the intersection between the Line L1 defined by A and B
#     and the Line L2 defined by C and D, if exists.
#     """
#     # L1 is the line defined by 2 points A(ax, ay, az) and B(bx, by, bz), and
#     # may be also defined as the line crossing A(ax, ay, az) and along the
#     # direction AB = U1(bx-ax, by-ay, bz-az)
#     # If U1(u1x, u1y, u1z) = U1(bx-ax, by-ay, bz-az) the Line L1 is the set of
#     # points M1 as defined by eq(1):
#     # Vector(M1A) = k1 * Vector(U1)
#     # with k1 Real
#     if A == B:
#         return None
#     ax, ay, az = A.x, A.y, A.z
#     bx, by, bz = B.x, B.y, B.z
#     u1x, u1y, u1z = bx - ax, by - ay, bz - az
#
#     # L2 is the line defined by 2 points C(cx, cy, cz) and D(dx, dy, dz), and
#     # may be also defined as the line crossing C(cx, cy, cz) and along the
#     # direction CD = U2(dx-cx, dy-cy, dz-cz)
#     # If U2(u2x, u2y, u2z) = U2(dx-cx, dy-cy, dz-cz) the Line L1 is the set of
#     # points M2 as defined by eq(2):
#     # Vector(M2C) = k2 * Vector(U2)
#     # with k2 Real
#     if C == D:
#         return None
#     cx, cy, cz = C.x, C.y, C.z
#     dx, dy, dz = D.x, D.y, D.z
#     u2x, u2y, u2z = dx - cx, dy - cy, dz - cz
#
#     # We look for point T(tx, ty, tz) as eq(3):
#     #Vector(TA) = k1 * Vector(U1) and
#     #Vector(TC) = k2 * Vector(U2)
#     tx = ax + k * ux
#
#     ty = ay + k * uy
#     tz = az + k * uz
#
#     return T
# ==============================================================================
def intersecPerpendicularLine(A, B, C, info=0):
    """ Return the intersection between the Line L defined by A and B
    and the Line perpendicular crossing the point C.
    """
    # L is the line defined by 2 points A(ax, ay, az) and B(bx, by, bz), and
    # may be also defined as the line crossing A(ax, ay, az) and along the
    # direction AB = U(bx-ax, by-ay, bz-az)
    # If U(ux, uy, uz) = U(bx-ax, by-ay, bz-az) the Line L is the set of
    # points M as defined by eq(1):
    # Vector(MA) = k * Vector(U)
    # with k Real
    if A == B:
        return None
    ax, ay, az = A.x, A.y, A.z
    bx, by, bz = B.x, B.y, B.z
    cx, cy, cz = C.x, C.y, C.z
    ux, uy, uz = bx - ax, by - ay, bz - az
    #U = App.Vector(ux, uy, uz)
    # We look for T(tx, ty, tz) on the Line L
    # eq(1) in parametric form; k exists and follows eq(2):
    # tx = ax + k * ux
    # ty = ay + k * uy
    # tz = az + k * uz

    # and vector V(vx, vy, vz) defined by point C and point T
    # vx, vy, vz = tx - cx, ty - cy, tz - cz
    # V must be perpendicular to the Line L
    # We consider Dot product between U and V and give us eq(3)
    # U.V = 0
    # so ux * vx + uy * vy + uz * vz = 0
    # ux * (tx - cx) + uy * (ty - cy) + uz * (tz - cz) = 0
    # ux * (ax + k * ux  - cx) + uy * (ay + k * uy - cy) + uz * (az + k * uz  - cz) = 0
    # ux*ax + ux*(k*ux) - ux*cx + uy*ay + uy*(k*uy) - uy*cy +  uz*az + uz*(k*uz) - uz*cz = 0
    if (ux*ux + uy*uy + uz*uz) == 0.0:
        return None
    k = (ux*cx + uy*cy + uz*cz - ux*ax - uy*ay - uz*az)/(ux*ux + uy*uy + uz*uz)
    tx = ax + k * ux
    ty = ay + k * uy
    tz = az + k * uz
    T = App.Vector(tx, ty, tz)
    vx, vy, vz = tx - cx, ty - cy, tz - cz
    V = App.Vector(vx, vy, vz)
    distance = math.sqrt(V.dot(V))
    Tprime = T + V
    if info == 1:
        print_point(T, msg="Intersection Point at distance of " +
                    str(distance) + " is: ")
    return T, distance, Tprime


def intersecLinePlane(A, B, Plane_Normal, Plane_Point, info=0):
    """ Return the intersection between the Line L defined by A and B
    and the Plane defined by Plane_Normal and Plane_Point.
    """
    # Plane Equation is eq(0) P(x, y, z):
    # a * x + b * y + c * z + d = 0
    # where Normal to P is  N(a, b, c)
    N = Plane_Normal
    if info == 1:
        print_point(N, "N is: ")
    # if N == App.Vector(0.0, 0.0, 0.0):
    #    return None
    a, b, c = N.x, N.y, N.z
    if info == 1:
        print_msg("a = " + str(a) + " b = " + str(b) + " c = " + str(c))
    # p1(px,py,pz) belongs to the plane P, so
    # a * px + b * py + c * pz + d = 0 and
    # d = -(a * px + b * py + c * pz)
    p1 = Plane_Point
    d = -((a * p1.x) + (b * p1.y) + (c * p1.z))
    if info == 1:
        print_msg("d = " + str(d))
    # L is the line defined by 2 points A(ax, ay, az) and B(bx, by, bz), and
    # may be also defined as the line crossing A(ax, ay, az) and along
    # the direction AB = U(bx-ax, by-ay, bz-az)
    # If U(ux, uy, uz) = U(bx-ax, by-ay, bz-az) the Line L is the set of
    # points M as defined by eq(1):
    # Vector(MA) = k * Vector(U)
    # with k Real
    if A == B:
        return None
    ax, ay, az = A.x, A.y, A.z
    bx, by, bz = B.x, B.y, B.z
    ux, uy, uz = bx - ax, by - ay, bz - az
    U = App.Vector(ux, uy, uz)
    if info == 1:
        print_point(U, "U is: ")
    # We consider Dot product between U and N
    # 1> U.N = 0
    if info == 1:
        print_msg("U.dot(N) =" + str(U.dot(N)))

    if U.dot(N) == 0.0:
        # if A belongs to P: the full Line L is included in the Plane
        if (a * ax) + (b * ay) + (c * az) + d == 0.0:
            if info == 1:
                print_msg("The full Line is included in the Plane !")
            return A
        # if not the Plane and line are parallel without intersection
        else:
            if info == 1:
                print_msg("The Plane and the line are parallel without intersection !")
            return None
    # 2> U.N != 0
    else:
        # We look for T(tx, ty, tz) on the Line L
        # eq(1) in parametric form; k exists and follows eq(2):
        # tx = ax + k * ux
        # ty = ay + k * uy
        # tz = az + k * uz
        # and T(tx, ty, tz) on the plane too so eq(1) is
        # a * tx + b * ty + c * tz + d = 0
        # by pasting the tx, ty and tz expressions into eq(1) we have a first
        # deg equation with one unknown 'k':
        # a * (ax + k * ux) + b * (ay + k * uy) + c * (az + k * uz) + d = 0
        # so
        # a * ax + a * k * ux + b * ay + b * k * uy + c * az + c * k * uz + d = 0
        # k * ( a * ux + b * uy  c *uz ) + a * ax + b * ay + c * az  + d = 0
        # k = -1 * (a * ax + b * ay + c * az  + d) / ( a * ux + b * uy + c *uz )
        if (a * ux + b * uy + c * uz) == 0.0:
            if info == 1:
                print_msg("a * ux + b * uy + c *uz == " + str(a * ux + b * uy + c * uz))
            return None
        k = -1 * (a * ax + b * ay + c * az  + d) / (a * ux + b * uy + c * uz)
        tx = ax + k * ux
        ty = ay + k * uy
        tz = az + k * uz
        if info == 1:
            print_msg("tx =" + str(tx) + " ty=" + str(ty) + " tz=" + str(tz))
        T = App.Vector(tx, ty, tz)
        if info == 1:
            print_point(T, msg="Intersection Point is: ")
        return T


def sel_attachPoint(*argc):
    """ Attach point location by combo box.
    Options:
    Start
    Mid
    End
    """
    global m_attach_point
    global verbose
    msg = verbose
    if msg != 0:
        print_msg("Attach point location by combo box !")
    m_attach_point = "Mid"
    if str(*argc) == "Start":
        m_attach_point = "Start"
    if str(*argc) == "Mid":
        m_attach_point = "Mid"
    if str(*argc) == "End":
        m_attach_point = "End"

    if msg != 0:
        print_msg("argc is " + str(*argc) + " and Attach point " + str(m_attach_point) + " selected !")


def intersecPlanePlane(Plane_Normal1, Plane_Point1, Plane_Normal2, Plane_Point2, info=0):
    """ Return the intersection Line between two Planes.
    """
    # Plane Equation is eq(0) P1(x, y, z):
    # a1 * x + b1 * y + c1 * z + d1 = 0
    # where Normal to P1 is  N1(a1, b1, c1)
    N1 = Plane_Normal1
    if info == 1:
        print_point(N1, "N1 is: ")
    a1, b1, c1 = N1.x, N1.y, N1.z
    if info == 1:
        print_msg("a1 = " + str(a1) + " b1 = " + str(b1) + " c1 = " + str(c1))
    # Plane Equation is eq(1) P2(x, y, z):
    # a2 * x + b2 * y + c2 * z + d2 = 0
    # where Normal to P2 is  N2(a2, b2, c2)
    N2 = Plane_Normal2
    if info == 1:
        print_point(N2, "N2 is: ")
    a2, b2, c2 = N2.x, N2.y, N2.z
    if info == 1:
        print_msg("a2 = " + str(a2) + " b2 = " + str(b2) + " c2 = " + str(c2))

    # p1(p1x,p1y,p1z) belongs to the plane P1, so
    # a1 * p1x + b1 * p1y + c1 * p1z + d1 = 0 and
    # d1 = -(a1 * p1x + b1 * p1y + c1 * p1z)
    p1 = Plane_Point1
    d1 = -((a1 * p1.x) + (b1 * p1.y) + (c1 * p1.z))
    if info == 1:
        print_msg("d1 = " + str(d1))

    # p2(p2x,p2y,p2z) belongs to the plane P2, so
    # a2 * p2x + b2 * p2y + c2 * p2z + d2 = 0 and
    # d2 = -(a2 * p2x + b2 * p2y + c2 * p2z)
    p2 = Plane_Point2
    d2 = -((a2 * p2.x) + (b2 * p2.y) + (c2 * p2.z))
    if info == 1:
        print_msg("d2 = " + str(d2))

    U = N2.cross(N1)
    if abs(U.x) <= 1.e-16 and abs(U.y) <= 1.e-16 and abs(U.z) <= 1.e-16:
        U.x, U.y, U.z = 0.0, 0.0, 0.0

    if info == 1:
        print_point(U, "N2.cross( N1 ): ")

    if abs(U.x) == 0.0 and abs(U.y) == 0.0 and abs(U.z) == 0.0:
        if a1/a2 == d1/d2:
            if info == 1:
                print_msg("The 2 Planes are unique !")
            return None, "The 2 Planes are unique !"
        else:
            if info == 1:
                print_msg("The 2 Planes are parallel !")
            return None, "The 2 Planes are parallel !"
    else:
        return U


def properties_point(Point_User_Name):
    """ Define the properties of a Work feature Point.
    PointColor
    PointSize
    Transparency
    """
    try:
        Gui.ActiveDocument.getObject(Point_User_Name).PointColor = (1.00, 0.67, 0.00)
    except Exception as inst:
        print(inst.args)
        print_msg("Not able to set PointColor !")
    try:
        Gui.ActiveDocument.getObject(Point_User_Name).PointSize = 5.00
    except Exception as inst:
        print(inst.args)
        print_msg("Not able to set PointSize !")
    try:
        Gui.ActiveDocument.getObject(Point_User_Name).Transparency = 0
    except Exception as inst:
        print(inst.args)
        print_msg("Not able to set Transparency !")

    return


def properties_line(Line_User_Name, color=(1.00, 0.67, 0.00)):
    """ Define the properties of a Work feature Line.
    PointColor
    LineColor
    LineWidth
    PointSize
    Transparency
    """
    try:
        Gui.ActiveDocument.getObject(Line_User_Name).PointColor = color
    except Exception as inst:
        print(inst.args)
        print_msg("Not able to set PointColor !")
    try:
        Gui.ActiveDocument.getObject(Line_User_Name).LineColor = color
    except Exception as inst:
        print(inst.args)
        print_msg("Not able to set LineColor !")
    try:
        Gui.ActiveDocument.getObject(Line_User_Name).LineWidth = 2.00
    except Exception as inst:
        print(inst.args)
        print_msg("Not able to set LineWidth !")
    try:
        Gui.ActiveDocument.getObject(Line_User_Name).PointSize = 2.00
    except Exception as inst:
        print(inst.args)
        print_msg("Not able to set PointSize !")
    try:
        Gui.ActiveDocument.getObject(Line_User_Name).Transparency = 0
    except Exception as inst:
        print(inst.args)
        print_msg("Not able to set Transparency !")

    return


def properties_plane(Plane_User_Name):
    """ Define the properties of a Work feature Plane.
    PointColor
    LineColor
    ShapeColor
    Transparency
    """
    try:
        Gui.ActiveDocument.getObject(Plane_User_Name).PointColor = (1.00, 0.67, 0.00)
    except Exception as inst:
        print(inst.args)
        print_msg("Not able to set PointColor !")
    try:
        Gui.ActiveDocument.getObject(Plane_User_Name).LineColor = (1.00, 0.67, 0.00)
    except Exception as inst:
        print(inst.args)
        print_msg("Not able to set LineColor !")
    try:
        Gui.ActiveDocument.getObject(Plane_User_Name).ShapeColor = (0.00, 0.33, 1.00)
    except Exception as inst:
        print(inst.args)
        print_msg("Not able to set ShapeColor !")
    try:
        Gui.ActiveDocument.getObject(Plane_User_Name).Transparency = 75
    except Exception as inst:
        print(inst.args)
        print_msg("Not able to set Transparency !")

    return


def plot_text(letter, size, part, name, grp="WorkObjects"):
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    m_s = letter
    # get the path of the current python script
    m_current_path = os.path.realpath(__file__)
    m_current_path = os.path.dirname(m_current_path)
    m_ff = str(m_current_path) + "/FreeFonts/FreeSans.ttf"
    # m_ff = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"  # for Linux
    # m_ff = "C:/Windows/Fonts/ARIAL.TTF"                       # for Windows
    # search the path in FreeCAD parameter#####################################
    # p = App.ParamGet("User parameter:BaseApp/Preferences/Mod/Draft")
    # m_ff = p.GetString("FontFile")
    # search the path in FreeCAD parameter 11/11/2017##########################
    ss = Draft.makeShapeString(String=m_s, FontFile=m_ff, Size=size, Tracking=0)
    App.ActiveDocument.getObject(grp).addObject(ss)
    text_User_Name = ss.Label
    return text_User_Name, ss


def plot_point(Vector_point, part="Part::Feature", name="Point", grp="WorkPoints"):
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    point = App.ActiveDocument.addObject(part, name)
    point.Shape = Part.Vertex(Vector_point)
    App.ActiveDocument.getObject(grp).addObject(point)
    point_User_Name = point.Label
    properties_point(point_User_Name)
    return point_User_Name

# object2 = FreeCAD.ActiveDocument.addObject("App::FeaturePython", "Icon_XPM_In_Macro")                                    #
# object2.addProperty("App::PropertyString","Identity","ExampleTitle","Identity of object").Identity = "FCSpring"
# ...other Property Data
# object2.ViewObject.Proxy = IconViewProviderToFile( object2, setIconInMacro(""))              # icon in macro (.XPM)
# App.ActiveDocument.recompute()


def plot_axis(Vector_A, Vector_B, part="Part::Feature", name="Axis", grp="WorkAxis", color=(1.00, 0.67, 0.00)):
    m_diff = Vector_B.sub(Vector_A)
    if abs(m_diff.x) <= tolerance and abs(m_diff.y) <= tolerance and abs(m_diff.z) <= tolerance:
        return None
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    axis = App.ActiveDocument.addObject(part, name)
    axis.Shape = Part.makeLine(Vector_A, Vector_B)
    App.ActiveDocument.getObject(grp).addObject(axis)
    axis_User_Name = axis.Label
    properties_line(axis_User_Name, color)
    return axis_User_Name, axis


def plot_curve(Matriz, Close, Face, part="Part::Feature", name="Curve", grp="WorkWires", color=(1.00, 0.67, 0.00)):
    m_close = Close
    m_face = Face
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    curvea = Part.makePolygon(Matriz)
    curve = Draft.makeWire(curvea, closed=m_close, face=m_face)
    FreeCAD.ActiveDocument.ActiveObject.Label = str(name)

    if m_close is True and m_face is True:
        Draft.upgrade(Gui.Selection.getSelection(), delete=True)
        FreeCAD.ActiveDocument.recompute()
    App.ActiveDocument.getObject(grp).addObject(curve)
    curve_User_Name = curve.Label
    # Gui.ActiveDocument.getObject(curve_User_Name).LineColor = color
    return curve_User_Name, curve


def plot_polygon(Matriz, part="Part::Feature", name="Polygon", grp="WorkWires", color=(1.00, 0.67, 0.00)):
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    polygon = App.ActiveDocument.addObject(part, name)
    polygon.Shape = Part.makePolygon(Matriz)
    App.ActiveDocument.getObject(grp).addObject(polygon)
    polygon_User_Name = polygon.Label
    Gui.ActiveDocument.getObject(polygon_User_Name).LineColor = color
    return polygon_User_Name, polygon


def plot_circle(Radius, Position, Direction, part="Part::Feature", name="Circle", grp="WorkCircles"):
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    circle = App.ActiveDocument.addObject(part, name)
    circle.Shape = Part.makeCircle(Radius, Position, Direction)
    App.ActiveDocument.getObject(grp).addObject(circle)
    circle_User_Name = circle.Label
    Gui.ActiveDocument.getObject(circle_User_Name).LineColor = (1.00, 0.67, 0.00)
    return circle_User_Name, circle


def plot_arc(center, normal, radius, startangle, endangle, part="Part::Feature", name="Circle", grp="WorkCircles"):
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    arc = App.ActiveDocument.addObject(part, name)
    c = Part.Circle(center, normal, radius)
    start = math.radians(startangle)
    end = math.radians(endangle)
    Arc = Part.Arc(c, start, end)
    arc.Shape = Arc.toShape()
    App.ActiveDocument.getObject(grp).addObject(arc)
    arc_User_Name = arc.Label
    Gui.ActiveDocument.getObject(arc_User_Name).LineColor = (1.00, 0.67, 0.00)
    return arc_User_Name, arc


def plot_arc2(Radius, Placem, Face, Startangle, Endangle, Support, part= "Part::Feature", name= "Circle", grp="WorkCircles"):
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    arc = App.ActiveDocument.addObject(part, name)
    print_msg(str(Placem))
    #arc.Shape = Part.makeCircle(Radius, Position, Direction)
    toto = Draft.makeCircle(radius=Radius, placement=Placem, face=Face, startangle=Startangle, endangle=Endangle, support=Support)
    print_msg(str(toto))
    return
    #arc.Shape =
    App.ActiveDocument.getObject(grp).addObject(arc)
    arc_User_Name = arc.Label
    Gui.ActiveDocument.getObject(arc_User_Name).LineColor = (1.00, 0.67, 0.00)
    return arc_User_Name, arc


def plot_arc3(point0, point1, point2, part= "Part::Feature", name= "Arc", grp="WorkArcs"):
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    arc = App.ActiveDocument.addObject(part, name)
    Arc = Part.Arc(point0, point1, point2)
    arc.Shape = Part.Shape([Arc])
    App.ActiveDocument.getObject(grp).addObject(arc)
    arc_User_Name = arc.Label
    Gui.ActiveDocument.getObject(arc_User_Name).LineColor = (1.00, 0.67, 0.00)
    return arc_User_Name, arc


def plot_ellipse(S1, S2, Center, part= "Part::Feature", name= "Ellipse", grp="Circles"):
    """Creates an ellipse centered on the point Center, where
    the plane of the ellipse is defined by Center, S1 and S2,
    its major axis is defined by Center and S1,
    its major radius is the distance between Center and S1, and
    its minor radius is the distance between S2 and the major axis.
    """
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    ellipse = App.ActiveDocument.addObject(part, name)

    print_point(Center, "Center =:")
    print_point(S1, "S1 =:")
    print_point(S2, "S2 =:")

    P1C = (Center - S1).Length
    P2C = (Center - S2).Length
    if P1C > P2C:
        e = Part.Ellipse(S1, S2, Center)
    else:
    # e = Part.Ellipse(S1+Center,S2,Center)
        e = Part.Ellipse(S2, S1, Center)
    # e = Part.Ellipse()
    print_msg(str(e))

    ellipse.Shape = e.toShape()
    App.ActiveDocument.getObject(grp).addObject(ellipse)
    ellipse_User_Name = ellipse.Label
    Gui.ActiveDocument.getObject(ellipse_User_Name).LineColor = (1.00, 0.67, 0.00)
    return ellipse_User_Name, ellipse


def plot_plane(Edge_Length1, Edge_Length2, Plane_Point, Plane_Normal, part, name, grp="WorkPlanes"):
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)

    plane = App.ActiveDocument.addObject(part, name)

    Plane_face = Part.makePlane(Edge_Length1, Edge_Length2, Plane_Point, Plane_Normal)
    Plane_Center = Plane_face.CenterOfMass
    Plane_Translate =  Plane_Point - Plane_Center
    Plane_face.translate(Plane_Translate)
    plane.Shape = Plane_face

    App.ActiveDocument.getObject(grp).addObject(plane)
    plane_User_Name = plane.Label

    properties_plane(plane_User_Name)
# ==============================================================================
#     Gui.ActiveDocument.getObject( plane_User_Name ).PointColor = (1.00,0.67,0.00)
#     Gui.ActiveDocument.getObject( plane_User_Name ).LineColor = (1.00,0.67,0.00)
#     Gui.ActiveDocument.getObject( plane_User_Name ).ShapeColor = (0.00,0.33,1.00)
#     Gui.ActiveDocument.getObject( plane_User_Name ).Transparency = 75
# ==============================================================================
    return plane_User_Name, plane



def plot_cube(length, width, height, point, axis, part, name, grp="WorkObjects"):
    """ Creating a Cube in the view.
    One of the Cube's extremities will be at the given point location.
    The Cube's axis will be along given axis
    Function used: makeBox(length,width,height,[pnt,axis]).
    By default pnt=Vector(0,0,0) and axis=Vector(0,0,1) 
    """
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)

    cube = App.ActiveDocument.addObject(part, name)

    Cube = Part.makeBox(length, width, abs(height), point, axis)
    Cube_Center = Cube.CenterOfMass
    Cube_Translate =  point - Cube_Center
    Cube.translate(Cube_Translate)
    Cube_Translate = axis.normalize().multiply(height/2.)
    Cube.translate(Cube_Translate)
    cube.Shape = Cube

    App.ActiveDocument.getObject(grp).addObject(cube)
    cube_User_Name = cube.Label

    Gui.ActiveDocument.getObject(cube_User_Name).PointColor = (1.00, 0.67, 0.00)
    Gui.ActiveDocument.getObject(cube_User_Name).LineColor = (1.00, 0.67, 0.00)
    Gui.ActiveDocument.getObject(cube_User_Name).ShapeColor = (0.00, 0.33, 1.00)
    Gui.ActiveDocument.getObject(cube_User_Name).Transparency = 75
    return cube_User_Name, cube


def plot_cylinder(radius, height, point, axis, part, name, grp="WorkObjects"):
    """ Creating a Cylinder in the view.
    One of the Cylinder's extremities will be at the given point location.
    The Cylinder's axis will be along given axis
    Function used: makeCylinder(radius,height,[pnt,axis,angle]). 
    By default pnt=Vector(0,0,0),axis=Vector(0,0,1) and angle=360 
    """
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)

    cylinder = App.ActiveDocument.addObject(part, name)

    Cylinder = Part.makeCylinder(radius, abs(height), point, axis)
    Cylinder_Center = Cylinder.CenterOfMass
    Cylinder_Translate =  point - Cylinder_Center
    Cylinder.translate(Cylinder_Translate)
    Cylinder_Translate = axis.normalize().multiply(height/2.)
    Cylinder.translate(Cylinder_Translate)
    cylinder.Shape = Cylinder

    App.ActiveDocument.getObject(grp).addObject(cylinder)
    cylinder_User_Name = cylinder.Label
    Gui.ActiveDocument.getObject(cylinder_User_Name).PointColor = (1.00, 0.67, 0.00)
    Gui.ActiveDocument.getObject(cylinder_User_Name).LineColor = (1.00, 0.67, 0.00)
    Gui.ActiveDocument.getObject(cylinder_User_Name).ShapeColor = (0.00, 0.33, 1.00)
    Gui.ActiveDocument.getObject(cylinder_User_Name).Transparency = 75
    return cylinder_User_Name, cylinder


def plot_sphere(Radius, Point, part="Part::Feature", name="Sphere", grp="WorkObjects"):
    """    
    makeSphere(radius,[pnt, dir, angle1,angle2,angle3]) -- Make a sphere with a given radius
    By default pnt=Vector(0,0,0), dir=Vector(0,0,1), angle1=0, angle2=90 and angle3=360
    """
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    sphere = App.ActiveDocument.addObject(part, name)
    Sphere = Part.makeSphere(Radius, Point)
    sphere.Shape = Sphere
    App.ActiveDocument.getObject(grp).addObject(sphere)
    sphere_User_Name = sphere.Label
    Gui.ActiveDocument.getObject(sphere_User_Name).PointColor = (1.00, 0.67, 0.00)
    Gui.ActiveDocument.getObject(sphere_User_Name).LineColor = (1.00, 0.67, 0.00)
    Gui.ActiveDocument.getObject(sphere_User_Name).ShapeColor = (0.00, 0.33, 1.00)
    Gui.ActiveDocument.getObject(sphere_User_Name).Transparency = 75
    return sphere_User_Name, sphere


def plot_Shape(shape, part="Part::Feature", name="Shape", grp="WorkObjects"):
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    obj = App.ActiveDocument.addObject(part, name)
    obj.Shape = shape
    App.ActiveDocument.getObject(grp).addObject(obj)
    obj_User_Name = obj.Label
    Gui.ActiveDocument.getObject(obj_User_Name).PointColor = (1.00, 0.67, 0.00)
    Gui.ActiveDocument.getObject(obj_User_Name).LineColor = (1.00, 0.67, 0.00)
    Gui.ActiveDocument.getObject(obj_User_Name).ShapeColor = (0.00, 0.33, 1.00)
    return obj_User_Name, obj


def plot_Dome(Point, Radius, Frequency, part="Part::Feature", name="Dome", grp="WorkObjects"):
    print_msg("plot_Dome:")
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    dome = App.ActiveDocument.addObject(part, name)
    icosahedre = App.ActiveDocument.addObject(part, "Icosahedre")
    Dome, Icosahedron = makeDome(Point, Radius, Frequency)

    icosahedre.Shape = Icosahedron
    App.ActiveDocument.getObject(grp).addObject(icosahedre)
    dome_User_Name = icosahedre.Label
    if Dome is not None:
        dome.Shape = Dome
        App.ActiveDocument.getObject(grp).addObject(dome)
        dome_User_Name = dome.Label
        Gui.ActiveDocument.getObject(icosahedre.Label).Visibility = False

    Gui.ActiveDocument.getObject(dome_User_Name).PointColor = (1.00, 0.67, 0.00)
    Gui.ActiveDocument.getObject(dome_User_Name).LineColor = (1.00, 0.67, 0.00)
    Gui.ActiveDocument.getObject(dome_User_Name).ShapeColor = (0.00, 0.33, 1.00)
    Gui.ActiveDocument.getObject(dome_User_Name).Transparency = 75
    return dome_User_Name, dome


def plot_sweep(traj, section, makeSolid=True, isFrenet=True, transition=2, part="Part::Feature", name="Sweep", grp="WorkObjects"):
    if not(App.ActiveDocument.getObject(grp)):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    sweep = App.ActiveDocument.addObject(part, name)
    # create a 3D shape and assigh it to the current document
# ==============================================================================
#     makePipeShell(shapeList,[isSolid,isFrenet,transition])
#     Make a loft defined by a list of profiles along a wire. Transition can be
#     0 (default), 1 (right corners) or 2 (rounded corners).
# ==============================================================================
    Sweep = Part.Wire(traj).makePipeShell([section], makeSolid, isFrenet, transition)

    sweep.Shape = Sweep
    App.ActiveDocument.getObject(grp).addObject(sweep)
    obj_User_Name = sweep.Label
    Gui.ActiveDocument.getObject(obj_User_Name).PointColor  = (1.00, 0.67, 0.00)
    Gui.ActiveDocument.getObject(obj_User_Name).LineColor   = (1.00, 0.67, 0.00)
    Gui.ActiveDocument.getObject(obj_User_Name).ShapeColor  = (0.00, 0.33, 1.00)
    Gui.ActiveDocument.getObject(obj_User_Name).Transparency = 75
    return obj_User_Name, sweep


def bounding_box(grp, ori_X, ori_Y, ori_Z, length_X, length_Y, length_Z,
                 m_grp_info=None, m_grp_vol=None):
    """ Create a bounding box.
    """
    msg = verbose

    m_grp = grp
    m_l_X = length_X
    m_l_Y = length_Y
    m_l_Z = length_Z
    m_o_X = ori_X
    m_o_Y = ori_Y
    m_o_Z = ori_Z
    global flag_for_face
    flag_for_face     = True
    flag_for_dimension = False
    flag_for_volume   = False

    if m_grp_info is not None:
        flag_for_dimension = True
    if m_grp_vol is not None:
        flag_for_volume   = True

    nameLabel = m_grp.Label

    if msg != 0:
        print_msg("Group           : "   + str(m_grp.Label))
        if m_grp_info is not None:
            print_msg("Group Info      : "   + str(m_grp_info.Label))
        if m_grp_vol is not None:
            print_msg("Group Volume      : "   + str(m_grp_vol.Label))
        print_msg("Xmin, Ymin, Zmin: \n" +
        str(m_o_X) + ", " + str(m_o_Y) + ", " + str(m_o_Z))
        print_msg("Lengths m_l_X, m_l_Y, m_l_Z: \n" +
        str(m_l_X) + ", " + str(m_l_Y) + ", " + str(m_l_Z))
        print_msg("Flag for face     : " + str(flag_for_face))
        print_msg("Flag for dimension: " + str(flag_for_dimension))
        print_msg("Flag for volume   : " + str(flag_for_volume))

    if flag_for_dimension:
        # createDim        = 1          # 1 = create dimension info: 0 = not create dimension info
        DisplayModeText  = "Screen"    # available: "Screen" or "World"
        JustificationText = "Center"    # available: "Center" or "Left" or "Right"
        FontSizeText     = 10.0        # text info dimension
        TextColorText_R      = 0.0         # text color info red      1 = 255
        TextColorText_G      = 0.0         # text color info green    1 = 255
        TextColorText_B      = 0.0         # text color info blue     1 = 255
        rounded          = 3           # round the info ex: 3 = 3 decimals

        if flag_for_volume:
            pass

    if (m_l_X != 0.0) and (m_l_Y != 0.0):
        try:
            m_pl_0 = App.Placement(App.Vector(m_o_X, m_o_Y, m_o_Z),
                                App.Rotation(0.0, 0.0, 0.0))
            print_msg("m_pl_0:" + str(m_pl_0))
            m_rect = Draft.makeRectangle(length=m_l_X, height=m_l_Y,
                                placement=m_pl_0, face=flag_for_face, support=None)
            print_msg("m_rect:" + str(m_rect))
            addObjectToGrp(m_rect, m_grp, info=1)
            definePropOfActiveObj()
            if flag_for_volume:
                Gui.ActiveDocument.getObject(m_rect.Label).Visibility = False

            if flag_for_dimension:    # section create dimension info
                pl_0C1 = Draft.makeText([str(round(m_l_X, rounded))], point=App.Vector(m_pl_0.Base.x + (m_l_X/2), m_pl_0.Base.y, m_pl_0.Base.z))
                pl_0C1.ViewObject.DisplayMode  = DisplayModeText
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize     = FontSizeText
                pl_0C1.Label     = "Rectangle_Bo_0X_" + str(round(m_l_X, rounded))

                addObjectToGrp(pl_0C1, m_grp_info, info=1)

                pl_0C2 = Draft.makeText([str(round(m_l_Y, rounded))], point=App.Vector(m_pl_0.Base.x, m_pl_0.Base.y + (m_l_Y/2), m_pl_0.Base.z))
                pl_0C2.ViewObject.DisplayMode  = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize     = FontSizeText
                pl_0C2.Label     = "Rectangle_Bo_0Y_" + str(round(m_l_Y, rounded))

                addObjectToGrp(pl_0C2, m_grp_info, info=1)

        except Exception as inst:
            print(inst.args)
            printError_msg("Rectangle 0 not done !")
            return
        try:
            m_pl_1 = App.Placement(App.Vector(m_o_X, m_o_Y, m_o_Z+m_l_Z),
                                App.Rotation(0.0, 0.0, 0.0))
            m_rect = Draft.makeRectangle(length=m_l_X, height=m_l_Y,
                                placement=m_pl_1, face=flag_for_face, support=None)
            addObjectToGrp(m_rect, m_grp, info=1)
            definePropOfActiveObj()
            if flag_for_volume:
                Gui.ActiveDocument.getObject(m_rect.Label).Visibility = False

            if flag_for_dimension:    # section create dimension info
                pl_0C1 = Draft.makeText([str(round(m_l_X, rounded))], point=App.Vector(m_pl_1.Base.x + (m_l_X/2), m_pl_1.Base.y, m_pl_1.Base.z))
                pl_0C1.ViewObject.DisplayMode  = DisplayModeText
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize     = FontSizeText
                pl_0C1.Label     = "Rectangle_To_1X_" + str(round(m_l_X, rounded))

                addObjectToGrp(pl_0C1, m_grp_info, info=1)

                pl_0C2 = Draft.makeText([str(round(m_l_Y, rounded))], point=App.Vector(m_pl_1.Base.x, m_pl_1.Base.y + (m_l_Y/2), m_pl_1.Base.z))
                pl_0C2.ViewObject.DisplayMode  = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize     = FontSizeText
                pl_0C2.Label     = "Rectangle_To_1Y_" + str(round(m_l_Y, rounded))

                addObjectToGrp(pl_0C2, m_grp_info, info=1)

        except Exception as inst:
            print(inst.args)
            printError_msg("Rectangle 1 not done !")
            return

    if (m_l_X != 0.0) and (m_l_Z != 0.0):
        try:
            m_pl_2 = App.Placement(App.Vector(m_o_X, m_o_Y, m_o_Z),
                                App.Rotation(0.0, 0.0, 90))
            m_rect = Draft.makeRectangle(length=m_l_X, height=m_l_Z,
                                placement=m_pl_2, face=flag_for_face, support=None)
            addObjectToGrp(m_rect, m_grp, info=1)
            definePropOfActiveObj()
            if flag_for_volume:
                Gui.ActiveDocument.getObject(m_rect.Label).Visibility = False

            if flag_for_dimension:    # section create dimension info
                pl_0C1 = Draft.makeText([str(round(m_l_X, rounded))], point=App.Vector(m_pl_2.Base.x + (m_l_X/2), m_pl_2.Base.y, m_pl_2.Base.z))
                pl_0C1.ViewObject.DisplayMode  = DisplayModeText
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize     = FontSizeText
                pl_0C1.Label     = "Rectangle_Fr_2X_" + str(round(m_l_X, rounded))

                addObjectToGrp(pl_0C1, m_grp_info, info=1)

                pl_0C2 = Draft.makeText([str(round(m_l_Z, rounded))], point=App.Vector(m_pl_2.Base.x, m_pl_2.Base.y, m_pl_2.Base.z + (m_l_Z/2)))
                pl_0C2.ViewObject.DisplayMode  = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize     = FontSizeText
                pl_0C2.Label     = "Rectangle_Fr_2Z_" + str(round(m_l_Z, rounded))

                addObjectToGrp(pl_0C2, m_grp_info, info=1)
        except:
            printError_msg("Rectangle 2 not done !")
        try:
            m_pl_3 = App.Placement(App.Vector(m_o_X, m_o_Y+m_l_Y, m_o_Z),
                                App.Rotation(0.0, 0.0, 90))
            m_rect = Draft.makeRectangle(length=m_l_X, height=m_l_Z,
                                placement=m_pl_3, face=flag_for_face, support=None)
            addObjectToGrp(m_rect, m_grp, info=1)
            definePropOfActiveObj()
            if flag_for_volume:
                Gui.ActiveDocument.getObject(m_rect.Label).Visibility = False

            if flag_for_dimension:    # section create dimension info
                pl_0C1 = Draft.makeText([str(round(m_l_X, rounded))], point=App.Vector(m_pl_3.Base.x + (m_l_X/2), m_pl_3.Base.y, m_pl_3.Base.z))
                pl_0C1.ViewObject.DisplayMode  = DisplayModeText
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize     = FontSizeText
                pl_0C1.Label     = "Rectangle_Re_3X_" + str(round(m_l_X, rounded))

                addObjectToGrp(pl_0C1, m_grp_info, info=1)

                pl_0C2 = Draft.makeText([str(round(m_l_Z, rounded))], point=App.Vector(m_pl_3.Base.x, m_pl_3.Base.y, m_pl_3.Base.z + (m_l_Z/2)))
                pl_0C2.ViewObject.DisplayMode  = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize     = FontSizeText
                pl_0C2.Label     = "Rectangle_Re_3Z_" + str(round(m_l_Z, rounded))

                addObjectToGrp(pl_0C2, m_grp_info, info=1)
        except Exception as inst:
            print(inst.args)
            printError_msg("Rectangle 3 not done !")

    if (m_l_Y != 0.0) and (m_l_Z != 0.0):
        try:
            m_pl_4 = App.Placement(App.Vector(m_o_X, m_o_Y, m_o_Z),
                                App.Rotation(90, 0.0, 90))
            m_rect = Draft.makeRectangle(length=m_l_Y, height=m_l_Z,
                                placement=m_pl_4, face=flag_for_face, support=None)
            addObjectToGrp(m_rect, m_grp, info=1)
            definePropOfActiveObj()
            if flag_for_volume:
                Gui.ActiveDocument.getObject(m_rect.Label).Visibility = False

            if flag_for_dimension:    # section create dimension info
                pl_0C1 = Draft.makeText([str(round(m_l_Y, rounded))], point=App.Vector(m_pl_4.Base.x, m_pl_4.Base.y + (m_l_Y/2), m_pl_4.Base.z))
                pl_0C1.ViewObject.DisplayMode  = DisplayModeText
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize     = FontSizeText
                pl_0C1.Label     = "Rectangle_Le_4Y_" + str(round(m_l_Y, rounded))

                addObjectToGrp(pl_0C1, m_grp_info, info=1)

                pl_0C2 = Draft.makeText([str(round(m_l_Z, rounded))], point=App.Vector(m_pl_4.Base.x, m_pl_4.Base.y, m_pl_4.Base.z + (m_l_Z/2)))
                pl_0C2.ViewObject.DisplayMode  = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize     = FontSizeText
                pl_0C2.Label     = "Rectangle_Le_4Z_" + str(round(m_l_Z, rounded))

                addObjectToGrp(pl_0C2, m_grp_info, info=1)
        except Exception as inst:
            print(inst.args)
            printError_msg("Rectangle 4 not done !")
        try:
            m_pl_5 = App.Placement(App.Vector(m_o_X+m_l_X, m_o_Y, m_o_Z),
                                App.Rotation(90, 0.0, 90))
            m_rect = Draft.makeRectangle(length=m_l_Y, height=m_l_Z,
                                placement=m_pl_5, face=flag_for_face, support=None)
            addObjectToGrp(m_rect, m_grp, info=1)
            definePropOfActiveObj()
            if flag_for_volume:
                Gui.ActiveDocument.getObject(m_rect.Label).Visibility = False

            if flag_for_dimension:    # section create dimension info
                pl_0C1 = Draft.makeText([str(round(m_l_Y, rounded))], point=App.Vector(m_pl_5.Base.x, m_pl_5.Base.y + (m_l_Y/2), m_pl_5.Base.z))
                pl_0C1.ViewObject.DisplayMode  = DisplayModeText
                pl_0C1.ViewObject.Justification = JustificationText
                pl_0C1.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C1.ViewObject.FontSize     = FontSizeText
                pl_0C1.Label     = "Rectangle_Ri_5Y_" + str(round(m_l_Y, rounded))

                addObjectToGrp(pl_0C1, m_grp_info, info=1)

                pl_0C2 = Draft.makeText([str(round(m_l_Z, rounded))], point=App.Vector(m_pl_5.Base.x, m_pl_5.Base.y, m_pl_5.Base.z + (m_l_Z/2)))
                pl_0C2.ViewObject.DisplayMode  = DisplayModeText
                pl_0C2.ViewObject.Justification = JustificationText
                pl_0C2.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
                pl_0C2.ViewObject.FontSize     = FontSizeText
                pl_0C2.Label     = "Rectangle_Ri_5Z_" + str(round(m_l_Z, rounded))

                addObjectToGrp(pl_0C2, m_grp_info, info=1)
        except Exception as inst:
            print(inst.args)
            printError_msg("Rectangle 5 not done !")

    if not flag_for_volume:
        print_msg("Bounding Box Planes created !")
        return

    # Else Create Volume
    # if (m_l_X != 0.0) and (m_l_Y != 0.0) and (m_l_Z != 0.0):
    try:
        if (m_l_X == 0.0):
            m_l_X = 0.5
            m_o_X = m_o_X - 0.25
        if (m_l_Y == 0.0):
            m_l_Y = 0.5
            m_o_Y = m_o_Y - 0.25
        if (m_l_Z == 0.0):
            m_l_Z = 0.5
            m_o_Z = m_o_Z - 0.25
        m_pnt = App.Vector(m_o_X, m_o_Y, m_o_Z)

        oripl_X = m_o_X
        oripl_Y = m_o_Y
        oripl_Z = m_o_Z
        print_point(m_pnt, msg="m_pnt")
        # adds object to the document group
        box = App.ActiveDocument.addObject("Part::Feature", "BBoxVolume")
        #By default pnt=Vector(0,0,0) and dir=Vector(0,0,1)
        Box_face = Part.makeBox(m_l_X, m_l_Y, m_l_Z, m_pnt)
        # print_msg("Box_face:" + str(Box_face) )
        box.Shape = Box_face
        #m_grp.addObject( box )
        addObjectToGrp(box, m_grp_vol, info=1)

        Gui.activeDocument().activeObject().Transparency = (50)

        if flag_for_dimension:    # section create dimension info for volume
            pl_0C1 = Draft.makeText([str(round(m_l_X, rounded))], point=App.Vector(oripl_X + (m_l_X/2), oripl_Y, oripl_Z))
            pl_0C1.ViewObject.DisplayMode  = DisplayModeText
            pl_0C1.ViewObject.Justification = JustificationText
            pl_0C1.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
            pl_0C1.ViewObject.FontSize     = FontSizeText
            pl_0C1.Label     = "Length_X_" + str(round(m_l_X, rounded))
            # conteneurVol.addObject(pl_0C1)
            addObjectToGrp(pl_0C1, m_grp_vol, info=1)

            pl_0C2 = Draft.makeText([str(round(m_l_Y, rounded))], point=App.Vector(oripl_X, oripl_Y + (m_l_Y/2), oripl_Z))
            pl_0C2.ViewObject.DisplayMode  = DisplayModeText
            pl_0C2.ViewObject.Justification = JustificationText
            pl_0C2.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
            pl_0C2.ViewObject.FontSize     = FontSizeText
            pl_0C2.Label     = "Length_Y_" + str(round(m_l_Y, rounded))
            # conteneurVol.addObject(pl_0C2)
            addObjectToGrp(pl_0C2, m_grp_vol, info=1)

            pl_0C3 = Draft.makeText([str(round(m_l_Z, rounded))], point=App.Vector(oripl_X, oripl_Y, oripl_Z + (m_l_Z/2)))
            pl_0C3.ViewObject.DisplayMode  = DisplayModeText
            pl_0C3.ViewObject.Justification = JustificationText
            pl_0C3.ViewObject.TextColor    = (TextColorText_R, TextColorText_G, TextColorText_B)
            pl_0C3.ViewObject.FontSize     = FontSizeText
            pl_0C3.Label     = "Length_Z_" + str(round(m_l_Z, rounded))
            # conteneurVol.addObject(pl_0C3)
            addObjectToGrp(pl_0C3, m_grp_vol, info=1)

        print_msg("Bounding Box Volume created !")
    except Exception as inst:
        print(inst.args)
        printError_msg("Bounding Box Volume not created !")


def bBox_toggled(flag):
    """ Respond to the change of bounding box flag.
    """
    global centerOfMass
    centerOfMass = True
    if flag is True:
        centerOfMass = False


def setTolerance(value):
    """ Respond to the change in tolerance value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global tolerance
        if str(value) == '-':
            return
        tolerance = float(value)
        print_msg("New tolerance is:" + str(tolerance))
        # plot_alongLinePoint()
    except ValueError:
        printError_msg("Tolerance must be valid number !")


def plot_originObject():
    """
    Create at origin of the document:
      a point,
      X, Y, Z axis,
      XZ, XY, YZ planes.
    """
    global verbose
    msg = verbose
    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None
    createFolders('Origin')
    try:
        if not(App.ActiveDocument.getObject("Origin_Point")):
            Line_Color = (1.00, 0.33, 0.00)
            Shape_Color =  (0.00, 1.00, 0.50)
            Transparency = 75
            # Origin
            Origin = Base.Vector(0, 0, 0)
            Origin_Vertex = Part.Vertex(Origin)
            Origin = App.ActiveDocument.addObject("Part::Feature", "Origin_Point")
            App.ActiveDocument.getObject("Origin").addObject(Origin)
            Origin.Shape = Origin_Vertex
            Origin_User_Name = Origin.Label
            Gui.ActiveDocument.getObject(Origin_User_Name).PointColor = (0.33, 0.00, 1.00)
            Gui.ActiveDocument.getObject(Origin_User_Name).PointSize = 4.00
            Gui.ActiveDocument.getObject("Origin_Point").Visibility = False

            # Work-AxisX
            AX_Length = 300
            PX_A = Base.Vector(AX_Length, 0, 0)
            PX_B = Base.Vector(-AX_Length, 0, 0)
            Axis_X = Part.makeLine(PX_A, PX_B)
            Axis = App.ActiveDocument.addObject("Part::Feature", "Ori_X_Axis")
            Axis.Shape = Axis_X
            App.ActiveDocument.getObject("Origin").addObject(Axis)
            Axis_User_Name = Axis.Label
            Gui.ActiveDocument.getObject(Axis_User_Name).LineColor = (1.00, 0.00, 0.00)
            Gui.ActiveDocument.getObject(Axis_User_Name).PointColor = (1.00, 0.00, 0.00)
            Gui.ActiveDocument.getObject("Ori_X_Axis").Visibility = True

            # Work-AxisY
            AY_Length = 300
            PY_A = Base.Vector(0, AY_Length, 0)
            PY_B = Base.Vector(0, -AY_Length, 0)
            Axis_Y = Part.makeLine(PY_A, PY_B)
            Axis = App.ActiveDocument.addObject("Part::Feature", "Ori_Y_Axis")
            Axis.Shape = Axis_Y
            App.ActiveDocument.getObject("Origin").addObject(Axis)
            Axis_User_Name = Axis.Label
            Gui.ActiveDocument.getObject(Axis_User_Name).LineColor = (0.00, 0.67, 0.00)
            Gui.ActiveDocument.getObject(Axis_User_Name).PointColor = (0.00, 0.67, 0.00)
            Gui.ActiveDocument.getObject("Ori_Y_Axis").Visibility = True

            # Work-AxisZ
            AZ_Length = 300
            PZ_A = Base.Vector(0, 0, AZ_Length)
            PZ_B = Base.Vector(0, 0, -AZ_Length)
            Axis_Z = Part.makeLine(PZ_A, PZ_B)
            Axis = App.ActiveDocument.addObject("Part::Feature", "Ori_Z_Axis")
            Axis.Shape = Axis_Z
            App.ActiveDocument.getObject("Origin").addObject(Axis)
            Axis_User_Name = Axis.Label
            Gui.ActiveDocument.getObject(Axis_User_Name).LineColor =  (0.33, 0.00, 1.00)
            Gui.ActiveDocument.getObject(Axis_User_Name).PointColor =  (0.33, 0.00, 1.00)
            Gui.ActiveDocument.getObject("Ori_Z_Axis").Visibility = True

            # Work-PlaneXY
            PXY_A_SIZE = 300
            PXY_A = Base.Vector(PXY_A_SIZE, PXY_A_SIZE, 0)
            PXY_B = PXY_A + Base.Vector(-2.0 * PXY_A_SIZE, 0, 0)
            PXY_C = PXY_A + Base.Vector(-2.0 * PXY_A_SIZE, -2.0 * PXY_A_SIZE, 0)
            PXY_D = PXY_A + Base.Vector(0, -2.0 * PXY_A_SIZE, 0)
            PlaneXY_list = [PXY_A, PXY_B, PXY_C, PXY_D, PXY_A]
            PlaneXY_wire = Part.makePolygon(PlaneXY_list)
            PlaneXY_face = Part.Face(PlaneXY_wire)
            PlaneXY = App.ActiveDocument.addObject("Part::Feature", "XY_WPlane")
            PlaneXY.Shape = PlaneXY_face
            App.ActiveDocument.getObject("Origin").addObject(PlaneXY)
            PlaneXY_User_Name = PlaneXY.Label
            Gui.ActiveDocument.getObject(PlaneXY_User_Name).PointColor = Line_Color
            Gui.ActiveDocument.getObject(PlaneXY_User_Name).LineColor = Line_Color
            Gui.ActiveDocument.getObject(PlaneXY_User_Name).ShapeColor = Shape_Color
            Gui.ActiveDocument.getObject(PlaneXY_User_Name).Transparency = Transparency
            Gui.ActiveDocument.getObject("XY_WPlane").Visibility = False

            # Work-PlaneXY
            PXZ_A_SIZE = 300
            PXZ_A = Base.Vector(PXZ_A_SIZE, 0, PXZ_A_SIZE)
            PXZ_B = PXZ_A + Base.Vector(-2.0 * PXZ_A_SIZE, 0, 0)
            PXZ_C = PXZ_A + Base.Vector(-2.0 * PXZ_A_SIZE, 0, -2.0 * PXZ_A_SIZE)
            PXZ_D = PXZ_A + Base.Vector(0, 0, -2.0 * PXZ_A_SIZE)
            PlaneXZ_list = [PXZ_A, PXZ_B, PXZ_C, PXZ_D, PXZ_A]
            PlaneXZ_wire = Part.makePolygon(PlaneXZ_list)
            PlaneXZ_face = Part.Face(PlaneXZ_wire)
            PlaneXZ = App.ActiveDocument.addObject("Part::Feature", "XZ_WPlane")
            PlaneXZ.Shape = PlaneXZ_face
            App.ActiveDocument.getObject("Origin").addObject(PlaneXZ)
            PlaneXZ_User_Name = PlaneXZ.Label
            Gui.ActiveDocument.getObject(PlaneXZ_User_Name).PointColor = Line_Color
            Gui.ActiveDocument.getObject(PlaneXZ_User_Name).LineColor = Line_Color
            Gui.ActiveDocument.getObject(PlaneXZ_User_Name).ShapeColor = Shape_Color
            Gui.ActiveDocument.getObject(PlaneXZ_User_Name).Transparency = Transparency
            Gui.ActiveDocument.getObject("XZ_WPlane").Visibility = False

            # Work-PlaneZY
            PYZ_A_SIZE = 300
            PYZ_A = Base.Vector(0, PYZ_A_SIZE, PYZ_A_SIZE)
            PYZ_B = PYZ_A + Base.Vector(0, -2.0 * PYZ_A_SIZE, 0)
            PYZ_C = PYZ_A + Base.Vector(0, -2.0 * PYZ_A_SIZE, -2.0 * PYZ_A_SIZE)
            PYZ_D = PYZ_A + Base.Vector(0, 0, -2.0 * PYZ_A_SIZE)
            PlaneYZ_list = [PYZ_A, PYZ_B, PYZ_C, PYZ_D, PYZ_A]
            PlaneYZ_wire = Part.makePolygon(PlaneYZ_list)
            PlaneYZ_face = Part.Face(PlaneYZ_wire)
            PlaneYZ = App.ActiveDocument.addObject("Part::Feature", "YZ_WPlane")
            PlaneYZ.Shape = PlaneYZ_face
            App.ActiveDocument.getObject("Origin").addObject(PlaneYZ)
            PlaneYZ_User_Name = PlaneYZ.Label
            Gui.ActiveDocument.getObject(PlaneYZ_User_Name).PointColor = Line_Color
            Gui.ActiveDocument.getObject(PlaneYZ_User_Name).LineColor = Line_Color
            Gui.ActiveDocument.getObject(PlaneYZ_User_Name).ShapeColor = Shape_Color
            Gui.ActiveDocument.getObject(PlaneYZ_User_Name).Transparency = Transparency
            Gui.ActiveDocument.getObject("YZ_WPlane").Visibility = False
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create Origin objects !")


def plot_centerObjectPoint():
    """ Create a Point at center location of all selected Object(s).
    if BBox is not toggled:
      This point is the MEAN location of all center of Mass (if exist) of all objects.
      All  center of Mass of al selected object(s) will be created too.

    if BBox check box is toggled:
      This point is the center of the Global X,Y,Z bounding box of all objects.
      This global bounding box always exists (especially for draft objects).
      Be aware this point is not necessary the center of Mass of all Objects!

    - First select one or several Object(s)
    - Then push this button
    """
    global centerOfMass
    msg = verbose

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None
    createFolders('WorkPoints')
    error_msg = "Unable to create Center Point of Object(s): \nSelect at least one Object !"
    flag_centerOfMass = centerOfMass
    if flag_centerOfMass:
        result_msg = ": Mean of Center of Mass of Object(s) created !"
        name = "MeanCenterMass"
    else:
        result_msg = ": Center Point of global bounding box of Object(s) created !"
        name = "CenterBBObject"
    part = "Part::Feature"

    # Return a list of SelectionObjects for a given document name.
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    m_objs = [selobj.Object for selobj in m_selEx]
    m_objNames = [selobj.ObjectName for selobj in m_selEx]
    m_num = len(m_objs)
    if m_num >= 1:
        if msg != 0:
            print_msg(str(m_num) + " object(s) selected:\n" + str(m_objNames))
        if flag_centerOfMass:
            m_i = 0
            m_list = []
            m_c = None
            Center_User_Name = None
            for m_obj in m_objs:
                if msg != 0:
                    print_msg("Processing: " + str(m_objNames[m_i]))
                try:
                    m_c = m_obj.Shape.CenterOfMass
                    if msg != 0:
                        print_msg(str(m_c))

                    Center_User_Name = plot_point(m_c, part, name)
                    m_list.append(m_c)
                except Exception as inst:
                    print(inst.args)
                    printError_msg(str(m_objNames[m_i]) + "\nThis object has no attribute 'Center of Mass' !\nSelect another one !\n")
                    break
            if len(m_list) >= 2:
                m_mean = meanVectorsPoint(m_list, info=msg)
                Center_User_Name = plot_point(m_mean, part, name)
                print_point(m_mean, str(Center_User_Name) + result_msg + " at:")
            else:
                print_point(m_c, str(Center_User_Name) + result_msg + " at:")
        else:
            Vector_Objects_Center = centerObjectsPoint(m_objs, info=msg)
            if Vector_Objects_Center is not None:
                Center_User_Name = plot_point(Vector_Objects_Center, part, name)
                print_point(Vector_Objects_Center, str(Center_User_Name) + result_msg + " at:")
            else:
                printError_msg(error_msg)
    else:
        printError_msg(error_msg)


def plot_NpointsPoint():
    """ Create a Point at MEAN location of all selected points.
    """
    msg = verbose

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None
    createFolders('WorkPoints')
    error_msg = "Unable to create Center Point of Points: \nSelect at least 2 points !"
    result_msg = ": Center Point of Points created !"
    name = "CenterPoint"
    part = "Part::Feature"

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
        points = []
        if Number_of_Points >= 2:
            Point_List = SelectedObjects[3]
            for m_point in Point_List:
                points.append(m_point.Point)
                if msg != 0:
                    print_point(m_point.Point, msg="Point: ")
            Vector_Center = meanVectorsPoint(points, info=msg)

            Center_User_Name = plot_point(Vector_Center, part, name)
            print_point(Vector_Center, str(Center_User_Name) + result_msg + " at:")
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def numberLinePart(value):
    """ Respond to the change in number of part value from the spin box.
    """
    msg = verbose

    try:
        # First we check if a valid number have been entered
        global m_numberLinePart
        if str(value) == '-':
            return
        m_numberLinePart = int(value)
        if msg != 0:
            print_msg("New number is:" + str(m_numberLinePart))
    except ValueError:
        printError_msg("Number must be valid !")


def plot_centerLinePoint():
    """ Create Point(s):
    Cut each selected Line(s) in 2 (n) parts and
    create a (n-1) Point(s) along selected edge(s) except at extrema.
    The number indicates how many parts to consider.
    
    - First define the number of Parts, then
    - Select at least 2 Points and/or
    - Select one or several Line/Edge(s) and/or
    - Select one Plane/Face to process all (4) Edges and/or
    - Select one Object to process all Edges at once
    - Then Click on the button 
    """
    msg = verbose

    error_msg = """Unable to create Mid Line Point(s):
    Select at least 2 Points and/or
    Select one or several Line/Edge(s) and/or
    Select one Plane/Face to process all (4) Edges and/or
    Select one Object to process all Edges at once !"""
    result_msg = ": Mid Line Point(s) created !"

    createFolders('WorkPoints')
    m_dir = 'Set'
    name = "MidPoint"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    global m_numberLinePart
    if not (m_numberLinePart >= 2 and m_numberLinePart <= 100):
        m_numberLinePart = 2

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))

    try:
        Number_of_Edges, Edge_List = m_sel.get_segments(getfrom=["Points", "Segments", "Curves", "Planes", "Objects"])
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))
        if Number_of_Edges >= 1:
            for i in range(Number_of_Edges):
                edge = Edge_List[i]
                if m_numberLinePart == 2:
                    if msg != 0:
                        print_msg(str(edge))
                    Vector_Line_Center = centerLinePoint(edge, info=msg)
                    if msg != 0:
                        print_point(Vector_Line_Center, msg="MidPoint: ")

                    Center_User_Name = plot_point(Vector_Line_Center, part, name, str(m_dir))
                    print_point(Vector_Line_Center, str(Center_User_Name) + result_msg + " at:")
                else:
                    for j in range(1, m_numberLinePart):
                        Vector_Line_Center = centerLinePoints(edge, j, m_numberLinePart, info=msg)
                        Center_User_Name = plot_point(Vector_Line_Center, part, name, str(m_dir))
                        print_point(Vector_Line_Center, str(Center_User_Name) + result_msg + " at:")
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_extremaLinePoint():
    """ Create Points at start and end location of each selected Line(s).

    - Select one or several Line/Edge(s) and/or
    - Select one Plane/Face to process all (4) Edges and/or
    - Select one Object to process all Edges at once
    - Then Click on the button 
    """
    msg = verbose

    error_msg = """Unable to create First and Last Line Point(s):
    Select one or several Line/Edge(s) and/or
    Select one Plane/Face to process all (4) Edges and/or
    Select one Object to process all Edges at once !"""
    result_msg = ": First and Last Line Point(s) created !"

    createFolders('WorkPoints')
    m_dir = 'Set'
    name = "ExtremumPoint"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))

    try:
        Number_of_Edges, Edge_List = m_sel.get_segments(getfrom=["Points", "Segments", "Curves", "Planes", "Objects"])
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))
        if Number_of_Edges >= 1:
            for i in range(Number_of_Edges):
                edge = Edge_List[i]
                if msg != 0:
                    print_msg(str(edge))

                Vector_A = edge.Vertexes[0].Point
                Vector_B = edge.Vertexes[-1].Point
                if msg != 0:
                    print_point(Vector_A, msg="First Point: ")
                    print_point(Vector_B, msg="Last Point: ")

                Center_User_Name = plot_point(Vector_A, part, name, str(m_dir))
                print_point(Vector_A, str(Center_User_Name) + result_msg + " at:")
                Center_User_Name = plot_point(Vector_B, part, name, str(m_dir))
                print_point(Vector_B, str(Center_User_Name) + result_msg + " at:")
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_centerCirclePoint():
    """ Create a Point at center location of each selected Circle(s), Arc(s) or Ellipse(s).

    - Select one or several Circle(s), Arc(s) or Ellipse(s)
    - Then Click on the button 
    """
    msg = verbose

    error_msg = """Unable to create Center Circle Point(s):
    Select at least one Edge of Circle !"""
    result_msg = ": Center Circle Point(s) created !"

    createFolders('WorkPoints')
    m_dir = 'Set'
    name = "CenterCircle"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))

    try:
        Number_of_Edges, Edge_List = m_sel.get_segments()
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))
        if Number_of_Edges >= 1:
            for i in range(Number_of_Edges):
                edge = Edge_List[i]
                try:
                    edge.Curve.Radius
                    Vector_Circle_Center = centerCirclePoint(edge, info=0)
                    Center_User_Name = plot_point(Vector_Circle_Center, part, name, str(m_dir))
                    print_point(Vector_Circle_Center, str(Center_User_Name) + result_msg + " at:")
                except Exception as inst:
                    print(inst.args)
                    try:
                        m_c = edge.Center
                        Center_User_Name = plot_point(m_c, part, name, str(m_dir))
                        print_point(m_c, str(Center_User_Name) + result_msg + " at:")
                    except Exception as inst:
                        print(inst.args)
                        try:
                            m_c = edge.Curve.Center
                            Center_User_Name = plot_point(m_c, part, name, str(m_dir))
                            print_point(m_c, str(Center_User_Name) + result_msg + " at:")
                        except AttributeError:
                            continue

        Number_of_Curves, Curve_List = m_sel.get_curves()
        if msg != 0:
            print_msg("Number_of_Curves=" + str(Number_of_Curves))
        if Number_of_Curves >= 1:
            for i in range(Number_of_Curves):
                curve = Curve_List[i]
                if msg != 0:
                    print_msg(str(curve))
                try:
                    m_c = curve.Center
                    Center_User_Name = plot_point(m_c, part, name, str(m_dir))
                    print_point(m_c, str(Center_User_Name) + result_msg + " at:")
                except AttributeError:
                    try:
                        m_c = curve.Curve.Radius
                        Vector_Circle_Center = centerCirclePoint(curve, info=0)
                        Center_User_Name = plot_point(Vector_Circle_Center, part, name, str(m_dir))
                        print_point(Vector_Circle_Center, str(Center_User_Name) + result_msg + " at:")
                    except AttributeError:
                        continue
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_centerFacePoint():
    """ Create a Point at center location of each selected Face(s).

    - Select one or several Plane/Face(s) to process and/or
    - Select one or several Object(s) to process all Faces at once
    - Then Click on the button
    """
    msg = verbose

    error_msg = """Unable to create Center Face Point(s):
    Select at least one Plane surface !"""
    result_msg = ": Center Face Point(s) created !"

    createFolders('WorkPoints')
    m_dir = 'Set'
    name = "CenterFace"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))


    try:
        Number_of_Planes, Plane_List = m_sel.get_planes(getfrom=["Planes", "Objects"])
        if msg != 0:
            print_msg("Number_of_Planes=" + str(Number_of_Planes))
        if Number_of_Planes >= 1:
            for i in range(Number_of_Planes):
                plane = Plane_List[i]
                if msg != 0:
                    print_msg(str(plane))

                Vector_Plane_Center = plane.CenterOfMass

                Center_User_Name = plot_point(Vector_Plane_Center, part, name, str(m_dir))
                print_point(Vector_Plane_Center, str(Center_User_Name) + result_msg + " at:")
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_lineFacePoint():
    """ Create a point at the intersection of the Line(s) and Plane(s) selected.

    First
    - Select at least 2 Points and/or
    - Select one or several Line/Edge(s) 
    and Second
    - Select one or several Plane/Face(s) to process and/or
    - Select one or several Object(s) to process all Faces at once
    - Then Click on the button
    """
    msg = verbose

    error_msg = """Unable to create (Line,Face) Intersection(s):
    First
    - Select at least 2 Points and/or
    - Select one or several Line/Edge(s) 
    and Second 
    - Select one or several Plane/Face(s) to process and/or
    - Select one or several Object(s) to process all Faces at once
    Select one Line and one Plane surface ! !"""
    result_msg = ": (Line,Face) Intersection(s) created !"

    createFolders('WorkPoints')
    m_dir = 'Set'
    name = "LineFacePoint"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))


    try:
        Number_of_Edges, Edge_List = m_sel.get_segments(getfrom=["Points", "Segments"])
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))

        Number_of_Planes, Plane_List = m_sel.get_planes(getfrom=["Planes", "Objects"])
        if msg != 0:
            print_msg("Number_of_Planes=" + str(Number_of_Planes))

        if Number_of_Edges >= 1 and Number_of_Planes >= 1:
            for i in range(Number_of_Edges):
                edge = Edge_List[i]
                if msg != 0:
                    print_msg(str(edge))
                for j in range(Number_of_Planes):
                    plane = Plane_List[j]
                    if msg != 0:
                        print_msg(str(plane))
                    Vector_A = edge.valueAt(0.0)
                    Vector_B = edge.valueAt(edge.Length)
                    if msg != 0:
                        print_point(Vector_A, msg="Point A: ")
                        print_point(Vector_B, msg="Point B: ")
                    Plane_Normal = plane.normalAt(0, 0)
                    Plane_Point = plane.CenterOfMass
                    if msg != 0:
                        print_msg("Plane_Normal is: " + str(Plane_Normal))
                        print_point(Plane_Point, "Plane_Point is: ")

                    Vector_T = intersecLinePlane(Vector_A, Vector_B, Plane_Normal, Plane_Point, info=0)

                    Center_User_Name = plot_point(Vector_T, part, name, str(m_dir))
                    print_point(Vector_T, str(Center_User_Name) + result_msg + " at:")
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_pointFacePoint():
    """ Point(s)=(Point(s),Face(s)):
    Create projection(s) of Point(s) onto Face(s).

    First
    - Select one (or several) Point(s) and/or
    - Select one or several Line/Edge(s)
    and Second
    - Select one or several Plane/Face(s) to process and/or
    - Select one or several Object(s) to process all Faces at once
    - Then Click on the button

    Plot the intersection point T on a Plane given one Plane and One Point C.
    The Vector TC is perpendicular to the plane.

    Be aware that if the plane is not extended enough the intersection Point is still created (as if).
    """
    msg = verbose

    error_msg = """Unable to create (Point,Face) Intersection(s):
    First
    - Select one (or several) Point(s) and/or
    - Select one or several Line/Edge(s)
    and Second
    - Select one or several Plane/Face(s) to process and/or
    - Select one or several Object(s) to process all Faces at once
    but at least select one Face and one Point not on the Face !"""
    result_msg = ": (Point,Face) Intersection created !"

    createFolders('WorkPoints')
    m_dir = 'Set'
    name = "PointFacePoint"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))

    try:
        Number_of_Points, Point_List = m_sel.get_points(getfrom=["Points", "Segments", "Curves"])
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
        Number_of_Planes, Plane_List = m_sel.get_planes(getfrom=["Planes", "Objects"])
        if msg != 0:
            print_msg("Number_of_Planes=" + str(Number_of_Planes))

        if (Number_of_Points >= 1) and (Number_of_Planes >= 1):
            for Selected_Plane in Plane_List:
                for Selected_Point in Point_List:
                    Vector_C = Selected_Point.Point
                    Plane_Point = Selected_Plane.CenterOfMass
                    Plane_Normal = Selected_Plane.normalAt(0, 0)

                    Vector_B = Vector_C + Plane_Normal

                    Vector_T = intersecLinePlane(Vector_C, Vector_B, Plane_Normal, Plane_Point, info=0)

                    Center_User_Name = plot_point(Vector_T, part, name, str(m_dir))
                    print_point(Vector_T, str(Center_User_Name) + result_msg + " at:")
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_pointLinePoint():
    """ Point(s)=(Point(s),Line(s)):
    Create projection(s) of Point(s) onto Line(s).

    First
    - Select one (or several) Point(s)
    and Second
    - Select one or several Line/Edge(s) and/or
    - Select one or several Plane/Face(s) to process and/or
    - Select one or several Object(s) to process all Faces at once
    - Then Click on the button

    Plot the intersection point T on a Line given one Line and One Point C.
    The Vector TC is perpendicular to the Line.
    The symmetrical point Cprime is also created as TC=TCprime.

    Be aware that if the line is not extended enough the intersection Point is still created (as if).
    """
    msg = verbose

    error_msg = """Unable to create (Point,Line) Intersection(s):
    First
    - Select one (or several) Point(s)
    and Second
    - Select one or several Line/Edge(s) and/or
    - Select one or several Plane/Face(s) to process and/or
    - Select one or several Object(s) to process all Faces at once
    - Then Click on the button
    but at least select one Line and one Point not on the Line !"""
    result_msg = ": (Point,Line) Intersection(s) and symmetric(s) are created !"

    createFolders('WorkPoints')
    m_dir = 'Set'
    name = "PointLinePoint"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))

    try:
        Number_of_Points, Point_List = m_sel.get_points(getfrom=["Points"])
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
        Number_of_Edges, Edge_List = m_sel.get_segments(getfrom=["Segments", "Curves", "Planes", "Objects"])
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))

        if (Number_of_Points >= 1) and (Number_of_Edges >= 1):
            for Selected_Edge in Edge_List:
                for Selected_Point in Point_List:

                    Vector_A = Selected_Edge.valueAt(0.0)
                    Vector_B = Selected_Edge.valueAt(Edge_List[0].Length)
                    Vector_C = Selected_Point.Point

                    Vector_T, Distance, Vector_Tprime = intersecPerpendicularLine(Vector_A, Vector_B, Vector_C, info=0)

                    Center_User_Name = plot_point(Vector_T, part, name, str(m_dir))
                    print_point(Vector_T, str(Center_User_Name) + result_msg + " at:")
                    Center_User_Name2 = plot_point(Vector_Tprime, part, name + "_PRIM", str(m_dir))
                    print_point(Vector_Tprime, str(Center_User_Name2) + result_msg + " at:")

                    print_msg(str(Center_User_Name) + result_msg + " at a distance from the line of " + str(Distance))
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_pointLinePoint2():
    """ Point(s)=(Point(s),Line(s)):
        Create projection(s) of Point(s) onto Line(s).
        Plot the intersection point T on a Line given one Linee and One Point C.
        The Vector TC is perpendicular to the Line.
        The symmetric point Cprime is also created as TC=TCprime.
        - First select one (or several) Point(s)
        - Second select one or several) Line(s)
    """
    msg = verbose
    createFolders('WorkPoints')
    error_msg = "Unable to create (Point,Line) Intersection: \n" +\
                "Select at least one Line and one Point not on the Line !"
    result_msg = ": (Point,Line) Intersection and symmetric are created !"
    name = "PointLinePoint"
    part = "Part::Feature"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg(" Number_of_Points=" + str(Number_of_Points))
            print_msg(" Number_of_Edges=" + str(Number_of_Edges))
        if (Number_of_Points >= 1) and (Number_of_Edges >= 1):
            Point_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]

            for Selected_Edge in Edge_List:
                for Selected_Point in Point_List:

                    Vector_A = Selected_Edge.valueAt(0.0)
                    Vector_B = Selected_Edge.valueAt(Edge_List[0].Length)
                    Vector_C = Selected_Point.Point

                    Vector_T, Distance, Vector_Tprime = intersecPerpendicularLine(Vector_A, Vector_B, Vector_C, info=0)

                    Center_User_Name = plot_point(Vector_T, part, name)
                    print_point(Vector_T, str(Center_User_Name) + result_msg + " at:")
                    Center_User_Name2 = plot_point(Vector_Tprime, part, name)
                    print_point(Vector_Tprime, str(Center_User_Name2) + result_msg + " at:")

                    print_msg(str(Center_User_Name) + result_msg + " at a distance from the line of " + str(Distance))
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def distanceLinePoint(value):
    """ Respond to the change in distance value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_distanceLinePoint
        if str(value) == '-':
            return
        m_distanceLinePoint = float(value)
        print_msg("New distance is:" + str(m_distanceLinePoint))
        # plot_alongLinePoint()
    except ValueError:
        printError_msg("Distance must be valid number !")


def plot_alongLinePoint():
    """ Plot a point at a certain distance along the line respecting to the chosen
    reference starting point.
    """
    msg = verbose

    error_msg = """Unable to create a point along a Line:
    Select one Edge and one Point on this Edge only !\n"
    or Select one Edge only and the first point of this Edge will be used as ref.!"""
    result_msg = ": Point along a Line created !"

    createFolders('WorkPoints')
    name = "PointLine"
    part = "Part::Feature"

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))
            print_msg("Number_of_Points=" + str(Number_of_Points))
        if (Number_of_Edges == 1) and (Number_of_Points) == 1:
            Point_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg(str(Point_List))
                print_msg(str(Edge_List))
            Vector_C = Point_List[0].Point
            Vector_A = Edge_List[0].Vertexes[0].Point
            Vector_B = Edge_List[0].Vertexes[-1].Point
            if msg != 0:
                print_point(Vector_C, msg="Reference Point: ")
                print_point(Vector_A, msg="Point A: ")
                print_point(Vector_B, msg="Point B: ")
            if colinearVectors(Vector_A, Vector_B, Vector_C, info=msg):
                Vector_Translate = (Vector_B - Vector_A)
                if msg != 0:
                    print_point(Vector_Translate, msg="Vector_Translate")
                Vector_Translate = Vector_Translate.normalize() * m_distanceLinePoint
                if msg != 0:
                    print_point(Vector_Translate, msg="Vector_Translate")
                Vector_Line_Point = Vector_C + Vector_Translate

                Center_User_Name = plot_point(Vector_Line_Point, part, name)

                print_point(Vector_Line_Point, str(Center_User_Name) + result_msg + " at:")
            else:
                printError_msg("The Point and the line MUST be aligned !")
        elif (Number_of_Edges == 1) and (Number_of_Points) == 0:
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg(str(Edge_List))
            Vector_C = Edge_List[0].Vertexes[0].Point
            Vector_A = Edge_List[0].Vertexes[0].Point
            Vector_B = Edge_List[0].Vertexes[-1].Point
            if msg != 0:
                print_point(Vector_C, msg="Reference Point: ")
                print_point(Vector_A, msg="Point A: ")
                print_point(Vector_B, msg="Point B: ")
            Vector_Translate = (Vector_B - Vector_A)
            if msg != 0:
                print_point(Vector_Translate, msg="Vector_Translate")
            Vector_Translate = Vector_Translate.normalize() * m_distanceLinePoint
            if msg != 0:
                print_point(Vector_Translate, msg="Vector_Translate")
            Vector_Line_Point = Vector_C + Vector_Translate

            Center_User_Name = plot_point(Vector_Line_Point, part, name)
            print_point(Vector_Line_Point, str(Center_User_Name) + result_msg + " at:")
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_2LinesPoint():
    """ Point(s)=(Line(s),Line(s)):
    Plot one or two Point(s) at minimum distance of two Lines
    Create a unique Point at intersection of 2 crossing Lines.

    First
    - Select two or more Line/Edge(s) and
    - Then Click on the button

    Plot the point A on the first Line given and the point  B on the second Line.
    The Vector AB perpendicular to the first and second Line.

    """
    msg = verbose

    error_msg = """Unable to create (Line,Line) Intersection(s):
    First
    - Select two or more Line/Edge(s) and
    - Then Click on the button
    but at least select two different Lines !"""
    result_msg = ": (Line,Line) Intersection(s) are created !"

    createFolders('WorkPoints')
    m_dir = 'Set'
    name = "Intersection"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))

    try:
        Number_of_Edges, Edge_List = m_sel.get_segments(getfrom=["Segments", "Curves", "Planes", "Objects"])
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))

        if Number_of_Edges >= 2:
            for i in range(Number_of_Edges - 1):
                f1 = Edge_List[i]
                f2 = Edge_List[i + 1]
                # print_msg(str(f1))
                # print_msg(str(f2))
                d = f1.distToShape(f2)
                print_msg(str(d))
                Distance = d[0]
                Vector_A = d[1][0][0]
                # print_point(Vector_A,"Vector_A is: ")
                Vector_B = d[1][0][1]
                if abs(Distance) <= 1.e-14:
                    Center_User_Name = plot_point(Vector_A, part, name, str(m_dir))
                    print_msg(str(Center_User_Name) + result_msg)
                else:
                    Center_User_Name = plot_point(Vector_A, part, name, str(m_dir))
                    print_point(Vector_A, str(Center_User_Name) + result_msg + " at:")
                    Center_User_Name = plot_point(Vector_B, part, name, str(m_dir))
                    print_point(Vector_B, str(Center_User_Name) + result_msg + " at:")
                    print_msg(" Distance between the points is: " + str(Distance))
        else:
            printError_msg(error_msg)

    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_2LinesPoint2():
    """ Plot one or two Point(s) at minimum distance of two Lines.
    """
    msg = verbose

    error_msg = "Unable to create (Line,Line) Intersection(s): \nSelect two Lines !"
    result_msg = ": (Line,Line) Intersection(s) are created !"

    createFolders('WorkPoints')
    name = "Intersection"
    part = "Part::Feature"
    Selection = get_SelectedObjects(info=msg)
    try:
        SelectedObjects = Selection
        Number_of_Edges = SelectedObjects[1]
        if Number_of_Edges == 2:
            Edge_List = SelectedObjects[4]
            f1 = Edge_List[0]
            f2 = Edge_List[1]
            # print_msg(str(f1))
            # print_msg(str(f2))
            d = f1.distToShape(f2)
            # print_msg(str(d))
            Distance = d[0]
            Vector_A = d[1][0][0]
            # print_point(Vector_A,"Vector_A is: ")
            Vector_B = d[1][0][1]
            if abs(Distance) <= 1.e-14:
                Center_User_Name = plot_point(Vector_A, part, name)
                print_msg(str(Center_User_Name) + result_msg)
            else:
                Center_User_Name = plot_point(Vector_A, part, name)
                print_point(Vector_A, str(Center_User_Name) + result_msg + " at:")
                Center_User_Name = plot_point(Vector_B, part, name)
                print_point(Vector_B, str(Center_User_Name) + result_msg + " at:")
                print_msg(str(Center_User_Name) + result_msg + " at a distance of " + str(Distance))
        else:
            printError_msg(error_msg)

    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def numberPoint(value):
    """ Respond to the change in number of point from the spin box.
    """
    msg = verbose

    try:
        # First we check if a valid number have been entered
        global m_numberPoint
        if str(value) == '-':
            return
        m_numberPoint = int(value)
        if m_numberPoint == 0:
            m_numberPoint = 1
        if msg != 0:
            print_msg("New number is:" + str(m_numberPoint))
    except ValueError:
        printError_msg("Number must be valid !")


def distPoint(value):
    """ Respond to the change in Distance between point value from the text box.
    """
    msg = verbose
    try:
        # First we check if a valid number have been entered
        global m_distPoint
        if str(value) == '-':
            return
        m_distPoint = float(value)
        if msg != 0:
            print_msg("New Distance between point is:" + str(m_distPoint))
    except ValueError:
        printError_msg("Distance between point must be valid number !")


def plot_distPoint():
    """ Axes=(Axis,Pt,dist)):
        Create an Axis parallel to a given Axis, Point at a given distance.
        The Axis is created on the Plane defined by the given Axis and Point.
        - First select an Axis (or several Axes) and a Point
        (you can also select several points to define different Planes)

        NB: The distance to the Axis created can be defined first.
        Positive number in one direction and negative in the other one.
        The second number indicates the number of Axes to create.

        If an Edge of a Cube is selected the Cube is duplicate with the corresponding
    """
    global verbose
    global m_numberPoint
    global m_distPoint
    msg = verbose
    createFolders('WorkPoints')
    error_msg = "Unable to create Point(s): \nSelect one (or several) Point and one or several Lines"
    result_msg = ": Point(s) created !"

    Selection = get_SelectedObjectsWithParent(info=msg, printError=False)

    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]

        if (Number_of_Edges >= 1) and (Number_of_Points >= 1):
            Edge_List = SelectedObjects[4]
            Points_List = SelectedObjects[3]
            if msg != 0:
                print_msg("Number_of_Points = " + str(Number_of_Points))
                print_msg("Number_of_Edges = " + str(Number_of_Edges))
                print_msg("Point List = " + str(Points_List))
                print_msg("Edge List = " + str(Edge_List))

            # Loop on the Points
            for Selected_Point_dict in Points_List:
                if msg != 0:
                    print_msg("Selected_Point_dict = " + str(Selected_Point_dict))
                for Selected_Point, Parent_Point in Selected_Point_dict.iteritems():
                    if msg != 0:
                        print_msg("Selected_Point = " + str(Selected_Point))
                        print_msg("Parent_Point = " + str(Parent_Point))
                    Point_C = Selected_Point.Point
                    if msg != 0:
                        print_point(Point_C, msg="Point_C: ")
                    Placement1 = Selected_Point.Placement
                    # Placement1 = Parent_Point.Placement
                    # base1 = Placement1.Base
                    # base1 = Point_C
                    rot1 = Placement1.Rotation
                    center_Vector = Point_C
                    m_move = Base.Vector(0, 0, 0)
                    Move_Vector = Base.Vector(0, 0, 0)
                    # Loop on the Edges
                    for Selected_Edge_dict in Edge_List:
                        for Selected_Edge, Parent_Edge in Selected_Edge_dict.iteritems():
                            if msg != 0:
                                print_msg("Selected_Edge = " + str(Selected_Edge))
                                print_msg("Parent_Edge = " + str(Parent_Edge))

                            Point_A = Selected_Edge.Vertexes[0].Point
                            Point_B = Selected_Edge.Vertexes[-1].Point
                            if msg != 0:
                                print_point(Point_A, msg="Selected_Edge.Vertexes[0]  Point_A: ")
                                print_point(Point_B, msg="Selected_Edge.Vertexes[-1] Point_B: ")
                            AB_Vector = Point_B.sub(Point_A)
                            AB_Vector = AB_Vector.normalize()
                            # plot_axis(Base.Vector(0, 0, 0), AB_Vector, "Part::Feature", "AB")
                            Move_Vector = AB_Vector.multiply(m_distPoint)
                            Move_Vector = Move_Vector.add(center_Vector)
                            # plot_axis(Base.Vector(0, 0, 0), Move_Vector, "Part::Feature", "Move_Vector")
                            m_move = Move_Vector.sub(center_Vector)

                            if msg != 0:
                                print_point(Move_Vector, msg="Move_Vector = ")
                                print_point(m_move, msg="m_move = ")
                                print_msg("m_numberPoint = " + str(m_numberPoint))

                            for m_i in range(m_numberPoint):
                                # if objCopy == 1:
                                #     m_new_point = App.activeDocument().copyObject(Parent_Point)
                                # else:
                                m_new_point_shape = Selected_Point.copy()
                                m_new_point = App.ActiveDocument.addObject("Part::Feature", "Point_at_distance")
                                m_new_point.Shape = m_new_point_shape
                                App.ActiveDocument.getObject('WorkPoints').addObject(m_new_point)
                                Point_User_Name = m_new_point.Label

                                newplace1 = App.Placement(m_move, rot1)
                                m_new_point.Placement = newplace1
                                # Update the move
                                m_move = m_move.add(Move_Vector.sub(center_Vector))

                                properties_point(Point_User_Name)
                                print_msg(str(Point_User_Name) + result_msg)

        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_distPoint2():
    """ Axes=(Axis,Pt,dist)):
        Create an Axis parallel to a given Axis, Point at a given distance.
        The Axis is created on the Plane defined by the given Axis and Point.
        - First select an Axis (or several Axes) and a Point
        (you can also select several points to define different Planes)

        NB: The distance to the Axis created can be defined first.
        Positive number in one direction and negative in the other one.
        The second number indicates the number of Axes to create.

        If an Edge of a Cube is selected the Cube is duplicate with the corresponding
    """
    global verbose
    global m_numberPoint
    global m_distPoint
    msg = verbose
    createFolders('WorkPoints')
    error_msg = "Unable to create Point(s): \nSelect one (or several) Point and one or several Lines"
    result_msg = ": Point(s) created !"

    Selection = get_SelectedObjectsWithParent(info=msg, printError=False)

    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]

        if (Number_of_Edges >= 1) and (Number_of_Points >= 1):
            Edge_List = SelectedObjects[4]
            Points_List = SelectedObjects[3]
            if msg != 0:
                print_msg("Number_of_Points = " + str(Number_of_Points))
                print_msg("Number_of_Edges = " + str(Number_of_Edges))
                print_msg("Point List = " + str(Points_List))
                print_msg("Edge List = " + str(Edge_List))

            # Loop on the Points
            for Selected_Point_dict in Points_List:
                if msg != 0:
                    print_msg("Selected_Point_dict = " + str(Selected_Point_dict))
                for Selected_Point, Parent_Point in Selected_Point_dict.iteritems():
                    if msg != 0:
                        print_msg("Selected_Point = " + str(Selected_Point))
                        print_msg("Parent_Point = " + str(Parent_Point))
                    Point_C = Selected_Point.Point
                    if msg != 0:
                        print_point(Point_C, msg="Point_C: ")
                    Placement1 = Selected_Point.Placement
                    # Placement1 = Parent_Point.Placement
                    # base1 = Placement1.Base
                    # base1 = Point_C
                    rot1 = Placement1.Rotation
                    center_Vector = Point_C
                    m_move = Base.Vector(0, 0, 0)
                    Move_Vector = Base.Vector(0, 0, 0)
                    # Loop on the Edges
                    for Selected_Edge_dict in Edge_List:
                        for Selected_Edge, Parent_Edge in Selected_Edge_dict.iteritems():
                            if msg != 0:
                                print_msg("Selected_Edge = " + str(Selected_Edge))
                                print_msg("Parent_Edge = " + str(Parent_Edge))

                            Point_A = Selected_Edge.Vertexes[0].Point
                            Point_B = Selected_Edge.Vertexes[-1].Point
                            if msg != 0:
                                print_point(Point_A, msg="Selected_Edge.Vertexes[0]  Point_A: ")
                                print_point(Point_B, msg="Selected_Edge.Vertexes[-1] Point_B: ")
                            AB_Vector = Point_B.sub(Point_A)
                            AB_Vector = AB_Vector.normalize()
                            # plot_axis(Base.Vector(0, 0, 0), AB_Vector, "Part::Feature", "AB")
                            Move_Vector = AB_Vector.multiply(m_distPoint)
                            Move_Vector = Move_Vector.add(center_Vector)
                            # plot_axis(Base.Vector(0, 0, 0), Move_Vector, "Part::Feature", "Move_Vector")
                            m_move = Move_Vector.sub(center_Vector)

                            if msg != 0:
                                print_point(Move_Vector, msg="Move_Vector = ")
                                print_point(m_move, msg="m_move = ")
                                print_msg("m_numberPoint = " + str(m_numberPoint))

                            for m_i in range(m_numberPoint):
                                # if objCopy == 1:
                                #      m_new_point = App.activeDocument().copyObject(Parent_Point)
                                # else:
                                m_new_point_shape = Selected_Point.copy()
                                m_new_point = App.ActiveDocument.addObject("Part::Feature", "Point_at_distance")
                                m_new_point.Shape = m_new_point_shape
                                App.ActiveDocument.getObject('WorkPoints').addObject(m_new_point)
                                Point_User_Name = m_new_point.Label

                                newplace1 = App.Placement(m_move, rot1)
                                m_new_point.Placement = newplace1
                                # Update the move
                                m_move = m_move.add(Move_Vector.sub(center_Vector))

                                properties_point(Point_User_Name)
                                print_msg(str(Point_User_Name) + result_msg)

        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def numberPointCutWire(value):
    """ Respond to the change in number of cut value from the spin box.
    """
    global verbose
    msg = verbose

    try:
        # First we check if a valid number have been entered
        global m_numberPointCutWire
        if str(value) == '-':
            return
        m_numberPointCutWire = int(value)
        if msg != 0:
            print_msg("New number is:" + str(m_numberPointCutWire))
    except ValueError:
        printError_msg("Number must be valid !")


def cutWire(numberOfPoints, createPoint=1, createLine=0):
    """ Partition a Wire and create points, lines, with possible two colours of line.

    Original code from: Mario52 03/2015
    Adapted to WF by  : Rentlau_64 03/2015
    """

    def createLines(number, listOfPoints):
        """ Create line
        """
        global biColor
        m_points = listOfPoints
        m_numberOfLines = number - 1
        m_biColor = biColor
        if msg != 0:
            print_msg("Number of Lines =" + str(m_numberOfLines))
            print_msg("Points =" + str(m_points))
            print_msg("biColor =" + str(m_biColor))

        red = 0
        createFolders('WorkAxis')
        for m_lin in range(m_numberOfLines):
            Vector_A = Base.Vector(m_points[m_lin])
            Vector_B = Base.Vector(m_points[m_lin + 1])
            # creaLine = [Vector_A,Vector_B]
            axis_User_Name, axis = plot_axis(Vector_A, Vector_B, part="Part::Feature", name="Axis_Wire", grp="WorkAxis")
            # wire = Draft.makeWire(creaLine,closed=False,face=False,support=None)
            # Optional biColor
            if m_biColor != 0:
                if red == 0:
                    # 255 = 1 (10 = (1/255 * 10 ))
                    # Gui.ActiveDocument.getObject(wire.Name).LineColor = (1.0,0.0,0.0)
                    Gui.ActiveDocument.getObject(axis_User_Name).LineColor = (1.0, 0.0, 0.0)
                    red = 1
                else:
                    # Gui.ActiveDocument.getObject(wire.Name).LineColor = (1.0,1.0,1.0)
                    Gui.ActiveDocument.getObject(axis_User_Name).LineColor = (1.0, 1.0, 1.0)
                    red = 0

    global verbose
    msg = verbose

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    error_msg = "Unable to select Wire(s): \nSelect at least one Edge\nor one Object !"
    m_points = []
    del m_points[:]
    if msg != 0:
        print_msg("Number of cuts =" + str(numberOfPoints))
        print_msg("CreatePoint flag=" + str(createPoint))
        print_msg("CreateLine flag =" + str(createLine))
    numberOfPoints += 1

    try:
        selectionObjects = Gui.Selection.getSelectionEx()
        if msg != 0:
            print_msg("SelectionObjects is:" + str(selectionObjects))
        found = 0
        for sel in selectionObjects:
            if msg != 0:
                print_msg("Selection is:" + str(sel))
            # if hasattr(sel,'SubObjects')
            if sel.HasSubObjects:
                if msg != 0:
                    print_msg("Found SubObjects")
                for sub in sel.SubObjects:
                    if hasattr(sub, 'Edges'):
                        compteur = 0
                        for edge in sub.Edges:
                            if msg != 0:
                                print_msg("Edge is:" + str(edge))
                            if hasattr(edge, 'discretize'):
                                found = 1
                                compteur += 1
                                points = edge.discretize(numberOfPoints)
                                for p in points:
                                    if createPoint != 0:
                                        plot_point(p, part="Part::Feature", name="Point_Wire", grp="WorkPoints")
                                        # Draft.makePoint( p.x, p.y, p.z)
                                    print_point(p, msg=str(compteur) + ":")
                                if createLine != 0:
                                    if msg != 0:
                                        print_msg("createLines function call ")
                                    createLines(numberOfPoints, points)

            else:
                shape = sel.Object.Shape
                if msg != 0:
                    print_msg("Found NO SubObjects")
                    print_msg("Shape is:" + str(shape))

                if hasattr(shape, 'Edges'):
                    compteur = 0
                    for edge in shape.Edges:
                        if msg != 0:
                            print_msg("Edge is:" + str(edge))
                        if hasattr(edge, 'discretize'):
                            found = 1
                            compteur += 1
                            points = edge.discretize(numberOfPoints)
                            for p in points:
                                if createPoint != 0:
                                    plot_point(p, part="Part::Feature", name="Point_Wire", grp="WorkPoints")
                                    # Draft.makePoint( p.x, p.y, p.z)
                                print_point(p, msg=str(compteur) + ":")
                            if createLine != 0:
                                createLines(numberOfPoints, points)
        if found == 0:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)

    return


def plot_cutWirePoint():
    createFolders('WorkPoints')
    global m_numberPointCutWire
    if not (m_numberPointCutWire >= 2 and m_numberPointCutWire <= 100):
        m_numberPointCutWire = 2
    cutWire(m_numberPointCutWire, createPoint=1, createLine=0)


def plot_clickForPoint():
    """ Plot a Point at location of a mouse click.
    """
    msg = verbose

    createFolders('WorkPoints')

    global m_set
    global m_stack
    global m_callback
    global m_clickForPoint

    if msg != 0:
        print_msg("plot_clickForPoint: flag is " + str(m_clickForPoint))

    # Mimic behavior of toggle button
    view = get_ActiveView()
    if m_clickForPoint:
        try:
            m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_set))
        except Exception as inst:
            print(inst.args)
            printError_msg("Could not Create '" + str(m_set) + "' Objects Group!")
            return None
        m_set = m_r.Name

        m_callback = view.addEventCallback("SoMouseButtonEvent", getClickedPoint)
    else:
        del m_stack[:]
        m_set = 'Set'
        view.removeEventCallback("SoMouseButtonEvent", m_callback)

    m_clickForPoint = not m_clickForPoint


def plot_baseObjectPoint():
    """ Plot base point of all selected objects.
    """
    msg = verbose

    createFolders('WorkPoints')
    error_msg = "Unable to create Base point of Object(s): \nSelect at least one Object !"
    result_msg = ": Base point of Object(s) created !"
    name = "BasePoint"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    # Return a list of SelectionObjects for a given document name.
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    m_objs = [selobj.Object for selobj in m_selEx]
    m_num = len(m_objs)
    if m_num >= 1:
        for m_i in range(0, m_num):
            m_base = m_objs[m_i].Placement.Base
            if m_base is not None:
                Center_User_Name = plot_point(m_base, part, name)
                print_point(m_base, str(Center_User_Name) + result_msg + " at:")
            else:
                printError_msg(error_msg)
    else:
        printError_msg(error_msg)


def plot_centerMassObjectPoint():
    """ Plot Center of Mass Point of all selected Object(s).
    """
    msg = verbose
    msg = 1

    createFolders('WorkPoints')
    error_msg = "Unable to create Center of Mass point of Object(s): \nSelect at least one Object !"
    result_msg = ": Center of Mass point of Object(s) created !"
    name = "CenterMassPoint"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    # Return a list of selected objects for a given document name.
    SelectedObjects = get_SelectedObjects(info=msg, printError=False)

    Number_of_Objects = len(SelectedObjects[6])
    if Number_of_Objects >= 1:
        for m_object in SelectedObjects[6]:

            m_center = m_object.Shape.CenterOfMass
            if m_center is not None:
                Center_User_Name = plot_point(m_center, part, name)
                print_point(m_center, str(Center_User_Name) + result_msg + " at:")
            else:
                printError_msg(error_msg)
    else:
        printError_msg(error_msg)


def plot_objectNPoints():
    """Create a set of points from selected Objects:
    - Select object(s)
    to create points from these object(s) !
    If you select an Edge: 2 points will be created;
    if you select a Plane: 4 points will be created;
    if you select an Object: many points will be created.
    """
    msg = verbose

    error_msg = "Create a set of points from selected Objects: \n" +\
                "Select object(s) \n" +\
                "to create points from these object(s) !\n" +\
                "If you select an Edge: 2 points will be created;\n" +\
                "if you select a Plane: 4 points will be created;\n" +\
                "if you select an Object: many points will be created.\n"

    createFolders('WorkPoints')
    m_dir = 'Object'
    name = "Point"
    part = "Part::Feature"
    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
    m_dir = m_r.Name
    result_msg = " Point(s) created into: WorkPoints/" + str(m_dir)

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    SelectedObjects = get_SelectedObjects(info=msg, printError=False)

    try:
        Selected_Points = []

        Number_of_Edges = SelectedObjects[1]
        Number_of_Faces = SelectedObjects[2]
        Number_of_Objects = len(SelectedObjects[6])
        if msg != 0:
            print_msg("Number_of_Edges = " + str(Number_of_Edges))
            print_msg("Number_of_Faces = " + str(Number_of_Faces))
            print_msg("Number_of_Objects = " + str(Number_of_Objects))
        if Number_of_Edges > 0:
            Edge_List = SelectedObjects[4]
            for m_edge in Edge_List:
                Selected_Points.append(m_edge.Vertexes[0])
                Selected_Points.append(m_edge.Vertexes[-1])

        if Number_of_Faces > 0:
            Face_List = SelectedObjects[5]
            for m_face in Face_List:
                Edge_List = m_face.Edges
                for m_edge in Edge_List:
                    Selected_Points.append(m_edge.Vertexes[0])
                    Selected_Points.append(m_edge.Vertexes[-1])

        if Number_of_Objects > 0:
            Object_List = SelectedObjects[6]
            for m_object in Object_List:
                for m_vertex in m_object.Shape.Vertexes:
                    Selected_Points.append(m_vertex)
        m_points = Selected_Points
        Number_of_Points = len(m_points)
        if msg != 0:
            print_msg("Number_of_Points = " + str(Number_of_Points))
        if Number_of_Points >= 1:
            for m_point in m_points:
                if msg != 0:
                    print_point(FreeCAD.Vector(m_point.Point))
                plot_point(m_point.Point, part, name, str(m_dir))

            print_msg(str(m_dir) + ": " + str(Number_of_Points) + result_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def point_toSketch():
    """ Transform Point(s) in Sketch's Point(s) by projection onto the Sketch's Plane:
    - First select an existing Sketch;
    - Select as much as Points needed;
    Then click on this button.
    """
    msg = verbose

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None
    error_msg = "Transform Point(s) in Sketch's Point(s): \n" +\
                "First select an existing Sketch\n" +\
                "then select point(s) !"
    result_msg = ": Point(s) transformed in Sketch's Point(s) done!"

    m_sel  = Gui.Selection.getSelection(m_actDoc.Name)
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg("m_sel       : " + str(m_sel))
    m_num = len(m_sel)
    m_num_point = 0
    if m_num > 1:
        # Get the Sketch from the selection
        m_obj = m_sel[0]
        if msg != 0:
            print_msg("m_obj       : " + str(m_obj))
        if hasattr(m_obj, 'TypeId'):
            m_type = m_obj.TypeId
            if msg != 0:
                print_msg("m_obj.TypeId: " + str(m_type))
        else:
            m_type = m_obj.Type
            if msg != 0:
                print_msg("m_obj.Type: " + str(m_type))

        if m_type[:6] == "Sketch":
            if msg != 0:
                print_msg("Found a Sketch object!")
            m_sketch = m_obj

            # Build a point list
            m_pointList = []
            # Get Point(s) from the selection
            for m_obj in m_selEx[1:]:
                if len(m_obj.SubObjects) != 0:
                    SubObject = m_obj.SubObjects[0]
                    if SubObject.ShapeType == "Vertex":
                        if msg != 0:
                            print_msg("Found a Points object!")
                        # Get the Point
                        m_Point = m_obj.SubObjects[0]
                        # Append the Point
                        m_pointList.append(m_Point)
                        m_num_point = m_num_point + 1
                    else:
                        continue
                else:
                    continue

            num_point, return_points = vertexToSketch(m_pointList, m_sketch)
            if m_num_point != num_point:
                printError_msg(error_msg)
                return
            if msg != 0:
                createFolders('WorkPoints')
                for point in return_points:
                    plot_point(point, part="Part::Feature", name="Sketch_Proj", grp="WorkPoints")
            # Refresh
            App.getDocument(str(m_actDoc.Name)).recompute()
            print_msg(str(num_point) + result_msg)
        else:
            printError_msg(error_msg)
    else:
        printError_msg(error_msg)
    return


def point_toSketch_old():
    """ Transform Point(s) in Sketch's Point(s) by projection onto the Sketch's Plane:
    - First select an existing Sketch;
    - Select as much as Points needed;
    Then click on this button.
    """
    msg = verbose

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None
    error_msg = "Transform Point(s) in Sketch's Point(s): \n" +\
                "First select an existing Sketch\n" +\
                "then select point(s) !"
    result_msg = ": Point(s) transformed in Sketch's Point(s) done!"

    m_sel = Gui.Selection.getSelection(m_actDoc.Name)
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg("m_sel       : " + str(m_sel))
    m_num = len(m_sel)
    m_num_point = 0
    if m_num > 1:
        # Get the Sketch from the selection
        m_obj = m_sel[0]
        if msg != 0:
            print_msg("m_obj       : " + str(m_obj))
        if hasattr(m_obj, 'TypeId'):
            m_type = m_obj.TypeId
            if msg != 0:
                print_msg("m_obj.TypeId: " + str(m_type))
        else:
            m_type = m_obj.Type
            if msg != 0:
                print_msg("m_obj.Type: " + str(m_type))

        if m_type[:6] == "Sketch":
            if msg != 0:
                print_msg("Found a Sketch object!")
            m_sketch = m_obj
            # Get the Sketch Plane info
            m_rec1 = Part.makePlane(1, 1)
            m_rec2 = Part.makePlane(1, 1)
            m_rec1.Placement = m_sketch.Placement.inverse()
            m_rec2.Placement = m_sketch.Placement

            if msg != 0:
                print_msg("m_sketch.Placement.inverse = " + str(m_rec1.Placement))
                print_msg("m_sketch.Placement = " + str(m_rec2.Placement))

            m_rec2N = m_rec2.normalAt(0, 0)

            # Build a geometry list
            geoList = []
            # Get Point(s) from the selection
            for m_obj in m_selEx[1:]:
                if len(m_obj.SubObjects) != 0:
                    SubObject = m_obj.SubObjects[0]
                    if SubObject.ShapeType == "Vertex":
                        if msg != 0:
                            print_msg("Found a Points object!")
                        # Get the Point
                        Point = m_obj.SubObjects[0]
                        m_p1 = App.Base.Vector(Point.Point)
                        # App.Base.Placement.multVec
                        # multVector(Vector) -> Vector
                        # Compute the transformed vector using the placement
                        Projection1 = m_rec1.Placement.multVec(m_p1)

                        if msg != 0:
                            m_p2 = App.Base.Vector(Point.Point)
                            # Projection of the Point selected onto the Sketch Plane
                            Projection2 = m_p2.projectToPlane(m_sketch.Placement.Base, m_rec2N)
                            createFolders('WorkAxis')
                            plot_axis(Point.Point, Projection1, part="Part::Feature", name="Norml1", grp="WorkAxis")
                            plot_axis(Point.Point, Projection2, part="Part::Feature", name="Norml2", grp="WorkAxis")
                            createFolders('WorkPoints')
                            plot_point(Projection1, part="Part::Feature", name="Proj1", grp="WorkPoints")
                            plot_point(Projection2, part="Part::Feature", name="Proj2", grp="WorkPoints")

                        # Append the Projection
                        geoList.append(Part.Point(Projection1))

                        # Add the geometry list to the Sketch
                        m_sketch.addGeometry(geoList)
                        m_num_point = m_num_point + 1

                    else:
                        continue
                else:
                    continue
            # Refresh
            App.getDocument(str(m_actDoc.Name)).recompute()
            print_msg(str(m_num_point) + result_msg)
        else:
            printError_msg(error_msg)
    else:
        printError_msg(error_msg)
    return


def point_toLoad():
    """Load a set of points from an ASCII file:
    ASCII format is 3 values by line separated by blank as:
        <15.3f  <15.3f  <15.3f
    Values are read as float.

    Lines starting with characeter: # or / are considered as comment lines
    """
    msg = verbose

    error_msg = "Unable to load Point(s) !"
    result_msg = " Point(s) loaded from "

    if not createFolders('WorkPoints'):
        return
    m_dir = 'Load'
    name = "Point"
    part = "Part::Feature"

    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
    m_dir = m_r.Name

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        import WorkFeature.Utils.WF_points_set as WFps
    except Exception as inst:
        print(inst.args)
        printError_msg("Unable to import Utils.WF_points_set !")

    # fname, _ = QtGui.QFileDialog.getOpenFileName(None, 'Select a file',os.environ['HOME'],"Text Files (*.txt *.asc *.dat)")
    fname, _ = QtGui.QFileDialog.getOpenFileName(None, 'Select a file', os.path.expanduser('~'), "Text Files (*.txt *.asc *.dat)")

    try:
        m_pts = WFps.points_set([], str(fname))
        m_points = m_pts.load()
        Number_of_Points = len(m_points)
        if Number_of_Points >= 1:
            for m_point in m_points:
                if msg != 0:
                    print_point(FreeCAD.Vector(m_point))
                plot_point(m_point, part, name, str(m_dir))

            print_msg(str(m_dir) + ": " + str(Number_of_Points) + result_msg + str(fname))
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def point_toSave():
    """Save a point or a set of points into an ASCII file.
    One (x, y, z) triplet per line separated by blank.
    - Select as much as Points as needed and/or select object(s)
    to save points from these object(s) !
    If you select an Edge: 2 points will be saved;
    if you select a Plane: 4 points will be saved;
    if you select an Object: many points will be saved.
    Then click on this button.
    """
    msg = verbose

    error_msg = """Save a point or a set of points into an ASCII file:
     Select as much as Points as needed and/or select object(s)
    to save points from these object(s) !
    If you select an Edge: 2 points will be saved;
    if you select a Plane: 4 points will be saved;
    if you select an Object: many points will be saved!"""
    result_msg = " Point(s) saved into: "

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))

    try:
        import WF_points_set as WFps
    except Exception as inst:
        print(inst.args)
        printError_msg("Unable to import Utils.WF_points_set !")

    try:
        Number_of_Points, Point_List = m_sel.get_points(getfrom=["Points", "Segments", "Curves", "Planes", "Objects"])
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
        m_points = []
        if Number_of_Points >= 1:
            for m_point in Point_List:
                if msg != 0:
                    print_point(FreeCAD.Vector(m_point.Point))
                m_x = m_point.Point.x
                m_y = m_point.Point.y
                m_z = m_point.Point.z
                m_points.append((m_x, m_y, m_z))

            if msg != 0:
                print_msg(str(m_points))

            m_pts = WFps.points_set(m_points)

            # fname, _ = QtGui.QFileDialog.getSaveFileName(None, 'Select a file',os.environ['HOME'])
            fname, _ = QtGui.QFileDialog.getSaveFileName(None, 'Select a file', os.path.expanduser('~'))

            if m_pts.save(str(fname)):
                print_msg(str(Number_of_Points) + result_msg + str(fname))
            else:
                printError_msg("Not able to save the requested Point(s)!")
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def point_toSave2():
    """Save a point or a set of points into an ASCII file.
    One (x, y, z) triplet per line separated by blank.
    - Select as much as Points as needed and/or select object(s)
    to save points from these object(s) !
    If you select an Edge: 2 points will be saved;
    if you select a Plane: 4 points will be saved;
    if you select an Object: many points will be saved.
    Then click on this button.
    """
    msg = verbose

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    error_msg = "Save a point or a set of points into an ASCII file: \n" +\
                "Select point(s) and/or select object(s) \n" +\
                "to save points from these object(s) !"
    result_msg = " Point(s) saved into: "

    # Return a list of Points selected for a given document name.
    Selection = get_pointsFromSelectedObjects(info=0, printError=True)

    try:
        import WF_points_set as WFps
    except Exception as inst:
        print(inst.args)
        printError_msg("Unable to import Utils.WF_points_set !")

    try:
        SelectedPoints = Selection
        Number_of_Points = len(SelectedPoints)
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
            print_msg("Point_List=" + str(SelectedPoints))
        m_points = []
        if Number_of_Points >= 1:
            Point_List = SelectedPoints
            for m_point in Point_List:
                if msg != 0:
                    print_point(FreeCAD.Vector(m_point.Point))
                m_x = m_point.Point.x
                m_y = m_point.Point.y
                m_z = m_point.Point.z
                m_points.append((m_x, m_y, m_z))

            if msg != 0:
                print_msg(str(m_points))

            m_pts = WFps.points_set(m_points)

            # fname, _ = QtGui.QFileDialog.getSaveFileName(None, 'Select a file',os.environ['HOME'])
            fname, _ = QtGui.QFileDialog.getSaveFileName(None, 'Select a file', os.path.expanduser('~'))

            if m_pts.save(str(fname)):
                print_msg(str(Number_of_Points) + result_msg + str(fname))
            else:
                printError_msg("Not able to save the requested Point(s)!")
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def numberRandomPoint(value):
    """ Respond to the change in number of cut value from the spin box.
    """
    global verbose
    msg = verbose

    try:
        # First we check if a valid number have been entered
        global m_numberRandomPoint
        if str(value) == '-':
            return
        m_numberRandomPoint = int(value)
        if msg != 0:
            print_msg("New number is:" + str(m_numberRandomPoint))
    except ValueError:
        printError_msg("Number must be valid !")


def distanceRandomPoints(value):
    """ Respond to the change in distance value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_distanceRandomPoints
        if str(value) == '-':
            return
        m_distanceRandomPoints = float(value)
        print_msg("New distance is:" + str(m_distanceRandomPoints))
        # plot_alongLinePoint()
    except ValueError:
        printError_msg("Distance must be valid number !")


def plot_points_random():
    """Create random Point(s).
    Define first the number of points to create and the coordinates limits.
    - Then push the button,
    or
    - Select first one point to the center desired location;
    - Then push the button.
    """
    msg = verbose
    import numpy as np

    error_msg = """Unable to create random Point(s):
    Define first the number of points to create and the coordinates limits.
    - Then push the button, 
    or
    - Select first one point to the center desired location;
    - Then push the button.
    """
    result_msg = ": random Point(s) created !"

    createFolders('WorkPoints')
    m_dir = 'Set'
    name = "RandomPoint"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    Number_of_Points = 0
    Number_of_Edges = 0

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if m_selEx:
        if msg != 0:
            print_msg(str(m_selEx))
        m_sel = Selection(m_selEx)
        Number_of_Points, Point_List = m_sel.get_points(getfrom=["Points"])
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
        Number_of_Edges, Edge_List = m_sel.get_segments(getfrom=["Segments", "Curves"])
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))

    m_limit = m_distanceRandomPoints/2
    np.random.random_sample()
    if (Number_of_Points >= 1):
        for m_Point in Point_List:
        #m_Point = Point_List[-1]
            try:
                for m_point_id in range(m_numberRandomPoint):
                    x, y, z = m_distanceRandomPoints * np.random.random_sample((3,)) - m_limit
                    x += m_Point.Point.x
                    y += m_Point.Point.y
                    z += m_Point.Point.z
                    Point_User_Name = plot_point(Base.Vector(x, y, z), part, name, str(m_dir))
                    print_point(Base.Vector(x, y, z), str(Point_User_Name) + result_msg + " at:")
            except Exception as inst:
                print(inst.args)
                printError_msg(error_msg)
    elif (Number_of_Edges >= 1):
        for m_line in Edge_List:
            try:
                if not hasattr(m_line, 'discretize'):
                    break
                m_points = m_line.discretize(m_numberRandomPoint)
                for m_point in m_points:
                    x, y, z = m_distanceRandomPoints * np.random.random_sample((3,)) - m_limit
                    x += m_point.x
                    y += m_point.y
                    z += m_point.z
                    Point_User_Name = plot_point(Base.Vector(x, y, z), part, name, str(m_dir))
                    print_point(Base.Vector(x, y, z), str(Point_User_Name) + result_msg + " at:")
            except Exception as inst:
                print(inst.args)
                printError_msg(error_msg)
    else:
        try:
            for m_point_id in range(m_numberRandomPoint):
                x, y, z = m_distanceRandomPoints * np.random.random_sample((3,)) - m_limit
                Point_User_Name = plot_point(Base.Vector(x, y, z), part, name, str(m_dir))
                print_point(Base.Vector(x, y, z), str(Point_User_Name) + result_msg + " at:")
        except Exception as inst:
            print(inst.args)
            printError_msg(error_msg)


def sel_projection(*argc):
    """ Projection plane by combo box.
    Options:
    All
    XY plane
    YZ plane
    XZ plane
    """
    global m_projection_plane
    global verbose
    msg = verbose
    if msg != 0:
        print_msg("Projection plane location by combo box !")
    m_projection_plane = "All"
    if str(*argc) == "XY plane":
        m_projection_plane = "XY"
    if str(*argc) == "YZ plane":
        m_projection_plane = "YZ"
    if str(*argc) == "XZ plane":
        m_projection_plane = "XZ"

    if msg != 0:
        print_msg("argc is " + str(*argc) + " and Projection plane " + str(m_attach_point) + " selected !")


def plot_projected_points():
    """Create projected point(s) on the chosen main planes.
    - Select one (or several) Point(s) and/or one (or several) Axis.
    Define the projection plane if needed.
    It can be either
    XY plane,
    YZ plane,
    XZ plane or
    All 3 planes
    """
    msg = verbose

    error_msg = """Unable to create projected Point(s):
    - Select one (or several) Point(s) and/or one (or several) Axis.
    Define the projection plane if needed.
    It can be either
    XY plane,
    YZ plane,
    XZ plane or
    All 3 planes
    - Then push the button.
    """
    result_msg = ": projected Point(s) created !"

    createFolders('WorkPoints')
    m_dir = 'Set'
    name = "ProjectedPoint"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))

    try:
        Number_of_Points, Point_List = m_sel.get_points(getfrom=["Points"])
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
        Number_of_Edges, Edge_List = m_sel.get_segments(getfrom=["Segments", "Curves", "Planes", "Objects"])
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))

        my_point_list = []
        if (Number_of_Edges >= 1):
            for Selected_Edge in Edge_List:
                Vector_A = Selected_Edge.valueAt(0.0)
                Vector_B = Selected_Edge.valueAt(Edge_List[0].Length)
                my_point_list.append(Vector_A)
                my_point_list.append(Vector_B)

        if (Number_of_Points >= 1):
            for Selected_Point in Point_List:
                my_point_list.append(Selected_Point.Point)

        for m_point in my_point_list:
            x = m_point.x
            y = m_point.y
            z = m_point.z
            if m_projection_plane == "All" or m_projection_plane == "XY":
                Vector_A = Base.Vector(x, y, 0.0)
                Vector_B = Base.Vector(x, y, z)
                Point_User_Name = plot_point(Vector_A, part, name, str(m_dir))
                print_point(Vector_A, str(Point_User_Name) + result_msg + " at:")
                Axis_User_Name, axis = plot_axis(Vector_A, Vector_B, part="Part::Feature", name="Axis_ProjectionToXY", grp=str(m_dir))
                try:
                    Gui.ActiveDocument.getObject(Axis_User_Name).DrawStyle = "Dotted"
                except Exception as inst:
                    print(inst.args)
                    print_msg("Not able to set DrawStyle !")
            if m_projection_plane == "All" or m_projection_plane == "YZ":
                Vector_A = Base.Vector(0.0, y, z)
                Vector_B = Base.Vector(x, y, z)
                Point_User_Name = plot_point(Vector_A, part, name, str(m_dir))
                print_point(Vector_A, str(Point_User_Name) + result_msg + " at:")
                Axis_User_Name, axis = plot_axis(Vector_A, Vector_B, part="Part::Feature", name="Axis_ProjectionToYZ", grp=str(m_dir))
                try:
                    Gui.ActiveDocument.getObject(Axis_User_Name).DrawStyle = "Dotted"
                except Exception as inst:
                    print(inst.args)
                    print_msg("Not able to set DrawStyle !")
            if m_projection_plane == "All" or m_projection_plane == "XZ":
                Vector_A = Base.Vector(x, 0.0, z)
                Vector_B = Base.Vector(x, y, z)
                Point_User_Name = plot_point(Vector_A, part, name, str(m_dir))
                print_point(Vector_A, str(Point_User_Name) + result_msg + " at:")
                Axis_User_Name, axis = plot_axis(Vector_A, Vector_B, part="Part::Feature", name="Axis_ProjectionToXZ", grp=str(m_dir))
                try:
                    Gui.ActiveDocument.getObject(Axis_User_Name).DrawStyle = "Dotted"
                except Exception as inst:
                    print(inst.args)
                    print_msg("Not able to set DrawStyle !")
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_centerObjectAxes():
    """ Create 3 Axes XY, and Z at center point of all selected objects.
    """
    msg = 0
    createFolders('WorkAxis')
    error_msg = "Unable to create Axes: \nSelect at least one object !"
    result_msg = ": Axes created !"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    # Return a list of SelectionObjects for a given document name.
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    m_objs = [selobj.Object for selobj in m_selEx]
    m_num = len(m_objs)
    if m_num < 1:
        printError_msg(error_msg)
        return
    Center = centerObjectsPoint(m_objs)
    if Center is not None:
        xmax, xmin, ymax, ymin, zmax, zmin = minMaxObjectsLimits(m_objs)
        # Work-AxisX
        if xmax != xmin:
            AX_Length = (xmax - xmin) * 1.3
        else:
            AX_Length = 10.
        PX_A = Base.Vector(AX_Length, 0, 0)
        PX_B = Base.Vector(-AX_Length, 0, 0)
        Axis_X = Part.makeLine(Center+ PX_A, Center+ PX_B)
        Axis = App.ActiveDocument.addObject("Part::Feature", "X_Axis")
        Axis.Shape = Axis_X
        App.ActiveDocument.getObject("WorkAxis").addObject(Axis)
        Axis_User_Name = Axis.Label
        Gui.ActiveDocument.getObject(Axis_User_Name).LineColor = (1.00, 0.00, 0.00)
        Gui.ActiveDocument.getObject(Axis_User_Name).PointColor = (1.00, 0.00, 0.00)
        Gui.ActiveDocument.getObject("X_Axis").Visibility = True
        print_msg(str(Axis_User_Name) + result_msg)
        # Work-AxisY
        if ymax != ymin:
            AY_Length = (ymax - ymin) * 1.3
        else:
            AY_Length = 10.
        PY_A = Base.Vector(0, AY_Length, 0)
        PY_B = Base.Vector(0, -AY_Length, 0)
        Axis_Y = Part.makeLine(Center + PY_A, Center + PY_B)
        Axis = App.ActiveDocument.addObject("Part::Feature", "Y_Axis")
        Axis.Shape = Axis_Y
        App.ActiveDocument.getObject("WorkAxis").addObject(Axis)
        Axis_User_Name = Axis.Label
        Gui.ActiveDocument.getObject(Axis_User_Name).LineColor = (0.00, 0.67, 0.00)
        Gui.ActiveDocument.getObject(Axis_User_Name).PointColor = (0.00, 0.67, 0.00)
        Gui.ActiveDocument.getObject("Y_Axis").Visibility = True
        print_msg(str(Axis_User_Name) + result_msg)
        # Work-AxisZ
        if zmax != zmin:
            AZ_Length = (zmax - zmin) * 1.3
        else:
            AZ_Length = 10.
        PZ_A = Base.Vector(0, 0, AZ_Length)
        PZ_B = Base.Vector(0, 0, -AZ_Length)
        Axis_Z = Part.makeLine(Center+ PZ_A, Center+ PZ_B)
        Axis = App.ActiveDocument.addObject("Part::Feature", "Z_Axis")
        Axis.Shape = Axis_Z
        App.ActiveDocument.getObject("WorkAxis").addObject(Axis)
        Axis_User_Name = Axis.Label
        Gui.ActiveDocument.getObject(Axis_User_Name).LineColor =  (0.33, 0.00, 1.00)
        Gui.ActiveDocument.getObject(Axis_User_Name).PointColor =  (0.33, 0.00, 1.00)
        Gui.ActiveDocument.getObject("Z_Axis").Visibility = True
        print_msg(str(Axis_User_Name) + result_msg)
    else:
        printError_msg(error_msg)


def extensionTwoPointsAxis(value):
    """ Respond to the change in extension value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_extensionTwoPointsAxis
        if str(value) == '-':
            return
        m_extensionTwoPointsAxis = float(value)
        print_msg("New extension is:" + str(m_extensionTwoPointsAxis))
    except ValueError:
        printError_msg("Extension must be valid number !")


def plot_2PointsAxis():
    """ Create an Axis with the 2 points selected as ends.
    """
    global verbose
    msg = verbose

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    createFolders('WorkAxis')
    error_msg = "Unable to create Axis: \nSelect two points only !"
    result_msg = ": Axis created !"
    name = "Line from 2 Points"
    part = "Part::Feature"

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        # print_msg(" Number_of_Points=" + str(Number_of_Points))
        if Number_of_Points == 2:
            Point_List = SelectedObjects[3]
            # print_msg(str(Point_List))
            Axis_A = Point_List[0].Point
            Axis_B = Point_List[1].Point
            Axis_dir = Axis_B - Axis_A
            Axis_E1 = Axis_B
            Axis_E2 = Axis_A

            if m_extensionTwoPointsAxis != 0.0:
                Axis_E1 = Axis_B +  Axis_dir.normalize().multiply(m_extensionTwoPointsAxis)
                if m_extensionTwoPointsAxis >= 0.0:
                    Axis_E2 = Axis_A -  Axis_dir.normalize().multiply(m_extensionTwoPointsAxis)
                else:
                    Axis_E2 = Axis_A +  Axis_dir.normalize().multiply(m_extensionTwoPointsAxis)
            if Axis_E1 == Axis_E2:
                Axis_E1 = Axis_E1 + Axis_dir.multiply(0.1)
                Axis_E2 = Axis_E2 - Axis_dir.multiply(0.9)
            Axis_User_Name, axis = plot_axis(Axis_E1, Axis_E2, part, name)

            print_msg(str(Axis_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def plot_NPointsAxis():
    """ Create a "best fit" line from a set of points using Singular Value Decomposition.
    - First select several Points

    The 3 eigenvectors are generated.
    Orange one is the best fit line.
    """
    msg = verbose

    try:
        import numpy as np
    except:
        error_msg = "Unable to import numpy !\n" +\
        "You MUSt install numpy to use this function !"
        printError_msg(error_msg)

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    createFolders('WorkAxis')
    error_msg = "Unable to create Axis: \nSelect at least two points!"
    result_msg = ": Axis created !"
    name = "Line_from_N_Points"
    part = "Part::Feature"
    grp = "WorkAxis"

    Selection = get_SelectedObjects(info=msg, printError=False)

    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
        if Number_of_Points > 1:
            m_x = []
            m_y = []
            m_z = []
            Point_List = SelectedObjects[3]
            if msg != 0:
                print_msg("Point_List=" + str(Point_List))
            for Selected_Point in Point_List:
                m_point = Selected_Point.Point
                m_x.append(m_point.x)
                m_y.append(m_point.y)
                m_z.append(m_point.z)

            m_np_x = np.asfarray(m_x)
            m_np_y = np.asfarray(m_y)
            m_np_z = np.asfarray(m_z)
            if msg != 0:
                print_msg(" m_np_x=" + str(m_np_x))
                print_msg(" m_np_y=" + str(m_np_y))
                print_msg(" m_np_z=" + str(m_np_z))
            m_data = np.concatenate((m_np_x[:, np.newaxis],
                        m_np_y[:, np.newaxis],
                        m_np_z[:, np.newaxis]),
                        axis=1)
            if msg != 0:
                print_msg(" m_data=" + str(m_data))
            # Calculate the mean of the points, i.e. the 'center' of the cloud
            m_datamean = m_data.mean(axis=0)
            if msg != 0:
                print_msg(" m_datamean=" + str(m_datamean))
            Axis_E0 = Base.Vector(m_datamean[0], m_datamean[1], m_datamean[2])

            # Do an SVD on the mean-centered data.
            m_uu, m_dd, m_vv = np.linalg.svd(m_data - m_datamean)
            if msg != 0:
                print_msg(" m_uu=" + str(m_uu))
                print_msg(" m_dd=" + str(m_dd))
                print_msg(" m_vv=" + str(m_vv))
            # Now vv[0] contains the first principal component, i.e. the direction
            # vector of the 'best fit' line in the least squares sense.
            Axis_dir = Base.Vector(m_vv[0][0], m_vv[0][1], m_vv[0][2])
            Axis_E1 = Axis_E0 - Axis_dir.normalize().multiply(m_dd[0]/2.)
            Axis_E2 = Axis_E0 + Axis_dir.normalize().multiply(m_dd[0]/2.)
            Axis_User_Name, axis = plot_axis(Axis_E1, Axis_E2, part, name, grp, orange)
            print_msg(str(Axis_User_Name) + result_msg)
            Axis_dir = Base.Vector(m_vv[1][0], m_vv[1][1], m_vv[1][2])
            #Axis_E2 = Axis_E0 + Axis_dir.normalize().multiply(m_dd[1]/2.)
            Axis_E2 = Axis_E0 + Axis_dir
            Axis_User_Name, axis = plot_axis(Axis_E0, Axis_E2, part, name, grp, red)
            print_msg(str(Axis_User_Name) + result_msg)
            Axis_dir = Base.Vector(m_vv[2][0], m_vv[2][1], m_vv[2][2])
            #Axis_E2 = Axis_E0 + Axis_dir.normalize().multiply(m_dd[2]/2.)
            Axis_E2 = Axis_E0 + Axis_dir
            Axis_User_Name, axis = plot_axis(Axis_E0, Axis_E2, part, name, grp, green)
            print_msg(str(Axis_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def plot_cylinderAxis():
    global verbose
    msg = verbose
    createFolders('WorkAxis')
    error_msg = "Unable to create Cylinder Axis: \nSelect one cylindrical face only !"
    result_msg = ": Cylinder Axis created !"
    name = "Cylinder Axis"
    part = "Part::Feature"
    global m_extensionFaceNormal

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Faces = SelectedObjects[2]
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg("Number_of_Faces=" + str(Number_of_Faces))
            print_msg("Number_of_Edges=" + str(Number_of_Edges))
        if Number_of_Faces >= 1:
            Face_list = SelectedObjects[5]
            for Face in Face_list:
            #Face = Face_list[0]
                Face_Wire = Face.OuterWire
                Face_Edges = Face_Wire.Edges
                try:
                    Circle_Center_1 = None
                    Circle_Center_2 = None
                    for i in range(len(Face_Edges)):
                        Current_Edge = Face_Edges[i]
                        Edge_Info = Current_Edge.Curve
                        Edge_Type_Name = str(Edge_Info)
                        # print_msg("Edge_Type_Name = " + str(Edge_Type_Name))
                        Edge_Circle = Edge_Type_Name[0:6]
                        Edge_Line = Edge_Type_Name[1:5]
                        if Edge_Circle == "Circle":
                            Circle_Axis = Current_Edge.Curve.Axis
                            Circle_Axis = Circle_Axis.normalize()
                            if Circle_Center_1 is None:
                                Circle_Center_1 = Current_Edge.Curve.Center
                                #Circle_Radius_1 = Current_Edge.Curve.Radius
                            else:
                                Circle_Center_2 = Current_Edge.Curve.Center
                                #Circle_Radius_2 = Current_Edge.Curve.Radius
                        if Edge_Line == "Line":
                            Line_Start = Current_Edge.Curve.StartPoint
                            Line_End = Current_Edge.Curve.EndPoint
                            Edge_Length = (Line_End - Line_Start).Length
                except:
                    printError_msg("Not valid cylinder !")
                # print_msg("Circle_Center_1 = " + str(Circle_Center_1))
                # print_msg("Circle_Center_2 = " + str(Circle_Center_2))
                Axis_A = Circle_Center_1
                Axis_B = Circle_Center_2
                Axis_dir = Axis_B - Axis_A
                if m_extensionFaceNormal != 0.0:
                    Axis_dir_norm = Axis_B - Axis_A
                    Axis_dir_norm = Axis_dir_norm.normalize()
                    Axis_dir_norm = Axis_dir_norm.multiply(abs(m_extensionFaceNormal))
                    if m_extensionFaceNormal > 0.0:
                        Axis_E1 = Axis_B + Axis_dir_norm
                        Axis_E2 = Axis_A - Axis_dir_norm
                    else:
                        Axis_E1 = Axis_B - Axis_dir_norm
                        Axis_E2 = Axis_A + Axis_dir_norm
                else:
                    Axis_E1 = Axis_B + Axis_dir.multiply(0.1)
                    Axis_E2 = Axis_A - Axis_dir.multiply(0.9)

                if Axis_E1 == Axis_E2:
                    Axis_E1 = Axis_E1 + Axis_dir.multiply(0.1)
                    Axis_E2 = Axis_E2 - Axis_dir.multiply(0.9)

                Axis_User_Name, axis = plot_axis(Axis_E1, Axis_E2, part, name)

                print_msg(str(Axis_User_Name) + result_msg)
        elif Number_of_Edges >= 1:
            m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
            m_objs = [selobj.Object for selobj in m_selEx]
            for m_obj in m_objs:
# ==============================================================================
#            look for sketch
#                 if hasattr(m_obj, 'TypeId'):
#                     m_type = m_obj.TypeId
#                 else:
#                     m_type = m_obj.Type
#                 if msg != 0:
#                     print_msg("m_obj.Type  : " + str(m_obj.Type))
# ==============================================================================

                if hasattr(m_obj.Shape.Curve, 'Radius'):
                    print_msg('Radius')
                    m_r = m_obj.Shape.Curve.Radius
                if hasattr(m_obj.Shape.Curve, 'MajorRadius'):
                    print_msg('MajorRadius')
                    m_r = m_obj.Shape.Curve.MajorRadius
                m_a = m_obj.Shape.Curve.Axis
                m_c = m_obj.Shape.Curve.Center
                if m_r:
                    m_mult = m_r * 0.5
                else:
                    m_mult = 5
                if m_extensionFaceNormal != 0.0:
                    m_mult = m_extensionFaceNormal
                Center_User_Name = plot_point(m_c, part, name)
                Axis_User_Name, axis = plot_axis(m_c, m_c + m_a.multiply(m_mult), part, name)
                Axis_User_Name, axis = plot_axis(m_c, m_c - m_a, part, name)

                print_msg(str(Axis_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def plot_planeAxis():
    """ Plot 2 Axis perpendicular to a Plane and passing trougth center.
    """
    msg = verbose
    global m_extensionFaceNormal

    def plot_normalAt(Selected_Plane, Point_A):
        if m_extensionFaceNormal != 0.0:
            Length = m_extensionFaceNormal
        else:
            Length = Selected_Plane.Length * 0.1
        if msg != 0:
            print_point(Point_A, msg="Point_A: ")
            print_msg("Length = " + str(Length))
        Normal = Selected_Plane.normalAt(0, 0)
        Normal = Normal.normalize().multiply(Length)
        Point_B = App.Vector(Point_A) + Normal
        Point_Bprime = App.Vector(Point_A) - Normal
        if msg != 0:
            print_point(Normal, msg="Normal: ")
            print_point(Point_B, msg="Point_B: ")
            print_point(Point_Bprime, msg="Point_Bprime: ")

        Axis_User_Name, axis = plot_axis(Point_B, Point_A, part, name)
        print_msg(str(Axis_User_Name) + result_msg)
        Axis_User_Name, axis = plot_axis(Point_Bprime, Point_A, part, name)
        print_msg(str(Axis_User_Name) + result_msg)


    createFolders('WorkAxis')
    error_msg = "Unable to create Plane Axis: \nSelect at least one plane face !"
    result_msg = ": Plane Axis created !"
    name = "Axis"
    part = "Part::Feature"

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Planes = SelectedObjects[2]
        Number_of_Points = SelectedObjects[0]
        if msg != 0:
            print_msg(" Number_of_Planes=" + str(Number_of_Planes))
            print_msg(" Number_of_Points=" + str(Number_of_Points))
        Point_List = SelectedObjects[3]
        Plane_List = SelectedObjects[5]
        if msg != 0:
            print_msg(" Point_List=" + str(Point_List))
            print_msg(" Plane_List=" + str(Plane_List))

        if (Number_of_Planes == 0):
                printError_msg(error_msg)
                return

        if (Number_of_Points == 0):
            for Selected_Plane in Plane_List:
                try:
                    # print_msg(str(Selected_Plane))
                    Point_A = Selected_Plane.CenterOfMass
                    plot_normalAt(Selected_Plane, Point_A)
                except:
                    printError_msg("Non Planar Surface !")
        else:
            if Number_of_Points >= Number_of_Planes:

                if Number_of_Points == Number_of_Planes:
                    if msg != 0:
                        print_msg(" Number_of_Points = Number_of_Planes")
                    for Selected_Plane, Selected_Point in zip(Plane_List, Point_List):
                        if msg != 0:
                            print_msg(" Selected_Plane=" + str(Selected_Plane))
                            print_msg(" Selected_Point=" + str(Selected_Point))
                        plot_normalAt(Selected_Plane, Selected_Point.Point)
                else:
                    if msg != 0:
                        print_msg(" Number_of_Points > Number_of_Planes")
                    for Selected_Plane, Selected_Point in itertools.izip_longest(Plane_List, Point_List, fillvalue=Plane_List[-1]):
                        if msg != 0:
                             print_msg(" Selected_Plane=" + str(Selected_Plane))
                             print_msg(" Selected_Point=" + str(Selected_Point))
                        plot_normalAt(Selected_Plane, Selected_Point.Point)
            else:
                printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def extensionFaceNormal(value):
    """ Respond to the change in extension value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_extensionFaceNormal
        if str(value) == '-':
            return
        m_extensionFaceNormal = float(value)
        print_msg("New extension is:" + str(m_extensionFaceNormal))
    except ValueError:
        printError_msg("Extension must be valid number !")


def plot_faceNormal():
    """Create a normal Axis at click location of a Face or at a selected point location.
    """
    msg = verbose
    global m_callback

    createFolders('WorkAxis')
    error_msg = "Unable to create Normal Axis: \n" + \
                "To create a Normal at click location on a Face:\n"  + \
                "- Click first in the view to select and object,\n" + \
                "- then push the button,\n" + \
                "- then click on a location on the selected Face.\n" + \
                "or\n" + \
                "To create several Normal of the face:\n" + \
                "- Click first in the view to select and object,\n" + \
                "- then select one or several points of the face\n" + \
                "- then push the button.\n" + \
                "(These selections can also be done into the Combined View)"
    result_msg = "Normal Axis created !"

    def plot_normal(m_sel, m_point):
        import Mesh
        global m_extensionFaceNormal
        part = "Part::Feature"
        if hasattr(m_sel, 'Shape'):
            if len(m_sel.Shape.Faces) > 0:
                m_face = m_sel.Shape.Faces[0]
                m_surf = m_face.Surface
                m_p = m_point
                m_uv = m_surf.parameter(m_p)
                u, v = m_uv[0], m_uv[1]
                m_p1 = m_face.valueAt(u, v)
                m_p2 = m_face.normalAt(u, v)
                if m_extensionFaceNormal == 0.0:
                    m_extensionFaceNormal = 10.0
                m_p3 = m_p1 + m_p2.normalize().multiply(m_extensionFaceNormal)
                createFolders('WorkAxis')
                name = "Normal"
                plot_axis(m_p1, m_p3, part, name)
                createFolders('WorkPoints')
                name = "Point"
                plot_point(m_p1, part,  name)
                return True
            else:
                printError_msg("No Face selected !")
                return False
        else:
            if isinstance(m_sel, Mesh.Feature):
                print_msg("Mesh selected !")
                # find the facet selected
                r = Gui.ActiveDocument.ActiveView.getCameraOrientation()
                start = r.Axis
                m_mesh = m_sel.Mesh
                m_FacetsSel = m_mesh.nearestFacetOnRay((m_point.x, m_point.y, m_point.z), (start.x, start.y, start.z))
                if len(m_FacetsSel) == 0:
                    return
                m_p1 = m_point
                for idx in m_FacetsSel.keys():
                    m_p2 = App.Vector(m_mesh.Facets[idx].Normal)

                if m_extensionFaceNormal == 0.0:
                    m_extensionFaceNormal = 10.0
                m_p3 = m_p1 + m_p2.normalize().multiply(m_extensionFaceNormal)
                createFolders('WorkAxis')
                name = "Normal"
                plot_axis(m_p1, m_p3, part, name)
                createFolders('WorkPoints')
                name = "Point"
                plot_point(m_p1, part,  name)
                return True
            else:
                printError_msg("No Shape available for: " + str(m_sel) + "\nat " + str(m_point))
                return False

    if len(Gui.Selection.getSelectionEx()) >= 2:
        SelectedObjects = get_SelectedObjects(info=msg, printError=False)

        Number_of_Points = SelectedObjects[0]
        Number_of_Planes = SelectedObjects[2]
        if msg != 0:
            print_msg(" Number_of_Planes=" + str(Number_of_Planes))
            print_msg(" Number_of_Points=" + str(Number_of_Points))
        Point_List = SelectedObjects[3]
        Plane_List = SelectedObjects[5]
        if msg != 0:
            print_msg(" Point_List=" + str(Point_List))
            print_msg(" Plane_List=" + str(Plane_List))

        if Number_of_Planes == 1 and Number_of_Points >= 1:
            m_sel = Plane_List[0]
            m_sel = Gui.Selection.getSelection()[0]
            for Selected_Point in Point_List:
                m_point = Selected_Point.Point
                if not plot_normal(m_sel, m_point):
                    break
                else:
                    print_msg(result_msg)
        else:
            printError_msg(error_msg)
    else:
        view = Gui.ActiveDocument.ActiveView
        m_callback = view.addEventCallback("SoMouseButtonEvent", getClickedNormal)


def plot_faceNormal_old():
    """Create a normal Axis at click location of a Face.
    """
    global m_callback
    view = Gui.ActiveDocument.ActiveView
    m_callback = view.addEventCallback("SoMouseButtonEvent", getClickedNormal)


def plot_2LinesAxis():
    msg = 0
    createFolders('WorkAxis')
    error_msg = "Unable to create Axis between 2 Lines: \nSelect two lines only !"
    result_msg = ": Axis between 2 Lines created !"
    name = "MidLine"
    part = "Part::Feature"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Edges = SelectedObjects[1]
        # print_msg("Number_of_Edges=" + str(Number_of_Edges))
        if (Number_of_Edges == 2):
            Edge_List = SelectedObjects[4]
            # print_msg(str(Edge_List))
            Vector_A = Edge_List[0].valueAt(0.0)
            Vector_B = Edge_List[0].valueAt(Edge_List[0].Length)
            # print_point(Vector_A, msg="Point A: ")
            # print_point(Vector_B, msg="Point B: ")

            Vector_C = Edge_List[1].valueAt(0.0)
            Vector_D = Edge_List[1].valueAt(Edge_List[1].Length)
            # print_point(Vector_C, msg="Point C: ")
            # print_point(Vector_D, msg="Point D: ")

            Vector_edge_1 = Vector_A + Vector_C
            Vector_edge_2 = Vector_B + Vector_D

            Axis_E1 = Vector_edge_1.multiply(0.5)
            Axis_E2 = Vector_edge_2.multiply(0.5)

            Axis_User_Name, axis = plot_axis(Axis_E1, Axis_E2, part, name)

            print_msg(str(Axis_User_Name) + result_msg)
    except:
        printError_msg(error_msg)


def numberLineCut(value):
    """ Respond to the change in number of cut value from the spin box.
    """
    global verbose
    msg = verbose

    try:
        # First we check if a valid number have been entered
        global m_numberLineCut
        if str(value) == '-':
            return
        m_numberLineCut = int(value)
        if msg != 0:
            print_msg("New number is:" + str(m_numberLineCut))
    except ValueError:
        printError_msg("Number must be valid !")


def plot_cutAxis():
    """Create Axes:
    Cut the selected Line in 2(n) parts and create 2(n) Axes.
    The number indicates in how many parts to cut.
    """
    global verbose
    msg = verbose
    global biColor
    red = 0

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    createFolders('WorkAxis')
    error_msg = "Unable to cut the Line/Axis: \nSelect at least one Line !"
    result_msg = ": is last axis created from Axis cut !"
    name = "Axes_from_axis"
    part = "Part::Feature"

    global m_numberLineCut
    if not (m_numberLineCut >= 2 and m_numberLineCut <= 100):
        m_numberLineCut = 2
    if msg != 0:
        print_msg("Number_of_cuts=" + str(m_numberLineCut))
    Selection = get_SelectedObjects(info=msg, printError=False)
    m_num, m_selEx, m_objs, m_objNames = get_InfoObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))
        if (Number_of_Edges >= 1):
            Edge_List = SelectedObjects[4]
            for i in range(Number_of_Edges):
                edge = Edge_List[i]
                if msg != 0:
                    print_msg(str(edge))
                #Vector_A = edge.valueAt( 0.0 )
                Vector_A = edge.Vertexes[0].Point
                for j in range(1, m_numberLineCut):
                    Vector_B = centerLinePoints(edge, j, m_numberLineCut, info=msg)
                    if msg != 0:
                        print_point(Vector_A, "Vector_A is: ")
                        print_point(Vector_B, "Vector_B is: ")
                    Axis_User_Name, axis = plot_axis(Vector_A, Vector_B, part, name)
                    if biColor != 0:
                        if red == 0:
                            Gui.ActiveDocument.getObject(Axis_User_Name).LineColor = (1.0, 0.0, 0.0)
                            red = 1
                        else:
                            Gui.ActiveDocument.getObject(Axis_User_Name).LineColor = (1.0, 1.0, 1.0)
                            red = 0

                    Vector_A = Vector_B
                #Vector_B = edge.valueAt( edge.Length )
                Vector_B = edge.Vertexes[-1].Point
                if msg != 0:
                    print_point(Vector_A, "Vector_A is: ")
                    print_point(Vector_B, "Vector_B is: ")
                Axis_User_Name, axis = plot_axis(Vector_A, Vector_B, part, name)
                if biColor != 0:
                    if red == 0:
                        Gui.ActiveDocument.getObject(Axis_User_Name).LineColor = (1.0, 0.0, 0.0)
                        red = 1
                    else:
                        Gui.ActiveDocument.getObject(Axis_User_Name).LineColor = (1.0, 1.0, 1.0)
                        red = 0

                print_msg(str(Axis_User_Name) + result_msg)

                Gui.ActiveDocument.getObject(str(m_objNames[i])).Visibility = False

    except:
        printError_msg(error_msg)


def numberAxisCutWire(value):
    """ Respond to the change in number of cut value from the spin box.
    """
    global verbose
    msg = verbose

    try:
        # First we check if a valid number have been entered
        global m_numberAxisCutWire
        if str(value) == '-':
            return
        m_numberAxisCutWire = int(value)
        if msg != 0:
            print_msg("New number is:" + str(m_numberAxisCutWire))
    except ValueError:
        printError_msg("Number must be valid !")


def plot_cutWireAxis():
    createFolders('WorkAxis')
    global m_numberAxisCutWire
    if not (m_numberAxisCutWire >= 2 and m_numberAxisCutWire <= 100):
        m_numberAxisCutWire = 2
    cutWire(m_numberAxisCutWire, createPoint=0, createLine=1)


def extensionLinePointAxis(value):
    """ Respond to the change in extension value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_extensionLinePointAxis
        if str(value) == '-':
            return
        m_extensionLinePointAxis = float(value)
        print_msg("New extension is:" + str(m_extensionLinePointAxis))
    except ValueError:
        printError_msg("Extension must be valid number !")


def plot_linePointAxis():
    """ 
    Plot an Axis Perpendicular to an Axis and crossing a Point
    -Select one Axis and one Point NOT on the previous Axis.
    """
    msg = 0
    createFolders('WorkAxis')
    error_msg = "Unable to create Perpendicular Axis: \n " + \
                "Select one Point and one Line only !\n" + \
                "The Point is NOT on the Line!"
    result_msg = ": Perpendicular Axis created !"
    name = "Perpendicular_Line"
    part = "Part::Feature"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges) +
                      " Number_of_Points=" + str(Number_of_Points))
        if (Number_of_Edges == 1) and (Number_of_Points) >= 1:
            Point_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg(str(Point_List))
                print_msg(str(Edge_List))
            for Selected_Point in Point_List:
                Vector_C     = Selected_Point.Point
                Vector_A     = Edge_List[0].valueAt(0.0)
                Vector_B     = Edge_List[0].valueAt(Edge_List[0].Length)

                Vector_T, Distance, Vector_Tprime = intersecPerpendicularLine(Vector_A, Vector_B, Vector_C, info=msg)

                print_msg("Distance from the Point to the Axis is: " + str(Distance))

                Axis_dir = Vector_C - Vector_T
                Axis_E1 = Vector_C
                Axis_E2 = Vector_T

                if m_extensionLinePointAxis != 0.0:
                    Axis_E1 = Vector_C +  Axis_dir.normalize().multiply(m_extensionLinePointAxis)
                    if m_extensionLinePointAxis >= 0.0:
                        Axis_E2 = Vector_T -  Axis_dir.normalize().multiply(m_extensionLinePointAxis)
                    else:
                        Axis_E2 = Vector_T +  Axis_dir.normalize().multiply(m_extensionLinePointAxis)

                if Axis_E1 == Axis_E2:
                    Axis_E1 = Axis_E1 + Axis_dir.multiply(0.1)
                    Axis_E2 = Axis_E2 - Axis_dir.multiply(0.9)
                Axis_User_Name, axis = plot_axis(Axis_E1, Axis_E2, part, name)

                print_msg(str(Axis_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def plot_planeLinePointAxis():
    """
    Plot an Axis Perpendicular to an Axis, crossing a Point and Parallel to a Plane.
    -Select one Plane, one Axis and one Point ON the previous Axis.
    """
    msg = verbose
    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None
    createFolders('WorkAxis')
    error_msg = "Unable to create Perpendicular Axis: \nSelect one Plane, one Axis and one Point ON the previous Axis !"
    result_msg = ": Perpendicular Axis created !"
    name = "Perpendicular_Line_on_plane"
    part = "Part::Feature"
    Selection = get_SelectedObjects(info=msg, printError=False)
    m_num, m_selEx, m_objs, m_objNames = get_InfoObjects(info=0)
    m_xmax, m_xmin, m_ymax, m_ymin, m_zmax, m_zmin = minMaxObjectsLimits(m_objs, info=0)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        Number_of_Planes = SelectedObjects[2]
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points) + \
                      "\nNumber_of_Edges=" + str(Number_of_Edges) + \
                      "\nNumber_of_Planes=" + str(Number_of_Planes))
        if (Number_of_Points == 1) and (Number_of_Edges == 1) and (Number_of_Planes) == 1:
            Point_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]
            Plane_List = SelectedObjects[5]
            # Create a Perpendicular plane to selected line and crossing the point
            Vector_A = Edge_List[0].Vertexes[0].Point
            Vector_B = Edge_List[0].Vertexes[-1].Point
            Vector_C = Point_List[0].Point
            if msg != 0:
                print_point(Vector_A, msg="Vector_A: ")
                print_point(Vector_B, msg="Vector_B: ")
                print_point(Vector_C, msg="Vector_C: ")
            # Intersection point T on a Line given one Line and One Point C.
            if colinearVectors(Vector_A, Vector_B, Vector_C, info=msg, tolerance=1e-10):
                Vector_T = Vector_C
                Distance = Vector_B.sub(Vector_A).Length
            else:
                Vector_T, Distance, Vector_Tprime = intersecPerpendicularLine(Vector_A, Vector_B, Vector_C, info=msg)
            if msg != 0:
                print_point(Vector_T, msg="Intersection point T: ")
            Plane_Normal = Vector_B.sub(Vector_A)
            Plane_Point = Vector_T +  (Vector_C - Vector_T).multiply(0.5)
            #Edge_Length = Distance * 1.5

            #Plane_User_Name, plane = plot_plane(Edge_Length, Edge_Length, Plane_Point, Plane_Normal, part, name)
            # print_msg(str(Plane_User_Name) + result_msg )

            # Then intersection of the 2 planes
            Selected_Plane1 = Plane_List[0]
            Selected_Plane2 = plane.Shape
            Plane_Normal1 = Selected_Plane1.normalAt(0, 0)
            Plane_Normal2 = Plane_Normal
            if msg != 0:
                print_point(Plane_Normal1, msg="Normal1: ")
                print_point(Plane_Normal2, msg="Normal2: ")
            Plane_Point1 = Selected_Plane1.CenterOfMass
            Plane_Point2 = Plane_Point
            if msg != 0:
                print_point(Plane_Point1, msg="Plane_Point1: ")
                print_point(Plane_Point2, msg="Plane_Point2: ")

            Axis_dir = intersecPlanePlane(Plane_Normal1, Plane_Point1, Plane_Normal2, Plane_Point2, info=msg)
            if msg != 0:
                print_point(Axis_dir, msg="Axis_dir: ")

            # Intersection Line found
            if Axis_dir is not None:
                if msg != 0:
                    print_msg("Selected_Plane1=" + str(Selected_Plane1))
                    print_msg("Selected_Plane1.Edges=" + str(Selected_Plane1.Edges))
                Number_of_Edges = len(Selected_Plane1.Edges)
                if msg != 0:
                    print_msg("Number_of_Edges=" + str(Number_of_Edges))
                Vertx = []
                Vertx.append(App.Vector(0.0, 0.0, 0.0))
                Vertx.append(App.Vector(0.0, 0.0, 0.0))

                min_val, max_val = init_min_max()
                dist_to_center_min = max_val
                # For the first plane look after all edges and look at
                # intersections of the edges with the second plane
                for j in range(Number_of_Edges):
                    A = Selected_Plane1.Edges[j].Vertexes[0].Point
                    B = Selected_Plane1.Edges[j].Vertexes[-1].Point
                    if msg != 0:
                        print_point(A, msg="A: ")
                        print_point(B, msg="B: ")
                    T = intersecLinePlane(A, B, Plane_Normal2, Plane_Point2, info=0)
                    if T is not None:
                        if msg != 0:
                            print_point(T, msg="T: ")
                        D = T - Plane_Point1
                        dist_to_center = math.sqrt(D.dot(D))
                        if msg != 0:
                            print_msg("D=" + str(D))
                            print_msg("dist_to_center=" + str(dist_to_center))
                        if dist_to_center < dist_to_center_min:
                            dist_to_center_min = dist_to_center
                            Vertx[0] = T

                if msg != 0:
                    print_msg("Selected_Plane2=" + str(Selected_Plane2))
                    print_msg("Selected_Plane2.Edges=" + str(Selected_Plane2.Edges))

                Number_of_Edges = len(Selected_Plane2.Edges)
                if msg != 0:
                    print_msg("Number_of_Edges=" + str(Number_of_Edges))

                dist_to_center_min = max_val
                for j in range(Number_of_Edges):
                    A = Selected_Plane2.Edges[j].valueAt(0.0)
                    B = Selected_Plane2.Edges[j].valueAt(Selected_Plane2.Edges[j].Length)
                    if msg != 0:
                        print_point(A, msg="A: ")
                        print_point(B, msg="B: ")
                    T = intersecLinePlane(A, B, Plane_Normal1, Plane_Point1, info=0)
                    if T is not None:
                        if msg != 0:
                            print_point(T, msg="T: ")
                        D = T - Plane_Point2
                        dist_to_center = math.sqrt(D.dot(D))
                        if msg != 0:
                            print_msg("D=" + str(D))
                            print_msg("dist_to_center=" + str(dist_to_center))
                        if dist_to_center < dist_to_center_min:
                            dist_to_center_min = dist_to_center
                            Vertx[1] = T

                C = meanVectorsPoint(Vertx, info=1)

                if C is not None:
                    extension = m_xmax - m_xmin
                    if extension < m_ymax - m_ymin:
                        extension = m_ymax - m_ymin
                    if extension < m_zmax - m_zmin:
                        extension = m_zmax - m_zmin
                    extension = extension/2
                    A = C -  Axis_dir.normalize().multiply(extension*1.3)
                    B = C +  Axis_dir
                    Axis_User_Name, axis = plot_axis(A, B, part, name)
                    print_msg(str(Axis_User_Name) + result_msg)
                else:
                    printError_msg(error_msg)
            else:
                printError_msg(error_msg)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def extensionLine(value):
    """ Respond to the change in extension value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_extensionLine
        if str(value) == '-':
            return
        m_extensionLine = float(value)
        print_msg("New extension is:" + str(m_extensionLine))
    except ValueError:
        printError_msg("Extension must be valid number !")


def plot_pointLineAxis():
    """ 
    Create an Axis Parallel to an Axis (as Direction) and crossing a Point.
    - Select one Axis and one (or several) Point(s) NOT on the previous Axis.
    Define the length and the attach point if needed.
    A Length of Zero means the length of already selected Axis will be used.
    """
    msg = verbose
    createFolders('WorkAxis')
    error_msg = "Unable to create Parallel Axis: \nSelect one Point and one Line only !"
    result_msg = ": Parallel Axis created !"
    name = "Parallel Line"
    part = "Part::Feature"
    global m_attach_point
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges) + " Number_of_Points=" + str(Number_of_Points))
        if (Number_of_Edges == 1) and (Number_of_Points) >= 1:
            Point_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg(str(Point_List))
                print_msg(str(Edge_List))
            Vector_A     = Edge_List[0].valueAt(0.0)
            Vector_B     = Edge_List[0].valueAt(Edge_List[0].Length)
            Vector_C     = centerLinePoint(Edge_List[0], info=1)

            if m_extensionLine != 0.0:
                AB_Vector = Vector_B.sub(Vector_A)
                new_Vector = AB_Vector.normalize().multiply(m_extensionLine/2.)
                Vector_A = Vector_C.sub(new_Vector)
                Vector_B = Vector_C.add(new_Vector)

            for Selected_Point in Point_List:
                #Vector_Cprime = Point_List[0].Point
                Vector_Cprime = Selected_Point.Point
                Vector_Translate = (Vector_Cprime - Vector_C)

                Vector_Aprime = Vector_A + Vector_Translate
                Vector_Bprime = Vector_B + Vector_Translate

                if str(m_attach_point) == "Start":
                    Vector_Translate2 = (Vector_A - Vector_B)
                    Vector_Translate2 = Vector_Translate2.multiply(0.5)
                    Vector_Aprime = Vector_Aprime + Vector_Translate2
                    Vector_Bprime = Vector_Bprime + Vector_Translate2
                if str(m_attach_point) == "End":
                    Vector_Translate2 = (Vector_B - Vector_A)
                    Vector_Translate2 = Vector_Translate2.multiply(0.5)
                    Vector_Aprime = Vector_Aprime + Vector_Translate2
                    Vector_Bprime = Vector_Bprime + Vector_Translate2

                Axis_User_Name, axis = plot_axis(Vector_Aprime, Vector_Bprime, part, name)

                print_msg(str(Axis_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_linePlaneAxis():
    """ Axes=(Pl(s),Axes):
        Create projection(s) of Axes onto Plane(s).
        - First select one (or several) Line(s)
        - Second select one or several) Plane(s)
    """
    msg = verbose
    createFolders('WorkAxis')
    error_msg = "Unable to create projection Axis onto a Plane: \n" +\
                "Select at least one Line and one Plane !"
    result_msg = ": Projection Axis onto a Plane created !"
    name = "Line"
    part = "Part::Feature"

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Edges = SelectedObjects[1]
        Number_of_Planes = SelectedObjects[2]
        if msg != 0:
            print_msg(" Number_of_Edges=" + str(Number_of_Edges))
            print_msg(" Number_of_Planes=" + str(Number_of_Planes))
        if Number_of_Edges >= 1 and Number_of_Planes >= 1:
            Edge_List = SelectedObjects[4]
            Plane_List = SelectedObjects[5]

            for Selected_Plane in Plane_List:
                for Selected_Edge in Edge_List:
                    Point_A = Selected_Edge.Vertexes[0].Point
                    Point_B = Selected_Edge.Vertexes[1].Point
                    if msg != 0:
                        print_point(Point_A, msg="Point_A: ")
                        print_point(Point_B, msg="Point_B: ")

                    #Plane_Point = Selected_Plane.CenterOfMass
                    Plane_Placement = Selected_Plane.Placement
                    Plane_Normal = Selected_Plane.normalAt(0, 0)
                    # Projection of A and B onto the Plane Aprime and Bprime
                    #Vector_A = Point_A + Plane_Normal
                    #Vector_B = Point_B + Plane_Normal

                    #Point_Aprime = intersecLinePlane(Point_A, Vector_A, Plane_Normal, Plane_Point, info=0)
                    #Point_Bprime = intersecLinePlane(Point_B, Vector_B, Plane_Normal, Plane_Point, info=0)
                    Point_Aprime = Point_A.projectToPlane(Plane_Placement.Base, Plane_Normal)
                    Point_Bprime = Point_B.projectToPlane(Plane_Placement.Base, Plane_Normal)

                    if msg != 0:
                        # Plot them
                        plot_point(Point_Aprime, part, "PointFacePoint")
                        plot_point(Point_Bprime, part, "PointFacePoint")
                    Axis_User_Name, axis = plot_axis(Point_Aprime, Point_Bprime, part, name)

                    print_msg(str(Axis_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def extensionAxis(value):
    """ Respond to the change in Axis extension value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_extensionAxis
        m_extensionAxis = float(value)
        print_msg("New Axis extension is:" + str(m_extensionAxis))
    except ValueError:
        printError_msg("Axis extension must be valid number percentage)!")


def plot_extensionAxis():
    """ Extend an Axis at two extrema
    """
    global verbose
    msg = verbose
    createFolders('WorkAxis')
    error_msg = "Unable to create Axis: \nSelect Axis(es) only !"
    result_msg = ": Axis created !"
    name = "Axis_extended"
    part = "Part::Feature"
    global m_extensionAxis
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))
        if Number_of_Edges >= 1:
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg("Edge_List=" + str(Edge_List))
            for Selected_Edge in Edge_List:
                if msg != 0:
                    print_msg("Selected_Edge=" + str(Selected_Edge))
                Point_A = Selected_Edge.Vertexes[0].Point
                Point_B = Selected_Edge.Vertexes[-1].Point
                if msg != 0:
                    print_point(Point_A, msg="Selected_Edge.Vertexes[0]  Point_A: ")
                    print_point(Point_B, msg="Selected_Edge.Vertexes[-1] Point_B: ")
                AB_Vector = Point_B.sub(Point_A)
                demi_add_length = Selected_Edge.Length * ((m_extensionAxis/200))
                print_msg("demi_add_length=" + str(demi_add_length))
                add_Vector = AB_Vector.normalize().multiply(demi_add_length)
                Point_A = Point_A.sub(add_Vector)
                Point_B = Point_B.add(add_Vector)

                if Point_A == Point_B:
                    Point_A = Point_A.sub(add_Vector.multiply(0.1))
                    Point_B = Point_B.add(add_Vector.multiply(0.9))
                Axis_User_Name, axis = plot_axis(Point_A, Point_B, part, name)

                print_msg(str(Axis_User_Name) + result_msg)
        else:
            printError_msg(error_msg)

    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_clickForAxis():
    """ Plot an axis at location of 2 mouse clicks. 
    """
    global verbose
    msg = verbose
    createFolders('WorkAxis')
    global m_stack
    global m_callback
    global m_clickForAxis

    if msg != 0:
        print_msg("plot_clickForAxis: flag is " + str(m_clickForAxis))

    # Mimic behavior of toggle button
    view = get_ActiveView()
    if m_clickForAxis:
        #m_callback = view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(),getClickedAxis)
        m_callback = view.addEventCallback("SoMouseButtonEvent", getClickedAxis2)
    else:
        del m_stack[:]
        view.removeEventCallback("SoMouseButtonEvent", m_callback)
    m_clickForAxis = not m_clickForAxis


def plot_objectNAxes():
    """Create a set of axes from selected Objects:
    - Select object(s)
    to create axes from these object(s) !
    if you select a Plane: 4 axes will be created;
    if you select an Object: many axes will be created.
    """
    msg = verbose

    error_msg = "Create a set of axes from selected Objects: \n" +\
                "Select object(s) \n" +\
                "to create axes from these object(s) !\n" +\
                "if you select a Plane: 4 axes will be created;\n" +\
                "if you select an Object: many axes will be created.\n"

    createFolders('WorkAxis')
    m_dir = 'Object'
    name = "Axis"
    part = "Part::Feature"
    try:
        m_r = App.ActiveDocument.getObject("WorkAxis").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
    m_dir = m_r.Name
    result_msg = " Axes created into: WorkAxis/" + str(m_dir)

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    SelectedObjects = get_SelectedObjects(info=msg, printError=False)

    try:
        Selected_Axes = []

        Number_of_Faces = SelectedObjects[2]
        Number_of_Objects = len(SelectedObjects[6])
        if msg != 0:
            print_msg("Number_of_Faces = " + str(Number_of_Faces))
            print_msg("Number_of_Objects = " + str(Number_of_Objects))

        if Number_of_Faces > 0:
            Face_List = SelectedObjects[5]
            for m_face in Face_List:
                Edge_List = m_face.Edges
                for m_edge in Edge_List:
                    Selected_Axes.append(m_edge)

        if Number_of_Objects > 0:
            Object_List = SelectedObjects[6]
            for m_object in Object_List:
                for m_edge in m_object.Shape.Edges:
                    Selected_Axes.append(m_edge)

        m_axes = Selected_Axes
        Number_of_Axes = len(m_axes)
        if msg != 0:
            print_msg("Number_of_Axes = " + str(Number_of_Axes))
        if Number_of_Axes >= 1:
            for m_axis in m_axes:
                if msg != 0:
                    print_msg("m_axis.Vertexes[0] = " + str(m_axis.Vertexes[0]))
                    print_msg("m_axis.Vertexes[-1] = " + str(m_axis.Vertexes[-1]))
                Vector_A = m_axis.Vertexes[0].Point
                Vector_B = m_axis.Vertexes[-1].Point

                plot_axis(Vector_A, Vector_B, part, name, str(m_dir))

            print_msg(str(m_dir) + ": " + str(Number_of_Axes) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_object3Axes():
    """Create a set of 2 or 3 axes from selected Objects:
    The most representative axes will be selected from all axis.
    The length of main axes will be the cumulative length of all axes with the same direction.
    - Select object(s)
    to create axes from these object(s) !
    if you select a Plane: 2 axes will be created;
    if you select an Object: 3 axes will be created.
    """
    msg = verbose

    error_msg = "Create a set of 2 or 3 axes from selected Objects: \n" +\
                "The most representative axes will be selected from all axis.\n" +\
                "The length of main axes will be the cumulative length of all axes with the same direction.\n" +\
                "Select object(s) \n" +\
                "to create axes from these object(s) !\n" +\
                "if you select a Plane: 2 axes will be created;\n" +\
                "if you select an Object: 3 axes will be created.\n"

    createFolders('WorkAxis')
    m_dir = 'Object'
    name = "Axis"
    part = "Part::Feature"
    try:
        m_r = App.ActiveDocument.getObject("WorkAxis").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as inst:
        print(inst.args)
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
    m_dir = m_r.Name
    result_msg = " Axes created into: WorkAxis/" + str(m_dir)

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    SelectedObjects = get_SelectedObjects(info=msg, printError=False)

    try:
        Selected_Axes = []

        Number_of_Faces = SelectedObjects[2]
        Number_of_Objects = len(SelectedObjects[6])
        if msg != 0:
            print_msg("Number_of_Faces = " + str(Number_of_Faces))
            print_msg("Number_of_Objects = " + str(Number_of_Objects))

        if Number_of_Faces > 0:
            Face_List = SelectedObjects[5]
            for m_face in Face_List:
                Edge_List = m_face.Edges
                for m_edge in Edge_List:
                    Selected_Axes.append(m_edge)

        if Number_of_Objects > 0:
            Object_List = SelectedObjects[6]
            for m_object in Object_List:
                for m_edge in m_object.Shape.Edges:
                    Selected_Axes.append(m_edge)

        # =======================================================================
        # m_axes = Selected_Axes
        # Number_of_Axes = len(m_axes)
        # if msg != 0:
        #     print_msg("Number_of_Axes = " + str(Number_of_Axes))
        # if Number_of_Axes >= 1:
        #     Selected_AxesWithLength = []
        #     Selected_Points = []
        #     # Generate list of (Axes, lengthOfAxes)
        #     for m_axis in m_axes:
        #         if msg != 0:
        #             print_msg("m_axis.Vertexes[0] = " + str(m_axis.Vertexes[0]))
        #             print_msg("m_axis.Vertexes[-1] = " + str(m_axis.Vertexes[-1]))
        #         m_start = m_axis.Vertexes[0].Point
        #         m_end = m_axis.Vertexes[-1].Point
        #         m_diff = m_end.sub(m_start)
        #         if abs(m_diff.x) <= tolerance and abs(m_diff.y) <= tolerance and abs(m_diff.z) <= tolerance:
        #             continue
        #         Selected_Points.append(m_start)
        #         Selected_Points.append(m_end)
        #         m_length = distanceBetween(m_start, m_end)
        #         #m_A = (m_axis.Curve.EndPoint - m_axis.Curve.StartPoint).normalize()
        #         m_A = (m_axis.Vertexes[-1].Point).sub(m_axis.Vertexes[0].Point).normalize()
        #         m_B = Base.Vector(0, 0, 0)
        #         m_dim = len(Selected_AxesWithLength)
        #         if msg != 0:
        #             print_msg("m_length = " + str(m_length))
        #             print_msg("len(Selected_AxesWithLength) = " + str(m_dim))
        #
        #         if m_dim == 0:
        #             Selected_AxesWithLength.append([m_axis, m_length])
        #             if msg != 0:
        #                 print_msg("Selected_AxesWithLength = " + str(Selected_AxesWithLength))
        #         else:
        #             m_found = False
        #             if msg != 0:
        #                 print_msg("Selected_AxesWithLength = " + str(Selected_AxesWithLength))
        #             for m_axiswithlength in Selected_AxesWithLength:
        #                 m_C = (m_axiswithlength[0].Vertexes[-1].Point).sub(m_axiswithlength[0].Vertexes[0].Point).normalize()
        #                 #m_C = (m_axiswithlength[0].Curve.EndPoint - m_axiswithlength[0].Curve.StartPoint).normalize()
        #                 #m_found = colinearVectors(m_A, m_B, m_C, info=msg, tolerance=1e-10)
        #                 if abs((m_A.cross(m_C)).Length) <= 1e-10:
        #                     m_found = True
        #                     if msg != 0:
        #                         print_msg("m_found = " + str(m_found))
        #                     m_axiswithlength[1] += m_length
        #
        #             if not m_found:
        #                 Selected_AxesWithLength.append([m_axis, m_length])
        #     m_new_dim = len(Selected_AxesWithLength)
        #     if msg != 0:
        #         print_msg("len(Selected_AxesWithLength) = " + str(m_new_dim))
        #         print_msg("before sort: Selected_AxesWithLength = " + str(Selected_AxesWithLength))
        #     # sort by length
        #     # sorted(l, key=lambda x: x[2])
        #     # sorted(Selected_AxesWithLength, key=lambda AxesWithLength: AxesWithLength[1])
        #     Selected_AxesWithLength.sort(key=lambda x: x[1])
        #     if msg != 0:
        #         print_msg("after sort: Selected_AxesWithLength = " + str(Selected_AxesWithLength))
        # =======================================================================
        Number_of_Axes = len(Selected_Axes)
        if Number_of_Axes == 0:
            printError_msg(error_msg)
            return

        Selected_AxesWithLength, Selected_Points =  get_mainAxesFromSelectedAxes(Selected_Axes, info=msg)
        if Selected_AxesWithLength:
            m_new_dim = len(Selected_AxesWithLength)
            Vector_Center = meanVectorsPoint(Selected_Points, info=0)
            if m_new_dim >= 3:
                m_limit = -4
            elif m_new_dim == 2:
                m_limit = -3
            elif m_new_dim == 1:
                m_limit = -2
            else:
                printError_msg(error_msg)
                return
            m_color =  []
            m_color.append((1.00, 0.00, 0.00))
            m_color.append((0.00, 0.67, 0.00))
            m_color.append((0.33, 0.00, 1.00))

            for i in range(-1, m_limit, -1):
                m_axiswithlength = Selected_AxesWithLength[i]
                m_p1 = m_axiswithlength[0].Vertexes[0].Point
                m_p2 = m_axiswithlength[0].Vertexes[-1].Point
                m_c = centerLinePoint(m_axiswithlength[0])
                m_mv = Vector_Center.sub(m_c)
                Vector = m_p2.sub(m_p1).normalize().multiply(m_axiswithlength[1]/2)
                #Axis_User_Name, _ = plot_axis(m_p1, m_p2, part, name, m_dir)
                #Axis_User_Name, _ = plot_axis(m_c.add(Vector), m_c.add(Vector.multiply(-1)), part, name, m_dir)

                Axis_User_Name, _ = plot_axis(m_c.add(Vector).add(m_mv), m_c.add(Vector.multiply(-1)).add(m_mv), part, name, m_dir, m_color[i])
                print_msg(str(Axis_User_Name) + result_msg)

            print_msg(str(m_dir) + ": " + str(abs(i)) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_2PlanesAxis():
    """ Plot the intersection Axis between two planes.
    """
    msg = 0
    createFolders('WorkAxis')
    error_msg = "Unable to create Axis between 2 Planes: \nSelect two Planes not parallel !"
    result_msg = ": Axis between 2 Planes created !"
    name = "Line"
    part = "Part::Feature"
    Selection = get_SelectedObjects(info=msg, printError=False)
    m_num, m_selEx, m_objs, m_objNames = get_InfoObjects(info=0)
    m_xmax, m_xmin, m_ymax, m_ymin, m_zmax, m_zmin = minMaxObjectsLimits(m_objs, info=0)
    try:
        SelectedObjects = Selection
        Number_of_Planes = SelectedObjects[2]
        # print_msg("Number_of_Planes=" + str(Number_of_Planes))
        if (Number_of_Planes) >= 2:
            Plane_List = SelectedObjects[5]
            Selected_Plane1 = Plane_List[0]
            Selected_Plane2 = Plane_List[1]
            # print_msg(str(Selected_Plane1))
            # print_msg(str(Selected_Plane2))
            Plane_Normal1 = Selected_Plane1.normalAt(0, 0)
            Plane_Normal2 = Selected_Plane2.normalAt(0, 0)
            # print_point(Plane_Normal1, msg="Normal1: ")
            # print_point(Plane_Normal2, msg="Normal2: ")
            Plane_Point1 = Selected_Plane1.CenterOfMass
            Plane_Point2 = Selected_Plane2.CenterOfMass
            # print_point(Plane_Point1, msg="Plane_Point1: ")
            # print_point(Plane_Point2, msg="Plane_Point2: ")

            Axis_dir = intersecPlanePlane(Plane_Normal1, Plane_Point1, Plane_Normal2, Plane_Point2, info=0)
            # print_point(Axis_dir, msg="Axis_dir: ")

            # Intersection Line found
            if Axis_dir is not None:
                # print_msg("Selected_Plane1=" + str(Selected_Plane1))
                # print_msg("Selected_Plane1.Edges=" + str(Selected_Plane1.Edges))
                Number_of_Edges = len(Selected_Plane1.Edges)
                # print_msg("Number_of_Edges=" + str(Number_of_Edges))
                Vertx = []
                Vertx.append(App.Vector(0.0, 0.0, 0.0))
                Vertx.append(App.Vector(0.0, 0.0, 0.0))

                min_val, max_val = init_min_max()
                dist_to_center_min = max_val
                # For the first plane look after all edges and look at
                # intersections of the edges with the second plane
                for j in range(Number_of_Edges):
                    A = Selected_Plane1.Edges[j].valueAt(0.0)
                    B = Selected_Plane1.Edges[j].valueAt(Selected_Plane1.Edges[j].Length)
                    # print_point(A, msg="A: ")
                    # print_point(B, msg="B: ")
                    T = intersecLinePlane(A, B, Plane_Normal2, Plane_Point2, info=0)
                    if T is not None:
                        print_point(T, msg="T: ")
                        D = T - Plane_Point1
                        dist_to_center = math.sqrt(D.dot(D))
                        # print_msg("D=" + str(D))
                        # print_msg("dist_to_center=" + str(dist_to_center))
                        if dist_to_center < dist_to_center_min:
                            dist_to_center_min = dist_to_center
                            Vertx[0] = T
                #Center_User_Name = plot_point(Vertx[0], part, name)
                # print_msg("Selected_Plane2=" + str(Selected_Plane2))
                # print_msg("Selected_Plane2.Edges=" + str(Selected_Plane2.Edges))
                Number_of_Edges = len(Selected_Plane2.Edges)
                # print_msg("Number_of_Edges=" + str(Number_of_Edges))
                dist_to_center_min = max_val
                for j in range(Number_of_Edges):
                    A = Selected_Plane2.Edges[j].valueAt(0.0)
                    B = Selected_Plane2.Edges[j].valueAt(Selected_Plane2.Edges[j].Length)
                    # print_point(A, msg="A: ")
                    # print_point(B, msg="B: ")
                    T = intersecLinePlane(A, B, Plane_Normal1, Plane_Point1, info=0)
                    if T is not None:
                        # print_point(T, msg="T: ")
                        D = T - Plane_Point2
                        dist_to_center = math.sqrt(D.dot(D))
                        # print_msg("D=" + str(D))
                        # print_msg("dist_to_center=" + str(dist_to_center))
                        if dist_to_center < dist_to_center_min:
                            dist_to_center_min = dist_to_center
                            Vertx[1] = T

                #Center_User_Name = plot_point(Vertx[1], part, name)
                # print_msg("Selected_Points=" + str(Vertx))
                #Number_of_Points = len(Vertx)
                # print_msg("Number_of_Points=" + str(Number_of_Points))
                #C = centerBBVectorsPoint(Vertx,info=0)
                C = meanVectorsPoint(Vertx, info=1)
                # print_point(C, msg="C: ")

                if C is not None:
                    extension = m_xmax - m_xmin
                    if extension < m_ymax - m_ymin:
                        extension = m_ymax - m_ymin
                    if extension < m_zmax - m_zmin:
                        extension = m_zmax - m_zmin
                    extension = extension/2
                    A = C -  Axis_dir.normalize().multiply(extension*1.3)
                    B = C +  Axis_dir
                    Axis_User_Name, _ = plot_axis(A, B, part, name)
                    print_msg(str(Axis_User_Name) + result_msg)
        else:
            printError_msg(error_msg)

    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def numberLine(value):
    """ Respond to the change in number of line from the spin box.    
    """
    global verbose
    msg = verbose

    try:
        # First we check if a valid number have been entered
        global m_numberLine
        if str(value) == '-':
            return
        m_numberLine = int(value)
        if m_numberLine == 0:
            m_numberLine = 1
        if msg != 0:
            print_msg("New number is:" + str(m_numberLine))
    except ValueError:
        printError_msg("Number must be valid !")


def distLine(value):
    """ Respond to the change in Distance between line value from the text box.
    """
    global verbose
    msg = verbose
    try:
        # First we check if a valid number have been entered
        global m_distLine
        if str(value) == '-':
            return
        m_distLine = float(value)
        if msg != 0:
            print_msg("New Distance between lines is:" + str(m_distLine))
    except ValueError:
        printError_msg("Distance between lines must be valid number !")


def plot_distLine():
    """ Axes=(Axis,Pt,dist)):
        Create an Axis parallel to a given Axis, Point at a given distance.
        The Axis is created on the Plane defined by the given Axis and Point.
        - First select an Axis (or several Axes) and a Point 
        (you can also select several points to define different Planes)

        NB: The distance to the Axis created can be defined first.
        Positive number in one direction and negative in the other one.
        The second number indicates the number of Axes to create.
                
        If an Edge of a Cube is selected the Cube is duplicate with the corresponding
        Edge at the defined distance from the original.
    """
    global verbose
    global m_numberLine
    global m_distLine
    msg = verbose
    createFolders('WorkAxis')
    error_msg = "Unable to create Line(s): \nSelect one (or several) Line and one or several Points\nwith Point(s) NOT on the Line!"
    result_msg = ": Line(s) created !"

    Selection = get_SelectedObjectsWithParent(info=msg, printError=False)

    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]

        if (Number_of_Edges >= 1) and (Number_of_Points >= 1):
            Edge_List = SelectedObjects[4]
            Points_List = SelectedObjects[3]
            if msg != 0:
                print_msg("Number_of_Points = " + str(Number_of_Points))
                print_msg("Number_of_Edges = " + str(Number_of_Edges))
                print_msg("Point List = " + str(Points_List))
                print_msg("Edge List = " + str(Edge_List))

            # Loop on the Edges
            for Selected_Edge_dict in Edge_List:
                if msg != 0:
                    print_msg("Selected_Edge_dict = " + str(Selected_Edge_dict))
                for Selected_Edge, Parent_Edge in Selected_Edge_dict.iteritems():
                    if msg != 0:
                        print_msg("Selected_Edge = " + str(Selected_Edge))
                        print_msg("Parent_Edge = " + str(Parent_Edge))

                    Point_A = Selected_Edge.Vertexes[0].Point
                    Point_B = Selected_Edge.Vertexes[-1].Point
                    if msg != 0:
                        print_point(Point_A, msg="Selected_Edge.Vertexes[0]  Point_A: ")
                        print_point(Point_B, msg="Selected_Edge.Vertexes[-1] Point_B: ")
                    Placement1 = Selected_Edge.Placement
                    base1 = Placement1.Base
                    rot1 = Placement1.Rotation
                    AB_Vector = Point_B.sub(Point_A)
                    AB_Vector = AB_Vector.normalize()
                    # plot_axis(Base.Vector(0, 0, 0), AB_Vector, "Part::Feature", "AB")
                    center_Vector = centerLinePoint(Selected_Edge, info=msg)

                    # Loop on the Points
                    for Selected_Point_dict in Points_List:
                        if msg != 0:
                            print_msg("Selected_Point_dict = " + str(Selected_Point_dict))
                        for Selected_Point, Parent_Point in Selected_Point_dict.iteritems():
                            Point_C = Selected_Point.Point
                            if msg != 0:
                                print_point(Point_C, msg="Point_C: ")

                            AC_Vector = Point_C.sub(Point_A)
                            AC_Vector = AC_Vector.normalize()
                            # plot_axis(Base.Vector(0, 0, 0), AC_Vector, "Part::Feature", "AC")
                            Plane_Normal = AB_Vector.cross(AC_Vector)
                            Plane_Normal = Plane_Normal.normalize()
                            # plot_axis(Base.Vector(0, 0, 0), Plane_Normal, "Part::Feature", "Plane_Normal")
                            Move_Vector = Plane_Normal.cross(AB_Vector)
                            # plot_axis(Base.Vector(0, 0, 0), Move_Vector, "Part::Feature", "Move_Vector")
                            Move_Vector = Move_Vector.normalize().multiply(m_distLine)
                            Move_Vector = Move_Vector.add(center_Vector)
                            # plot_axis(center_Vector, Move_Vector, "Part::Feature", "End_Move_Vector")
                            m_move = Move_Vector.sub(center_Vector)
                            if msg != 0:
                                print_point(Move_Vector, msg="Move_Vector = ")
                                print_point(m_move, msg="m_move = ")
                                print_msg("m_numberLine = " + str(m_numberLine))

                            for m_i in range(m_numberLine):
                                if objCopy == 1:
                                    m_new_line = App.activeDocument().copyObject(Parent_Edge)
                                else:
                                    m_new_line_shape = Selected_Edge.copy()
                                    m_new_line = App.ActiveDocument.addObject("Part::Feature", "Line_at_distance")
                                    m_new_line.Shape = m_new_line_shape
                                App.ActiveDocument.getObject('WorkAxis').addObject(m_new_line)
                                Line_User_Name = m_new_line.Label

                                if msg != 0:
                                    print_msg("m_new_line = " + str(m_new_line))

                                newplace1 = App.Placement(base1.add(m_move), rot1)
                                m_new_line.Placement = newplace1
                                # Update the move
                                m_move = m_move.add(Move_Vector.sub(center_Vector))

                                properties_line(Line_User_Name)
                                print_msg(str(Line_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def numberLine2(value):
    """ Respond to the change in number of line from the spin box.
    """
    global verbose
    msg = verbose

    try:
        # First we check if a valid number have been entered
        global m_numberLine2
        if str(value) == '-':
            return
        m_numberLine2 = int(value)
        if m_numberLine2 == 0:
            m_numberLine2 = 1
        if msg != 0:
            print_msg("New number is:" + str(m_numberLine2))
    except ValueError:
        printError_msg("Number must be valid !")


def angleLine(value):
    """ Respond to the change in Angle between line value from the text box.
    """
    global verbose
    msg = verbose
    try:
        # First we check if a valid number have been entered
        global m_angleLine
        m_angleLine = float(value)
        if msg != 0:
            print_msg("New Angle between lines is:" + str(m_angleLine))
    except ValueError:
        printError_msg("Angle between lines must be valid number in degrees !")


def plot_angleLine():
    """ Axes=(Axis,Pt,Pl,a):
        Create an Axis with an Angle to a origin Axis.
        - First select an Axis to rotate, then a Plane and a rotation Point
        or
        - First select an Axis to rotate, then a rotation Axis and a rotation Point

        NB:
        The Axis is created by rotation using:
          The Normal of the selected Plane as rotation Axis
        and selected Point as rotation Point.
        or
          The second selected Axis as rotation Axis
        and selected Point as rotation Point.

         - The angle (in degrees) of rotation can be defined first.
        Positive number in one direction and negative in the other one.
         - The second number indicates the number of Axes to create.
    """
    msg = verbose
    createFolders('WorkAxis')
    error_msg = "Unable to create Line(s): \n " +\
                "Select first one Line then one Point and one Plane! \n" +\
                "or\n" +\
                "Select first one Line then one Point and one second Axis!"
    result_msg = ": Line(s) created !"
    name = "Line_with_angle"
    part = "Part::Feature"

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        Number_of_Planes = SelectedObjects[2]
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points) + \
                      "\nNumber_of_Edges=" + str(Number_of_Edges) + \
                      "\nNumber_of_Planes=" + str(Number_of_Planes))

        if (Number_of_Points == 1) and (Number_of_Edges == 1) and (Number_of_Planes) == 1:
            Point_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]
            Plane_List = SelectedObjects[5]
            if msg != 0:
                print_msg("Point List = " + str(Point_List))
                print_msg("Edge List = " + str(Edge_List))
                print_msg("Plane_List = " + str(Plane_List))
            Vector_A = Edge_List[0].Vertexes[0].Point
            Vector_B = Edge_List[0].Vertexes[-1].Point
            m_Edge = Edge_List[0]
            Vector_C = Point_List[0].Point
            Plane_D = Plane_List[0]
            if msg != 0:
                print_point(Vector_A, msg="Vector_A: ")
                print_point(Vector_B, msg="Vector_B: ")
                print_point(Vector_C, msg="Vector_C: ")

            rot_center = Vector_C
            rot_axis = Plane_D.normalAt(0, 0)
            rot_angle = m_angleLine
            rot_copy = m_numberLine2
            if msg != 0:
                print_msg("rot_center = " + str(rot_center))
                print_msg("rot_axis = " + str(rot_axis))
                print_msg("rot_angle = " + str(rot_angle))
                print_msg("rot_copy = " + str(rot_copy))
            for i in range(rot_copy):
                m_Edge2 = m_Edge.copy()
                # Apply the rotation (degree) to the current location of this shape
                # Shp.rotate(Vector(0,0,0),Vector(0,0,1),180)
                # rotate the shape around the Z Axis 180 degrees.
                m_Edge2.rotate(rot_center, rot_axis, rot_angle)
                Axis_E1 = m_Edge2.Vertexes[0].Point
                Axis_E2 = m_Edge2.Vertexes[1].Point

                Axis_User_Name, axis = plot_axis(Axis_E1, Axis_E2, part, name)
                print_msg(str(Axis_User_Name) + result_msg)
                rot_angle = rot_angle + m_angleLine

        elif (Number_of_Points == 1) and (Number_of_Edges == 2):
            Point_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg("Point List = " + str(Point_List))
                print_msg("Edge List = " + str(Edge_List))
            Vector_A = Edge_List[0].Vertexes[0].Point
            Vector_B = Edge_List[0].Vertexes[-1].Point
            m_Edge = Edge_List[0]
            Vector_C = Point_List[0].Point

            if msg != 0:
                print_point(Vector_A, msg="Vector_A: ")
                print_point(Vector_B, msg="Vector_B: ")
                print_point(Vector_C, msg="Vector_C: ")

            rot_center = Vector_C
            Point_A = Edge_List[1].Vertexes[0].Point
            Point_B = Edge_List[1].Vertexes[-1].Point
            rot_axis = Point_B.sub(Point_A)
            rot_angle = m_angleLine
            rot_copy = m_numberLine2
            if msg != 0:
                print_msg("rot_center = " + str(rot_center))
                print_msg("rot_axis = " + str(rot_axis))
                print_msg("rot_angle = " + str(rot_angle))
                print_msg("rot_copy = " + str(rot_copy))
            for i in range(rot_copy):
                m_Edge2 = m_Edge.copy()
                # Apply the rotation (degree) to the current location of this shape
                # Shp.rotate(Vector(0,0,0),Vector(0,0,1),180)
                # rotate the shape around the Z Axis 180 degrees.
                m_Edge2.rotate(rot_center, rot_axis, rot_angle)
                Axis_E1 = m_Edge2.Vertexes[0].Point
                Axis_E2 = m_Edge2.Vertexes[1].Point

                Axis_User_Name, axis = plot_axis(Axis_E1, Axis_E2, part, name)
                print_msg(str(Axis_User_Name) + result_msg)
                rot_angle = rot_angle + m_angleLine

        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_baseObjectAxes():
    msg = 0
    createFolders('Origin')
    error_msg = "Unable to create Axes: \nSelect at least one object !"
    result_msg = ": Axes created !"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    # Return a list of SelectionObjects for a given document name.
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    m_objs = [selobj.Object for selobj in m_selEx]
    m_num = len(m_objs)
    if m_num < 1:
        printError_msg(error_msg)
        return
    CommonCenter = centerObjectsPoint(m_objs, info=1)
    for m_i in range(0, m_num):
        m_base = m_objs[m_i].Placement.Base
        print_msg("Base =" + str(m_base))
        print_msg("Center=" + str(CommonCenter))
        if m_base is not None:
            xmax, xmin, ymax, ymin, zmax, zmin = minMaxObjectsLimits(m_objs)
            # Work-AxisX
            if xmax != xmin:
                AX_Length = (xmax - xmin) * 1.3
            else:
                AX_Length = 10.
            PX_A = Base.Vector(AX_Length, 0, 0)
            PX_B = Base.Vector(-AX_Length, 0, 0)
            Axis_X = Part.makeLine(m_base + PX_A, m_base + PX_B)
            Axis = App.ActiveDocument.addObject("Part::Feature", "X_Axis")
            Axis.Shape = Axis_X
            App.ActiveDocument.getObject("WorkAxis").addObject(Axis)
            Axis_User_Name = Axis.Label
            Gui.ActiveDocument.getObject(Axis_User_Name).LineColor = (1.00, 0.00, 0.00)
            Gui.ActiveDocument.getObject(Axis_User_Name).PointColor = (1.00, 0.00, 0.00)
            Gui.ActiveDocument.getObject("X_Axis").Visibility = True
            print_msg(str(Axis_User_Name) + result_msg)
            # Work-AxisY
            if ymax != ymin:
                AY_Length = (ymax - ymin) * 1.3
            else:
                AY_Length = 10.
            PY_A = Base.Vector(0, AY_Length, 0)
            PY_B = Base.Vector(0, -AY_Length, 0)
            Axis_Y = Part.makeLine(m_base + PY_A, m_base + PY_B)
            Axis = App.ActiveDocument.addObject("Part::Feature", "Y_Axis")
            Axis.Shape = Axis_Y
            App.ActiveDocument.getObject("WorkAxis").addObject(Axis)
            Axis_User_Name = Axis.Label
            Gui.ActiveDocument.getObject(Axis_User_Name).LineColor = (0.00, 0.67, 0.00)
            Gui.ActiveDocument.getObject(Axis_User_Name).PointColor = (0.00, 0.67, 0.00)
            Gui.ActiveDocument.getObject("Y_Axis").Visibility = True
            print_msg(str(Axis_User_Name) + result_msg)
            # Work-AxisZ
            if zmax != zmin:
                AZ_Length = (zmax - zmin) * 1.3
            else:
                AZ_Length = 10.
            PZ_A = Base.Vector(0, 0, AZ_Length)
            PZ_B = Base.Vector(0, 0, -AZ_Length)
            Axis_Z = Part.makeLine(m_base + PZ_A, m_base + PZ_B)
            Axis = App.ActiveDocument.addObject("Part::Feature", "Z_Axis")
            Axis.Shape = Axis_Z
            App.ActiveDocument.getObject("WorkAxis").addObject(Axis)
            Axis_User_Name = Axis.Label
            Gui.ActiveDocument.getObject(Axis_User_Name).LineColor = (0.33, 0.00, 1.00)
            Gui.ActiveDocument.getObject(Axis_User_Name).PointColor = (0.33, 0.00, 1.00)
            Gui.ActiveDocument.getObject("Z_Axis").Visibility = True
            print_msg(str(Axis_User_Name) + result_msg)
        else:
            printError_msg(error_msg)


def vertexToSketch(points, sketch):
    """
    Project the selected points onto Sketch plane and add
    them to Sketch domain.
    (return num_point, return_points)
    Return the number of points transferred in Sketch domain
    and their corresponding projections.
    """
    if (None in [points, sketch]):
        return None
    import Part
    m_sketch = sketch
    m_points = points
    # Get the Sketch Plane info
    m_rec1 = Part.makePlane(1, 1)
    m_rec2 = Part.makePlane(1, 1)
    m_rec1.Placement = m_sketch.Placement.inverse()
    m_rec2.Placement = m_sketch.Placement
    m_rec2N = m_rec2.normalAt(0, 0)

    # Build a geometry list
    geoList = []
    return_points = []
    num_point = 0
    for m_point in m_points:
        m_p1 = App.Base.Vector(m_point.Point)
        m_p2 = App.Base.Vector(m_point.Point)
        # App.Base.Placement.multVec
        # multVector(Vector) -> Vector
	    # Compute the transformed vector using the placement
        Projection1 = m_rec1.Placement.multVec(m_p1)
        Projection2 = m_p2.projectToPlane(m_sketch.Placement.Base, m_rec2N)
        # Append the Projection
        geoList.append(Part.Point(Projection1))
        return_points.append(Part.Point(Projection2))
        num_point = num_point + 1

    m_sketch.addGeometry(geoList)
    return num_point, return_points

#                P = BRep_Tool.Pnt(TopoDS.Vertex(refSubShape))
#                GeomAPI_ProjectPointOnSurf proj(P,gPlane)
#                P = proj.NearestPoint()
#                Base.Vector3d p(P.X(),P.Y(),P.Z())
#                invPlm.multVec(p,p)
#                point = Part.GeomPoint(p)
#                point.Construction = True
#                ExternalGeo.push_back(point)

def edgeToSketch(edges, sketch):
    """
    Project the selected edges onto Sketch plane and add
    them to Sketch domain.
    (return num_edge, return_edges, num_point, return_points)
    Return the number of edges transferred in Sketch domain
    and the corresponding projections and if any
    the number of points transferred in Sketch domain
    and their corresponding projections. 
    """
    if (None in [edges, sketch]):
        return None
    import Part
    m_tolerance = 1e-12

    m_sketch = sketch
    m_edges = edges
    # Get the Sketch Plane info
    m_rec1 = Part.makePlane(1, 1)
    m_rec2 = Part.makePlane(1, 1)
    m_rec1.Placement = m_sketch.Placement.inverse()
    m_rec2.Placement = m_sketch.Placement
    m_rec2N = m_rec2.normalAt(0, 0)

    # Build a geometry list
    geoList = []
    return_edges = []
    num_edge = 0
    return_points = []
    num_point = 0
    for m_edge in m_edges:
        m_Vertex1 = m_edge.Vertexes[0]
        m_Vertex2 = m_edge.Vertexes[-1]
        m_p1 = App.Base.Vector(m_Vertex1.Point)
        m_p2 = App.Base.Vector(m_Vertex1.Point)
        m_p3 = App.Base.Vector(m_Vertex2.Point)
        m_p4 = App.Base.Vector(m_Vertex2.Point)

        # Compute the transformed vector using the placement
        Projection1 = m_rec1.Placement.multVec(m_p1)
        Projection2 = m_p2.projectToPlane(m_sketch.Placement.Base, m_rec2N)
        Projection3 = m_rec1.Placement.multVec(m_p3)
        Projection4 = m_p4.projectToPlane(m_sketch.Placement.Base, m_rec2N)

        if distanceBetween(Projection2, Projection4) < m_tolerance:
            # Append one projected point only the Projection
            geoList.append(Part.Point(Projection1))
            return_points.append(Part.Point(Projection2))
            num_point = num_point + 1
        else:
            # Append the line
            geoList.append(Part.Line(Projection1, Projection3))
            return_edges.append(Part.Line(Projection2, Projection4))
            num_edge = num_edge + 1
    m_sketch.addGeometry(geoList)

    return num_edge, return_edges, num_point, return_points


def circleToSketch(circles, sketch):
    """
    Project the selected circles onto Sketch plane and add
    them to Sketch domain.
    (return num_edge, return_circles, num_point, return_points)
    Return the number of circles transferred in Sketch domain
    and the corresponding projections and if any
    the number of points transferred in Sketch domain
    and their corresponding projections. 
    """
    if (None in [circles, sketch]):
        return None
    import Part
    m_tolerance = 1e-12

    m_sketch = sketch
    m_circles = circles
    # Get the Sketch Plane info
    m_rec1 = Part.makePlane(1, 1)
    m_rec2 = Part.makePlane(1, 1)
    m_rec1.Placement = m_sketch.Placement.inverse()
    m_rec2.Placement = m_sketch.Placement
    m_rec2N = m_rec2.normalAt(0, 0)

    # Build a geometry list
    geoList = []
    return_circles = []
    num_circle = 0
    return_points = []
    num_point = 0
# ==============================================================================
#                    for SubObject in m_obj.SubObjects:
#                     if SubObject.ShapeType == "Edge":
#                         if msg != 0:
#                             print_msg("Found a Edge object!")
#                         # Get the Edge
#                         m_Edge = SubObject
#                         # Append the Edge
#                         m_edgeList.append(m_Edge)
#                         m_num_line = m_num_line + 1
#                     else:
#                         continue
# ==============================================================================
    for m_circle in m_circles:
        m_Vertex1 = m_circle.Vertexes[0]
        m_Vertex2 = m_circle.Vertexes[-1]
        m_p1 = App.Base.Vector(m_Vertex1.Point)
        m_p2 = App.Base.Vector(m_Vertex1.Point)
        m_p3 = App.Base.Vector(m_Vertex2.Point)
        m_p4 = App.Base.Vector(m_Vertex2.Point)

    	# Compute the transformed vector using the placement
        Projection1 = m_rec1.Placement.multVec(m_p1)
        Projection2 = m_p2.projectToPlane(m_sketch.Placement.Base, m_rec2N)
        Projection3 = m_rec1.Placement.multVec(m_p3)
        Projection4 = m_p4.projectToPlane(m_sketch.Placement.Base, m_rec2N)

        if distanceBetween(Projection2, Projection4) < m_tolerance:
            # Append one projected point only the Projection
            geoList.append(Part.Point(Projection1))
            return_points.append(Part.Point(Projection2))
            num_point = num_point + 1
        else:
            # Append the line
            geoList.append(Part.Line(Projection1, Projection3))
            return_circles.append(Part.Line(Projection2, Projection4))
            num_circle = num_circle + 1
        m_sketch.addGeometry(geoList)

    return num_circle, return_circles, num_point, return_points


def faceToSketch(m_obj):
    msg = verbose
    if msg != 0:
        print_msg("Found a Face !" + str(m_obj))

    print_gui_msg("Faces are not yet supported for external geometry of sketches !")
    return


def errorToSketch(m_obj):
    print_gui_msg("Unknown type of geometry !")
    return

options = {'Edge': edgeToSketch, 'Vertex': vertexToSketch, 'Face': faceToSketch,
           'Unknown': errorToSketch}

def toSketch():

    msg = verbose

    m_actDoc = get_ActiveDocument(info=msg)
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    for m_obj in m_selEx:
        for m_sub in m_obj.SubObjects:
            options[getShapeType(m_sub)](m_sub)
#    #FACE:
#    #EDGE:
#    #VERTEX:
#    pass

def circle_toSketch():
    """ Transform Circle(s) and Arc(s) in Sketch's Cirlce(s) and Arc(s) by projection onto the Sketch's Plane:
    - First select an existing Skecth;
    - Select as much as Circles and Arcs needed;
    Then click on this button.
    """
    msg = verbose
    m_tolerance = 1e-12

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None
    error_msg = "Transform Circle(s) and Arc(s) in Sketch's Circle(s) and Arc(s): \nFirst select an existing Skecth\nthen select Circles and Arcs !"
    result_msg = ": Circle(s) and Arc(s) transformed in Sketch's done!"

    m_sel  = Gui.Selection.getSelection(m_actDoc.Name)
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg("m_sel       : " + str(m_sel))
        print_msg("m_selEx      : " + str(m_selEx))
    m_num = len(m_sel)
    m_num_arc = 0
    if m_num > 1:
        # Get the Sketch from the selection
        m_obj = m_sel[0]
        if msg != 0:
            print_msg("m_obj       : " + str(m_obj))
        if hasattr(m_obj, 'TypeId'):
            m_type = m_obj.TypeId
            if msg != 0:
                print_msg("m_obj.TypeId: " + str(m_type))
        else:
            m_type = m_obj.Type
            if msg != 0:
                print_msg("m_obj.Type: " + str(m_type))

        if m_type[:6] == "Sketch":
            if msg != 0:
                print_msg("Found a Sketch object!")
            m_sketch = m_obj
            # Get the Sketch Plane info
            m_rec = Part.makePlane(1, 1)
            m_rec.Placement = m_sketch.Placement
            m_recN = m_rec.normalAt(0, 0)
            # Build a geometry list
            geoList = []
            # Get Point(s) from the selection
            for m_i in range(1, m_num):
                m_obj = m_selEx[m_i]
                #SubObject = m_obj.SubObjects[0]
                for SubObject in m_obj.SubObjects:
                    if SubObject.ShapeType == "Edge":
                        if msg != 0:
                            print_msg("Found a Edge object!")

                        m_curve = SubObject.Curve
                        # if str(m_curve)[:6] == "Circle":
                        if getEdgeType(SubObject) == "Circle":
                            if msg != 0:
                                print_msg("SubObject.Curve=" + str(SubObject.Curve))
                                print_msg("Object is Circle")
                            if hasattr(m_curve, 'Center'):
                                m_center = m_curve.Center
                                # Projection of the Point selected onto the Sketch Plane
                                m_center_Proj = m_center.projectToPlane(m_sketch.Placement.Base, m_recN)
                                # Append the Projection
                                geoList.append(Part.Point(m_center_Proj))
                                # Add the geometry list to the Sketch
                                m_sketch.addGeometry(geoList)
                            # Get Normal of the Circle
                            m_cirN = m_curve.Axis
                            m_radius = m_curve.Radius
                            if msg != 0:
                                print_msg("m_radius=" + str(m_radius))
                            # Check if the Plane of the Sketch is the same than the Plane of the Circle
                            if colinearVectors(m_recN, Base.Vector(0, 0, 0), m_cirN, info=msg, tolerance=m_tolerance):
                                # creates a circle
                                print_msg("Sketch and Circle are on Parallel Planes !")
                                m_begin = SubObject.FirstParameter
                                m_end = SubObject.LastParameter
                                if msg != 0:
                                    print_msg("m_begin=" + str(m_begin))
                                    print_msg("m_end=" + str(m_end))

                                m_circle = Part.Circle(m_center_Proj, m_recN, m_radius)
                                if msg != 0:
                                    print_msg("m_circle=" + str(m_circle))

                                if abs((m_begin - m_end)%(2*math.pi)) < m_tolerance:
                                    geoList.append(m_circle)
                                else:
                                    m_curve = Part.ArcOfCircle(m_circle, m_begin, m_end)
                                    if msg != 0:
                                        print_msg("m_curve=" + str(m_curve))
                                    geoList.append(m_curve)
                                m_sketch.addGeometry(geoList)
                                m_num_arc = m_num_arc + 1
                            else:
                                # creates an ellipse
                                print_msg("Sketch and Circle are NOT on Parallel Planes !")
                                # Projection of a Circle(R)from a Plane towaerd another
                                # not parallel Plane gives an Ellipse(R,Rcos(teta))
                                # with teta is angle betwwen the 2 Planes and center on
                                # projected center Point

                                m_angle, m_angle_rad = angleBetween(m_recN, m_cirN)
                                if msg != 0:
                                    print_msg("m_angle=" + str(m_angle))
                                    print_msg("m_angle_rad=" + str(m_angle_rad))

                                m_minRadius = m_radius*math.cos(m_angle_rad)
                                if msg != 0:
                                    print_msg("m_minRadius=" + str(m_minRadius))

                                if abs(m_minRadius) < m_tolerance:
                                    S1 = m_center_Proj.add(m_recN.cross(m_cirN).normalize().multiply(m_radius))
                                    S2 = m_center_Proj.sub(m_recN.cross(m_cirN).normalize().multiply(m_radius))
                                    geoList.append(Part.Line(S1, S2))
                                else:
                                    S1 = m_center_Proj.add(m_recN.cross(m_cirN).normalize().multiply(m_radius))
                                    S2 = m_center_Proj.add(m_recN.cross(m_recN.cross(m_cirN).normalize()).multiply(m_minRadius))
                                    m_curve = Part.Ellipse(S1, S2, m_center_Proj)
                                    if msg != 0:
                                        print_msg("m_curve=" + str(m_curve))
                                    geoList.append(m_curve)
                                m_sketch.addGeometry(geoList)
                                m_num_arc = m_num_arc + 1
                        elif getEdgeType(SubObject) == "Ellipse":
                            if msg != 0:
                                print_msg("SubObject.Curve=" + str(SubObject.Curve))
                                print_msg("Object is Ellipse")
                            if hasattr(m_curve, 'Center'):
                                m_center = m_curve.Center
                                # Projection of the Point selected onto the Sketch Plane
                                m_center_Proj = m_center.projectToPlane(m_sketch.Placement.Base, m_recN)
                                # Append the Projection
                                geoList.append(Part.Point(m_center_Proj))
                                # Add the geometry list to the Sketch
                                m_sketch.addGeometry(geoList)
                            # Get Normal of the Ellipse
                            m_cirN = m_curve.Axis
                            # Check if the Plane of the Sketch is the same than the Plane of the Ellipse
                            if colinearVectors(m_recN, Base.Vector(0, 0, 0), m_cirN, info=msg, tolerance=m_tolerance):
                                # creates an Ellipse
                                print_msg("Sketch and Ellipse are on Parallel Planes !")
                                m_majorRadius = m_curve.MajorRadius
                                m_minorRadius = m_curve.MinorRadius
                                m_focus1 = m_curve.Focus1
                                m_axis1 = m_center.sub(m_focus1)
                                if msg != 0:
                                    print_msg("m_majorRadius=" + str(m_majorRadius))
                                    print_msg("m_minorRadius=" + str(m_minorRadius))
                                    print_msg("m_focus1=" + str(m_focus1))
                                S1 = m_center_Proj.add(m_axis1.normalize().multiply(m_majorRadius))
                                S2 = m_center_Proj.add(m_axis1.cross(m_cirN).normalize().multiply(m_minorRadius))

                                m_curve = Part.Ellipse(S1, S2, m_center_Proj)
                                if msg != 0:
                                    print_msg("m_curve=" + str(m_curve))
                                geoList.append(m_curve)
                            else:
                                # creates an ellipse
                                print_msg("Sketch and Ellipse are NOT on Parallel Planes !")
                                printError_msg("Sketch and Ellipse are NOT on Parallel Planes ! \nNot yet supported developed !")
                            m_sketch.addGeometry(geoList)
                            m_num_arc = m_num_arc + 1
                        else:
                            printError_msg("Not a Circle neither an ellipse \nNot yet supported geometry !")

                    else:
                        continue
            # Refresh
            App.getDocument(str(m_actDoc.Name)).recompute()
            print_msg(str(m_num_arc) + result_msg)
        else:
            printError_msg(error_msg)
    else:
        printError_msg(error_msg)
    return


def line_toSketch():
    """ Transform Line(s) in Sketch's Line(s) by projection onto the Sketch's Plane:
    - First select an existing Skecth;
    - Select as much as Lines needed;
    Then click on this button.
    """
    global verbose
    msg = verbose

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None
    error_msg = "Transform Line(s) in Sketch's Line(s): \nFirst select an existing Skecth\nthen select line(s) !"
    result_msg = ": Line(s) transformed in Sketch's Line(s) done!"

    m_sel  = Gui.Selection.getSelection(m_actDoc.Name)
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg("m_sel       : " + str(m_sel))
    m_num = len(m_sel)
    m_num_line = 0
    if m_num > 1:
        # Get the Sketch from the selection
        m_obj = m_sel[0]
        if msg != 0:
            print_msg("m_obj       : " + str(m_obj))
        if hasattr(m_obj, 'TypeId'):
            m_type = m_obj.TypeId
            if msg != 0:
                print_msg("m_obj.TypeId: " + str(m_type))
        else:
            m_type = m_obj.Type
            if msg != 0:
                print_msg("m_obj.Type: " + str(m_type))

        if m_type[:6] == "Sketch":
            if msg != 0:
                print_msg("Found a Sketch object!")
            m_sketch = m_obj

            # Build a edge list
            m_edgeList = []
            # Get Point(s) from the selection
            for m_i in range(1, m_num):
                m_obj = m_selEx[m_i]

                for SubObject in m_obj.SubObjects:
                    if SubObject.ShapeType == "Edge":
                        if msg != 0:
                            print_msg("Found a Edge object!")
                        # Get the Edge
                        m_Edge = SubObject
                        # Append the Edge
                        m_edgeList.append(m_Edge)
                        m_num_line = m_num_line + 1
                    else:
                        continue

            num_edge, return_edges, num_point, return_points = \
            edgeToSketch(m_edgeList, m_sketch)
            if m_num_line != (num_edge + num_point):
                printError_msg(error_msg)
                return
            if msg != 0:
                createFolders('WorkPoints')
                createFolders('WorkAxis')
                for point in return_points:
                    plot_point(point, part="Part::Feature", name="Sketch_Proj", grp="WorkPoints")
                for edge in return_edges:
                    plot_axis(edge.StartPoint, edge.EndPoint, part="Part::Feature", name="Sketch_Proj", grp="WorkAxis")

            # Refresh
            App.getDocument(str(m_actDoc.Name)).recompute()
            print_msg(str(m_num_line) + result_msg)
        else:
            printError_msg(error_msg)
    else:
        printError_msg(error_msg)
    return


def line_toSketch_old():
    """ Transform Line(s) in Sketch's Line(s) by projection onto the Sketch's Plane:
    - First select an existing Skecth;
    - Select as much as Lines needed;
    Then click on this button.
    """
    global verbose
    msg = verbose
    m_tolerance = 1e-12

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None
    error_msg = "Transform Line(s) in Sketch's Line(s): \nFirst select an existing Skecth\nthen select line(s) !"
    result_msg = ": Line(s) transformed in Sketch's Line(s) done!"

    m_sel  = Gui.Selection.getSelection(m_actDoc.Name)
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg("m_sel       : " + str(m_sel))
    m_num = len(m_sel)
    m_num_line = 0
    if m_num > 1:
        # Get the Sketch from the selection
        m_obj = m_sel[0]
        if msg != 0:
            print_msg("m_obj       : " + str(m_obj))
        if hasattr(m_obj, 'TypeId'):
            m_type = m_obj.TypeId
            if msg != 0:
                print_msg("m_obj.TypeId: " + str(m_type))
        else:
            m_type = m_obj.Type
            if msg != 0:
                print_msg("m_obj.Type: " + str(m_type))

        if m_type[:6] == "Sketch":
            if msg != 0:
                print_msg("Found a Sketch object!")
            m_sketch = m_obj
            # Get the Sketch Plane info
            m_rec = Part.makePlane(1, 1)
            m_rec.Placement = m_sketch.Placement
            m_recN = m_rec.normalAt(0, 0)
            # Build a geometry list
            geoList = []
            # Get Point(s) from the selection
            for m_i in range(1, m_num):
                m_obj = m_selEx[m_i]
                #SubObject = m_obj.SubObjects[0]
                for SubObject in m_obj.SubObjects:
                    if SubObject.ShapeType == "Edge":
                        if msg != 0:
                            print_msg("Found a Edge object!")
                        if len(SubObject.Vertexes) == 2:
                            m_Vertex1 = SubObject.Vertexes[0]
                            m_Vertex2 = SubObject.Vertexes[1]
                        else:
                            printError_msg(error_msg)
                            return
                        # Get the Point
                        m_p1 = m_Vertex1.Point
                        m_p2 = m_Vertex2.Point
                        # Projection of the Point selected onto the Sketch Plane
                        Projection1 = m_p1.projectToPlane(m_sketch.Placement.Base, m_recN)
                        Projection2 = m_p2.projectToPlane(m_sketch.Placement.Base, m_recN)
                        if distanceBetween(Projection1, Projection2) < m_tolerance:
                            # Append the Projection
                            geoList.append(Part.Point(Projection1))
                        else:
                            # Append the Projection
                            geoList.append(Part.Line(Projection1, Projection2))
                        # Add the geometry list to the Sketch
                        m_sketch.addGeometry(geoList)
                        m_num_line = m_num_line + 1
                    else:
                        continue
            # Refresh
            App.getDocument(str(m_actDoc.Name)).recompute()
            print_msg(str(m_num_line) + result_msg)
        else:
            printError_msg(error_msg)
    else:
        printError_msg(error_msg)
    return


def radiusCircle(value):
    """ Respond to the change in radius value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_radiusCircle
        if str(value) == '-':
            return
        m_radiusCircle = float(value)
        print_msg("New extension is:" + str(m_radiusCircle))
    except ValueError:
        printError_msg("Extension must be valid number !")


def plot_linecenterCircle():
    """Select an Axis and a Point to create a Circle
    centered on the Point, perpendicular to the Axis 
    with the given radius.
    """
    msg = verbose

    global m_radiusCircle
    createFolders('WorkCircles')
    error_msg = "Unable to create a Circle: \nSelect one Edge and one Point only!"
    result_msg = ": Circle centered on a Point created !"
    name = "Circle"
    part = "Part::Feature"
    grp = "WorkCircles"
    Selection = get_SelectedObjects(info=msg, printError=False)

    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges) +
                      " Number_of_Points=" + str(Number_of_Points))
        if (Number_of_Edges == 1) and (Number_of_Points) == 1:
            Point_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg(str(Point_List))
                print_msg(str(Edge_List))
            Vector_C = Point_List[0].Point
            Vector_A = Edge_List[0].valueAt(0.0)
            Vector_B = Edge_List[0].valueAt(Edge_List[0].Length)
            Vector_dir = (Vector_B - Vector_A)

            Circle_User_Name, circle = plot_circle(m_radiusCircle, Vector_C, Vector_dir, part, name, grp)
            print_msg(str(Circle_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_linepointCircle():
    """Select an Axis and a Point to create a Circle
    centered on the Axis and tangenting the Point.
    """
    msg = verbose

    createFolders('WorkCircles')
    error_msg = "Unable to create a Circle: \nSelect one Edge and one Point only!"
    result_msg = ": Circle tangented to a Point created !"
    name = "Circle"
    part = "Part::Feature"
    grp = "WorkCircles"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges) +
                      " Number_of_Points=" + str(Number_of_Points))
        if (Number_of_Edges == 1) and (Number_of_Points) == 1:
            Point_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg(str(Point_List))
                print_msg(str(Edge_List))
            Vector_C  = Point_List[0].Point
            Vector_A  = Edge_List[0].valueAt(0.0)
            Vector_B  = Edge_List[0].valueAt(Edge_List[0].Length)
            Vector_dir = (Vector_B - Vector_A)

            Vector_T, Distance, Vector_Tprime = intersecPerpendicularLine(Vector_A, Vector_B, Vector_C, info=msg)

            Circle_User_Name, circle = plot_circle(Distance, Vector_T, Vector_dir, part, name, grp)
            print_msg(str(Circle_User_Name) + result_msg)

        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_3pointsArc():
    """Select 3 Points to create an Arc.
    """
    msg = verbose

    createFolders('WorkArcs')
    error_msg = "Unable to create an Arc: \nSelect 3 Points only!"
    result_msg = ": Arc from 3 points created !"
    name = "Arc"
    part = "Part::Feature"
    grp = "WorkArcs"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if Number_of_Points == 3:
            Point_List = SelectedObjects[3]

            P1 = Point_List[0].Point
            P2 = Point_List[1].Point
            P3 = Point_List[2].Point

            l = ((P1 - P2).cross(P2 - P3)).Length

            P1P2 = (P2 - P1).Length
            P2P3 = (P3 - P2).Length
            P3P1 = (P1 - P3).Length
            r = 0.0
            try:
                # Circle radius.
                r = P1P2 * P2P3 * P3P1 / 2 / l
            except Exception as inst:
                print(inst.args)
                printError_msg("The three points are aligned !")
            else:
                # Normal
                Arc_User_Name, arc = plot_arc3(P1, P2, P3, part, name, grp)
                print_msg(str(Arc_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_3pointsCircle():
    """Select 3 Points to create a Circle.
    """
    msg = verbose

    createFolders('WorkCircles')
    error_msg = "Unable to create a Circle: \nSelect 3 Points only!"
    result_msg = ": Circle from 3 points created !"
    name = "Circle"
    part = "Part::Feature"
    grp = "WorkCircles"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if Number_of_Points == 3:
            Point_List = SelectedObjects[3]

            P1 = Point_List[0].Point
            P2 = Point_List[1].Point
            P3 = Point_List[2].Point

            l = ((P1 - P2).cross(P2 - P3)).Length

            P1P2 = (P2 - P1).Length
            P2P3 = (P3 - P2).Length
            P3P1 = (P1 - P3).Length
            r = 0.0
            try:
                # Circle radius.
                r = P1P2 * P2P3 * P3P1 / 2 / l
            except Exception as inst:
                print(inst.args)
                printError_msg("The three points are aligned !")
            else:
                # Normal
                Vector1 = P2 - P1
                Vector2 = P3 - P1
                V_Normal = Vector1.cross(Vector2)
                # Sphere center.
                a = P2P3**2 * (P1 - P2).dot(P1 - P3) / 2 / l**2
                b = P3P1**2 * (P2 - P1).dot(P2 - P3) / 2 / l**2
                c = P1P2**2 * (P3 - P1).dot(P3 - P2) / 2 / l**2
                P1.multiply(a)
                P2.multiply(b)
                P3.multiply(c)
                Center = P1 + P2 + P3

                Circle_User_Name, circle = plot_circle(r, Center, V_Normal, part, name, grp)
                print_msg(str(Circle_User_Name) + result_msg + "radius = " + str(r))
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def numberCircleCut(value):
    """ Respond to the change in number of cut value from the spin box.
    """
    global verbose
    msg = verbose

    try:
        # First we check if a valid number have been entered
        global m_numberCircleCut
        if str(value) == '-':
            return
        m_numberCircleCut = int(value)
        if msg != 0:
            print_msg("New number is:" + str(m_numberCircleCut))
    except ValueError:
        printError_msg("Number must be valid !")


def plot_cutCircle():
    """Create Arcs:
    Cut the selected Circle in 2(n) parts and create 2(n) Arcs.
    The number indicates in how many parts to cut.

    Original code from Mario52, 24/02/2015
    """
    global verbose
    msg = verbose
    global biColor
    red = 0

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    createFolders('WorkCircles')
    error_msg = "Unable to cut the Circle: \nSelect at least one Circle !"
    result_msg = ": is last arc created from Circle cut !"
    name = "Arc_from_circle"
    part = "Part::Feature"

    global m_numberCircleCut
    if not (m_numberCircleCut >= 2 and m_numberCircleCut <= 100):
        m_numberCircleCut = 2
    if msg != 0:
        print_msg("Number of cuts is:" + str(m_numberCircleCut))

    selection = Gui.Selection.getSelection()
    if msg != 0:
        print_msg("Number of selected objects=" + str(len(selection)))
    for piece in selection:
        if msg != 0:
            print_msg("Processing object=" + str(piece))

        if hasattr(piece, 'Name') and hasattr(piece, 'Placement'):
            label = str(piece.Name)
            circonference = 0.0
            if (label[:6] == "Circle"):
                if msg != 0:
                    print_msg("Object is Circle")

                if hasattr(piece.Shape, 'Length'):
                    circonference = piece.Shape.Length
                if circonference == 0.0:
                    printError_msg("Null circonference for this object !")
                    continue

                # Part::Part2DObject
                if (label[:6] == "Circle") and hasattr(piece, 'Radius'):
                    radius = piece.Radius
                    if len(piece.Shape.Edges) == 1:
                        edge = piece.Shape.Edges[0]
                        center = edge.Curve.Center
                        normal = edge.Curve.Axis
                    else:
                        printError_msg("No edge for this object !")
                        continue
                # Part::PartFeature
                elif (label[:6] == "Circle") and hasattr(piece.Shape, 'Curve') and hasattr(piece.Shape.Curve, 'Radius'):
                    radius = piece.Shape.Curve.Radius
                    center = piece.Shape.Curve.Center
                    normal = piece.Shape.Curve.Axis
                else:
                    printError_msg("No radius for this object !")
                    continue

                pivot1 = 0.0
                pivot0 = float(360/m_numberCircleCut)
                if msg != 0:
                    print_msg("Circonference =" + str(circonference))
                    print_msg("Radius       =" + str(radius))
                    print_msg("Center       =" + str(center))
                    print_msg("Normal       =" + str(normal))

                for i in range(m_numberCircleCut):
                    pivot2 = pivot1 + pivot0
                    if msg != 0:
                        print_msg("Start at =" + str(pivot1))
                        print_msg("End   at =" + str(pivot2))
                    Arc_User_Name, arc = plot_arc(center, normal, radius, pivot1, pivot2, part, name)
                    if biColor != 0:
                        if red == 0:
                            Gui.ActiveDocument.getObject(Arc_User_Name).LineColor = (1.0, 0.0, 0.0)
                            red = 1
                        else:
                            Gui.ActiveDocument.getObject(Arc_User_Name).LineColor = (1.0, 1.0, 1.0)
                            red = 0
                    pivot1 += pivot0

                print_msg(str(Arc_User_Name) + result_msg)
                Gui.ActiveDocument.getObject(label).Visibility = False

            elif (label[:8] == "Cylinder"):
                if msg != 0:
                    print_msg("Object is Cylinder")

                pivot0 = float(piece.Angle/m_numberCircleCut)
                printError_msg(error_msg_print_not_yet)

            elif label[:3] == "Arc":
                if msg != 0:
                    print_msg("Object is Arc")

                if hasattr(piece.Shape, 'Length'):
                    circonference = piece.Shape.Length
                if circonference == 0.0:
                    printError_msg("Null circonference for this object !")
                    continue

                # Part::Part2DObject
                if (label[:3] == "Arc") and hasattr(piece, 'Radius'):
                    radius = piece.Radius
                    if len(piece.Shape.Edges) == 1:
                        edge = piece.Shape.Edges[0]
                        center = edge.Curve.Center
                        normal = edge.Curve.Axis
                    else:
                        printError_msg("No edge for this object !")
                        continue
                    First = float(piece.FirstAngle)
                    Last = float(piece.LastAngle)
                # Part::PartFeature
                elif (label[:3] == "Arc") and hasattr(piece.Shape, 'Curve') and hasattr(piece.Shape.Curve, 'Radius'):
                    radius = piece.Shape.Curve.Radius
                    center = piece.Shape.Curve.Center
                    normal = piece.Shape.Curve.Axis
                    First = float(piece.Shape.FirstParameter)
                    Last = float(piece.Shape.LastParameter)
                    First = math.degrees(First)
                    Last = math.degrees(Last)
                else:
                    printError_msg("No radius for this object !")
                    continue

                pivot0 = abs((First - Last) / m_numberCircleCut)
                pivot1 = First
                for i in range(m_numberCircleCut):
                    pivot2 = pivot1 + pivot0
                    if msg != 0:
                        print_msg("Start at =" + str(pivot1))
                        print_msg("End   at =" + str(pivot2))
                    Arc_User_Name, arc = plot_arc(center, normal, radius, pivot1, pivot2, part, name)
                    if biColor != 0:
                        if red == 0:
                            Gui.ActiveDocument.getObject(Arc_User_Name).LineColor = (1.0, 0.0, 0.0)
                            red = 1
                        else:
                            Gui.ActiveDocument.getObject(Arc_User_Name).LineColor = (1.0, 1.0, 1.0)
                            red = 0
                    pivot1 += pivot0

                print_msg(str(Arc_User_Name) + result_msg)
                Gui.ActiveDocument.getObject(label).Visibility = False

        else:
            printError_msg(error_msg)


def plot_3pointsEllipse():
    """Select a center and 2 Points to create an Ellipse.
    """
    msg = verbose

    createFolders('WorkCircles')
    error_msg = "Unable to create a Ellipse: \nSelect one Center and 2 Points only!"
    result_msg = ": Ellipse from 3 points created !"
    name = "Ellipse"
    part = "Part::Feature"
    grp = "WorkCircles"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if (Number_of_Points == 3):
            Point_List = SelectedObjects[3]
            if msg != 0:
                print_msg(str(Point_List))
            P1 = Point_List[0].Point
            Center = P1
            P2 = Point_List[1].Point
            P3 = Point_List[2].Point
            if msg != 0:
                print_point(Center, "Center =:")
                print_point(P2, "P2 =:")
                print_point(P3, "P3 =:")

            Ellipse_User_Name, ellipse = plot_ellipse(P2, P3, Center, part, name, grp)
            print_msg(str(Ellipse_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_3PointsPlane():
    """ Plane=(3 Points):
    Create a Plane crossing 3 Points.
     - Select at least 3 Points and/or
    Select at least 2 Line/Edge(s)
    """
    msg = verbose

    error_msg = """Unable to create Plane(s):
    Select at least 3 Points and/or
    Select at least 2 Line/Edge(s) !"""
    result_msg = ": Plane(s) created !"

    createFolders('WorkPlanes')
    m_dir = 'Set'
    name = "WorkPlane"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkPoints").newObject("App::DocumentObjectGroup", str(m_dir))
    except Exception as err:
        printError_msg(err.args[0], title="plot_3PointsPlane")
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))

    try:
        Number_of_Points, Point_List = m_sel.get_points(getfrom=["Points",
                                                                 "Segments",
                                                                 "Curves",
                                                                 "Objects"])
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))

        points = []
        m_i = 0
        if Number_of_Points < 3:
            printError_msg(error_msg)

        for m_i in xrange(0, Number_of_Points, 3):
            if m_i+1 > Number_of_Points or m_i+2 > Number_of_Points:
                break
            Point_A = Point_List[m_i+0].Point
            points.append(Point_A)
            Point_B = Point_List[m_i+1].Point
            points.append(Point_B)
            Point_C = Point_List[m_i+2].Point
            points.append(Point_C)
            if msg != 0:
                print_point(Point_A, msg="Point_A: ")
                print_point(Point_B, msg="Point_B: ")
                print_point(Point_C, msg="Point_C: ")

            Vector_Center = meanVectorsPoint(points, info=msg)
            #Vector_Center = centerBBVectorsPoint(points, info=0)
            xmax, xmin, ymax, ymin, zmax, zmin = minMaxVectorsLimits(points, info=0)
            # print_point(Vector_Center, msg="Center of A, B and C: ")

            length = xmax - xmin
            if (ymax - ymin) > length:
                length = ymax - ymin
            if (zmax - zmin) > length:
                length = zmax - zmin
            print_msg("length = " + str(length))

            Edge_Vector = Point_B - Point_A
            # Edge_Length = Edge_Vector.Length
            Edge_Length = length * 1.5
            AC_Vector = Point_C - Point_A
            Plane_Point = Vector_Center
            Plane_Normal = Edge_Vector.cross(AC_Vector)

            Plane_User_Name, plane = plot_plane(Edge_Length, Edge_Length, Plane_Point, Plane_Normal, part, name, str(m_dir))
            print_msg(str(Plane_User_Name) + result_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_3PointsPlane_old():
    """ Create a Plane from 3 Points.
    """
    msg = verbose

    createFolders('WorkPlanes')
    error_msg = "Unable to create Plane: \nSelect three points only !"
    result_msg = ": Plane created !"
    name = "WorkPlane"
    part = "Part::Feature"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
        points = []
        if Number_of_Points == 3:
            Point_List = SelectedObjects[3]
            if msg != 0:
                print_msg(str(Points_List))

            Point_A = Point_List[0].Point
            points.append(Point_A)
            Point_B = Point_List[1].Point
            points.append(Point_B)
            Point_C = Point_List[2].Point
            points.append(Point_C)
            if msg != 0:
                print_point(Point_A, msg="Point_A: ")
                print_point(Point_B, msg="Point_B: ")
                print_point(Point_C, msg="Point_C: ")

            Vector_Center = meanVectorsPoint(points, info=msg)
            #Vector_Center = centerBBVectorsPoint(points, info=0)
            xmax, xmin, ymax, ymin, zmax, zmin = minMaxVectorsLimits(points, info=0)
            # print_point(Vector_Center, msg="Center of A, B and C: ")

            length = xmax - xmin
            if (ymax - ymin) > length:
                length = ymax - ymin
            if (zmax - zmin) > length:
                length = zmax - zmin
            print_msg("length = " + str(length))

            Edge_Vector = Point_B - Point_A
            # Edge_Length = Edge_Vector.Length
            Edge_Length = length * 1.5
            AC_Vector = Point_C - Point_A
            Plane_Point = Vector_Center
            Plane_Normal = Edge_Vector.cross(AC_Vector)

            Plane_User_Name, plane = plot_plane(Edge_Length, Edge_Length, Plane_Point, Plane_Normal, part, name)
            print_msg(str(Plane_User_Name) + result_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_2PointsPlane():
    """ Create a Plane from 2 Points.
    """
    msg = verbose

    createFolders('WorkPlanes')
    error_msg = "Unable to create Plane: \nSelect two points only !"
    result_msg = ": Plane created !"
    name = "WorkPlane"
    part = "Part::Feature"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
        points = []
        if Number_of_Points == 2:
            Point_List = SelectedObjects[3]
            if msg != 0:
                print_msg(str(Points_List))

            Point_A = Point_List[0].Point
            points.append(Point_A)
            Point_B = Point_List[1].Point
            points.append(Point_B)
            if msg != 0:
                print_point(Point_A, msg="Point_A: ")
                print_point(Point_B, msg="Point_B: ")

            Vector_Center = meanVectorsPoint(points, info=msg)
            #Vector_Center = centerBBVectorsPoint(points, info=0)
            xmax, xmin, ymax, ymin, zmax, zmin = minMaxVectorsLimits(points, info=0)
            # print_point(Vector_Center, msg="Center of A, B and C: ")

            length = xmax - xmin
            if (ymax - ymin) > length:
                length = ymax - ymin
            if (zmax - zmin) > length:
                length = zmax - zmin
            print_msg("length = " + str(length))

            Edge_Vector = Point_B - Point_A
            # Edge_Length = Edge_Vector.Length
            Edge_Length = length * 1.5
            Plane_Point = Vector_Center
            Plane_Normal = Edge_Vector

            Plane_User_Name, plane = plot_plane(Edge_Length, Edge_Length, Plane_Point, Plane_Normal, part, name)
            print_msg(str(Plane_User_Name) + result_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_NPointsPlane():
    """Create a "best fit" Plane from a set of points using Singular Value Decomposition.
    - First select several Points (at least 3).
    """
    msg = verbose

    try:
        import numpy as np
    except Exception as inst:
        print(inst.args)
        error_msg = "Unable to import numpy !\n" +\
        "You MUSt install numpy to use this function !"
        printError_msg(error_msg)

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    createFolders('WorkPlanes')
    error_msg = "Unable to create Plane: \nSelect at least three points!"
    result_msg = ": Plane created !"
    name = "Plane_from_N_Points"
    part = "Part::Feature"
    grp = "WorkPlanes"

    Selection = get_SelectedObjects(info=msg, printError=False)

    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
        if Number_of_Points > 2:
            m_x = []
            m_y = []
            m_z = []
            Point_List = SelectedObjects[3]
            if msg != 0:
                print_msg("Point_List=" + str(Point_List))
            for Selected_Point in Point_List:
                m_point = Selected_Point.Point
                if msg != 0:
                    print_point(m_point, "Point selected:")
                m_x.append(m_point.x)
                m_y.append(m_point.y)
                m_z.append(m_point.z)

            m_np_x = np.asfarray(m_x)
            m_np_y = np.asfarray(m_y)
            m_np_z = np.asfarray(m_z)
            if msg != 0:
                print_msg(" m_np_x=" + str(m_np_x))
                print_msg(" m_np_y=" + str(m_np_y))
                print_msg(" m_np_z=" + str(m_np_z))
            m_data = np.concatenate((m_np_x[:, np.newaxis],
                        m_np_y[:, np.newaxis],
                        m_np_z[:, np.newaxis]),
                        axis=1)
            if msg != 0:
                print_msg(" m_data=" + str(m_data))
            # Calculate the mean of the points, i.e. the 'center' of the cloud
            m_datamean = m_data.mean(axis=0)
            if msg != 0:
                print_msg(" m_datamean=" + str(m_datamean))
            Axis_E0 = Base.Vector(m_datamean[0], m_datamean[1], m_datamean[2])
            Plane_Point = Axis_E0

            # Do an SVD on the mean-centered data.
            m_uu, m_dd, m_vv = np.linalg.svd(m_data - m_datamean)
            if msg != 0:
                print_msg(" m_uu=" + str(m_uu))
                print_msg(" m_dd=" + str(m_dd))
                print_msg(" m_vv=" + str(m_vv))
            # Now vv[0] contains the first principal component, i.e. the direction
            # vector of the 'best fit' line in the least squares sense.
            Axis_dir1 = Base.Vector(m_vv[0][0], m_vv[0][1], m_vv[0][2])
            Axis_E1 = Axis_E0 - Axis_dir1.normalize().multiply(m_dd[0]/2.)
            Axis_E2 = Axis_E0 + Axis_dir1.normalize().multiply(m_dd[0]/2.)
            Axis_dir2 = Base.Vector(m_vv[1][0], m_vv[1][1], m_vv[1][2])
            Plane_Normal = Axis_dir1.cross(Axis_dir2)
            Edge_Length = m_dd[0]
            Plane_User_Name, plane = plot_plane(Edge_Length, Edge_Length, Plane_Point, Plane_Normal, part, name)
            print_msg(str(Plane_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_axisPointPlane():
    """ Create a plane passing trougth a Line and a Point.
    """
    global verbose
    msg = verbose

    createFolders('WorkPlanes')
    error_msg = "Unable to create Plane: \nSelect one Line and one Point only, \nwith the Point NOT on the Line !"
    result_msg = ": Plane created !"
    name = "WorkPlane"
    part = "Part::Feature"

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg("Number_of_Points = " + str(Number_of_Points) + \
                      "\nNumber_of_Edges = " + str(Number_of_Edges))
        points = []
        if (Number_of_Points == 1) and (Number_of_Edges == 1):
            Points_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg("Point list = " + str(Points_List))
                print_msg("Edge list = " + str(Edge_List))
            Point_C = Points_List[0].Point
            points.append(Point_C)
            Point_A = Edge_List[0].valueAt(0.0)
            points.append(Point_A)
            Point_B = Edge_List[0].valueAt(Edge_List[0].Length)
            points.append(Point_B)
            if msg != 0:
                print_point(Point_A, msg="Point_A: ")
                print_point(Point_B, msg="Point_B: ")
                print_point(Point_C, msg="Point_C: ")

            #Vector_Center = centerBBVectorsPoint(points, info=0)
            Vector_Center = meanVectorsPoint(points, info=msg)
            xmax, xmin, ymax, ymin, zmax, zmin = minMaxVectorsLimits(points, info=msg)
            # print_point(Vector_Center, msg="Center of A, B and C: ")

            length = xmax - xmin
            if (ymax - ymin) > length:
                length = ymax - ymin
            if (zmax - zmin) > length:
                length = zmax - zmin
            print_msg("length = " + str(length))

            Edge_Vector = Point_B - Point_A
            Edge_Length = length * 1.5
            AC_Vector = Point_C - Point_A
            Plane_Point = Vector_Center
            Plane_Normal = Edge_Vector.cross(AC_Vector)

            Plane_User_Name, plane = plot_plane(Edge_Length, Edge_Length, Plane_Point, Plane_Normal, part, name)
            print_msg(str(Plane_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_perpendicularAxisPointPlane():
    """ Create a Plane perpendicular to a Line a crossing a Point.
    """
    msg = verbose

    createFolders('WorkPlanes')
    error_msg = "Unable to create Plane: \nSelect one Line and one point only !"
    result_msg = ": Plane created !"
    name = "WorkPlane"
    part = "Part::Feature"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        # print_msg("Number_of_Points=" + str(Number_of_Points) + " Number_of_Edges=" + str(Number_of_Edges))
        if (Number_of_Points == 1) and (Number_of_Edges == 1):
            Point_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]
            Vector_A = Edge_List[0].valueAt(0.0)
            Vector_B = Edge_List[0].valueAt(Edge_List[0].Length)
            Vector_C = Point_List[0].Point
            # print_point(Vector_A, msg="Vector_A: ")
            # print_point(Vector_B, msg="Vector_B: ")
            # print_point(Vector_C, msg="Vector_C: ")
            # Intersection point T on a Line given one Line and One Point C.
            if colinearVectors(Vector_A, Vector_B, Vector_C, info=1):
                Vector_T = Vector_C
                Distance = Edge_List[0].Length
            else:
                Vector_T, Distance, Vector_Tprime = intersecPerpendicularLine(Vector_A, Vector_B, Vector_C, info=0)
            # print_point(Vector_T, msg="Intersection point T: ")
            Plane_Normal = Vector_B - Vector_A
            Plane_Point = Vector_T + (Vector_C - Vector_T).multiply(0.5)
            Edge_Length = Distance * 1.5

            Plane_User_Name, plane = plot_plane(Edge_Length, Edge_Length, Plane_Point, Plane_Normal, part, name)
            print_msg(str(Plane_User_Name) + result_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def extensionPlanePointPlane(value):
    """ Respond to the change in extension value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_extensionPlanePointPlane
        if str(value) == '-':
            return
        m_extensionPlanePointPlane = float(value)
        print_msg("New extension is:" + str(m_extensionPlanePointPlane))
    except ValueError:
        printError_msg("Extension must be valid number !")


def plot_planePointPlane():
    """ Create a plane passing through a Point and parallel to a given Plane.
    """
    msg = verbose

    createFolders('WorkPlanes')
    error_msg = "Unable to create Plane: \nSelect one Plane and one Point only !"
    result_msg = ": Plane created !"
    name = "WorkPlane"
    part = "Part::Feature"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Planes = SelectedObjects[2]

        # print_msg("Number_of_Points=" + str(Number_of_Points) + " Number_of_Planes=" + str(Number_of_Planes))
        if Number_of_Points == 1 and Number_of_Planes == 1:
            Points_List = SelectedObjects[3]
            Plane_List = SelectedObjects[5]
            # print_msg(str(Points_List))
            # print_msg(str(Plane_List))
            Point_C = Points_List[0].Point
            Reference_Plane = Plane_List[0]
            Edge_Length = Reference_Plane.Length / 4.0 + m_extensionPlanePointPlane
            Plane_Normal = Reference_Plane.normalAt(0, 0)
            Plane_Point = Point_C

            Plane_User_Name, plane = plot_plane(Edge_Length, Edge_Length, Plane_Point, Plane_Normal, part, name)
            print_msg(str(Plane_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def anglePlaneAxisPlane(value):
    """ Respond to the change in angle value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_anglePlaneAxisPlane
        if str(value) == '-':
            return
        m_anglePlaneAxisPlane = float(value)
        print_msg("New angle in degrees is:" + str(m_anglePlaneAxisPlane))
    except ValueError:
        printError_msg("Angle must be valid number !")


def plot_planeAxisPlane():
    """ Use a plane and a line to create Plane perpedicular 
    to the first Plane and crossing the Line
    """
    msg = verbose

    createFolders('WorkPlanes')
    error_msg = "Unable to create Planes: \nSelect one Line and one Plane only !"
    result_msg = ": Plane created !"
    name = "WorkPlane"
    part = "Part::Feature"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        #Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        Number_of_Planes = SelectedObjects[2]
        # print_msg("Number_of_Points=" + str(Number_of_Points))
        # print_msg("Number_of_Edges=" + str(Number_of_Edges) + " Number_of_Planes=" + str(Number_of_Planes))
        if Number_of_Planes == 1 and Number_of_Edges == 1:
            Edge_List = SelectedObjects[4]
            Plane_List = SelectedObjects[5]
            Point_A = Edge_List[0].valueAt(0.0)
            Point_B = Edge_List[0].valueAt(Edge_List[0].Length)
            # print_point(Point_A, msg="Point_A: ")
            # print_point(Point_B, msg="Point_B: ")
            Selected_Plane = Plane_List[0]
            Plane_Point = Selected_Plane.CenterOfMass
            Plane_Normal = Selected_Plane.normalAt(0, 0)
            # Projection of A and B onto the Plane Aprime and Bprime
            Vector_A = Point_A + Plane_Normal
            Vector_B = Point_B + Plane_Normal

            Point_Aprime = intersecLinePlane(Point_A, Vector_A, Plane_Normal, Plane_Point, info=0)
            Point_Bprime = intersecLinePlane(Point_B, Vector_B, Plane_Normal, Plane_Point, info=0)
            # Plot them
            # plot_point(Point_Aprime, part, "PointFacePoint")
            # plot_point(Point_Bprime, part, "PointFacePoint")
            # plot_axis(Point_Aprime, Point_Bprime, part, "Line from 2 Points")

            Edge_Vector = Point_Bprime - Point_Aprime
            Edge_Length = Edge_List[0].Length * 1.3

            Point_MidPoint = Point_Bprime + Point_Aprime
            Point_MidPoint = Point_MidPoint.multiply(0.5)

            Vector_Normal = Edge_Vector.cross(Plane_Normal)

            Plane_User_Name, plane = plot_plane(Edge_Length, Edge_Length, Point_MidPoint, Vector_Normal, part, name)

            print_msg("New plane is:" + str(plane))
            if m_anglePlaneAxisPlane != 0.0:
                rot_angle = m_anglePlaneAxisPlane
                rot_axis = Edge_Vector
                m_center = Point_MidPoint
                m_rot = App.Rotation(rot_axis, rot_angle)
                print_msg("rotation =       " + str(m_rot))
                print_msg("rotation axis  = " + str(rot_axis))
                m_place = App.Placement(plane.Placement)
                m_base1 = m_place.Base
                print_msg("base1  = " + str(m_base1))
                m_rot1 = m_place.Rotation
                print_msg("rot1  = " + str(m_rot1))
                m_rot = m_rot.multiply(m_rot1)
                m_newplace = App.Placement(m_base1, m_rot, m_center-m_base1)
                plane.Placement = m_newplace

            print_msg(str(Plane_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def numberPlane(value):
    """ Respond to the change in number of plane from the spin box.
    """
    global verbose
    msg = verbose

    try:
        # First we check if a valid number have been entered
        global m_numberPlane
        if str(value) == '-':
            return
        m_numberPlane = int(value)
        if m_numberPlane == 0:
            m_numberPlane = 1
        if msg != 0:
            print_msg("New number is:" + str(m_numberPlane))
    except ValueError:
        printError_msg("Number must be valid !")


def distPlane(value):
    """ Respond to the change in Distance between plane value from the text box.
    """
    global verbose
    msg = verbose

    try:
        # First we check if a valid number have been entered
        global m_distPlane
        if str(value) == '-':
            return
        m_distPlane = float(value)
        if msg != 0:
            print_msg("New Distance between plane is:" + str(m_distPlane))
    except ValueError:
        printError_msg("Distance between plane must be valid number !")


def plot_distPlane():
    """ Plane=(Plane,dist):
        Create a Plane parallel to a Plane at a given distance.
        - First select a plane or several Planes

        NB: The distance to the plane created can be defined first.
        Positive number in one direction and negative in the other one.
        The second number indicates the number of planes to create.

        If a Face of a Cube is selected the Cube is duplicate with the corresponding
        Face at the defined distance from the original.
    """
    global verbose
    global objCopy
    global m_numberPlane
    global m_distPlane
    msg = verbose

    createFolders('WorkPlanes')
    error_msg = "Unable to create Plane(s): \nSelect at least one Plane !"
    result_msg = ": Plane(s) created !"

    Selection = get_SelectedObjectsWithParent(info=msg, printError=False)

    try:
        SelectedObjects = Selection
        Number_of_Planes = SelectedObjects[2]

        if Number_of_Planes >= 1:
            Plane_List = SelectedObjects[5]
            if msg != 0:
                print_msg("Number_of_Planes = " + str(Number_of_Planes))
                print_msg("Plane list = " + str(Plane_List))

            for Selected_Plane_dict in Plane_List:
                if msg != 0:
                    print_msg("Selected_Plane_dict = " + str(Selected_Plane_dict))
                for Selected_Plane, Parent_Plane in Selected_Plane_dict.iteritems():
                    if msg != 0:
                        print_msg("Selected_Plane = " + str(Selected_Plane))
                        print_msg("Parent = " + str(Parent_Plane))
                    Plane_Point = Selected_Plane.CenterOfMass
                    Plane_Normal = Selected_Plane.normalAt(0, 0)
                    if msg != 0:
                        print_point(Plane_Point, msg="Plane_Point = ")
                        print_point(Plane_Normal, msg="Plane_Normal = ")
                    Placement1 = Selected_Plane.Placement
                    base1 = Placement1.Base
                    rot1 = Placement1.Rotation
                    New_Point = Plane_Point + Plane_Normal.normalize().multiply(m_distPlane)
                    m_move = New_Point.sub(Plane_Point)
                    if msg != 0:
                        print_point(New_Point, msg="New_Point = ")
                        print_point(m_move, msg="m_move = ")
                        print_msg("m_numberPlane = " + str(m_numberPlane))

                    for m_i in range(m_numberPlane):
                        if objCopy == 1:
                            m_new_plane = App.activeDocument().copyObject(Parent_Plane)
                        else:
                            m_new_plane_shape = Selected_Plane.copy()
                            m_new_plane = App.ActiveDocument.addObject("Part::Feature", "Plane_at_distance")
                            m_new_plane.Shape = m_new_plane_shape
                        App.ActiveDocument.getObject('WorkPlanes').addObject(m_new_plane)
                        Plane_User_Name = m_new_plane.Label
                        if msg != 0:
                            print_msg("m_new_plane = " + str(m_new_plane))
                            print_msg("Plane_User_Name = " + str(Plane_User_Name))

                        newplace1 = App.Placement(base1.add(m_move), rot1)
                        m_new_plane.Placement = newplace1
                        # Update the move
                        m_move = m_move.add(New_Point.sub(Plane_Point))

                        properties_plane(Plane_User_Name)

                        print_msg(str(Plane_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def lengthPlane(value):
    """ Respond to the change in Plane length value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_lengthPlane
        if str(value) == '-':
            return
        m_lengthPlane = float(value)
        print_msg("New Plane length is:" + str(m_lengthPlane))
    except ValueError:
        printError_msg("Plane length must be valid number !")


def widthPlane(value):
    """ Respond to the change in Plane length value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_widthPlane
        if str(value) == '-':
            return
        m_widthPlane = float(value)
        print_msg("New Plane length is:" + str(m_widthPlane))
    except ValueError:
        printError_msg("Plane length must be valid number !")


def plot_faceTangentPlane():
    """Create a tangent Plane at click location of a Face.
    """
    global m_callback
    view = Gui.ActiveDocument.ActiveView
    m_callback = view.addEventCallback("SoMouseButtonEvent", getClickedTangent)


def plot_clickForPlane():
    """ Create a Plane at location of one mouse click in the view or
    onto a clicked object or
    at a pre-selected point location:
    Create a Plane perpendicular to the view at location of one mouse click.
    - Click first on the Button then click once on the View.
    - Click first on the Button then click once on one object of the View
    to attach the plane at the object.
    But you can also select an already existing point first and click the button
    to attach the plane.
    """
    msg = verbose

    createFolders('WorkPlanes')

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if len(m_selEx) >= 1:
        SelectedObjects = get_SelectedObjects(info=1)
        Number_of_Points = SelectedObjects[0]
        if (Number_of_Points == 1):
            Point_List = SelectedObjects[3]
            name = "Plane"
            part = "Part::Feature"
            # return view direction as a vector
            Plane_Normal = Gui.ActiveDocument.ActiveView.getViewDirection()
            # Set the base of the plane at location of mouse click
            Plane_Point = Point_List[-1].Point
            # Create a Plane
            Plane_User_Name, plane = plot_plane(m_lengthPlane, m_widthPlane, Plane_Point, Plane_Normal, part, name)
        else:
            printError_msg("Either select first one Point and Click the button or \n" +
              "Click the button and one free mouse click in the view or" +
              "Click the button and one mouse click on an object of the view !")
    else:
        global m_callback
        #view = Gui.ActiveDocument.ActiveView
        view = get_ActiveView()
        # m_callback = view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(),getClickedPlane)
        m_callback = view.addEventCallback("SoMouseButtonEvent", getClickedPlane2)


def extensionPlane(value):
    """ Respond to the change in Plane extension value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_extensionPlane
        m_extensionPlane = float(value)
        print_msg("New Plane extension is:" + str(m_extensionPlane))
    except ValueError:
        printError_msg("Plane extension must be valid number 5percentage)!")


def plot_extensionPlane():
    """ Extend a Plane in each dimension, based on a percentage.
    """
    global verbose
    msg = verbose

    createFolders('WorkPlanes')
    error_msg = "Unable to create Plane: \nSelect Plane(s) only !"
    result_msg = ": Plane created !"
    name = "Plane_extended"
    part = "Part::Feature"
    global m_extensionPlane
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Planes = SelectedObjects[2]
        if msg != 0:
            print_msg("Number_of_Planes=" + str(Number_of_Planes))
        if (Number_of_Planes) >= 1:
            Plane_List = SelectedObjects[5]
            if msg != 0:
                print_msg("Plane_List=" + str(Plane_List))
            for Selected_Plane in Plane_List:
                if msg != 0:
                    print_msg("Selected_Plane=" + str(Selected_Plane))
                Plane_Normal = Selected_Plane.normalAt(0, 0)
                Plane_Point = Selected_Plane.CenterOfMass
                max_val, min_val = init_min_max()
                for edge in Selected_Plane.Edges:
                    if msg != 0:
                        print_msg("edge=" + str(edge))
                        print_msg("edge.Length=" + str(edge.Length))
                    min_val = min(min_val, edge.Length)
                    max_val = max(max_val, edge.Length)
                    if msg != 0:
                        print_msg("min_val=" + str(min_val))
                        print_msg("max_val=" + str(max_val))
                min_val = min_val * (1 + (m_extensionPlane/50))
                max_val = max_val * (1 + (m_extensionPlane/50))
                Plane_User_Name, plane = plot_plane(min_val, max_val, Plane_Point, Plane_Normal, part, name)
                print_msg(str(Plane_User_Name) + result_msg)
    except Exception as inst:
        print(inst.args)
        printError_msg(error_msg)


def plot_clickForPlane2():
    """ A circular plane is created facing the screen to mouse click coordinates 
    on an object.
    The radius of the plane is equal to the maximum dimension of BoundBox.
    If no object is selected, the plane is created to 0, 0, 0 coordinates with 
    a radius of 20 mm
    """
    msg = verbose

    createFolders('WorkPlanes')

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None
    m_radius = 20
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    m_objs = [selobj.Object for selobj in m_selEx]

    for m_obj in m_objs:
        if hasattr(m_obj, 'Shape'):
            s = m_obj.Shape
            m_bbox = s.BoundBox
            m_radius = m_bbox.XLength
            if m_radius < m_bbox.YLength:
                m_radius = m_bbox.YLength
            elif m_radius < m_bbox.ZLength:
                m_radius = m_bbox.ZLength

    if msg != 0:
        print_msg("Create plane (" + str(m_radius) + " mm)")

    pl = App.Placement()
    pl.Rotation = Gui.ActiveDocument.ActiveView.getCameraOrientation()


    printError_msg(error_msg)
    return



    # TODO to complete
    FcPlane = doc.addObject("App::DocumentObjectGroup", "FcPlane")
    plan = Gui.ActiveDocument.ActiveView.getCameraOrientation()
    xP = float(datExtract(plan)[0])
    yP = float(datExtract(plan)[1])
    zP = float(datExtract(plan)[2])
    qP = float(datExtract(plan)[3])
    pl = App.Placement()
    pl.Rotation.Q = (xP, yP, zP, qP)         # rotation of object

    pl.Base = App.Vector(positionX, positionY, positionZ) # here coordinates XYZ of plan
    points = [App.Vector(-(radiusP*1.5), 0, 0), App.Vector((radiusP*1.5), 0, 0)]
    mire01 = Draft.makeWire(points, closed=False, placement=pl, face=False, support=None)
    Gui.ActiveDocument.getObject(App.ActiveDocument.ActiveObject.Name).LineColor = (1.0, 0.0, 0.0)
    FcPlane.addObject(mire01)  # container character

    points = [App.Vector(0, -(radiusP*1.5), 0), App.Vector(0, (radiusP*1.5), 0)]
    mire02 = Draft.makeWire(points, closed=False, placement=pl, face=False, support=None)
    Gui.ActiveDocument.getObject(App.ActiveDocument.ActiveObject.Name).LineColor = (1.0, 0.0, 0.0)
    FcPlane.addObject(mire02)  # container character

    cercle = Draft.makeCircle(radius=radiusP, placement=pl, face=False, support=None)
    Rnameplane = App.ActiveDocument.ActiveObject.Name

    App.ActiveDocument.ActiveObject.Label  = "PlaneC"
    App.ActiveDocument.getObject(Rnameplane).MakeFace = True
    Gui.ActiveDocument.getObject(Rnameplane).LineColor = (1.0, 0.0, 0.0)
    Gui.ActiveDocument.getObject(Rnameplane).ShapeColor = (0.0, 0.66666669, 1.0)
    Gui.ActiveDocument.getObject(Rnameplane).Transparency = 80
    Gui.ActiveDocument.getObject(Rnameplane).GridSize = '10 mm'
#        Gui.ActiveDocument.getObject(Rnameplane).GridSnap = True
    Gui.ActiveDocument.getObject(Rnameplane).ShowGrid = True

    FcPlane.addObject(cercle)  # container character
    App.ActiveDocument.recompute()

    positionX = 0.0
    positionY = 0.0
    positionZ = 0.0


def plot_centerObjectPlanes():
    """ Create 3 Planes XY, YZ and XZ at center point of all selected objects.
    """
    msg = verbose

    createFolders('WorkPlanes')
    error_msg = "Unable to create Planes: \nSelect at least one object !"
    result_msg = ": Planes created !"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    Line_Color = (1.00, 0.33, 0.00)
    Shape_Color =  (0.00, 1.00, 0.50)
    Transparency = 75
    # Return a list of SelectionObjects for a given document name.
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    m_objs = [selobj.Object for selobj in m_selEx]
    m_num = len(m_objs)
    if m_num < 1:
        printError_msg(error_msg)
        return
    Center = centerObjectsPoint(m_objs)
    if Center is not None:
        xmax, xmin, ymax, ymin, zmax, zmin = minMaxObjectsLimits(m_objs, info=1)

        # Work-PlaneXY
        if xmax != xmin:
            PXY_A_SIZE = (xmax - xmin) * 1.3
        else:
            PXY_A_SIZE = 10.
        if PXY_A_SIZE < (ymax - ymin) * 1.3:
            PXY_A_SIZE = (ymax - ymin) * 1.3
        PXY_A = Center + Base.Vector(PXY_A_SIZE, PXY_A_SIZE, 0)
        PXY_B = PXY_A + Base.Vector(-2.0 * PXY_A_SIZE, 0, 0)
        PXY_C = PXY_A + Base.Vector(-2.0 * PXY_A_SIZE, -2.0 * PXY_A_SIZE, 0)
        PXY_D = PXY_A + Base.Vector(0, -2.0 * PXY_A_SIZE, 0)
        PlaneXY_list = [PXY_A, PXY_B, PXY_C, PXY_D, PXY_A]
        PlaneXY_wire = Part.makePolygon(PlaneXY_list)
        PlaneXY_face = Part.Face(PlaneXY_wire)
        PlaneXY = App.ActiveDocument.addObject("Part::Feature", "XY_WPlane")
        PlaneXY.Shape = PlaneXY_face
        App.ActiveDocument.getObject("WorkPlanes").addObject(PlaneXY)
        PlaneXY_User_Name = PlaneXY.Label
        Gui.ActiveDocument.getObject(PlaneXY_User_Name).PointColor = Line_Color
        Gui.ActiveDocument.getObject(PlaneXY_User_Name).LineColor = Line_Color
        Gui.ActiveDocument.getObject(PlaneXY_User_Name).ShapeColor = Shape_Color
        Gui.ActiveDocument.getObject(PlaneXY_User_Name).Transparency = Transparency
        Gui.ActiveDocument.getObject(PlaneXY_User_Name).Visibility = True
        # Gui.ActiveDocument.getObject("XY_WPlane").Visibility=True
        print_msg(str(PlaneXY_User_Name) + result_msg)
        # Work-PlaneXZ
        if xmax != xmin:
            PXZ_A_SIZE = (xmax - xmin) * 1.3
        else:
            PXZ_A_SIZE = 10.
        if PXZ_A_SIZE < (zmax - zmin) * 1.3:
            PXZ_A_SIZE = (zmax - zmin) * 1.3
        PXZ_A = Center + Base.Vector(PXZ_A_SIZE, 0, PXZ_A_SIZE)
        PXZ_B = PXZ_A + Base.Vector(-2.0 * PXZ_A_SIZE, 0, 0)
        PXZ_C = PXZ_A + Base.Vector(-2.0 * PXZ_A_SIZE, 0, -2.0 * PXZ_A_SIZE)
        PXZ_D = PXZ_A + Base.Vector(0, 0, -2.0 * PXZ_A_SIZE)
        PlaneXZ_list = [PXZ_A, PXZ_B, PXZ_C, PXZ_D, PXZ_A]
        PlaneXZ_wire = Part.makePolygon(PlaneXZ_list)
        PlaneXZ_face = Part.Face(PlaneXZ_wire)
        PlaneXZ = App.ActiveDocument.addObject("Part::Feature", "XZ_WPlane")
        PlaneXZ.Shape = PlaneXZ_face
        App.ActiveDocument.getObject("WorkPlanes").addObject(PlaneXZ)
        PlaneXZ_User_Name = PlaneXZ.Label
        Gui.ActiveDocument.getObject(PlaneXZ_User_Name).PointColor = Line_Color
        Gui.ActiveDocument.getObject(PlaneXZ_User_Name).LineColor = Line_Color
        Gui.ActiveDocument.getObject(PlaneXZ_User_Name).ShapeColor = Shape_Color
        Gui.ActiveDocument.getObject(PlaneXZ_User_Name).Transparency = Transparency
        Gui.ActiveDocument.getObject(PlaneXZ_User_Name).Visibility = True
        # Gui.ActiveDocument.getObject("XZ_WPlane").Visibility=True
        print_msg(str(PlaneXZ_User_Name) + result_msg)
        # Work-PlaneZY
        if zmax != zmin:
            PYZ_A_SIZE = (zmax - zmin) * 1.3
        else:
            PYZ_A_SIZE = 10
        if PYZ_A_SIZE < (ymax - ymin) * 1.3:
            PYZ_A_SIZE = (ymax - ymin) * 1.3
        PYZ_A = Center + Base.Vector(0, PYZ_A_SIZE, PYZ_A_SIZE)
        PYZ_B = PYZ_A + Base.Vector(0, -2.0 * PYZ_A_SIZE, 0)
        PYZ_C = PYZ_A + Base.Vector(0, -2.0 * PYZ_A_SIZE, -2.0 * PYZ_A_SIZE)
        PYZ_D = PYZ_A + Base.Vector(0, 0, -2.0 * PYZ_A_SIZE)
        PlaneYZ_list = [PYZ_A, PYZ_B, PYZ_C, PYZ_D, PYZ_A]
        PlaneYZ_wire = Part.makePolygon(PlaneYZ_list)
        PlaneYZ_face = Part.Face(PlaneYZ_wire)
        PlaneYZ = App.ActiveDocument.addObject("Part::Feature", "YZ_WPlane")
        PlaneYZ.Shape = PlaneYZ_face
        App.ActiveDocument.getObject("WorkPlanes").addObject(PlaneYZ)
        PlaneYZ_User_Name = PlaneYZ.Label
        Gui.ActiveDocument.getObject(PlaneYZ_User_Name).PointColor = Line_Color
        Gui.ActiveDocument.getObject(PlaneYZ_User_Name).LineColor = Line_Color
        Gui.ActiveDocument.getObject(PlaneYZ_User_Name).ShapeColor = Shape_Color
        Gui.ActiveDocument.getObject(PlaneYZ_User_Name).Transparency = Transparency
        Gui.ActiveDocument.getObject(PlaneYZ_User_Name).Visibility = True
        # Gui.ActiveDocument.getObject("YZ_WPlane").Visibility=True
        print_msg(str(PlaneYZ_User_Name) + result_msg)
    else:
        printError_msg(error_msg)


def plot_wire_on_plane():
    """Projects Wires on a Plane:

    - First select an existing Face/Plane  or 3 Points
    - Second one or several Wires
    - Then push this button
    from original Macro: FlattenWire3Points
    Author: Yorik
    """
    msg = verbose

    error_msg = """Unable to projection of Wires:
    Select an existing Face/Plane  or 3 Points and then
    Select one or several Wires!"""
    result_msg = ": Projection of Wire(s) created !"

    createFolders('WorkWires')
    m_dir = 'Set'
    name = "ProjectedWire"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkWires").newObject("App::DocumentObjectGroup", str(m_dir))
    except:
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))

    try:
        Number_of_Planes, Plane_List = m_sel.get_planes()
        if msg != 0:
            print_msg("Number_of_Planes=" + str(Number_of_Planes))
        if Number_of_Planes >= 1:
            plane = Plane_List[0]
            if msg != 0:
                print_msg(str(plane))

    except:
        printError_msg(error_msg)
    # define a plane
#     p1 = getattr(sel.Object.Shape,sel.SubElementNames[0]).Point
#     p2 = getattr(sel.Object.Shape,sel.SubElementNames[1]).Point
#     p3 = getattr(sel.Object.Shape,sel.SubElementNames[2]).Point
#     p4 = p2.sub(p1).cross(p3.sub(p1))
#
#     # project wire points
#     points = []
#     for p in sel.Object.Points:
#         points.append(p.projectToPlane(p1,p4))
#     sel.Object.Points = points


def plot_bezier():
    pass

def points_toPolygon():
    """ Create a polygon from a set of points.
    - First select several Points (at least 2).
    
    """
    msg = verbose
    m_close = False
    m_face = False

    error_msg = """Unable to create Polygon:
    Select at least 2 points !"""
    result_msg = ": Polygon created !"

    createFolders('WorkWires')
    m_dir = 'Set'
    name = "Polygon_from_N_Points"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkWires").newObject("App::DocumentObjectGroup", str(m_dir))
    except:
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    Selection = get_SelectedObjects(info=msg, printError=False)

    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
        if Number_of_Points > 1:
            m_x = 0.0
            m_y = 0.0
            m_z = 0.0
            matriz = []
            Point_List = SelectedObjects[3]
            if msg != 0:
                print_msg("Point_List=" + str(Point_List))

            for Selected_Point in Point_List:
                m_point = Selected_Point.Point
                m_x = m_point.x
                m_y = m_point.y
                m_z = m_point.z
                matriz.append(FreeCAD.Vector(m_x, m_y, m_z))

            curve_User_Name, curve = plot_curve(matriz, m_close, m_face, part, name, str(m_dir))
            # curve_User_Name, curve = plot_polygon(matriz, part, name, str(m_dir))
            print_msg(str(curve_User_Name) + result_msg + " into:" + str(m_dir))
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)

def sel_projection2(*argc):
    """ Projection plane by combo box.
    Options:
    All
    XY plane
    YZ plane
    XZ plane
    """
    global m_projection_plane2
    global verbose
    msg = verbose

    if msg != 0:
        print_msg("Projection plane location by combo box !")
    m_projection_plane2 = "All"
    if str(*argc) == "XY plane":
        m_projection_plane2 = "XY"
    if str(*argc) == "YZ plane":
        m_projection_plane2 = "YZ"
    if str(*argc) == "XZ plane":
        m_projection_plane2 = "XZ"

    if msg != 0:
        print_msg("argc is " + str(*argc) + " and Projection plane " + str(m_attach_point) + " selected !")



def Plot_convex2Dpolygon():
    """Create a Convex 2D Polygon (wire) from a set of points.
    The Convex Polygon is the outer limit of all selected Points.
    - First select several Points (at least 3);
    Define the projection plane if needed.
    It can be either
    XY plane,
    YZ plane,
    XZ plane or
    All 3 planes
    - Then push the button.
    """
    def isLeftTurn(p1, p2, p3):
        """ Return True if 3 2D points can be reached with a left turn. 
        """
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p1[1] - p3[1]) * (p2[0] - p3[0]) > tolerance

    def convex2Dpolygon (m_array):
        # Sort on x
        m_array.sort(key=lambda tup: tup[0])
        m_top = []
        m_bottom = []
        for m_p in m_array:
            while len(m_top) >= 2 and not isLeftTurn(m_p, m_top[-1], m_top[-2]):
                m_top.pop()
            m_top.append(m_p)
            while len(m_bottom) >= 2 and not isLeftTurn(m_bottom[-2], m_bottom[-1], m_p):
                m_bottom.pop()
            m_bottom.append(m_p)
        return m_bottom[:-1] + m_top[:0:-1]

    msg = verbose
    msg = 1
    m_close = True
    m_face = False

    error_msg = """Unable to create Polygon:
    Select at least 3 points !
    Define the projection plane if needed.
    It can be either
    XY plane,
    YZ plane,
    XZ plane or
    All 3 planes
    - Then push the button."""
    result_msg = ": Convex Polygon(s) created !"

    createFolders('WorkWires')
    m_dir = 'Set'
    name = "Convex_2DPolygon_from_N_Points"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkWires").newObject("App::DocumentObjectGroup", str(m_dir))
    except:
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
        if Number_of_Points > 2:
            m_x = 0.0
            m_y = 0.0
            m_z = 0.0
            m_array = []
            m_polygon = []
            matriz = []
            Point_List = SelectedObjects[3]
            if msg != 0:
                print_msg("Point_List=" + str(Point_List))
            if m_projection_plane2 == "All" or m_projection_plane2 == "XY":
                for m_point in Point_List:
                    x = m_point.Point.x
                    y = m_point.Point.y
                    z = m_point.Point.z
                    m_array.append((x, y))
                if msg != 0:
                    print_msg("m_array=" + str(m_array))
                m_polygon = convex2Dpolygon (m_array)
                for m_2Dpoint in m_polygon:
                    m_x = m_2Dpoint[0]
                    m_y = m_2Dpoint[1]
                    m_z = 0.0
                    matriz.append(FreeCAD.Vector(m_x, m_y, m_z))
                curve_User_Name, curve = plot_curve(matriz, m_close, m_face, part, name, str(m_dir))
                print_msg(str(curve_User_Name) + result_msg + " into: " + str(m_dir))
            m_array = []
            m_polygon = []
            matriz = []
            if m_projection_plane2 == "All" or m_projection_plane2 == "YZ":
                for m_point in Point_List:
                    x = m_point.Point.x
                    y = m_point.Point.y
                    z = m_point.Point.z
                    m_array.append((y, z))
                if msg != 0:
                    print_msg("m_array=" + str(m_array))
                m_polygon = convex2Dpolygon (m_array)
                for m_2Dpoint in m_polygon:
                    m_x = 0.0
                    m_y = m_2Dpoint[0]
                    m_z = m_2Dpoint[1]
                    matriz.append(FreeCAD.Vector(m_x, m_y, m_z))
                curve_User_Name, curve = plot_curve(matriz, m_close, m_face, part, name, str(m_dir))
                print_msg(str(curve_User_Name) + result_msg + " into: " + str(m_dir))
            m_array = []
            m_polygon = []
            matriz = []
            if m_projection_plane2 == "All" or m_projection_plane2 == "XZ":
                for m_point in Point_List:
                    x = m_point.Point.x
                    y = m_point.Point.y
                    z = m_point.Point.z
                    m_array.append((x, z))
                if msg != 0:
                    print_msg("m_array=" + str(m_array))
                m_polygon = convex2Dpolygon (m_array)
                for m_2Dpoint in m_polygon:
                    m_x = m_2Dpoint[0]
                    m_y = 0.0
                    m_z = m_2Dpoint[1]
                    matriz.append(FreeCAD.Vector(m_x, m_y, m_z))
                curve_User_Name, curve = plot_curve(matriz, m_close, m_face, part, name, str(m_dir))
                print_msg(str(curve_User_Name) + result_msg + " into: " + str(m_dir))

        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def plot_4points_bezier():
    msg = verbose

    def Bezier_Cubic_curve(poles):
        # draws a degree 3 rational bspline from first to last point,
        # second and third act as tangents
        # poles is a list: [[[x,y,z],w],[[x,y,z],w],[[x,y,z],w],[[x,y,z],w]]
        ## nKnot = 4 + 3 +1 = 8
        ## Order = 3 + 1 = 4
        degree = 3
        nPoles = 4
        knot = [0, 0, 0, 0, 1, 1, 1, 1]
        bs = Part.BSplineCurve()
        bs.increaseDegree(degree)
        id = 1
        for i in range(0, len(knot)):    #-1):
            bs.insertKnot(knot[i], id, 0.0000001)
        i = 0
        for ii in range(0, nPoles):
            bs.setPole(ii+1, poles[i][0], poles[i][1])
            i = i+1;
        return bs

    createFolders('WorkWires')

    Selection = get_SelectedObjects(info=msg, printError=False)

    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if (Number_of_Points >= 4):
            Point_List = SelectedObjects[3]
            pole0 = [Point_List[0].Point, 1]
            pole1 = [Point_List[1].Point, 1]
            pole2 = [Point_List[2].Point, 1]
            pole3 = [Point_List[3].Point, 1]

            poles = [pole0, pole1, pole2, pole3]

            curve = Bezier_Cubic_curve(poles)

            Part.show(curve.toShape())
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def get_all_from_bounding_box(ori_X, ori_Y, ori_Z, length_X, length_Y, length_Z, info=0, plot=0):
    """ Returns 8 points,12 edges and 6 planes from the bounding box
    """
    m_l_X = length_X
    m_l_Y = length_Y
    m_l_Z = length_Z
    m_o_X = ori_X
    m_o_Y = ori_Y
    m_o_Z = ori_Z
    Points = []
    Edges = []
    Faces = []

    Points.append(App.Vector(m_o_X, m_o_Y     , m_o_Z))
    Points.append(App.Vector(m_o_X, m_o_Y+m_l_Y, m_o_Z))
    Points.append(App.Vector(m_o_X, m_o_Y     , m_o_Z+m_l_Z))
    Points.append(App.Vector(m_o_X, m_o_Y+m_l_Y, m_o_Z+m_l_Z))

    Points.append(App.Vector(m_o_X+m_l_X, m_o_Y     , m_o_Z))
    Points.append(App.Vector(m_o_X+m_l_X, m_o_Y+m_l_Y, m_o_Z))
    Points.append(App.Vector(m_o_X+m_l_X, m_o_Y     , m_o_Z+m_l_Z))
    Points.append(App.Vector(m_o_X+m_l_X, m_o_Y+m_l_Y, m_o_Z+m_l_Z))

    m_list_of_edges = [(0, 1), (1, 3), (3, 2), (2, 0),
                (4, 5), (5, 7), (7, 6), (6, 4),
                (0, 4), (1, 5), (3, 7), (2, 6)]

    for i in m_list_of_edges:
        if info != 0:
            print_msg(str(i))
        line = Part.Line(Points[i[0]], Points[i[1]])
        edge = line.toShape()
        wire = Part.Wire([edge])
        if info != 0:
            Part.show(wire)
        mid_point = wire.CenterOfMass
        length = wire.Length
        Edges.append((i[0], i[1], (Points[i[0]], Points[i[1]]), edge, mid_point, length))

    m_list_of_faces = [(2, 11, 6, 10),
                        (0,  8, 4,  9),
                        (3,  8, 7, 11),
                        (1,  9, 5, 10),
                        (7,  4, 5,  6),
                        (3,  0,  1, 2)]

    for i in m_list_of_faces:
        if info != 0:
            print_msg(str(i))
        wire = Part.Wire([Edges[i[0]][3], Edges[i[1]][3], Edges[i[2]][3], Edges[i[3]][3]])
        if wire.isClosed():
            face = Part.Face(wire)
            mid_point = face.CenterOfMass
            length = face.Length
            if info != 0:
                Part.show(face)
            Faces.append((i[0], i[1], i[2], i[3], (Edges[i[0]][3], Edges[i[1]][3], Edges[i[2]][3], Edges[i[3]][3]), face, mid_point, length))

    # Print info if needed
    if info != 0:
        for m_i in range(len(Points)):
            print_point(Points[m_i], msg="Point_" + str(m_i) + ": ")
        for m_i in range(len(Edges)):
            print_msg("segment: " + str(Edges[m_i]))
        for m_i in range(len(Faces)):
            print_msg("face: " + str(Faces[m_i]))

    # Plot them if needed
    if plot != 0:
        for m_i in range(len(Points)):
            plot_point(Points[m_i], "Part::Feature", "point")
        for m_i in range(len(Edges)):
            #( 2, 6, (Points[2], Points[6]), edge, mid_point, length )
            plot_axis(Edges[m_i][2][0], Edges[m_i][2][1], "Part::Feature", "axis")
        #for m_i in range(len(Faces)):
            # ( 3,  0,  1, 2, (Edges[3][3],Edges[0][3],Edges[1][3],Edges[2][3]), face, mid_point, length )
            # print_msg("face: " + str(Faces[m_i]))

    return Points, Edges, Faces


def volumBBox_toggled(flag):
    """ Respond to the change of solid flag.
    """
    global BBox_volum
    BBox_volum = flag

def infoBBox_toggled(flag):
    """ Respond to the change of info flag.
    """
    global BBox_info
    BBox_info = flag

def plot_boundingBoxes():
    """Create bounding boxes around each of selected object(s).
    """
    msg = verbose

    # Flag for creating a Volume
    createVol = BBox_volum
    m_grp_vol = None
    # Flag for creating dimension info
    createDim = BBox_info
    m_grp_info = None

    createFolders('WorkBoxes')
    error_msg = "Select at least one object !"
    result_msg = "Bounding box created !"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    # Return a list of SelectionObjects for a given document name.
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    m_objs = [selobj.Object for selobj in m_selEx]
    m_objNames = [selobj.ObjectName for selobj in m_selEx]
    m_num = len(m_objs)

    if m_num >= 1:
        if msg != 0:
            print_msg(str(m_num) + " object(s) selected:\n" + str(m_objNames))
        m_i = 0
        for m_obj in m_objs:
            if msg != 0:
                print_msg("Processing: " + str(m_objNames[m_i]))

            m_dir = str(m_objNames[m_i]) + "_BBox"
            if createDim:
                m_dir_info = "Info"
            if createVol:
                m_dir_vol = "Vol"

            # Create a group
            try:
                m_ob = App.ActiveDocument.getObject("WorkBoxes").newObject("App::DocumentObjectGroup", str(m_dir))
            except:
                printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
                return None
            m_grp = m_actDoc.getObject(str(m_ob.Label))

            # Create sub groups
            if m_grp is not None:
                if createDim:
                    try:
                        m_ob2 = App.ActiveDocument.getObject(str(m_ob.Label)).newObject("App::DocumentObjectGroup", str(m_dir_info))
                    except:
                        printError_msg("Could not Create '" + str(m_dir_info) + "' Objects Group!")
                    m_grp_info = m_actDoc.getObject(str(m_ob2.Label))
                if createVol:
                    try:
                        m_ob3 = App.ActiveDocument.getObject(str(m_ob.Label)).newObject("App::DocumentObjectGroup", str(m_dir_vol))
                    except:
                        printError_msg("Could not Create '" + str(m_dir_vol) + "' Objects Group!")
                    m_grp_vol = m_actDoc.getObject(str(m_ob3.Label))

            # Create a solid out of the shells of a shape
            try:
                if hasattr(m_obj, "Shape"):
                    m_s = m_obj.Shape
                elif hasattr(m_obj, "Mesh"):      # upgrade with wmayer thanks #http://forum.freecadweb.org/viewtopic.php?f=13&t=22331
                    m_s = m_obj.Mesh
                elif hasattr(m_obj, "Points"):
                    m_s = m_obj.Points
                #m_s = m_obj.Shape
            except:
                printError_msg("This object has no attribute 'Shape' !\nSelect another one !\n")
                break
            # Get a boundBox A bounding box is an orthographic cube which is a way to describe outer boundaries
            m_boundBox = m_s.BoundBox
            if msg != 0:
                print_msg("BoundBox([Xmin,Ymin,Zmin,Xmax,Ymax,Zmax])\n" + str(m_boundBox))
            # Length of BoundBox in X, Y and Z dimensions
            m_length_X = m_boundBox.XLength
            m_length_Y = m_boundBox.YLength
            m_length_Z = m_boundBox.ZLength
            m_ori_X = m_boundBox.XMin
            m_ori_Y = m_boundBox.YMin
            m_ori_Z = m_boundBox.ZMin

            #bounding_box(m_grp,m_ori_X,m_ori_Y,m_ori_Z,m_length_X,m_length_Y,
            #             m_length_Z,createVol,createDim,m_grp_info,info=msg)
            bounding_box(m_grp, m_ori_X, m_ori_Y, m_ori_Z, m_length_X, m_length_Y,
                         m_length_Z, m_grp_info, m_grp_vol)

            m_actDoc.recompute()
            m_i = m_i + 1

        print_msg(result_msg)
    else:
        printError_msg(error_msg)


def plot_boundingBox():
    """ Create one bounding box around all of selected object(s).
    """
    msg = verbose

    # Flag for creating a Volume
    createVol = BBox_volum
    m_grp_vol = None
    # Flag for creating dimension info
    createDim = BBox_info
    m_grp_info = None

    createFolders('WorkBoxes')
    error_msg = "Select at least one object !"
    result_msg = "Bounding box created !"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return

    m_num, m_selEx, m_objs, m_objNames = get_InfoObjects(info=msg)

    if m_num == 0:
        return
    Center = centerObjectsPoint(m_objs)
    if Center is not None:
        m_dir = str("BoundingBox")
        if createDim:
            m_dir_info = "Info"
        if createVol:
            m_dir_vol = "Vol"

        # Create a group
        try:
            m_ob = App.ActiveDocument.getObject("WorkBoxes").newObject("App::DocumentObjectGroup", str(m_dir))
        except:
            printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        m_grp = m_actDoc.getObject(str(m_ob.Label))

        # Create sub groups
        if m_grp is not None:
            if createDim:
                try:
                    m_ob2 = App.ActiveDocument.getObject(str(m_ob.Label)).newObject("App::DocumentObjectGroup", str(m_dir_info))
                except:
                    printError_msg("Could not Create '" + str(m_dir_info) + "' Objects Group!")
                m_grp_info = m_actDoc.getObject(str(m_ob2.Label))
            if createVol:
                try:
                    m_ob3 = App.ActiveDocument.getObject(str(m_ob.Label)).newObject("App::DocumentObjectGroup", str(m_dir_vol))
                except:
                    printError_msg("Could not Create '" + str(m_dir_vol) + "' Objects Group!")
                m_grp_vol = m_actDoc.getObject(str(m_ob3.Label))


        # print_msg("m_grp = " + str(m_grp))
        m_xmax, m_xmin, m_ymax, m_ymin, m_zmax, m_zmin = minMaxObjectsLimits(m_objs, info=0)
        # Length of BoundBox in X, Y and Z dimensions
        m_length_X = m_xmax - m_xmin
        m_length_Y = m_ymax - m_ymin
        m_length_Z = m_zmax - m_zmin
        m_ori_X = m_xmin
        m_ori_Y = m_ymin
        m_ori_Z = m_zmin
        #bounding_box(m_grp,m_ori_X,m_ori_Y,m_ori_Z,m_length_X,m_length_Y,
        #             m_length_Z,createVol,info=msg)
        bounding_box(m_grp, m_ori_X, m_ori_Y, m_ori_Z, m_length_X, m_length_Y,
                     m_length_Z, m_grp_info, m_grp_vol)
        m_actDoc.recompute()
        print_msg(result_msg)

    else:
        printError_msg(error_msg)


def diameterCylinder(value):
    """ Respond to the change in diameter value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_diameterCylinder
        if str(value) == '-':
            return
        m_diameterCylinder = float(value)
        print_msg("New diameter is:" + str(m_diameterCylinder))
    except ValueError:
        printError_msg("Diameter must be valid number !")


def lengthCylinder(value):
    """ Respond to the change in length value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_lengthCylinder
        if str(value) == '-':
            return
        m_lengthCylinder = float(value)
        print_msg("New diameter is:" + str(m_lengthCylinder))
    except ValueError:
        printError_msg("Diameter must be valid number !")


def plot_axisPointCylinder():
    """ Plot a cylinder with axis aligned on the selected axis and with center at the
    selected point.
    """
    msg = verbose

    createFolders('WorkObjects')
    error_msg = "Unable to create a Cylinder: \n"\
                "Select one or several couple of one Axis and one point!"
    result_msg = ": Cylinder(s) created !"
    name = "Cylinder"
    part = "Part::Feature"
    # global m_diameterCylinder
    # global m_lengthCylinder

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg(" Number_of_Edges =" + str(Number_of_Edges))
            print_msg(" Number_of_Points=" + str(Number_of_Points))

        if (Number_of_Edges == 0):
            printError_msg(error_msg)
            return

        if (Number_of_Edges == Number_of_Points):
            Point_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg(str(Point_List))
                print_msg(str(Edge_List))
            for Selected_Line, Selected_Point in zip(Edge_List, Point_List):
                if msg != 0:
                    print_msg(" Selected_Line=" + str(Selected_Line))
                    print_msg(" Selected_Point=" + str(Selected_Point))
                Vector_C = Selected_Point.Point
                Vector_A = Selected_Line.valueAt(0.0)
                Vector_B = Selected_Line.valueAt(Selected_Line.Length)
                if msg != 0:
                    print_point(Vector_C, msg="Reference Point: ")
                    print_point(Vector_A, msg="Point A: ")
                    print_point(Vector_B, msg="Point B: ")

                Cyl_User_Name, cylinder = plot_cylinder(m_diameterCylinder, m_lengthCylinder, Vector_C, Vector_A - Vector_B, part, name)
                print_msg(str(Cyl_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def sectionCube(value):
    """ Respond to the change in length,width value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        print_msg(str(value))
        global m_lengthCube
        global m_widthCube
        values = value.split(',')
        m_lengthCube = abs(float(values[0]))
        m_widthCube = abs(float(values[1]))
        print_msg("New length,width are:" + str(m_lengthCube) + ", "  + str(m_widthCube))
    except ValueError:
        printError_msg("Length,width must be valid number !")


def heightCube(value):
    """ Respond to the change in height value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_heightCube
        if str(value) == '-':
            return
        m_heightCube = float(value)
        print_msg("New height is:" + str(m_heightCube))
    except ValueError:
        printError_msg("Height must be valid number !")


def plot_axisPointCube():
    """ Plot a cube with axis aligned on the selected axis and with center at the
    selected point.
    """
    msg = verbose

    createFolders('WorkObjects')
    error_msg = "Unable to create a Cube: \n"\
                "Select or several couple of one Axis and one point!"
    result_msg = ": Cube(s) created !"
    name = "Cuboid"
    part = "Part::Feature"
    # global m_lengthCube
    # global m_widthCube
    # global m_heightCube

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))
            print_msg(" Number_of_Points=" + str(Number_of_Points))

        if (Number_of_Edges == 0):
            printError_msg(error_msg)
            return

        if (Number_of_Edges == Number_of_Points):
            Point_List = SelectedObjects[3]
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg(str(Point_List))
                print_msg(str(Edge_List))
            for Selected_Line, Selected_Point in zip(Edge_List, Point_List):
                if msg != 0:
                    print_msg(" Selected_Line=" + str(Selected_Line))
                    print_msg(" Selected_Point=" + str(Selected_Point))
                Vector_C = Selected_Point.Point
                Vector_A = Selected_Line.valueAt(0.0)
                Vector_B = Selected_Line.valueAt(Selected_Line.Length)
                if msg != 0:
                    print_point(Vector_C, msg="Reference Point: ")
                    print_point(Vector_A, msg="Point A: ")
                    print_point(Vector_B, msg="Point B: ")

                Cube_User_Name, cube = plot_cube(m_lengthCube, m_widthCube, m_heightCube, Vector_C, Vector_A - Vector_B, part, name)
                print_msg(str(Cube_User_Name) + result_msg)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def diameterSphere(value):
    """ Respond to the change in diameter value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_diameterSphere
        if str(value) == '-':
            return
        m_diameterSphere = float(value)
        print_msg("New diameter is:" + str(m_diameterSphere))
    except ValueError:
        printError_msg("Diameter must be valid number !")


def plot_centerSphere():
    """ Plot a a Sphere shell:
        - First select one or several Center Point(s). 
        - Define Diameter if needed.
        It will create Sphere shell(s) centered
        at the selected point(s).
    """
    msg = verbose

    createFolders('WorkObjects')

    error_msg =\
    "Unable to create a Sphere: \n" +\
    "Select one (or several) point(s) first for the center location !\n" +\
    "No selection means the center will be at (0,0,0) !"
    result_msg = ": Sphere created !"
    name = "Sphere"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    try:
        Point_List = []

        Selection = get_SelectedObjects(info=msg, printError=False)
        if Selection is None:
            if msg != 0:
                print_msg("Append Origin as Center !")
            #Origin = Base.Vector(0, 0, 0)
            #Point_List.append(Part.Vertex(Origin).Point)
            Point_List.append(Base.Vector(0, 0, 0))
            Number_of_Points = 1
        else:
            SelectedObjects = Selection
            Number_of_Points = SelectedObjects[0]
            if (SelectedObjects[0] >= 1):
                for m_point in SelectedObjects[3]:
                    Point_List.append(m_point.Point)
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
            print_msg("Point_List=" + str(Point_List))

        radius =  m_diameterSphere/2.
        if msg != 0:
            print_msg("Radius is: " + str(radius))
        for center in Point_List:
            if msg != 0:
                print_point(center, msg="Center: ")
            sphere_User_Name, sphere = plot_sphere(radius, center, part, name, grp="WorkObjects")
            print_point(center, str(sphere_User_Name) + result_msg + " at:")
        m_actDoc.recompute()
    except:
        printError_msg(error_msg)


def diameterDome(value):
    """ Respond to the change in diameter value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_diameterDome
        if str(value) == '-':
            return
        m_diameterDome = float(value)
        print_msg("New diameter is:" + str(m_diameterDome))
    except ValueError:
        printError_msg("Diameter must be valid number !")


def frequencyDome(value):
    """ Respond to the change in frequency value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_frequencyDome
        if str(value) == '-':
            return
        m_frequencyDome = int(value)
        if m_frequencyDome in range(10):
            print_msg("New frequency is:" + str(m_frequencyDome))
        else:
            return
    except ValueError:
        printError_msg("Frequency must be valid number !")


def makeDome(point, radius, frequency):
    """
    """
    msg = verbose

    m_center = point
    m_radius = radius
    m_frequency = frequency

    if msg != 0:
        print_msg("makeDome(point=" + str(m_center) +\
                  ", radius=" + str(m_radius) +\
                  ", frequency=" + str(m_frequency) + ")")

    def makeFreqFaces(radius, center, f_Pt, s_Pt, th_Pt, freq):
        """Makes the geodesic dome faces out of the points of an
        icosahedron triangle
        """
        msg = verbose

        m_radius = radius
        m_center = center
        m_freq = freq
        m_domeFaces = []
        firstEdge = None
        secEdge = None
        thirdEdge = None

        if msg != 0:
            print_msg("m_radius =" + str(m_radius))
            print_msg("m_center =" + str(m_center))
            print_msg("m_freq =" + str(m_freq))

        # Definition of direction vectors
        growVec = s_Pt.sub(f_Pt)
        growVec.multiply(1.0/m_freq)

        crossVec = th_Pt.sub(s_Pt)
        crossVec.multiply(1.0/m_freq)

        if msg == 2:
            print_point(f_Pt, msg="f_Pt ")
            plot_point(f_Pt, "Part::Feature", "f_Pt", grp="WorkPoints")
            print_point(s_Pt, msg="s_Pt ")
            plot_point(s_Pt, "Part::Feature", "s_Pt", grp="WorkPoints")
            print_point(th_Pt, msg="th_Pt ")
            plot_point(th_Pt, "Part::Feature", "th_Pt", grp="WorkPoints")
        if msg == 3:
            print_point(growVec, msg="growVec ")
            plot_point(growVec, "Part::Feature", "growVec", grp="WorkPoints")
            print_point(crossVec, msg="crossVec ")
            plot_point(crossVec, "Part::Feature", "crossVec", grp="WorkPoints")

        for k in range(m_freq):
            print_msg("k = " + str(k))
            kThirdPt = f_Pt + growVec * (k+0.0)
            dThirdPt = kThirdPt.sub(m_center)
            dThirdPt = dThirdPt.normalize().multiply(m_radius).add(m_center)
            kSecPt = f_Pt + growVec * (k+1.0)
            dSecPt = kSecPt.sub(m_center)
            dSecPt = dSecPt.normalize().multiply(m_radius).add(m_center)
            if msg == 2:
                print_point(kThirdPt, msg="kThirdPt ")
                plot_point(kThirdPt, "Part::Feature", "kThirdPt", grp="WorkPoints")
                print_point(dThirdPt, msg="dThirdPt ")
                plot_point(dThirdPt, "Part::Feature", "dThirdPt", grp="WorkPoints")
                print_point(kSecPt, msg="kSecPt ")
                plot_point(kSecPt, "Part::Feature", "kSecPt", grp="WorkPoints")
                print_point(dSecPt, msg="dSecPt ")
                plot_point(dSecPt, "Part::Feature", "dSecPt", grp="WorkPoints")

            for l in range(k+1):
                print_msg("l = " + str(l))

                firstPt = kSecPt + crossVec * (l + 1.0)
                dFirstPt = firstPt.sub(m_center)
                dFirstPt = dFirstPt.normalize().multiply(m_radius).add(m_center)

                secPt = kSecPt + crossVec * (l + 0.0)
                dSecPt = secPt.sub(m_center)
                dSecPt = dSecPt.normalize().multiply(m_radius).add(m_center)

                thirdPt = kThirdPt + crossVec * (l + 0.0)
                dThirdPt = thirdPt.sub(m_center)
                dThirdPt = dThirdPt.normalize().multiply(m_radius).add(m_center)
                if msg == 2:
                    print_point(dFirstPt, msg="dFirstPt ")
                    plot_point(dFirstPt, "Part::Feature", "dFirstPt", grp="WorkPoints")
                    print_point(dSecPt, msg="dSecPt ")
                    plot_point(dSecPt, "Part::Feature", "dSecPt", grp="WorkPoints")
                    print_point(dThirdPt, msg="dThirdPt ")
                    plot_point(dThirdPt, "Part::Feature", "dThirdPt", grp="WorkPoints")


                thirdEdge = Part.makeLine(dSecPt, dThirdPt)
                if msg != 0:
                    print_msg("thirdEdge =" + str(thirdEdge))

                if l > 0:
                    secEdge = Part.makeLine(doThirdPt, dThirdPt)
                    if msg == 2:
                        print_msg("firstEdge =" + str(firstEdge))
                        Part.show(firstEdge)
                        print_msg("secEdge =" + str(secEdge))
                        Part.show(secEdge)
                        print_msg("thirdEdge =" + str(thirdEdge))
                        Part.show(thirdEdge)

                    triWire = Part.Wire([firstEdge, secEdge, thirdEdge])
                    triFace = Part.Face(triWire)
                    if msg == 2:
                        print_msg("triWire =" + str(triWire))
                        print_msg("triWire.isClosed() =" + str(triWire.isClosed()))
                        print_msg("triFace =" + str(triFace))
                    m_domeFaces.append(triFace)

                othirdPt = kThirdPt + crossVec * (l + 0.0)
                doThirdPt = othirdPt.sub(m_center)
                doThirdPt = doThirdPt.normalize().multiply(m_radius).add(m_center)
                if msg == 2:
                    print_point(doThirdPt, msg="doThirdPt ")
                    plot_point(doThirdPt, "Part::Feature", "doThirdPt", grp="WorkPoints")

                firstEdge = Part.makeLine(dThirdPt, dFirstPt)
                secEdge = Part.makeLine(dFirstPt, dSecPt)
                thirdEdge = Part.makeLine(dSecPt, dThirdPt)
                if msg == 2:
                    print_msg("firstEdge =" + str(firstEdge))
                    Part.show(firstEdge)
                    print_msg("secEdge =" + str(secEdge))
                    Part.show(secEdge)
                    print_msg("thirdEdge =" + str(thirdEdge))
                    Part.show(thirdEdge)

                triWire = Part.Wire([firstEdge, secEdge, thirdEdge])
                triFace = Part.Face(triWire)
                if msg == 2:
                    print_msg("triWire =" + str(triWire))
                    print_msg("triWire.isClosed() =" + str(triWire.isClosed()))
                    print_msg("triFace =" + str(triFace))
                m_domeFaces.append(triFace)

                if msg == 3:
                    Part.show(firstEdge)
                    Part.show(secEdge)
                    Part.show(thirdEdge)
                    Part.show(triFace)

        return m_domeFaces


    # Strutlength of underlying icosahedron:
    m_length = (4.0*m_radius)/math.sqrt(2.0*math.sqrt(5.0) +10.0)

    # Angle of vertices of icosahedron points
    # not a north or south pole
    m_icoAngle = math.atan(0.5)

    if msg != 0:
        print_msg("m_length =" + str(m_length))
        print_msg("m_icoAngle =" + str(m_icoAngle))

    m_icoLat = m_radius * math.sin(m_icoAngle)
    m_latRad = m_radius * math.cos(m_icoAngle)
    m_ang36 = math.radians(36.0)
    if msg != 0:
        print_msg("m_icoLat =" + str(m_icoLat))
        print_msg("m_latRad =" + str(m_latRad))
        print_msg("m_ang36 =" + str(m_ang36))

    # Calculation all points of the icosahedron
    m_icoPts = []
    m_new_icoPts = []
    m_icoPts.append(Base.Vector(0.0, 0.0, m_radius))
    for i in range(10):
        m_icoCos = m_latRad * math.cos(i*m_ang36)
        m_icoSin = m_latRad * math.sin(i*m_ang36)
        if i%2 == 0:
            m_icoPts.append(Base.Vector(m_icoSin, m_icoCos, m_icoLat))
        else:
            m_icoPts.append(Base.Vector(m_icoSin, m_icoCos, -1 * m_icoLat))

    m_icoPts.append(Base.Vector(0.0, 0.0, -1 * m_radius))
    if msg != 0:
        print_msg("m_icoPts =" + str(m_icoPts))

    for m_icoPt in m_icoPts:
        # print_point(m_icoPt, msg="icoPt")
        # plot_point(m_icoPt, "Part::Feature", "icoPt", grp="WorkPoints")
        m_new_icoPt = m_icoPt.add(m_center)
        # if msg != 0:
            # plot_point(m_new_icoPt, "Part::Feature", "new_icoPt", grp="WorkPoints")
        m_new_icoPts.append(m_new_icoPt)

    m_icoPts = m_new_icoPts

    # Making the faces of the icosahedron
    # Collects faces of the underlying icosahedron
    m_icoFaces = []
    # Collects the faces of the geodesic dome
    m_domeFaces = []

    secPt = m_icoPts[0]
    thirdPt = m_icoPts[9]
    thirdEdge = Part.makeLine(secPt, thirdPt)
    # Top Part
    for i in range(5):
        j = i*2+1
        firstPt = m_icoPts[j]
        firstEdge = Part.makeLine(thirdPt, firstPt)
        secEdge = Part.makeLine(firstPt, secPt)
        triWire = Part.Wire([firstEdge, secEdge, thirdEdge])
        triFace = Part.Face(triWire)
        m_icoFaces.append(triFace)
        # if msg != 0:
        #    Part.show(triFace)
        if m_frequency != 1:
            m_faces = makeFreqFaces(m_radius, m_center, firstPt, secPt, thirdPt, m_frequency)
            for m_face in m_faces:
                m_domeFaces.append(m_face)

        thirdPt = m_icoPts[j]
        thirdEdge = Part.makeLine(secPt, thirdPt)

    secPt = m_icoPts[10]
    thirdPt = m_icoPts[9]
    thirdEdge = Part.makeLine(secPt, thirdPt)
    # Middle part
    for i in range(10):
        j = i+1
        firstPt = m_icoPts[j]
        firstEdge = Part.makeLine(thirdPt, firstPt)
        secEdge = Part.makeLine(firstPt, secPt)
        triWire = Part.Wire([firstEdge, secEdge, thirdEdge])
        triFace = Part.Face(triWire)
        m_icoFaces.append(triFace)
        # if msg != 0:
        #    Part.show(triFace)
        if m_frequency != 1:
            m_faces = makeFreqFaces(m_radius, m_center, firstPt, secPt, thirdPt, m_frequency)
            for m_face in m_faces:
                m_domeFaces.append(m_face)

        thirdPt = secPt
        secPt = m_icoPts[j]
        thirdEdge = Part.makeLine(secPt, thirdPt)

    secPt = m_icoPts[11]
    thirdPt = m_icoPts[10]
    thirdEdge = Part.makeLine(secPt, thirdPt)
    # Bottom part
    for i in range(5):
        j = i*2+2
        firstPt = m_icoPts[j]
        firstEdge = Part.makeLine(thirdPt, firstPt)
        secEdge = Part.makeLine(firstPt, secPt)
        triWire = Part.Wire([firstEdge, secEdge, thirdEdge])
        triFace = Part.Face(triWire)
        m_icoFaces.append(triFace)
        # if msg != 0:
        #    Part.show(triFace)
        if m_frequency != 1:
            m_faces = makeFreqFaces(m_radius, m_center, firstPt, secPt, thirdPt, m_frequency)
            for m_face in m_faces:
                m_domeFaces.append(m_face)

        thirdPt = m_icoPts[j]
        thirdEdge = Part.makeLine(secPt, thirdPt)

    # Shell of a corresponding icosahedron
    m_icosahedron_Shell = Part.Shell(m_icoFaces)
    # if msg != 0:
        # Part.show(m_icosahedron_Shell)

    if m_frequency != 1:
        # Shell of the geodesic dome
        m_domeShell = Part.Shell(m_domeFaces)
        # if msg != 0:
            # Part.show(m_domeShell)
    else:
        m_domeShell = None

    return m_domeShell, m_icosahedron_Shell


def plot_centerDome():
    """ Plot a full geodesic dome shell.
    X-Y-symmetry plane
    for even frequencies
    Select first a point for the center of the dome.
    
    You might defined first the 2 parameters of the dome:
        Dome Diameter
        Frequency Parameter (Integer between 1 to 10)
    If Frequency Parameter = 1, the code create an icosahedron. 
    An icosahedron is a polyhedron with 20 faces.
    Original code from: Ulrich Brammer
    """
    msg = verbose

    createFolders('WorkObjects')

    error_msg =\
    "Unable to create a Dome: \n" +\
    "Select one (or several) point(s) first for the center location !\n" +\
    "No selection means the center will be at (0,0,0) !"
    result_msg = ": Dome created !"
    name = "Dome"
    part = "Part::Feature"
    Pt_List = []

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc.Name is None:
        return None

    Selection = get_SelectedObjects(info=msg, printError=False)

    if Selection is None:
        if msg != 0:
            print_msg("Append Origin as Center !")
        #Origin = Base.Vector(0, 0, 0)
        #Pt_List.append(Part.Vertex(Origin).Point)
        Pt_List.append(Base.Vector(0, 0, 0))
        Number_of_Points = 1
    else:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if (SelectedObjects[0] >= 1):
            for m_point in SelectedObjects[3]:
                Pt_List.append(m_point.Point)
        else:
            printError_msg(error_msg)
            return

    try:
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))
            print_msg("Point_List=" + str(Pt_List))

        frequency = int(m_frequencyDome)
        radius =  m_diameterDome/2.
        if msg != 0:
            print_msg("Radius is: " + str(radius))
            print_msg("Frequency is: " + str(frequency))

        for center in Pt_List:
            if msg != 0:
                print_point(center, msg="Center: ")
                #Sphere with radius of geodesic dome for debugging purposes
                sphere_User_Name, sphere = plot_sphere(radius, center, part, "Sphere", grp="WorkObjects")

            dome_User_Name, dome = plot_Dome(center, radius, frequency, part, name, grp="WorkObjects")

            print_point(center, str(dome_User_Name) + result_msg + " at:")
        m_actDoc.recompute()
        del Pt_List[:]
    except:
        printError_msg(error_msg)


def sizeLetter(value):
    """ Respond to the change in sizer value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_sizeLetter
        if str(value) == '-':
            return
        m_sizeLetter = float(value)
        print_msg("New diameter is:" + str(m_sizeLetter))
    except ValueError:
        printError_msg("Size must be valid number !")


def letter(value):
    """ Respond to the change in letter from the text box.
    """
    global verbose
    msg = verbose

    try:
        # First we check if a valid number have been entered
        global m_letter
        m_letter = value
        if msg != 0:
            print_msg("New letter is:" + str(m_letter))
    except ValueError:
        printError_msg("Letter must be valid text !")


def plot_letter():
    """ Create 3D Text attached to a Point.  
    - First select a  Plane
    in this case the center of the text is attached to center of the Plane;
    or
    - First select a Plane and a Point on the Plane

    NB:
        Change the text and his size if needed
    """
    msg = verbose

    import Draft

    def text_at(Plane_Point, Plane_Normal):
        msg = verbose
        text_User_Name, text = plot_text(m_letter, m_sizeLetter, part, name, grp="WorkObjects")
        text_Point = text.Shape.BoundBox.Center
        text_Normal = text.Shape.Faces[0].normalAt(0, 0)
        if msg != 0:
            print_point(text_Point, msg="text_Point = ")
            print_point(text_Normal, msg="text_Normal = ")
        # Rotation
        if colinearVectors(text_Normal, Origin, Plane_Normal, info=0, tolerance=1e-12):
            rot_axis = Base.Vector(0, 0, 1).cross(text_Normal)
            rot_center = text_Point
            rot_angle = 180.
        else:
            m_angle, m_angle_rad = angleBetween(text_Normal, Plane_Normal)
            rot_axis = text_Normal.cross(Plane_Normal)
            rot_center = text_Point
            rot_angle = m_angle
##################### replace Draft.rotate by ################
            pl = App.Placement()
            pl.Rotation = App.Rotation(rot_axis, rot_angle)
            pl.Base = App.Vector(rot_center)
            text.Placement = pl
###################### 11/11/17 ###############################
#        Draft.rotate(text,rot_angle,rot_center,rot_axis)
###############################################################
        # translation
        New_Point = Plane_Point + Plane_Normal.normalize().multiply(2)
        m_move = New_Point.sub(rot_center)
        if msg != 0:
            print_msg("m_move = " + str(m_move))
        m_rot = text.Placement.Rotation
        m_base = text.Placement.Base
        m_newplace = App.Placement(m_base.add(m_move), m_rot)
        text.Placement = m_newplace


    createFolders('WorkObjects')
    error_msg = "Unable to create Text: \nSelect one Plane and one Point !"
    result_msg = ": Text created !"
    name = "Text"
    part = "Part::Feature"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Planes = SelectedObjects[2]
        Number_of_Points = SelectedObjects[0]
        if msg != 0:
            print_msg(" Number_of_Planes=" + str(Number_of_Planes))
            print_msg(" Number_of_Points=" + str(Number_of_Points))
        Point_List = SelectedObjects[3]
        Plane_List = SelectedObjects[5]
        if msg != 0:
            print_msg(" Point_List=" + str(Point_List))
            print_msg(" Plane_List=" + str(Plane_List))

        if (Number_of_Planes == 0):
                printError_msg(error_msg)
                return

        Origin = Base.Vector(0, 0, 0)
        if (Number_of_Points == 0):
            for Selected_Plane in Plane_List:
                try:
                    # print_msg(str(Selected_Plane))
                    Plane_Point = Selected_Plane.CenterOfMass
                    Plane_Normal = Selected_Plane.normalAt(0, 0)
                    if msg != 0:
                        print_point(Plane_Point, msg="Plane_Point = ")
                        print_point(Plane_Normal, msg="Plane_Normal = ")
                    text_at(Plane_Point, Plane_Normal)

                except:
                    printError_msg("Non Planar Surface !")
        else:
            if Number_of_Points == Number_of_Planes:
                if msg != 0:
                    print_msg(" Number_of_Points = Number_of_Planes")
                for Selected_Plane, Selected_Point in zip(Plane_List, Point_List):
                    if msg != 0:
                        print_msg(" Selected_Plane=" + str(Selected_Plane))
                        print_msg(" Selected_Point=" + str(Selected_Point))
                    Plane_Point = Selected_Point.Point
                    Plane_Normal = Selected_Plane.normalAt(0, 0)
                    if msg != 0:
                        print_point(Plane_Point, msg="Plane_Point = ")
                        print_point(Plane_Normal, msg="Plane_Normal = ")
                    text_at(Plane_Point, Plane_Normal)

            else:
                printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def angleRevolve(value):
    """ Respond to the change in revolution angle value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_angleRevolve
        m_angleRevolve = float(value)
        print_msg("New revolution angle is:" + str(m_angleRevolve))
    except ValueError:
        printError_msg("Revolution angle must be valid number angle in degrees)!")


def plot_revolution():
    """
    Revolve:
    Make the revolution of Edge(s) or Wire(s) around an Axis:
    - Select one or several wire(s)
    or
    - Select FIRST one Point as center of rotation and one Axis as rotation axis !
    - Select one or several wire(s)
    
    NB:
      You can also define the angle of revolution if needed
       If no Axis is selected the Z axis is considered as Axis of rotation !
       If no Point is selected the Origin is considered as Center of rotation !

    """
    msg = verbose

    createFolders('WorkObjects')
    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select one Point as center of rotation\n" +\
    "and one Axis as rotation axis FIRST !\n" +\
    "Then Select Edge(s) or Wire(s) to create revolution(s)\n" +\
    "If no Axis is selected the Z axis is considered as Axis of rotation !\n" +\
    "If no Point is selected the Origin is considered as Center of rotation !"

    m_actDoc = App.activeDocument()
    if m_actDoc.Name:
        m_sel = Gui.Selection.getSelection(m_actDoc.Name)
        if msg != 0:
            print_msg("m_sel=" + str(m_sel))
        m_num_objs = len(m_sel)
        if msg != 0:
            print_msg("m_num_objs=" + str(m_num_objs))

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = m_sel
        SelectedObjects_rot = Selection
        Number_of_Edges = SelectedObjects_rot[1]
        Number_of_Points = SelectedObjects_rot[0]
        # No axis of rotation selected
        if Number_of_Edges == 0:
            Axis = Base.Vector(0, 0, 1)
        # No axis of rotation selected just one edge to revolve
        elif Number_of_Edges > 0 and m_num_objs == 1:
            Axis = Base.Vector(0, 0, 1)
        # Axis of rotation selected
        else:
            Edge_List = SelectedObjects_rot[4]
            edge = Edge_List[0]
            Axis = edge.Vertexes[-1].Point.sub(edge.Vertexes[0].Point)
            del SelectedObjects[0]
        if msg != 0:
             print_msg("Axis=" + str(Axis))

        if Number_of_Points == 0:
            Center = Base.Vector(0, 0, 0)
        else:
            Point_List = SelectedObjects_rot[3]
            Center = Point_List[0].Point
        if msg != 0:
             print_msg("Center=" + str(Center))

        if msg != 0:
             print_msg("SelectedObjects=" + str(SelectedObjects))

        m_num = 0
        for m_obj in SelectedObjects:
            if msg != 0:
                print_msg("m_obj.Shape=" + str(m_obj.Shape))
            if not (getShapeType(m_obj.Shape) == "Wire" or getShapeType(m_obj.Shape) == "Edge"):
                continue
            m_num = m_num + 1
            if msg != 0:
                print_msg("m_num=" + str(m_num))
            r = m_obj.Shape.revolve(Center, Axis, m_angleRevolve)
            plot_Shape(r, part="Part::Feature", name="Revolve", grp="WorkObjects")
            #Part.show(r)

        if m_num == 0:
            printError_msg("No Edge was selected !")

    except:
        printError_msg(error_msg)


def frenet_toggled(flag):
    """ Respond to the change of frenet flag.
    """
    global sweep_frenet
    sweep_frenet = flag


def solid_toggled(flag):
    """ Respond to the change of solid flag.
    """
    global sweep_solid
    sweep_solid = flag


def subselect_toggled(flag):
    """ Respond to the change of allsubselect flag.
    """
    global sweep_all
    sweep_all = flag


def sel_transition(*argc):
    """ Transition between profiles choice by combo box.
    Options:
    No Transition (or 0) (default)
    Right corners (or 1) 
    Rounded corners (or 2)
    """
    global sweep_transition
    msg = verbose

    if msg != 0:
        print_msg("Transition between profiles choice by combo box !")
    sweep_transition = 2
    if str(*argc) == "No Transition":
        sweep_transition = 0
    if str(*argc) == "Right corners":
        sweep_transition = 1
    if str(*argc) == "Rounded corners":
        sweep_transition = 2


def plot_sectionSweep():
    """ Section Sweep:
    #  Make a loft defined by a list of profiles along a wire.
    Will extrude/sweep a Section along a Trajectory like sweep from Part Workbench but:
    - the Section center (of Mass) is move at the first point of the Trajectory and;
    - the "plane" of the Section is rotate to be perpendicular to the Trajectory.
    
    - Select first one Section wire (Closed wire will generate volumes by default)
    (This Section can be a compound from sketch to realize "tube")
    - Select one or several wire(s) as Trajectory(ies)
    - Then push this button
    
    NB: You can change first:
    - Solid option (if toggled will generate a solid for Closed wire Section only) 
    - isFrenet option
    - All option (means if the trajectory selected is a compound, all sub wires will be used for the sweep)
    - Transition Option (Select a Transition option in case of trajectory with several wires; Transition can be:
    #     0 (default), 1 (right corners) or 2 (rounded corners).)   
    """
    global verbose
    msg = verbose

    # Variable makeSolid = 1 to create solid if section is closed, 0 to create surfaces
    makeSolid = sweep_solid
    isFrenet = sweep_frenet
    # Transition between profiles can be 0  (default), 1 (right corners)
    # or 2 (rounded corners)
    transition = sweep_transition
    # If several sub profiles when this flag is true only the sub profile selected
    # will be processed
    allSubProfile = sweep_all

    if msg != 0:
        print_msg("makeSolid = " + str(makeSolid))
        print_msg("isFrenet = " + str(isFrenet))
        print_msg("transition = " + str(transition))
        print_msg("allSubProfile = " + str(allSubProfile))

    createFolders('WorkAxis')
    createFolders('WorkPoints')
    createFolders('WorkObjects')
    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "First select the wire you want as section for Section Sweep (must be closed for solid creation!)\n" +\
    "Then select the second wire for the trajectory of the Sweep !"
    result_msg = ": Section Sweep created into WorkFeatures/WorkObjects!"
    name = "SectionSweep"
    part = "Part::Feature"

    m_actDoc = App.activeDocument()
    if m_actDoc.Name:
        m_sel = Gui.Selection.getSelection(m_actDoc.Name)
        m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    else:
        return

#    if msg != 0:
#        print_msg("m_sel = " + str(m_sel))
#        m_num_objs = len(m_sel)
#        print_msg("m_num_objs = " + str(m_num_objs))

    try:
        SelectedObjects = m_sel

        # First object selected is the section then other are trajectories
        if not (hasattr(SelectedObjects[0], 'Shape') and hasattr(SelectedObjects[1], 'Shape')):
            printError_msg("Object without Shape selected \n" + str(error_msg))
            return
        if msg != 0:
            print_msg("01-First object selected is the section then other are trajectories")
            print_msg("Object with Shape selected = " + str(SelectedObjects))

        # Make a copy of the section
        m_copy = App.activeDocument().copyObject(SelectedObjects[0])
        shape0 = m_copy.Shape
        if msg != 0:
            print_msg("02-Make a copy of the section")
            print_msg("shape0 = " + str(shape0))

        # Get the list of sections in case of first section is a Compound
        m_sections = []
        if isinstance(shape0, Part.Compound):
            if msg != 0:
                print_msg("Compound Section Found !")
            for wire in shape0.Wires:
                m_sections.append(Part.Wire([wire]))
        else:
            if msg != 0:
                print_msg("NO Compound Section Found !")
                print_msg(str(getShapeType(shape0)))
            try:
                if len(shape0.Wires):
                    for wire in shape0.Wires:
                        m_sections.append(Part.Wire([wire]))
                elif len(shape0.Edges):
                    for edge in shape0.Edges:
                        m_sections.append(Part.Wire([edge]))
                elif len(shape0.Vertexes):
                    for vertex in shape0.Vertexes:
                        m_sections.append(Part.Wire([vertex]))
                else:
                    print_msg("Not able to transform " + str(shape0) + "in wire !")
                    return
            except:
                pass

        if msg != 0:
            print_msg("03-Get the list of sections in case of first section is a Compound")
            print_msg("m_sections = " + str(m_sections))

        # Loop on sections
        for m_id in range(len(m_sections)):
            m_section = m_sections[m_id]
            if msg != 0:
                print_msg("04-Loop on sections")
                print_msg("Section Selected = " + str(m_section))

            # Loop on trajectories
            for selObj in SelectedObjects[1:]:
                if not hasattr(selObj, 'Shape'):
                    continue
#                if msg != 0:
#                    print_msg("Processing selObj.Name = " + str(selObj.Name))
                m_traj_points = []
                m_section_points = []
                rot_center = m_section.CenterOfMass

                # Look for the Normal of section wire
                m_section_normal, m_section_points = findNormal(m_section, forceDiscretize=True, msg=msg)

#                if msg != 0:
#                    print_point(m_section_normal, msg="NormalOfSection = ")
#                    axis_User_Name, axis = plot_axis(rot_center, rot_center.add(m_section_normal), part="Part::Feature", name="NormalOfSection", grp="WorkAxis")
#                    Gui.ActiveDocument.getObject(axis_User_Name).LineColor = (1.0,0.0,0.0)

                # List of trajectories
                m_trajs = []
                m_trajs = get_wireListFromObjectName(selObj.Name, subSelection=not(allSubProfile), msg=msg)
                if msg != 0:
                    print_msg("m_trajs = " + str(m_trajs))
                for s in m_trajs:
                    shape2 = s
                    m_traj = Part.Wire([shape2])
                    if msg != 0:
                        print_msg("m_section = " + str(m_section))
                        print_msg("m_traj = " + str(m_traj))

                    # Look for the Normal for trajectory wire
                    m_traj_normal, m_traj_points = findNormal(m_traj, forceDiscretize=False, msg=msg)

#                    if msg != 0:
#                        print_point(m_traj_normal, msg="NormalOfTrajectory = ")
#                        axis_User_Name, axis = plot_axis(rot_center, rot_center.add(m_traj_normal), part, name="NormalOfTrajectory", grp="WorkAxis")
#                        Gui.ActiveDocument.getObject(axis_User_Name).LineColor = (0.0,1.0,0.0)
#                        point_User_Name = plot_point(m_traj_points[0], part, name="End", grp="WorkPoints")
#                        Gui.ActiveDocument.getObject(point_User_Name).PointColor = (1.0,1.0,1.0)

                    m_angle, m_angle_rad = angleBetween(m_traj_normal, m_section_normal)
                    rot_axis = m_traj_normal.cross(m_section_normal)
                    rot_angle = -1 * m_angle
#                    if msg != 0:
#                        print_msg("rot_angle = " + str(rot_angle))
#                        axis_User_Name, axis = plot_axis(rot_center,rot_center.add( rot_axis), part, name="Normal", grp="WorkAxis")
#                        Gui.ActiveDocument.getObject(axis_User_Name).LineColor = (0.0,0.0,1.0)
#                        point_User_Name = plot_point(rot_center, part, name="Start", grp="WorkPoints")
#                        Gui.ActiveDocument.getObject( point_User_Name ).PointColor = (0.0,0.0,1.0)

                    Draft.rotate(m_copy, rot_angle, rot_center, rot_axis, copy=False)
#                    if msg != 0:
#                        print_msg("rotation done !")

                    # Reset the selection changed by Draft.rotate
                    reset_SelectedObjects(m_selEx, info=0)

                    m_move = m_traj_points[0].sub(rot_center)
                    m_oldplace = m_copy.Placement
                    m_rot = m_copy.Placement.Rotation
                    m_base = m_copy.Placement.Base
                    if msg != 0:
                        print_msg("m_copy.Placement = " + str(m_copy.Placement))

                    m_newplace = App.Placement(m_base.add(m_move), m_rot)
                    m_copy.Placement = m_newplace
#                    if msg != 0:
#                        print_msg("move done !")

                    shape3 = m_copy.Shape
                    m_sections3 = []
                    if isinstance(shape3, Part.Compound):
                        for wire in shape3.Wires:
                            m_sections3.append(Part.Wire([wire]))
                    else:
                        try:
                            if len(shape3.Wires):
                                for wire in shape3.Wires:
                                    m_sections3.append(Part.Wire([wire]))
                            elif len(shape0.Edges):
                                for edge in shape3.Edges:
                                    m_sections3.append(Part.Wire([edge]))
                            elif len(shape0.Vertexes):
                                for vertex in shape3.Vertexes:
                                    m_sections3.append(Part.Wire([vertex]))
                            else:
                                print_msg("Not able to transform " + str(shape3) + "in wire !")
                                return
                        except:
                            pass
#                    if msg != 0:
#                        print_msg("m_sections3 = " + str(m_sections3))

                    for m_id3 in range(len(m_sections3)):
                        m_section3 = m_sections3[m_id3]
                        if m_id == m_id3:
                            Sweep_User_Name, sweep = plot_sweep(m_traj, m_section3, makeSolid, isFrenet, transition, part, name)
                            print_msg(str(Sweep_User_Name) + result_msg)

                    m_copy.Placement = m_oldplace
                    rot_angle = -1*rot_angle
                    Draft.rotate(m_copy, rot_angle, rot_center, rot_axis, copy=False)
                    reset_SelectedObjects(m_selEx, info=0)

        # Remove duplicated section
        App.getDocument(str(App.activeDocument().Name)).removeObject(m_copy.Label)

    except:
        printError_msg(error_msg)


def plot_sectionBeam():
    """Section Beam:
    """
    import WorkFeature.Beam.beam as BM
    msg = verbose

    createFolders('WorkObjects')
    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "First select the wire you want as section for Section Beam \n" +\
    "Then select the second wire for the strait path trajectory of the Beam !"
    result_msg = ": Section Beam created into WorkFeatures/WorkObjects!"
    name = "Beam"
    part = "Part::FeaturePython"

    m_actDoc = App.activeDocument()
    if m_actDoc.Name:
        m_sel = Gui.Selection.getSelection(m_actDoc.Name)
        m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    else:
        return

    try:
        m_profile = m_sel[0]
        if msg != 0:
            print_msg("m_profile !" + str(m_profile))
            print_msg("m_selEx !" + str(m_selEx))
        for m_path_selected in m_selEx[1:]:
            m_path = m_path_selected.Object
            #m_path_name = m_path_selected.SubElementNames[0]
            for m_path_name in m_path_selected.SubElementNames:
                if msg != 0:
                    print_msg("m_path !" + str(m_path))
                    print_msg("m_path_name !" + str(m_path_name))
                m_beam = App.ActiveDocument.addObject(part, name)
                BM.Beam(m_beam, m_profile, m_path, m_path_name)
                BM.ViewProviderBeam(m_beam.ViewObject)
                App.ActiveDocument.getObject('WorkObjects').addObject(m_beam)

        App.ActiveDocument.recompute()
        print_msg(m_beam.Label + str(result_msg))
    except:
        printError_msg(error_msg)


def plot_sectionSweep2():
    """
    Beam Sweep:
    Will sweep a Section along a Trajectory like sweep from Part worbench but:
    - the Section center(of Mass) is move at the first point of the Trajectory and;
    - the"plane" of the Section is rotate to be perpendicular to the Trajectory.
    
    - Select first one Section wire (Closed wire will generate volumes by default)
    - Select one or several wire as Trajectory(ies)
    
    if Solid check box is toggled:
      The Beam sweep will generate a solid with a closed selected wire as Section.
    If this check box is toggle off:
      Or if the Section wire is not closed, only a shell will be created.
    """
    msg = verbose

    # variable makeSolid = 1 to create solid, 0 to create surfaces
    makeSolid = sweep_solid
    isFrenet = sweep_frenet
    transition = sweep_transition

    createFolders('WorkAxis')
    createFolders('WorkPoints')
    createFolders('WorkObjects')
    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "First select the wire you want as section for Beam Sweep (must be closed)\n" +\
    "Then select the second wire for the trajectory of the Sweep !"
    result_msg = ": Beam Sweep created !"
    name = "BeamSweep"
    part = "Part::Feature"

    m_actDoc = App.activeDocument()
    if m_actDoc.Name:
        m_sel = Gui.Selection.getSelection(m_actDoc.Name)
        m_num_objs = len(m_sel)
        if msg != 0:
            print_msg("m_sel=" + str(m_sel))
            print_msg("m_num_objs=" + str(m_num_objs))

    Origin = Base.Vector(0, 0, 0)
    try:
        SelectedObjects = m_sel

        if hasattr(SelectedObjects[0], 'Shape') and hasattr(SelectedObjects[1], 'Shape'):
            if msg != 0:
                print_msg("Both Object selected have a Shape")

            m_traj_points = []
            m_section_points = []
            shape0 = SelectedObjects[0].Shape

            # Look for Compound object like Sketch with several wires
            if isinstance(shape0, Part.Compound):
                m_face = Part.Face(shape0.Wires)
                if msg != 0:
                    print_msg("Face Created!" + str(m_face))
                    face = App.ActiveDocument.addObject("Part::Feature", 'Face')
                    face.Shape = m_face
                rot_center = m_face.CenterOfMass
                m_section_normal = m_face.normalAt(0, 0)
            else:
                m_section = Part.Wire([shape0])
                if msg != 0:
                    print_msg("Section Created!" + str(m_section))
                rot_center = m_section.CenterOfMass
                # Look for the Normal a Start of section wire
                if hasattr(m_section, 'discretize') is not True:
                    printError_msg("Unable to discretize the section!")
                    return
                m_section_points = m_section.discretize(4)
                if len(m_section_points) <= 2:
                    printError_msg("Unable to discretize the section!")
                    return
                m_vect01 = m_section_points[1] - m_section_points[0]
                m_vect02 = m_section_points[2] - m_section_points[0]
                m_section_normal = m_vect01.cross(m_vect02)
                if msg != 0:
                    print_msg("Normal by discretize() !")

            m_section_normal.normalize()
            if msg != 0:
                print_point(m_section_normal, msg="NormalOfSection is ")
                axis_User_Name, axis = plot_axis(Origin, m_section_normal, part, name="NormalOfSection", grp="WorkAxis")
                Gui.ActiveDocument.getObject(axis_User_Name).LineColor = (1.0, 0.0, 0.0)


            for selObj in SelectedObjects[1:]:
                if not hasattr(selObj, 'Shape'):
                    continue
                if isinstance(shape0, Part.Compound):
                    obj = App.ActiveDocument.addObject("Part::Feature", "Face")
                    m_obj.Shape = m_face
                    shape1 = m_obj.Shape
                else:
                    m_obj = App.activeDocument().copyObject(SelectedObjects[0], True)
                    shape1 = m_obj.Shape
                print_msg("shape 1 selected !" + str(shape1))

                shape2 = selObj.Shape
                print_msg("shape 2 selected !" + str(shape2))
                #shape2 = SelectedObjects[1].Shape
                if isinstance(shape2, Part.Compound):
                    m_traj = Part.Wire([shape2.Wires[0]])
                    if msg != 0:
                        print_msg("m_section !" + str(m_section))
                        print_msg("m_traj !" + str(m_traj))
                else:
                    m_traj = Part.Wire([shape2])
                    if msg != 0:
                        print_msg("m_section !" + str(m_section))
                        print_msg("m_traj !" + str(m_traj))

# ==============================================================================
#               Look for the Normal a Start of trajectory wire
# ==============================================================================
                if len(shape2.Edges) != 0:
                    m_traj_normal = shape2.Edges[0].tangentAt(0)
                    m_traj_points.append(shape2.Vertexes[0].Point)
                    if msg != 0:
                        print_msg("Normal by Tangent !")
                else:
                    if hasattr(m_traj, 'discretize') is not True:
                        printError_msg("Unable to discretize the trajectory!")
                        return
                    m_traj_points = m_traj.discretize(Distance=0.01)
                    if len(m_traj_points) <= 2:
                        printError_msg("Unable to discretize the trajectory!")
                        return
                    m_traj_normal = m_traj_points[1] - m_traj_points[0]
                    if msg != 0:
                        print_msg("Normal by discretize() !")

                m_traj_normal.normalize()
                if msg != 0:
                    print_point(m_traj_normal, msg="NormalOfTrajectory is ")
                    axis_User_Name, axis = plot_axis(Origin, m_traj_normal, part, name="NormalOfTrajectory", grp="WorkAxis")
                    Gui.ActiveDocument.getObject(axis_User_Name).LineColor = (0.0, 1.0, 0.0)
                    point_User_Name = plot_point(m_traj_points[0], part, name="End", grp="WorkPoints")
                    Gui.ActiveDocument.getObject(point_User_Name).PointColor = (1.0, 1.0, 1.0)

                m_angle, m_angle_rad = angleBetween(m_traj_normal, m_section_normal)
                rot_axis = m_traj_normal.cross(m_section_normal)
                rot_angle = -1 * m_angle
                #rot_center = m_section.CenterOfMass
                if msg != 0:
                    print_msg("rot_angle" + str(rot_angle))
                    axis_User_Name, axis = plot_axis(Origin, rot_axis, part, name="Normal", grp="WorkAxis")
                    Gui.ActiveDocument.getObject(axis_User_Name).LineColor = (0.0, 0.0, 1.0)
                    point_User_Name = plot_point(rot_center, part, name="Start", grp="WorkPoints")
                    Gui.ActiveDocument.getObject(point_User_Name).PointColor = (0.0, 0.0, 1.0)

                Draft.rotate(m_obj, rot_angle, rot_center, rot_axis)
                m_move = m_traj_points[0].sub(rot_center)
                #m_move = rot_center.add(m_move)
                m_rot = m_obj.Placement.Rotation
                m_base = m_obj.Placement.Base
                if msg != 0:
                    print_msg("m_obj.Placement" + str(m_obj.Placement))

                m_newplace = App.Placement(m_base.add(m_move), m_rot)
                m_obj.Placement = m_newplace
                shape3 = m_obj.Shape
                m_section2 = Part.Wire([shape3])
                Sweep_User_Name, sweep = plot_sweep(m_traj, m_section2, makeSolid, isFrenet, transition, part, name)
                print_msg(str(Sweep_User_Name) + result_msg)
                if msg == 0:
                    App.getDocument(str(App.activeDocument().Name)).removeObject(m_obj.Label)
    except:
        printError_msg(error_msg)


def rotate_image():
    print_not_yet()
    pass

def sel_imageAxisScale(*argc):
    """ Axis or Plane of Scaling for image choice by combo box.
    Options:
    XY
    XZ
    YZ
    X
    Y
    Z
    """
    global imageAxisScale
    msg = verbose

    if msg != 0:
        print_msg("Axis or Plane of Scaling for image choice by combo box !")
    # imageAxisScale = "XY"
    imageAxisScale = str(*argc)
    if msg != 0:
        print_msg("Axis selection is:" + str(imageAxisScale))


def lengthImage(value):
    """ Respond to the change in Image length value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_lengthImage
        if str(value) == '-':
            return
        m_lengthImage = float(value)
        print_msg("New Image length is:" + str(m_lengthImage))
    except ValueError:
        printError_msg("Image length must be valid number !")
    pass


def scale_image():
    msg = verbose

    error_msg = "Unable to scale Image: \n"\
                "Select at least \n"\
                "One Image and One line or \n"\
                "One Image and Two points!"

    result_msg = ": Image Scaled !"

    createFolders('WorkImages')
    m_dir = 'WorkImages'
    name = "ImageScaled"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    try:
        m_r = App.ActiveDocument.getObject("WorkImages").newObject("App::DocumentObjectGroup", str(m_dir))
    except:
        printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
        return None
    m_dir = m_r.Name

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))

    # Recover the desired length
    m_new_length = m_lengthImage
    Number_of_Images = 0
    Number_of_Points = 0
    Number_of_Lines = 0
    Image_List = []
    Point_List = []
    Line_List = []

    # One Image selected but need 2 more points
    # One Image and one point selected but need one more point
    # One Image and two points selected
    try:
        Number_of_Images, Image_List = m_sel.get_primerImages()
        Number_of_Points, Point_List = m_sel.get_points()
        Number_of_Lines, Line_List  = m_sel.get_segments()
        if msg != 0:
            print_msg("Number_of_Images=" + str(Number_of_Images))
            print_msg("Image_List=" + str(Image_List))
            print_msg("Number_of_Points=" + str(Number_of_Points))
            print_msg("Point_List=" + str(Point_List))
            print_msg("Number_of_Lines=" + str(Number_of_Lines))
            print_msg("Line_List=" + str(Line_List))

        # Recover the 2 points
        m_points = []
        if Number_of_Lines >= 1:
            m_points.append(Line_List[0].Vertexes[-1].Point)
            m_points.append(Line_List[0].Vertexes[0].Point)
        if Number_of_Points >= 2:
            m_points.append(Point_List[-1].Point)
            m_points.append(Point_List[0].Point)

        if Number_of_Images == 1:
            # Make a copy of the image
            #m_img = Image_List[0]
            m_img = App.activeDocument().copyObject(Image_List[0])
            App.ActiveDocument.getObject(m_dir).addObject(m_img)
            # Get angle(plane) of image
            m_img_angle = math.degrees(m_img.Placement.Rotation.Angle)
            if msg != 0:
                print_msg("Angle of Image selected = " + str(m_img_angle))
                print_msg("Scale Axis user choice = " + str(imageAxisScale))

            if m_img_angle == 0.0: # XY plane
                m_length_x = m_points[0].x - m_points[-1].x
                m_length_y = m_points[0].y - m_points[-1].y

                if str(imageAxisScale) == "XY":
                    if m_length_x == 0:
                        return
                    m_s = m_new_length/m_length_x
                    m_img.XSize.Value = m_img.XSize.Value * m_s
                    m_img.YSize.Value = m_img.YSize.Value * m_s
                elif str(imageAxisScale) == "X":
                    if m_length_x == 0:
                        return
                    m_s = m_new_length/m_length_x
                    m_img.XSize.Value = m_img.XSize.Value * m_s
                elif str(imageAxisScale) == "Y":
                    if m_length_y == 0:
                        return
                    m_s = m_new_length/m_length_y
                    m_img.YSize.Value = m_img.YSize.Value * m_s
                else:
                    m_local_error_msg = "Unable to scale Image: \n"\
                    "The selected Axis must be either: XY, X or Y !"
                    printError_msg(m_local_error_msg)
                    return

            elif m_img_angle == 120.0: # YZ plane
                m_length_y = m_points[0].y - m_points[-1].y
                m_length_z = m_points[0].z - m_points[-1].z

                if str(imageAxisScale) == "YZ":
                    if m_length_y == 0:
                        return
                    m_s = m_new_length/m_length_y
                    m_img.XSize.Value = m_img.XSize.Value * m_s
                    m_img.YSize.Value = m_img.YSize.Value * m_s
                elif str(imageAxisScale) == "Y":
                    if m_length_y == 0:
                        return
                    m_s = m_new_length/m_length_y
                    m_img.XSize.Value = m_img.XSize.Value * m_s
                elif str(imageAxisScale) == "Z":
                    if m_length_z == 0:
                        return
                    m_s = m_new_length/m_length_z
                    m_img.YSize.Value = m_img.YSize.Value * m_s
                else:
                    m_local_error_msg = "Unable to scale Image: \n"\
                    "The selected Axis must be either: YZ, Y or Z !"
                    printError_msg(m_local_error_msg)
                    return

            elif m_img_angle == 270.0: # XZ plane
                m_length_x = m_points[0].x - m_points[-1].x
                m_length_z = m_points[0].z - m_points[-1].z

                if str(imageAxisScale) == "XZ":
                    if m_length_x == 0:
                        return
                    m_s = m_new_length/m_length_x
                    m_img.XSize.Value = m_img.XSize.Value * m_s
                    m_img.YSize.Value = m_img.YSize.Value * m_s
                elif str(imageAxisScale) == "X":
                    if m_length_x == 0:
                        return
                    m_s = m_new_length/m_length_x
                    m_img.XSize.Value = m_img.XSize.Value * m_s
                elif str(imageAxisScale) == "Z":
                    if m_length_z == 0:
                        return
                    m_s = m_new_length/m_length_z
                    m_img.YSize.Value = m_img.YSize.Value * m_s
                else:
                    m_local_error_msg = "Unable to scale Image: \n"\
                    "The selected Axis must be either: XZ, X or Z !"
                    printError_msg(m_local_error_msg)
                    return
            else:
                pass

            print_msg(result_msg)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def view_align():
    """ Set the current view perpendicular to the selected Face, Edge
    or 2 points selected
    """
    # TODO
    # se mettre tangent a un object...
    error_msg = "Unable to align camera: \nSelect one Face, one Edge or 2 points !"
    m_actDoc = App.activeDocument()
    if m_actDoc.Name:
        # Return a list of Objects for a given document name.
        m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
        m_num = len(m_selEx)
        if m_num >= 1:
            Selected_Points = []
            m_cam = Gui.ActiveDocument.ActiveView.getCameraNode()
            m_camValues = m_cam.position.getValue()
            m_pos = App.Vector((m_camValues[0], m_camValues[1], m_camValues[2],))

            for m_i in range(m_num):
                Sel_i_Object = m_selEx[m_i]
                SubObjects_Inside = Sel_i_Object.SubObjects
                SubObject = SubObjects_Inside[0]

                if SubObject.ShapeType == "Vertex":
                    Selected_Points.append(SubObject)
                    Number_of_Points = len(Selected_Points)
                    if Number_of_Points == 2:
                        m_Vertex1 = Selected_Points[0]
                        m_dist1 = m_pos.sub(Selected_Points[0].Point)
                        m_Vertex2 = Selected_Points[1]
                        m_dist2 = m_pos.sub(Selected_Points[1].Point)

                        # print_msg("dist1=" + str(m_dist1.Length) + "\ndist2=" + str(m_dist2.Length))
                        if m_dist1.Length < m_dist2.Length:
                            alignCamera(m_Vertex1.Point, m_Vertex2.Point, False)
                        else:
                            alignCamera(m_Vertex1.Point, m_Vertex2.Point, True)

                        return

                if SubObject.ShapeType == "Edge":
                    if len(SubObject.Vertexes) >= 2:
                        m_Vertex1 = SubObject.Vertexes[0]
                        m_dist1 = m_pos.sub(SubObject.valueAt(0.0))
                        m_Vertex2 = SubObject.Vertexes[1]
                        m_dist2 = m_pos.sub(SubObject.valueAt(SubObject.Length))

                        # print_msg("dist1=" + str(m_dist1.Length) + "\ndist2=" + str(m_dist2.Length))
                        if m_dist1.Length < m_dist2.Length:
                            alignCamera(m_Vertex1.Point, m_Vertex2.Point, False)
                        else:
                            alignCamera(m_Vertex1.Point, m_Vertex2.Point, True)
                        return
                    else:
                        m_obj = SubObject

                        if hasattr(m_obj, 'Curve'):
                            m_dir = m_obj.Curve.Axis
                            m_c = m_obj.Curve.Center

                            m_edge = Part.makeLine(m_c, m_c.add(m_dir))

                            m_Vertex1 = m_edge.Vertexes[0]
                            m_dist1 = m_pos.sub(m_c)
                            m_Vertex2 = m_edge.Vertexes[1]
                            m_dist2 = m_pos.sub(m_c.add(m_dir))

                            # print_msg("dist1=" + str(m_dist1.Length) + "\ndist2=" + str(m_dist2.Length))
                            if m_dist1.Length < m_dist2.Length:
                                alignCamera(m_Vertex1.Point, m_Vertex2.Point, False)
                            else:
                                alignCamera(m_Vertex1.Point, m_Vertex2.Point, True)
                        return

                if SubObject.ShapeType == "Face":
                    m_faceSel = Sel_i_Object.SubObjects[0]
                    m_dir = m_faceSel.normalAt(0, 0)
                    m_dir = m_faceSel.Surface.Axis
                    m_edge = Part.makeLine(m_faceSel.CenterOfMass, m_faceSel.CenterOfMass.add(m_dir))

                    m_Vertex1 = m_edge.Vertexes[0]
                    m_dist1 = m_pos.sub(m_faceSel.CenterOfMass)
                    m_Vertex2 = m_edge.Vertexes[1]
                    m_dist2 = m_pos.sub(m_faceSel.CenterOfMass.add(m_dir))

                    # print_msg("dist1=" + str(m_dist1.Length) + "\ndist2=" + str(m_dist2.Length))
                    if m_dist1.Length < m_dist2.Length:
                        alignCamera(m_Vertex1.Point, m_Vertex2.Point, False)
                    else:
                        alignCamera(m_Vertex1.Point, m_Vertex2.Point, True)
                else:
                    printError_msg(error_msg)
        else:
            printError_msg(error_msg)


def view_trackCamera():
    """
    Originalcode: Tour camera by Javier Martinez Garcia November 2014
    """
    msg = verbose


    m_sleep = 0.0004
    m_camHeight = 10   # Height of the camera above the track
    m_lookVectorLength = 80   # Distance from next line start where the camera
    # starts to align with new direction

    def edgeDir(edge):
        #m_edgeDir = edge.Vertexes[-1].Point.sub(edge.Vertexes[0].Point).normalize()
        return edge.Vertexes[-1].Point.sub(edge.Vertexes[0].Point).normalize()

    def moveCameraAlong(camera, currPos, currEdge, currEdgeDir):

        while currPos.sub(currEdge.valueAt(0.0)).Length < currEdge.Length:
            currPos = currPos + currEdgeDir
            camera.position.setValue(currPos  + Base.Vector(0, 0, m_camHeight))
            cameraLookVector = currEdgeDir*m_lookVectorLength

            if (cameraLookVector + currPos - currEdge.valueAt(0.0)).Length > currEdge.Length:
                L = (cameraLookVector + (currPos - currEdge.valueAt(0.0))).Length - currEdge.Length
                m_lookVector = nextEdgeDir*L + nextEdge.valueAt(0.0)
            else:
                m_lookVector = currEdge.valueAt(currEdge.Length)

            camera.pointAt(coin.SbVec3f(m_lookVector[0], m_lookVector[1], m_lookVector[2] + m_camHeight), coin.SbVec3f(0, 0, 1))
            Gui.updateGui()
            cam = Gui.ActiveDocument.ActiveView.getCameraNode()
            direction = cam.orientation.getValue().multVec(coin.SbVec3f(0, 0, 1)).getValue()
            print_msg("Camera Orientattion is:" + str(direction))
            time.sleep(m_sleep)



    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select Edge(s) or Wire(s) !"

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    if msg != 0:
        print_msg(str(m_selEx))
    m_sel = Selection(m_selEx)
    if not m_sel:
        print_msg("Unable to create a Selection Object !")
        return None
    if msg != 0:
        print_msg(str(m_sel))

    try:
        Number_of_Edges, Edge_List = m_sel.get_segments(getfrom=["Points", "Segments", "Curves", "Planes", "Objects"])
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))

#         m_edges_num = 0
        if Number_of_Edges >= 1:
#             ## Edge rearrangement inside trajectory list
#             trajectory = []
#             trajectory.append( Edge_List[0] )
#             currentEdge = Edge_List[0]
#             for n in range( len( Edge_List ) ):
#                 for edge in Edge_List:
#                     if edge.valueAt(0.0) == currentEdge.valueAt( currentEdge.Length ):
#                         trajectory.append( edge )
#                         currentEdge = edge
#                         break
#             Edge_List = trajectory
#             m_edges_num = m_edges_num + len(Edge_List)

            m_camera = Gui.ActiveDocument.ActiveView.getCameraNode()

            for i in range(Number_of_Edges - 1):
                m_currEdge = Edge_List[i]
                m_currEdgeDir = edgeDir(m_currEdge)
                m_currPos = m_currEdge.valueAt(0.0)

                m_nextEdge = Edge_List[i+1]
                m_nextEdgeDir = edgeDir(m_nextEdge)

                if msg != 0:
                    print_msg("m_currEdge=" + str(m_currEdge))
                    print_msg("m_currEdgeDir=" + str(m_currEdgeDir))
                    print_point(m_currPos, "m_currPos ")
                    print_msg("m_nextEdge=" + str(m_nextEdge))
                    print_msg("m_nextEdgeDir=" + str(m_nextEdgeDir))

                moveCameraAlong(m_camera, m_currPos, m_currEdge, m_currEdgeDir)

                while m_currPos.sub(m_currEdge.valueAt(0.0)).Length < m_currEdge.Length:
                    currPos = currPos + currEdgeDir
                    m_camera.position.setValue(currPos  + Base.Vector(0, 0, m_camHeight))

                    m_cameraLookVector = currEdgeDir*m_lookVectorLength

                    if (m_cameraLookVector + currPos - currEdge.valueAt(0.0)).Length > currEdge.Length:
                        L = (m_cameraLookVector + (currPos - currEdge.valueAt(0.0))).Length - currEdge.Length
                        m_lookVector = nextEdgeDir*L + nextEdge.valueAt(0.0)
                    else:
                        m_lookVector = currEdge.valueAt(currEdge.Length)

                    m_camera.pointAt(coin.SbVec3f(m_lookVector[0], m_lookVector[1], m_lookVector[2] + m_camHeight), coin.SbVec3f(0, 0, 1))
                    Gui.updateGui()
                    cam = Gui.ActiveDocument.ActiveView.getCameraNode()
                    direction = cam.orientation.getValue().multVec(coin.SbVec3f(0, 0, 1)).getValue()
                    print_msg("Camera Orientattion is:" + str(direction))
                    time.sleep(m_sleep)

            while currPos.sub(currEdge.valueAt(0.0)).Length < currEdge.Length:
                currPos = currPos + currEdgeDir
                m_camera.position.setValue(currPos  + Base.Vector(0, 0, m_camHeight))

                m_lookVector = currEdge.valueAt(currEdge.Length)

                m_camera.pointAt(coin.SbVec3f(m_lookVector[0], m_lookVector[1], m_lookVector[2] + m_camHeight), coin.SbVec3f(0, 0, 1))
                Gui.updateGui()
                cam = Gui.ActiveDocument.ActiveView.getCameraNode()
                direction = cam.orientation.getValue().multVec(coin.SbVec3f(0, 0, 1)).getValue()
                print_msg("Camera Orientattion is:" + str(direction))
                time.sleep(m_sleep)
        else:
            printError_msg("No Edge was selected !")
    except:
        printError_msg(error_msg)


def view_trackCamera_old():
    """
    Originalcode: Tour camera by Javier Martinez Garcia November 2014
    """
    msg = verbose

    m_sleep = 0.0004
    m_camHeight = 10   # Height of the camera above the track
    m_lookVectorLength = 80   # Distance from next line start where the camera
    # starts to align with new direction
    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select Edge(s) or Wire(s) !"

    m_actDoc = App.activeDocument()
    if m_actDoc.Name:
        m_sel = Gui.Selection.getSelection(m_actDoc.Name)

    try:
        SelectedObjects = m_sel
        if msg != 0:
            print_msg("SelectedObjects=" + str(SelectedObjects))

        m_edges_num = 0
        for m_obj in SelectedObjects:
            if msg != 0:
                print_msg("m_obj.Shape=" + str(m_obj.Shape))
            if not (getShapeType(m_obj.Shape) == "Wire" or getShapeType(m_obj.Shape) == "Edge"):
                continue
            if msg != 0:
                print_msg("m_obj.Shape.Edges=" + str(m_obj.Shape.Edges))
            if len(m_obj.Shape.Edges) == 0:
                continue
            Edge_List = m_obj.Shape.Edges

            ## Edge rearrangement inside trajectory list
            trajectory = []
            trajectory.append(Edge_List[0])
            currentEdge = Edge_List[0]
            for n in range(len(Edge_List)):
                for edge in Edge_List:
                    if edge.valueAt(0.0) == currentEdge.valueAt(currentEdge.Length):
                        trajectory.append(edge)
                        currentEdge = edge
                        break
            Edge_List = trajectory
            m_edges_num = m_edges_num + len(Edge_List)
            m_camera = Gui.ActiveDocument.ActiveView.getCameraNode()
            currEdge = Edge_List[0]
            currEdgeDir = currEdge.Vertexes[-1].Point.sub(currEdge.Vertexes[0].Point).normalize()
            currPos = currEdge.valueAt(0.0)
            for i in range(len(m_obj.Shape.Edges) - 1):
                currEdge = Edge_List[i]
                # if msg != 0:
                # print_msg("currEdge=" + str(currEdge))
                currEdgeDir = currEdge.Vertexes[-1].Point.sub(currEdge.Vertexes[0].Point).normalize()
                # if msg != 0:
                    # print_msg("currEdgeDir=" + str(currEdgeDir))
                nextEdge = Edge_List[i+1]
                # if msg != 0:
                    # print_msg("nextEdge=" + str(nextEdge))
                nextEdgeDir = nextEdge.Vertexes[-1].Point.sub(nextEdge.Vertexes[0].Point).normalize()
                # if msg != 0:
                    # print_msg("nextEdgeDir=" + str(nextEdgeDir))
                currPos = currEdge.valueAt(0.0)
                # if msg != 0:
                    # print_point(currPos, "currPos ")

                while currPos.sub(currEdge.valueAt(0.0)).Length < currEdge.Length:
                    currPos = currPos + currEdgeDir
                    m_camera.position.setValue(currPos  + Base.Vector(0, 0, m_camHeight))
                    m_cameraLookVector = currEdgeDir*m_lookVectorLength
                    if (m_cameraLookVector + currPos - currEdge.valueAt(0.0)).Length > currEdge.Length:
                        L = (m_cameraLookVector + (currPos - currEdge.valueAt(0.0))).Length - currEdge.Length
                        m_lookVector = nextEdgeDir*L + nextEdge.valueAt(0.0)
                    else:
                        m_lookVector = currEdge.valueAt(currEdge.Length)
                    m_camera.pointAt(coin.SbVec3f(m_lookVector[0], m_lookVector[1], m_lookVector[2] + m_camHeight), coin.SbVec3f(0, 0, 1))
                    Gui.updateGui()
                    cam = Gui.ActiveDocument.ActiveView.getCameraNode()
                    direction = cam.orientation.getValue().multVec(coin.SbVec3f(0, 0, 1)).getValue()
                    print_msg("Camera Orientattion is:" + str(direction))
                    time.sleep(m_sleep)

            while currPos.sub(currEdge.valueAt(0.0)).Length < currEdge.Length:
                currPos = currPos + currEdgeDir
                m_camera.position.setValue(currPos  + Base.Vector(0, 0, m_camHeight))
                m_lookVector = currEdge.valueAt(currEdge.Length)
                m_camera.pointAt(coin.SbVec3f(m_lookVector[0], m_lookVector[1], m_lookVector[2] + m_camHeight), coin.SbVec3f(0, 0, 1))
                Gui.updateGui()
                cam = Gui.ActiveDocument.ActiveView.getCameraNode()
                direction = cam.orientation.getValue().multVec(coin.SbVec3f(0, 0, 1)).getValue()
                print_msg("Camera Orientattion is:" + str(direction))
                time.sleep(m_sleep)
        if m_edges_num == 0:
            printError_msg("No Edge was selected !")
    except:
        printError_msg(error_msg)

def angleCutObject(value):
    """ Respond to the change in angle value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_angleCutObject
        if str(value) == '-':
            return
        m_angleCutObject = float(value)
        print_msg("New angle in degrees is:" + str(m_angleCutObject))
    except ValueError:
        printError_msg("Angle must be valid number !")


def thicknessCutObject(value):
    """ Respond to the change in extension value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_thicknessCutObject
        if str(value) == '-':
            return
        m_thicknessCutObject = float(value)
        print_msg("New thickness is:" + str(m_thicknessCutObject))
    except ValueError:
        printError_msg("Thickness must be valid number !")


def cut_selectObject():
    """ Select the Object to cut.    
    """
    global myDialog
    global m_cut_selectObjects
    msg = verbose

    error_msg = "Select in order:\n" + \
                "First, one Object to cut and click 'Select Object' button,\n" + \
                "Second, one cutting Line and click 'Select Cut Line' button,\n" + \
                "Last, a reference Plane and click 'Select Ref. Plane' button!"
    m_num, m_selEx, m_objs, m_objNames = get_InfoObjects(info=msg, printError=False)
    if m_num == 1:
        m_cut_selectObjects.append([m_selEx, m_objs, m_objNames])
        m_text = str(m_objNames[0])
        myDialog.ui.info_cut_select_object.setText(_translate("Form", m_text, None))

    else:
        printError_msg(error_msg)
        return

    # Activate the button_cut_select_line
    myDialog.ui.button_cut_select_line.setEnabled(True)


def cut_selectLine():
    """ Select the Line to cut the Object along.
    """
    global myDialog
    global m_cut_selectObjects
    msg = verbose

    error_msg = "Select in order:\n" + \
                "First, one Object to cut and click 'Select Object' button,\n" + \
                "Second, one cutting Line and click 'Select Cut Line' button,\n" + \
                "Last, a reference Plane and click 'Select Ref. Plane' button!"
    # TODO: check if really a line
    m_num, m_selEx, m_objs, m_objNames = get_InfoObjects(info=msg, printError=False)
    if m_num == 1:
        m_cut_selectObjects.append([m_selEx, m_objs, m_objNames])
        m_text = str(m_objNames[0])
        myDialog.ui.info_cut_select_axis.setText(_translate("Form", m_text, None))

    else:
        printError_msg(error_msg)
        return

    # Activate the button_cut_select_plane
    myDialog.ui.button_cut_select_plane.setEnabled(True)


def cut_selectPlane():
    """ Select the reference Plane to cut the Object from.
    """
    global myDialog
    global m_cut_selectObjects
    msg = verbose

    error_msg = "Select in order:\n" + \
                "First, one Object to cut and click 'Select Object' button,\n" + \
                "Second, one cutting Line and click 'Select Cut Line' button,\n" + \
                "Last, a reference Plane and click 'Select Ref. Plane' button!"
    # TODO: check if really a plane
    m_num, m_selEx, m_objs, m_objNames = get_InfoObjects(info=msg, printError=False)
    if m_num == 1:
        m_cut_selectObjects.append([m_selEx, m_objs, m_objNames])
        m_text = str(m_objNames[0])
        myDialog.ui.info_cut_select_plane.setText(_translate("Form", m_text, None))
    else:
        printError_msg(error_msg)
        return

    # Activate the button_cut_apply
    myDialog.ui.button_cut_apply.setEnabled(True)


def cut_reset():
    """ Select the reference Plane to cut the Object from.
    """
    global myDialog
    global m_cut_selectObjects
    del m_cut_selectObjects[:]
    m_text = ""

    # deActivate the button_cut_select_line
    myDialog.ui.button_cut_select_line.setEnabled(False)
    # deActivate the button_cut_select_plane
    myDialog.ui.button_cut_select_plane.setEnabled(False)
    # deActivate the button_cut_apply
    myDialog.ui.button_cut_apply.setEnabled(False)
    myDialog.ui.info_cut_select_object.setText(_translate("Form", m_text, None))
    myDialog.ui.info_cut_select_axis.setText(_translate("Form", m_text, None))
    myDialog.ui.info_cut_select_plane.setText(_translate("Form", m_text, None))


def plot_cutObject():
    """ Cut an object in 2 pieces, based on a cut line, a plane,
    an angle regarding this plane and a thickness of the line.
    """
    global myDialog
    global m_cut_selectObjects
    global m_angleCutObject
    global m_thicknessCutObject
    global verbose
    msg = verbose

    createFolders('WorkObjects')
    error_msg = "Select in order:\n" + \
                "First, one Object to cut and click 'Select Object' button,\n" + \
                "Second, one cutting Line and click 'Select Cut Line' button,\n" + \
                "Last, a reference Plane and click 'Select Ref. Plane' button!"
    result_msg = "Cut object done into WorkFeatures/WorkObjects/"
    name = "Part"
    part = "Part::Feature"

    m_actDoc = get_ActiveDocument(info=0)
    if m_actDoc is None:
        return

    m_num = len(m_cut_selectObjects)
    if m_num == 3:
        #[m_selEx, m_objs, m_objNames]
        # Get the Object
        m_cut_obj = m_cut_selectObjects[0]
        # Get the Line
        m_cut_line = m_cut_selectObjects[1]
        # Get the Plane
        m_ref_plane = m_cut_selectObjects[2]
        if msg == 1:
            print_msg("Object to cut =" + str(m_cut_obj[2]) +
                      "\nCutting Line =" + str(m_cut_line[2]) +
                      "\nRef. Plane   =" + str(m_ref_plane[2]))
        # Check if we have correct shapes
        SubObjects_Inside = m_cut_line[0][0].SubObjects
        SubObject = SubObjects_Inside[0]
        if msg == 1:
            print_msg("SubObject = " + str(SubObject))
        if SubObject.ShapeType != "Edge":
            printError_msg(error_msg)
            return
        m_Edge = SubObject
        SubObjects_Inside = m_ref_plane[0][0].SubObjects
        SubObject = SubObjects_Inside[0]
        if msg == 1:
            print_msg("SubObject = " + str(SubObject))
        if SubObject.ShapeType != "Face":
            printError_msg(error_msg)
            return
        m_Plane = SubObject
        Ref_Plane = m_Plane
        Plane_Point = Ref_Plane.CenterOfMass
        Plane_Normal = Ref_Plane.normalAt(0, 0)
        m_Obj = m_cut_obj[1][0]
        try:
            m_Obj.Shape
        except:
            printError_msg("This object has no attribute 'Shape' ! Select another one !\n")
            return
        m_Obj_name = m_cut_obj[2][0]
        try:
            m_dir = str(m_Obj_name) + "_Cut"
            m_newdir = App.ActiveDocument.getObject("WorkObjects").newObject("App::DocumentObjectGroup", str(m_dir))
            m_dir = m_newdir.Name
        except:
            printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
            return

        if msg == 1:
            print_msg("Processing: " + str(m_Obj_name))
            print_msg("Into the group: " + str(m_dir))

        # Get Line's limits
        Point_A = m_Edge.valueAt(0.0)
        Point_B = m_Edge.valueAt(m_Edge.Length)
        Point_C = centerLinePoint(m_Edge)
        if msg == 1:
            print_msg("\nGet Line's limits")
            Point_A_User_Name = plot_point(Point_A, part, "Point_A", grp=str(m_dir))
            print_point(Point_A, msg=str(Point_A_User_Name) + ", (internal Point_A): ")
            Point_B_User_Name = plot_point(Point_B, part, "Point_B", grp=str(m_dir))
            print_point(Point_B, msg=str(Point_B_User_Name) + ", (internal Point_B): ")
            Point_C_User_Name = plot_point(Point_C, part, "Point_C", grp=str(m_dir))
            print_point(Point_C, msg=str(Point_C_User_Name) + ", (internal Point_C): ")
            print_msg("Length: " + str(m_Edge.Length))


        # Get object's limits
        m_xmax, m_xmin, m_ymax, m_ymin, m_zmax, m_zmin = minMaxObjectsLimits(m_cut_obj[1][0:], info=0)

        # Length of BoundBox in X, Y and Z dimensions
        m_length_X = m_xmax - m_xmin
        m_length_Y = m_ymax - m_ymin
        m_length_Z = m_zmax - m_zmin
        m_length_list = [m_length_X, m_length_Y, m_length_Z]
        m_length_max = max(m_length_list)
        m_ori_X = m_xmin
        m_ori_Y = m_ymin
        m_ori_Z = m_zmin

        # Get Points, Edges, Faces from the bounding box Object dimensions
        Points, BB_Edges, Faces = get_all_from_bounding_box(m_ori_X, m_ori_Y, m_ori_Z, m_length_X, m_length_Y, m_length_Z, info=0, plot=0)

# ==============================================================================
        # Looking for the min distance between center of line and center
        # of faces of the bounding box. And selection of this Plane if quite
        # Parallel to Ref. Plane
        _, max_val = init_min_max()
        m_min_distance = max_val
        Plane_Point1 = None
        Plane_Normal1 = None
        Selected_Plane1 = Faces[0][5]
        for m_i in range(len(Faces)):
            #( 3,  0,  1, 2, (BB_Edges[3][3],BB_Edges[0][3],BB_Edges[1][3],BB_Edges[2][3]), face, mid_point, length )
            m_distance = distanceBetween(Point_C, Faces[m_i][6])
            m_angle = Faces[m_i][5].normalAt(0, 0).getAngle(Plane_Normal)
            if msg == 1:
                print_msg("Distance between Point_C and face of bounding box: " + str(m_distance))
                print_msg("Angle between Ref Plane and selected bounding box Plane: " + str(math.fmod(math.degrees(m_angle), 180.)))
            if m_distance < m_min_distance and math.fmod(math.degrees(m_angle), 180.) <= 45.:
                m_min_distance = m_distance
                Selected_Plane1 = Faces[m_i][5]
                Plane_Point1 = Faces[m_i][6]
                Plane_Normal1 = Selected_Plane1.normalAt(0, 0)
                if msg == 1:
                    print_msg("Distance selected: " + str(m_distance))
                    print_msg("Angle selected: " + str(math.fmod(math.degrees(m_angle), 180.)))

        if Plane_Point1 is None:
            printError_msg("Plane_Point1 is Null!")
            return
        if Plane_Normal1 is None:
            printError_msg("Plane_Normal1 is Null!")
            return
        if msg == 1:
            print_msg("\nGet Bounding Planes info")
            print_msg("MIN Distance: " + str(m_min_distance))
            Point_Face01_User_Name = plot_point(Plane_Point1, part, "Point_Face01", grp=str(m_dir))
            print_point(Plane_Point1, msg=str(Point_Face01_User_Name) + ", (internal Point_Face01): ")

# ==============================================================================

# ==============================================================================
        # Select the second plane of the bounding box parallel to this first one
        Plane_Point2 = None
        Plane_Normal2 = None
        Selected_Plane2 = Faces[0][5]
        for m_i in range(len(Faces)):
            m_angle = Faces[m_i][5].normalAt(0, 0).getAngle(Plane_Normal1)
            if msg == 1:
                print_msg("Angle First Plane and selected bounding box Plane: " + str(math.fmod(math.degrees(m_angle), 180.)))
            if Faces[m_i][5] != Selected_Plane1 and math.fmod(math.degrees(m_angle), 180.) <= .5:
#                cross_product = Plane_Normal_new .cross(Plane_Normal1)
#                if abs(cross_product.x) <= 1e-12 and abs(cross_product.y) <= 1e-12 and abs(cross_product.z) <= 1e-12:
                Selected_Plane2 = Faces[m_i][5]
                Plane_Point2 = Faces[m_i][6]
                Plane_Normal2 = Selected_Plane2.normalAt(0, 0)
                break
        if Plane_Point2 is None:
            printError_msg("Plane_Point2 is Null!")
            return
        if Plane_Normal2 is None:
            printError_msg("Plane_Normal2 is Null!")
            return
        if msg == 1:
            Point_Face02_User_Name = plot_point(Plane_Point2, part, "Point_Face02", grp=str(m_dir))
            print_point(Plane_Point2, msg=str(Point_Face02_User_Name) + ", (internal Point_Face02): ")

# ==============================================================================

# ==============================================================================
        # Build The Plane Crossing the Line and making an angle with the Ref. Plane

        # Projection of A and B onto the Ref Plane A0 and B0
        Vector_A = Point_A + Plane_Normal
        Vector_B = Point_B + Plane_Normal
        Point_A0 = intersecLinePlane(Point_A, Vector_A, Plane_Normal, Plane_Point, info=0)
        Point_B0 = intersecLinePlane(Point_B, Vector_B, Plane_Normal, Plane_Point, info=0)
        # Plot them if needed
        if msg == 1:
            print_msg("\nProjection of A and B onto the Ref Plane in A0 and B0")
            Point_A0_User_Name = plot_point(Point_A0, part, "Point_A0", grp=str(m_dir))
            Point_B0_User_Name = plot_point(Point_B0, part, "Point_B0", grp=str(m_dir))
            print_point(Point_A0, msg=str(Point_A0_User_Name) + ", (internal Point_A0): ")
            print_point(Point_B0, msg=str(Point_B0_User_Name) + ", (internal Point_B0): ")

        AxisA0B0_User_Name, AxisA0B0 = plot_axis(Point_A0, Point_B0, part, "LineA0-B0", grp=str(m_dir))

        Point_A1 = Point_A0
        Point_B1 = Point_B0
        # Get intersections of this line with the Edges of the Ref. Plane
        # To update  points A0 and B0 into A1 and B1
        Number_of_Intersec, Intersec_Points = intersecPoints(AxisA0B0.Shape, Ref_Plane, info=0)
        if msg == 1:
            print_msg("\nIntersections of A0B0 line with the edges of Ref. Plane: A1 and B1")
            print_msg("Number_of_Intersec = " + str(Number_of_Intersec))
        if Number_of_Intersec == 0:
            printError_msg("No intersection point between projection of the Line and Object !")
            return
        if Number_of_Intersec == 1:
            printError_msg("Only one intersection point between projection of the Line and Object ! No cut possible !")
            return
        if Number_of_Intersec == 2:
            Point_A1 = Intersec_Points[0]
            Point_B1 = Intersec_Points[1]
            if msg == 1:
                Point_A1_User_Name = plot_point(Point_A1, part, "Point_A1", grp=str(m_dir))
                print_point(Point_A1, msg=str(Point_A1_User_Name) + ", (internal Point_A1): ")
                Point_B1_User_Name = plot_point(Point_B1, part, "Point_B1", grp=str(m_dir))
                print_point(Point_B1, msg=str(Point_B1_User_Name) + ", (internal Point_B1): ")

        # Line onto Ref Plane
        Edge_Vector = Point_B1 - Point_A1
        Edge_Length = m_length_max * 1.5 * 2
        # Mid point
        Point_MidPoint = Point_B1 + Point_A1
        Point_MidPoint = Point_MidPoint.multiply(0.5)
        # Attachment Point
        Attach_Point = Point_MidPoint
        # Normal
        Vector_Normal = Edge_Vector.cross(Plane_Normal)

        # Build a cutting Plane
        if msg == 1:
            print_msg("\nBuild a cutting Plane")

        Plane_Point = Attach_Point
        Plane_Normal = Edge_Vector.cross(Plane_Normal)
        # Get projection of Plane_Point1 to cutting Plane
        C1 = Plane_Point1
        B1 = C1 + Plane_Normal
        T1 = intersecLinePlane(C1, B1, Plane_Normal, Plane_Point, info=0)
        # Get projection of Plane_Point2 to cutting Plane
        C2 = Plane_Point2
        B2 = C2 + Plane_Normal
        T2 = intersecLinePlane(C2, B2, Plane_Normal, Plane_Point, info=0)
        # New Attachment Point
        Attach_Point = T2 - T1
        Attach_Point = Attach_Point.multiply(0.5)
        Attach_Point = Point_MidPoint + Attach_Point
        # Build a cutting Plane
        cutting_plane = None
        Plane_cutting_User_Name, cutting_plane = plot_plane(Edge_Length, Edge_Length, Attach_Point, Vector_Normal, part, "Cutting_plane", grp=str(m_dir))
        if cutting_plane is None:
            printError_msg("Unable to create Cutting plane !")
            return

        # Rotate the cutting Plane if needed
        if m_angleCutObject != 0.0:
            rot_angle = m_angleCutObject
            rot_axis = Edge_Vector
            m_center = Point_MidPoint
            m_rot = App.Rotation(rot_axis, rot_angle)
            if msg == 1:
                print_msg("rotation =       " + str(m_rot))
                print_msg("rotation axis  = " + str(rot_axis))
            m_place = App.Placement(cutting_plane.Placement)
            m_base1 = m_place.Base
            if msg == 1:
                print_msg("base1  = " + str(m_base1))
            m_rot1 = m_place.Rotation
            if msg == 1:
                print_msg("rot1  = " + str(m_rot1))
            m_rot = m_rot.multiply(m_rot1)
            m_newplace = App.Placement(m_base1, m_rot, m_center-m_base1)
            cutting_plane.Placement = m_newplace

        Attach_Point = cutting_plane.Shape.CenterOfMass
        Vector_Normal = cutting_plane.Shape.normalAt(0, 0)
        # Duplicate the cutting Plane and move if thickness not null
        if m_thicknessCutObject != 0.0:
            Attach_Point2 = Vector_Normal - Attach_Point
            Attach_Point2 =  Attach_Point + Attach_Point2.normalize().multiply(0.5 * m_thicknessCutObject)
            # Build a cutting Plane
            cutting_plane2 = None
            Plane_cutting2_User_Name, cutting_plane2 = plot_plane(Edge_Length, Edge_Length, Attach_Point2, Vector_Normal, part, "Cutting_plane", grp=str(m_dir))
            if cutting_plane2 is None:
                printError_msg("Unable to create Cutting plane 2 !")
                return

            Attach_Point3 = Vector_Normal - Attach_Point
            Attach_Point3 =  Attach_Point + Attach_Point3.normalize().multiply(-0.5 * m_thicknessCutObject)
            # Build a cutting Plane
            cutting_plane3 = None
            Plane_cutting3_User_Name, cutting_plane3 = plot_plane(Edge_Length, Edge_Length, Attach_Point3, Vector_Normal, part, "Cutting_plane", grp=str(m_dir))
            if cutting_plane3 is None:
                printError_msg("Unable to create Cutting plane 3 !")
                return





# ==============================================================================

        # Just need to find the intersection line between cutting Plane and
        # the object (nearest bounding Plane)
        cut_plane = cutting_plane.Shape
        near_plane = Selected_Plane1
        if msg == 1:
            print_msg(str(cut_plane))
            print_msg(str(near_plane))

        cut_plane_Normal = cut_plane.normalAt(0, 0)
        near_plane_Normal = near_plane.normalAt(0, 0)
        if msg == 1:
            print_msg("\nFind the intersection line between cutting Plane and the object (nearest plane of bounding box)")
            print_point(cut_plane_Normal, msg="Normal1: ")
            print_point(near_plane_Normal, msg="Normal2: ")

        cut_plane_Point  = cut_plane.CenterOfMass
        near_plane_Point = near_plane.CenterOfMass
        if msg == 1:
            print_point(cut_plane_Point, msg="cut_plane_Point: ")
            print_point(near_plane_Point, msg="near_plane_Point: ")

        Axis_dir = intersecPlanePlane(cut_plane_Normal, cut_plane_Point, near_plane_Normal, near_plane_Point, info=msg)

        if Axis_dir is None:
            printError_msg("Not able to find an intersection between the cutting Plane and the Object !")
            return

        # Intersection Line found
        Intersecline = None
        Vertx = []
        Distx = []
        Vertx_names = []

        _, max_val = init_min_max()
        dist_to_center_min = max_val
        # For the first plane look after all edges and look at
        # intersections of the edges with the second plane
        Number_of_Edges = len(cut_plane.Edges)
        for j in range(Number_of_Edges):
            A = cut_plane.Edges[j].valueAt(0.0)
            B = cut_plane.Edges[j].valueAt(cut_plane.Edges[j].Length)
            T = intersecLinePlane(A, B, near_plane_Normal, near_plane_Point, info=0)
            if T is not None:
                D = T - cut_plane_Point
                dist_to_center = math.sqrt(D.dot(D))
                if dist_to_center < dist_to_center_min:
                    dist_to_center_min = dist_to_center
                    Vertx.append(T)
                    Distx.append(dist_to_center)

# ==============================================================================
#         Number_of_Edges = len(near_plane.Edges)
#         dist_to_center_min = max_val
#         for jj in range(Number_of_Edges):
#             A = near_plane.Edges[jj].valueAt( 0.0 )
#             B = near_plane.Edges[jj].valueAt(near_plane.Edges[jj].Length )
#             T = intersecLinePlane(A, B, cut_plane_Normal, cut_plane_Point, info=0)
#             if T is not None:
#                 D = T - near_plane_Point
#                 dist_to_center = math.sqrt(D.dot(D))
#                 if dist_to_center < dist_to_center_min:
#                     dist_to_center_min = dist_to_center
#                     Vertx.append(T)
#                     Distx.append(dist_to_center)
# ==============================================================================

        if msg == 1:
            for k in range(len(Vertx)):
                Point_User_Name = plot_point(Vertx[k], part, "Edge_point", grp=str(m_dir))
                Vertx_names.append(str(Point_User_Name))
                print_point(Vertx[k], msg=str(Point_User_Name) + ", (internal Edge_point): ")

        C = meanVectorsPoint(Vertx, info=0)

        if msg == 1:
            Edge_point_C_User_Name = plot_point(C, part, "Edge_point_C", grp=str(m_dir))
            print_point(C, msg=str(Edge_point_C_User_Name) + ", (internal Edge_point_C): ")

        if C is not None:
            extension = max(Distx)
            A = C - Axis_dir.normalize().multiply(extension * 1.5)
            B = C + Axis_dir
            IntersecLine_User_Name, Intersecline = plot_axis(A, B, part, "IntersecLine", grp=str(m_dir))
        # Look for A2 and B2 intersection of Intersecline and edges of the object
        # (nearest plane of bounding box: Selected_Plane1)
        Point_A2 = Point_A1
        Point_B2 = Point_B1
        # Get intersections of this line with the Edges of the Face
        # To update  Point_A1 and Point_B1 into Point_A2 and Point_B2
        Number_of_Intersec, Intersec_Points = intersecPoints(Intersecline.Shape, Selected_Plane1, info=0)
        if msg == 1:
            print_msg("\nLook for A2 and B2 intersection of Intersecline and edges of the object (nearest plane of bounding box)")
            print_msg("Number_of_Intersec = " + str(Number_of_Intersec))

        if Number_of_Intersec == 0:
            printError_msg("No intersection point between Intersecline and Object !")
            return
        if Number_of_Intersec == 1:
            printError_msg("Only one intersection point between Intersecline and Object ! No cut possible !")
            return
        if Number_of_Intersec == 2:
            Point_A2 = Intersec_Points[0]
            Point_B2 = Intersec_Points[1]
            if msg == 1:
                print_msg("Intersections of Intersecline with the Edges of the Face:")
                Point_A2_User_Name = plot_point(Intersec_Points[0], part, "Point_A2", grp=str(m_dir))
                print_point(Point_A2, msg=str(Point_A2_User_Name) + ", (internal Point_A2): ")
                Point_B2_User_Name = plot_point(Intersec_Points[1], part, "Point_B2", grp=str(m_dir))
                print_point(Point_B2, msg=str(Point_B2_User_Name) + ", (internal Point_B2): ")

        # Now we need to extrude the cutting Plane
        BB_edges_names = []
        # First get 2 Vectors in which direction to extrude from Point_A2
        Vector_extrude1 = App.Vector(0.0, 0.0, 0.0)
        Vector_extrude2 = App.Vector(0.0, 0.0, 0.0)
        for m_i in range(len(BB_Edges)):
            # ( 2, 6, (Points[2], Points[6]), edge, mid_point, length )
            if msg == 1:
                Axis_User_Name, _ = plot_axis(BB_Edges[m_i][2][0], BB_Edges[m_i][2][1], part, "bb_edge", grp=str(m_dir))
                BB_edges_names.append(str(Axis_User_Name))
            if colinearVectors(BB_Edges[m_i][2][0], Point_A2, BB_Edges[m_i][2][1], info=0, tolerance=1e-10):
                # Plot them
                if msg == 1:
                    Point_A2_prime_User_Name = plot_point(BB_Edges[m_i][2][0], part, "Point_A2_prime", grp=str(m_dir))
                    print_point(BB_Edges[m_i][2][0], msg=str(Point_A2_prime_User_Name) + ", (internal Point_A2_prime): ")
                    Point_A2_second_User_Name = plot_point(BB_Edges[m_i][2][1], part, "Point_A2_second", grp=str(m_dir))
                    print_point(BB_Edges[m_i][2][1], msg=str(Point_A2_second_User_Name) + ", (internal Point_A2_second): ")

                Vector_extrude1 = BB_Edges[m_i][2][0] - Point_A2
                Vector_extrude2 = Point_A2 - BB_Edges[m_i][2][1]

        if Vector_extrude1 == App.Vector(0.0, 0.0, 0.0):
            for m_i in range(len(BB_Edges)):
                # ( 2, 6, (Points[2], Points[6]), edge, mid_point, length )
                if msg == 1:
                    Axis_User_Name, _ = plot_axis(BB_Edges[m_i][2][0], BB_Edges[m_i][2][1], part, "bb_edge", grp=str(m_dir))
                    BB_edges_names.append(str(Axis_User_Name))
                if colinearVectors(BB_Edges[m_i][2][0], Point_B2, BB_Edges[m_i][2][1], info=0, tolerance=1e-10):
                    # Plot them
                    if msg == 1:
                        Point_A2_prime_User_Name = plot_point(BB_Edges[m_i][2][0], part, "Point_B2_prime", grp=str(m_dir))
                        print_point(BB_Edges[m_i][2][0], msg=str(Point_A2_prime_User_Name) + ", (internal Point_B2_prime): ")
                        Point_A2_second_User_Name = plot_point(BB_Edges[m_i][2][1], part, "Point_B2_second", grp=str(m_dir))
                        print_point(BB_Edges[m_i][2][1], msg=str(Point_A2_second_User_Name) + ", (internal Point_B2_second): ")

                    Vector_extrude1 = BB_Edges[m_i][2][0] - Point_B2
                    Vector_extrude2 = Point_B2 - BB_Edges[m_i][2][1]

            if Vector_extrude1 == App.Vector(0.0, 0.0, 0.0):
                printError_msg("Vector_extrude1 is Null!")
                return

        if Vector_extrude2 == App.Vector(0.0, 0.0, 0.0):
            printError_msg("Vector_extrude2 is Null!")
            return

        # Get the max length of the bounding box
        Vector_extrude1 = Vector_extrude1.normalize().multiply(m_length_max)
        Vector_extrude2 = Vector_extrude2.normalize().multiply(m_length_max)
        # Extrude a bit after the extreme edges with a 45 deg angle (diagonal)
        Vector_extrude1 = Vector_extrude1.multiply(1.5).multiply(2)
        Vector_extrude2 = Vector_extrude2.multiply(-1.5).multiply(2)
        if msg == 1:
            print_msg("Vector_extrude1 =       " + str(Vector_extrude1))
            print_msg("Vector_extrude2 =       " + str(Vector_extrude2))

        # Get the shape of the cutting Plane
        plane_shape = cutting_plane.Shape
        if msg == 1:
            print_msg("plane      =       " + str(cutting_plane))
            print_msg("plane_shape =       " + str(plane_shape))

        # We extrude in the first direction
        extrude1 = plane_shape.extrude(Vector_extrude1)
        if msg == 1:
            print_msg("extrude1  =       " + str(extrude1))
        m_extrude1_name = str(m_Obj_name) + "_" + str(name) + "extrude01"
        Extrude1 = App.ActiveDocument.addObject(part, m_extrude1_name)
        App.ActiveDocument.getObject(str(m_dir)).addObject(Extrude1)
        m_extrude1_name = Extrude1.Name
        Extrude1.Shape = extrude1

        # We extrude in the second direction
        extrude2 = plane_shape.extrude(Vector_extrude2)
        if msg == 1:
            print_msg("extrude2  =       " + str(extrude2))
        m_extrude2_name = str(m_Obj_name) + "_" + str(name) + "extrude02"
        Extrude2 = App.ActiveDocument.addObject(part, m_extrude2_name)
        App.ActiveDocument.getObject(str(m_dir)).addObject(Extrude2)
        m_extrude2_name = Extrude2.Name
        Extrude2.Shape = extrude2

        # if thickness not null
        if m_thicknessCutObject != 0.0:
            plane_shape2 = cutting_plane2.Shape
            plane_shape3 = cutting_plane3.Shape
            Vector_extrude3 = Attach_Point3 - Attach_Point2
            Vector_extrude4 = Attach_Point2 - Attach_Point3

            extrude1b = plane_shape2.extrude(Vector_extrude3)
            if msg == 1:
                print_msg("extrude1b  =       " + str(extrude1b))
            m_extrude1b_name = str(m_Obj_name) + "_" + str(name) + "extrude01b"
            Extrude1b = App.ActiveDocument.addObject(part, m_extrude1b_name)
            App.ActiveDocument.getObject(str(m_dir)).addObject(Extrude1b)
            m_extrude1b_name = Extrude1b.Name
            Extrude1b.Shape = extrude1b

            extrude2b = plane_shape3.extrude(Vector_extrude4)
            if msg == 1:
                print_msg("extrude2b  =       " + str(extrude2b))
            m_extrude2b_name = str(m_Obj_name) + "_" + str(name) + "extrude02b"
            Extrude2b = App.ActiveDocument.addObject(part, m_extrude2b_name)
            App.ActiveDocument.getObject(str(m_dir)).addObject(Extrude2b)
            m_extrude2b_name = Extrude2b.Name
            Extrude2b.Shape = extrude2b
        # Let's duplicate the Object
        m_obj2 = m_actDoc.copyObject(m_Obj)
        m_obj3 = m_actDoc.copyObject(m_Obj)
        App.ActiveDocument.getObject(str(m_dir)).addObject(m_obj2)
        App.ActiveDocument.getObject(str(m_dir)).addObject(m_obj3)
        Obj2_User_Name = m_obj2.Name
        Obj3_User_Name = m_obj3.Name

        # and Split in two parts
        m_diff1_name = str(m_Obj_name) + "_01_" + str(name)
        Diff1 = App.ActiveDocument.addObject(part, m_diff1_name)
        Diff1.Shape = m_obj2.Shape.cut(extrude1)
        if m_thicknessCutObject != 0.0:
            Diff1.Shape = Diff1.Shape.cut(extrude1b)
        App.ActiveDocument.getObject(str(m_dir)).addObject(Diff1)

        m_diff2_name = str(m_Obj_name) + "_02_" + str(name)
        Diff2 = App.ActiveDocument.addObject(part, m_diff2_name)
        Diff2.Shape = m_obj3.Shape.cut(extrude2)
        if m_thicknessCutObject != 0.0:
            Diff2.Shape = Diff2.Shape.cut(extrude2b)
        App.ActiveDocument.getObject(str(m_dir)).addObject(Diff2)
        # Hide intermediate objects
        if msg == 1:
            Gui.ActiveDocument.getObject(str(Point_A_User_Name)).Visibility = False
            Gui.ActiveDocument.getObject(str(Point_B_User_Name)).Visibility = False
            Gui.ActiveDocument.getObject(str(Point_C_User_Name)).Visibility = False

            Gui.ActiveDocument.getObject(str(Point_Face01_User_Name)).Visibility = False
            Gui.ActiveDocument.getObject(str(Point_Face02_User_Name)).Visibility = False

            Gui.ActiveDocument.getObject(str(Point_A0_User_Name)).Visibility = False
            Gui.ActiveDocument.getObject(str(Point_B0_User_Name)).Visibility = False

            Gui.ActiveDocument.getObject(str(Point_A1_User_Name)).Visibility = False
            Gui.ActiveDocument.getObject(str(Point_B1_User_Name)).Visibility = False

            for k in range(len(Vertx)):
                Gui.ActiveDocument.getObject(str(Vertx_names[k])).Visibility = False
            Gui.ActiveDocument.getObject(str(Edge_point_C_User_Name)).Visibility = False

            Gui.ActiveDocument.getObject(str(Point_A2_User_Name)).Visibility = False
            Gui.ActiveDocument.getObject(str(Point_B2_User_Name)).Visibility = False
            for k in range(len(BB_edges_names)):
                Gui.ActiveDocument.getObject(str(BB_edges_names[k])).Visibility = False

            Gui.ActiveDocument.getObject(str(Point_A2_prime_User_Name)).Visibility = False
            Gui.ActiveDocument.getObject(str(Point_A2_second_User_Name)).Visibility = False

            Gui.ActiveDocument.getObject(str(m_extrude1_name)).Visibility = False
            Gui.ActiveDocument.getObject(str(m_extrude2_name)).Visibility = False
            if m_thicknessCutObject != 0.0:
                Gui.ActiveDocument.getObject(str(m_extrude1b_name)).Visibility = False
                Gui.ActiveDocument.getObject(str(m_extrude2b_name)).Visibility = False

            Gui.ActiveDocument.getObject(str(Obj2_User_Name)).Visibility = False
            Gui.ActiveDocument.getObject(str(Obj3_User_Name)).Visibility = False

        # hide lines
        Gui.ActiveDocument.getObject(str(AxisA0B0_User_Name)).Visibility = False
        Gui.ActiveDocument.getObject(str(IntersecLine_User_Name)).Visibility = False

        # hide the cutting planes
        Gui.ActiveDocument.getObject(str(Plane_cutting_User_Name)).Visibility = False
        if m_thicknessCutObject != 0.0:
            Gui.ActiveDocument.getObject(str(Plane_cutting2_User_Name)).Visibility = False
            Gui.ActiveDocument.getObject(str(Plane_cutting3_User_Name)).Visibility = False

        # hide the Original
        Gui.ActiveDocument.getObject(str(m_Obj_name)).Visibility = False
        # Remove intermediate objects
        if msg == 0:
            App.getDocument(str(m_actDoc.Name)).removeObject(m_extrude1_name)
            App.getDocument(str(m_actDoc.Name)).removeObject(m_extrude2_name)
            if m_thicknessCutObject != 0.0:
                App.getDocument(str(m_actDoc.Name)).removeObject(m_extrude1b_name)
                App.getDocument(str(m_actDoc.Name)).removeObject(m_extrude2b_name)
            App.getDocument(str(m_actDoc.Name)).removeObject(Obj2_User_Name)
            App.getDocument(str(m_actDoc.Name)).removeObject(Obj3_User_Name)

        print_msg(str(m_diff1_name) + result_msg + str(m_dir))
        print_msg(str(m_diff2_name) + result_msg + str(m_dir))

        del BB_edges_names[:]
        del Distx[:]
        del Vertx[:]
        del Vertx_names[:]
    else:
        printError_msg(error_msg)

    cut_reset()


def plot_cutObject2():
    """ Cut an object in 2 pieces, based on a cut line, a plane, 
    an angle regarding this plane and a thickness.
    """
    msg = verbose

    createFolders('WorkObjects')
    error_msg = "Select in order one Line first, and finally one Object to cut !"
    result_msg = "Cut object done !"
    name = "Cut"
    part = "Part::Feature"
    m_actDoc = get_ActiveDocument(info=0)
    if m_actDoc is None:
        return

    m_num, m_selEx, m_objs, m_objNames = get_InfoObjects(info=0)
    if m_num == 2:
        SelectedObjects = get_SelectedObjects(info=msg, printError=False)
        # Number_of_Points = SelectedObjects[0]
        Number_of_Edges = SelectedObjects[1]
        # Number_of_Planes = SelectedObjects[2]
        # print_msg("Number_of_Points=" + str(Number_of_Points) +
        #          " Number_of_Edges=" + str(Number_of_Edges) +
        #          " Number_of_Planes=" + str(Number_of_Planes))
        if (Number_of_Edges == 1):
            # Get the Line
            m_line = m_objs[0]
            # print_msg( "Processing: " + str(m_objNames[0]) )
            SubObjects_Inside = m_selEx[0].SubObjects
            SubObject = SubObjects_Inside[0]
            # print_msg( "SubObject = " + str(SubObject) )
            if SubObject.ShapeType != "Edge":
                printError_msg(error_msg)
                return
            Edge_List = SelectedObjects[4]
            Point_A = Edge_List[0].valueAt(0.0)
            Point_B = Edge_List[0].valueAt(Edge_List[0].Length)
            # print_point(Point_A, msg="Point_A: ")
            # print_point(Point_B, msg="Point_B: ")
            Point_C = centerLinePoint(Edge_List[0])
            # print_point(Point_C, msg="Center of AB: ")
            # print_msg( "Distance: " + str(distanceBetween(Point_A, Point_B) ))

            # Get the object
            m_obj = m_objs[1]
            try:
                # m_s = m_obj.Shape
                m_obj.Shape
            except:
                printError_msg("This object has no attribute 'Shape' ! Select another one !\n")
                return

            try:
                m_dir = str(m_objNames[1]) + "_Cut"
                App.ActiveDocument.getObject("WorkObjects").newObject("App::DocumentObjectGroup", str(m_dir))
            except:
                printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
                return
            #m_grp=m_actDoc.getObject( str(m_dir) )
            print_msg("Processing: " + str(m_objNames[1]))
            print_msg("m_grp: " + str(m_dir))

            # Get object's limits
            m_xmax, m_xmin, m_ymax, m_ymin, m_zmax, m_zmin = minMaxObjectsLimits(m_objs[1:], info=1)

            # Length of BoundBox in X, Y and Z dimensions
            m_length_X = m_xmax - m_xmin
            m_length_Y = m_ymax - m_ymin
            m_length_Z = m_zmax - m_zmin
            m_length_list = [m_length_X, m_length_Y, m_length_Z]
            m_length_max = max(m_length_list)
            m_ori_X = m_xmin
            m_ori_Y = m_ymin
            m_ori_Z = m_zmin

            # Get Points, Edges, Faces from the bounding box Object dimensions
            Points, Edges, Faces = get_all_from_bounding_box(m_ori_X, m_ori_Y, m_ori_Z, m_length_X, m_length_Y, m_length_Z, info=0, plot=0)


            # Looking for the min distance between center of line and center
            # of faces of the bounding box.
            min_val, max_val = init_min_max()
            m_min_distance = max_val
            Selected_Plane = Faces[0][5]
            for m_i in range(len(Faces)):
                #( 3,  0,  1, 2, (Edges[3][3],Edges[0][3],Edges[1][3],Edges[2][3]), face, mid_point, length )
                m_distance = distanceBetween(Point_C, Faces[m_i][6])
                if m_distance < m_min_distance:
                    m_min_distance = m_distance
                    Selected_Plane = Faces[m_i][5]
                    Plane_Point = Faces[m_i][6]
                    Plane_Normal = Selected_Plane.normalAt(0, 0)
            # print_msg( "MIN Distance: " + str(m_min_distance) )
            # plot_point(Plane_Point, part, "point")

            # Projection of the Line onto the closest Plane.
            # Projection of A and B onto the Plane in Aprime and B0
            Vector_A = Point_A + Plane_Normal
            Vector_B = Point_B + Plane_Normal
            Point_Aprime = intersecLinePlane(Point_A, Vector_A, Plane_Normal, Plane_Point, info=0)
            Point_Bprime = intersecLinePlane(Point_B, Vector_B, Plane_Normal, Plane_Point, info=0)
            # Plot them if needed
            # plot_point(Point_Aprime, part, "PointFacePoint", grp=str(m_dir))
            # plot_point(Point_Bprime, part, "PointFacePoint", grp=str(m_dir))
            Axis_User_Name, Axis = plot_axis(Point_Aprime, Point_Bprime, part, "Line from 2 Points", grp=str(m_dir))
            Gui.ActiveDocument.getObject(Axis_User_Name).Visibility = False

            # Get intersections of this line with the Edges of the Face
            Number_of_Intersec, Intersec_Points = intersecPoints(Axis.Shape, Selected_Plane, info=0)
            # print_msg("Number_of_Intersec = " + str(Number_of_Intersec))

            if Number_of_Intersec == 0:
                printError_msg("No intersection point between projection of the Line and Object !")
                return
            if Number_of_Intersec == 1:
                printError_msg("Only one intersection point between projection of the Line and Object ! No cut possible !")
                return
            if Number_of_Intersec == 2:
                for m_i in range(Number_of_Intersec):
                    Point_User_Name = plot_point(Intersec_Points[m_i], part, "PointFacePoint", grp=str(m_dir))
                    Gui.ActiveDocument.getObject(Point_User_Name).Visibility = False
                Point_A1 = Intersec_Points[0]
                Point_B1 = Intersec_Points[1]
                # print_point(Point_A1, msg="Point_A1: ")
                # print_point(Point_B1, msg="Point_B1: ")

                Plane_Point = Selected_Plane.CenterOfMass
                Plane_Normal = Selected_Plane.normalAt(0, 0)
                # print_point(Plane_Point, msg="Plane_Point: ")

                Edge_Vector = Point_B1 - Point_A1
                Edge_Length = m_length_max * 1.2
                Point_MidPoint = Point_B1 + Point_A1
                Point_MidPoint = Point_MidPoint.multiply(0.5)

                Vector_Normal = Edge_Vector.cross(Plane_Normal)
                # Generate cutting Plane
                Plane_User_Name, plane = plot_plane(Edge_Length, Edge_Length, Point_MidPoint, Vector_Normal, part, "Cut_Plane", grp=str(m_dir))
                Gui.ActiveDocument.getObject(Plane_User_Name).Visibility = False
            # Get the 2 of them closest to center of the Face
            if Number_of_Intersec > 2:
                printError_msg("Number_of_Intersec > 2:Not yet developed !")
                return

            # Adapt the angle of cutting
            if m_angleCutObject != 0.0:
                rot_angle = m_angleCutObject
                rot_axis = Edge_Vector
                m_center = Point_MidPoint
                m_rot = App.Rotation(rot_axis, rot_angle)
                print_msg("rotation =       " + str(m_rot))
                print_msg("rotation axis  = " + str(rot_axis))
                m_place = App.Placement(plane.Placement)
                m_base1 = m_place.Base
                print_msg("base1  = " + str(m_base1))
                m_rot1 = m_place.Rotation
                print_msg("rot1  = " + str(m_rot1))
                m_rot = m_rot.multiply(m_rot1)
                m_newplace = App.Placement(m_base1, m_rot, m_center-m_base1)
                plane.Placement = m_newplace

            # Now we need to extrude the cutting Plane
            # First get 2 Vectors in which direction to extrude from Point_A1
            Vector_extrude1 = App.Vector(0.0, 0.0, 0.0)
            Vector_extrude2 = App.Vector(0.0, 0.0, 0.0)
            for m_i in range(len(Edges)):
                #( 2, 6, (Points[2], Points[6]), edge, mid_point, length )
                # plot_axis(Edges[m_i][2][0], Edges[m_i][2][1], part, "axis")
                if colinearVectors(Edges[m_i][2][0], Point_A1, Edges[m_i][2][1], info=0):
                    # Plot them
                    # plot_point(Edges[m_i][2][0], part, "PointFacePoint")
                    # plot_point(Edges[m_i][2][1], part, "PointFacePoint")
                    Vector_extrude1 = Edges[m_i][2][0] - Point_A1
                    Vector_extrude2 = Point_A1 - Edges[m_i][2][1]
                    Vector_extrude1 = Vector_extrude1.multiply(1.5)
                    Vector_extrude2 = Vector_extrude2.multiply(-1.5)
            # Second we extrude in the first direction
            # print_msg("Vector_extrude1 =       " + str(Vector_extrude1))
            # print_msg("Vector_extrude2 =       " + str(Vector_extrude2))
            # print_msg("plane =       " + str(plane))
            plane_shape = plane.Shape
            print_msg("plane_shape =       " + str(plane_shape))
            extrude1 = plane_shape.extrude(Vector_extrude1)
            # print_msg("extrude1  =       " + str(extrude1))
            Extrude1 = App.ActiveDocument.addObject("Part::Feature", "extrude001")
            App.ActiveDocument.getObject(str(m_dir)).addObject(Extrude1)
            Extrude1.Shape = extrude1
            Gui.ActiveDocument.getObject("extrude001").Visibility = False
            #Part.show(extrude1)
            extrude2 = plane_shape.extrude(Vector_extrude2)
            # print_msg("extrude2  =       " + str(extrude2))
            Extrude2 = App.ActiveDocument.addObject("Part::Feature", "extrude002")
            App.ActiveDocument.getObject(str(m_dir)).addObject(Extrude2)
            Extrude2.Shape = extrude2
            Gui.ActiveDocument.getObject("extrude002").Visibility = False
            #Part.show(extrude2)

            # Let's duplicate the Object
            m_obj2 = m_actDoc.copyObject(m_obj)
            m_obj3 = m_actDoc.copyObject(m_obj)
            #m_obj4 = m_actDoc.copyObject(m_line)

            App.ActiveDocument.getObject(str(m_dir)).addObject(m_obj2)
            App.ActiveDocument.getObject(str(m_dir)).addObject(m_obj3)
            #App.ActiveDocument.getObject(str(m_dir)).addObject(m_obj4)
            Obj2_User_Name = m_obj2.Label
            Gui.ActiveDocument.getObject(Obj2_User_Name).Visibility = False
            Obj3_User_Name = m_obj3.Label
            Gui.ActiveDocument.getObject(Obj3_User_Name).Visibility = False

            m_diff1_name = str(m_objNames[1]) + "_" + str(name) + "01"
            m_diff1 = App.ActiveDocument.addObject(part, m_diff1_name)
            m_diff1.Shape = m_obj2.Shape.cut(extrude1)
            App.ActiveDocument.getObject(str(m_dir)).addObject(m_diff1)

            m_diff2_name = str(m_objNames[1]) + "_" + str(name) + "02"
            m_diff2 = App.ActiveDocument.addObject(part, m_diff2_name)
            m_diff2.Shape = m_obj3.Shape.cut(extrude2)
            App.ActiveDocument.getObject(str(m_dir)).addObject(m_diff2)

            #App.ActiveDocument.getObject(str(m_dir)).addObject(m_obj)
            Gui.ActiveDocument.getObject(str(m_objNames[1])).Visibility = False

            App.getDocument(str(m_actDoc.Name)).removeObject("extrude001")
            App.getDocument(str(m_actDoc.Name)).removeObject("extrude002")
            App.getDocument(str(m_actDoc.Name)).removeObject(Obj2_User_Name)
            App.getDocument(str(m_actDoc.Name)).removeObject(Obj3_User_Name)

            print_msg(result_msg)

    else:
        printError_msg(error_msg)


def two_objects_are(case):
    """
    Edge: E
    Plane: P
    if E not included into P:
        E, P intersection is empty: E Parallel to P
        E, P intersection is one Point: E intersects P
    
    Edge1: E1
    Edge2: E2
    if E1 coplanar with E2:
        E1, E2 intersection is empty: E1 Parallel to E2
    if E1prime Parallel to E1 and E2prime Parallel to E2: 
        if E1prime coplanar with E2prime and E1prime perpendicular to E2prime:
            E1 perpendicular to E2
            
    Edge: E
    Plane: P
    if E1 included into P and E2 included into P and E1, E2 intersection is one Point:
        if E perpendicular to E1 and E perpendicular to E2:        
            E perpendicular to P (E Normal to P)
            
    Plane1: P1
    Plane2: P2
    if P1 != P2:
        P1, P2 intersection is empty: P1 Parallel to P2 means E1 and E2 Normals are Parallel
        
    Original code from: Javier Martinez Garcia 02/2015
    Adapted to WF by  : Rentlau_64 03/2015
    """
    global verbose
    msg = verbose
    global tolerance

    if case == "parallel":
        error_msg = "Unable to check parallelism: \nSelect 2 objects \n(either 2 Planes or 2 Edges) !"
    elif case == "perpendicular":
        error_msg = "Unable to check perpendicularity: \nSelect 2 objects \n(either 2 Planes or 2 Edges) !"
    elif case == "coplanar":
        error_msg = "Unable to check coplanarity: \nSelect 2 objects \n(either 2 Planes or 2 Edges) !"

    try:
        SelObj = Gui.Selection.getSelectionEx()

        if len(SelObj) == 1:
            if SelObj[0].HasSubObjects:
                if len(SelObj[0].SubObjects) == 2:
                    sub01 = SelObj[0].SubObjects[0]
                    sub02 = SelObj[0].SubObjects[1]
                else:
                    printError_msg(error_msg)
            else:
                printError_msg(error_msg)
                return
        elif len(SelObj) == 2:
            if SelObj[0].HasSubObjects:
                sub01 = SelObj[0].SubObjects[0]
                sub02 = SelObj[1].SubObjects[0]
            else:
                printError_msg(error_msg)
        else:
            printError_msg(error_msg)
            return

        if sub01.ShapeType != sub02.ShapeType:
            printError_msg(error_msg)
            return

        if msg:
            print_msg("Tolerance = " + str(tolerance))
        m_tol_msg = "\n(for tolerance of " + str(tolerance) + ")"
        if sub01.ShapeType == 'Edge':
            if msg:
                print_msg("Comparing two Edges")
            EdgeA = sub01
            EdgeB = sub02
            VA = (EdgeA.Curve.EndPoint - EdgeA.Curve.StartPoint).normalize()
            VB = (EdgeB.Curve.EndPoint - EdgeB.Curve.StartPoint).normalize()
            # parallel
            if case == "parallel":
                # if (VA.cross(VB)).Length == 0.0:
                if abs((VA.cross(VB)).Length) <= tolerance:
                    print_gui_msg("Edges are parallel" + m_tol_msg)
                else:
                    print_gui_msg("Non parallel edges" + m_tol_msg)
            # perpendicular
            elif case == "perpendicular":
                # if VA.dot(VB) == 0.0:
                if abs(VA.dot(VB)) <= tolerance:
                    print_gui_msg("Edges are perpendicular" + m_tol_msg)
                else:
                    print_gui_msg("Non perpendicular edges" + m_tol_msg)
            # coplanar
            elif case == "coplanar":
                VC = EdgeB.Curve.StartPoint - EdgeA.Curve.StartPoint
                VD = EdgeB.Curve.EndPoint - EdgeA.Curve.EndPoint
                # if ((VA.cross(VB)).cross((VC.cross(VD)))).Length == 0.0:
                if abs(((VA.cross(VB)).cross((VC.cross(VD)))).Length) <= tolerance:
                    print_gui_msg("Edges are coplanar" + m_tol_msg)
                else:
                    print_gui_msg("Non coplanar edges" + m_tol_msg)


        if sub01.ShapeType == 'Face':
            if msg:
                print_msg("Comparing two Faces")
            NormalA = sub01.normalAt(0, 0)
            NormalB = sub02.normalAt(0, 0)
            # parallel
            if case == "parallel":
                # if NormalA.cross(NormalB).Length == 0.0:
                if msg:
                    print_msg("abs(NormalA.cross(NormalB).Length) = " + str(abs(NormalA.cross(NormalB).Length)))

                if abs(NormalA.cross(NormalB).Length) <= tolerance:
                    print_gui_msg("Faces are parallel" + m_tol_msg)
                else:
                    print_gui_msg("Non parallel faces" + m_tol_msg)
            # perpendicular
            elif case == "perpendicular":
                # if NormalA.dot(NormalB) == 0.0:
                if msg:
                    print_msg("abs(NormalA.dot(NormalB)) = " + str(abs(NormalA.dot(NormalB))))

                if abs(NormalA.dot(NormalB)) <= tolerance:
                    print_gui_msg("Faces are perpendicular" + m_tol_msg)
                else:
                    print_gui_msg("Non perpendicular faces" + m_tol_msg)
            # coplanar
            elif case == "coplanar":
                NormalA = sub01.normalAt(0, 0)
                VAB = (sub02.CenterOfMass-sub01.CenterOfMass).normalize()
                if msg:
                    print_msg("abs(NormalA.dot(VAB)) = " + str(abs(NormalA.dot(VAB))))
                    print_msg("abs(NormalB.dot(VAB)) = " + str(abs(NormalB.dot(VAB))))
                # if NormalA.dot(VAB) == 0.0:
                if abs(NormalA.dot(VAB)) <= tolerance and abs(NormalB.dot(VAB)) <= tolerance:
                    print_gui_msg("Coplanar faces" + m_tol_msg)
                else:
                    print_gui_msg("Non coplanar faces" + m_tol_msg)

    except:
        printError_msg(error_msg)


def object_parallel():
    two_objects_are("parallel")


def object_perpendicular():
    two_objects_are("perpendicular")


def object_coplanar():
    two_objects_are("coplanar")


def object_highlightCommon():
    """
    Compute the common parts between selected shapes:
    Quick measurements between parallel faces and similarly placed objects

    Original code from: 'JMG, galou and other contributors' 10/2015
    Adapted to WF by  : Rentlau_64 10/2015
    """
    msg = verbose

    pass
# ==============================================================================
# # -*- coding: utf-8 -*-
#
# from __future__ import unicode_literals
#
# __Name__ = 'Highlight Common parts'
# __Comment__ = 'Compute the common parts between selected shapes'
# __Web__ = 'http://freecadweb.org/wiki/index.php?title=Macro_HighlightCommon'
# __Wiki__ = 'http://freecadweb.org/wiki/index.php?title=Macro_HighlightCommon'
# __Icon__ = ""
# __Help__ = 'Select at least two objects and run'
# __Author__ = 'JMG, galou and other contributors'
# __Version__ = 1.0
# __Status__ = 'Production'
# __Requires__ = ''
#
# from PySide import QtCore
# from PySide import QtGui
#
# import FreeCAD
#
#
# def error_dialog(msg):
#     """Create a simple dialog QMessageBox with an error message"""
#     FreeCAD.Console.PrintError(msg + '\n')
#     diag = QtGui.QMessageBox(QtGui.QMessageBox.Icon.Critical,
#                              'Error in macro highlight_difference',
#                              msg)
#     diag.setWindowModality(QtCore.Qt.ApplicationModal)
#     diag.exec_()
#
# if len(FreeCAD.Gui.Selection.getSelectionEx()) < 2:
#     error_dialog('Select at least two objects')
#
# object_list = []
# for obj in FreeCAD.Gui.Selection.getSelectionEx():
#     object_list.append(obj.Object)
#
# for i, object_a in enumerate(object_list):
#     for object_b in object_list[(i + 1):]:
#         shape_a = object_a.Shape
#         shape_b = object_b.Shape
#         label_a = object_a.Label
#         label_b = object_b.Label
#         common = shape_a.common(shape_b)
#         if common.Volume > 1e-6:
#             FreeCAD.Console.PrintMessage(
#                 'Volume of the intersection between {} and {}: {}\n'.format(
#                     label_a,
#                     label_b,
#                     common.Volume))
#
#             intersection_object = FreeCAD.ActiveDocument.addObject(
#                 'Part::Feature')
#             intersection_object.Label = 'Common ({} - {})'.format(
#                 label_a, label_b)
#             intersection_object.Shape = common
#             intersection_object.ViewObject.ShapeColor = (1.0, 0.0, 0.0, 1.0)
#             object_a.ViewObject.Transparency = 80
#             object_b.ViewObject.Transparency = 80
#         else:
#             FreeCAD.Console.PrintMessage(
#
#                'No intersection between {} and {}\n'.format(
#                    label_a,
#                    label_b))
# ==============================================================================

def object_clearance():
    """
    Check for two Objects Clearance distance:
    Quick measurements between parallel faces and similarly placed objects

    Original code from: Bill 03/2015
    Adapted to WF by  : Rentlau_64 03/2015
    """
    global verbose
    msg = verbose

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    error_msg = "INCORRECT Object(s) Selection:\n\nYou Must Select Two(2) Objects !"
    try:
        selectionObjects = Gui.Selection.getSelectionEx()
        if msg != 0:
            print_msg("SelectionObjects is:" + str(selectionObjects))
            print_msg("Number of objects is:" + str(len(selectionObjects)))
        if len(selectionObjects) != 2:
            printError_msg(error_msg)
            return
        OBJ1 = selectionObjects[0].ObjectName
        OBJ2 = selectionObjects[1].ObjectName

        mindist = App.ActiveDocument.getObject(OBJ1).Shape.distToShape(App.ActiveDocument.getObject(OBJ2).Shape)[0]
        print_msg("Distance to Second Object is " + str(mindist) + "\n")
        if mindist == 0.0:
            result = 'POSSIBLE COLLISION DETECTED \n\nCLEARANCE(S) <= 0 \n\nCheck Clearances and Settings !'
        else:
            result = 'Object CLEARANCE is ' + str(mindist) + ' units !'
        print_gui_msg(result)
    except:
        printError_msg(error_msg)


def object_angle():
    """
    Check for two Edges/Planes angle:
    Angle measurement between two Edges, two Planes
    or One Edge and One Plane

    NB:
    Normals of Planes will be used.
    """
    global verbose
    msg = verbose

    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select Two(2) Edges !\n" +\
    "Or Two(2) Planes !\n" +\
    "Or One Edge and One Plane !"

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Edges = SelectedObjects[1]
        Number_of_Planes = SelectedObjects[2]
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))
            print_msg("Number_of_Planes=" + str(Number_of_Planes))

        if Number_of_Edges == 2:
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg(" Edge_List=" + str(Edge_List))
            m_angle, m_angle_rad = angleBetween(Edge_List[0], Edge_List[1])
            result = "Between 2 Edges:\n" +\
            "Angle is:\n" + str(m_angle) + " deg\n" + str(m_angle_rad) + " rad\n"
            print_gui_msg(result)

        elif Number_of_Planes == 2:
            Plane_List = SelectedObjects[5]
            if msg != 0:
                print_msg(" Plane_List=" + str(Plane_List))

            Normal1 = Plane_List[0].normalAt(0, 0)
            Normal2 = Plane_List[1].normalAt(0, 0)
            if msg != 0:
                print_point(Normal1, msg="Normal1: ")
                print_point(Normal2, msg="Normal2: ")

            m_angle, m_angle_rad = angleBetween(Normal1, Normal2)
            result = "Between 2 Planes:\n" +\
            "Angle is:\n" + str(m_angle) + " deg\n" + str(m_angle_rad) + " rad\n"
            print_gui_msg(result)

        elif Number_of_Planes == 1 and Number_of_Edges == 1:
            Edge_List = SelectedObjects[4]
            Plane_List = SelectedObjects[5]
            if msg != 0:
                print_msg(" Edge_List =" + str(Edge_List))
                print_msg(" Plane_List=" + str(Plane_List))

            Normal1 = Plane_List[0].normalAt(0, 0)

            m_angle, m_angle_rad = angleBetween(Edge_List[0], Normal1)
            result = "Between One Edge and One Plane:\n" +\
            "Angle is:\n" + str(m_angle) + " deg\n" + str(m_angle_rad) + " rad\n"
            print_gui_msg(result)
        else:
            printError_msg(error_msg)

    except:
        printError_msg(error_msg)


def points_distance():
    """
    Check for two Points distance:
        Distances measurement and Delta values (on main Axes) between two Points

    Original code from Mario52
    """
    msg = verbose

    error_msg = "INCORRECT Object(s) Selection:\n\nYou Must Select Two(2) Points !"

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))

        if Number_of_Points != 2:
            printError_msg(error_msg)
            return

        Point_List = SelectedObjects[3]

        pos_X1 = Point_List[0].Point.x
        pos_Y1 = Point_List[0].Point.y
        pos_Z1 = Point_List[0].Point.z
        if msg != 0:
            print_point(Point_List[0].Point, msg="First Point: ")

        pos_X2 = Point_List[1].Point.x
        pos_Y2 = Point_List[1].Point.y
        pos_Z2 = Point_List[1].Point.z
        if msg != 0:
            print_point(Point_List[1].Point, msg="Last Point: ")

        m_dist = distanceBetween(Point_List[0].Point, Point_List[1].Point)
        if msg != 0:
            print_msg("Distance is: " + str(m_dist))

        result =\
        "Begin: \n X1 " + str(pos_X1) + " \n Y1: " + str(pos_Y1) + " \n Z1: " + str(pos_Z1) + "\n" +\
        "End: \n X2 " + str(pos_X2) + " \n Y2: " + str(pos_Y2) + " \n Z2: " + str(pos_Z2) + "\n" +\
        "Delta X: " + str(abs(pos_X1-pos_X2)) + "\n" +\
        "Delta Y: " + str(abs(pos_Y1-pos_Y2)) + "\n" +\
        "Delta Z: " + str(abs(pos_Z1-pos_Z2)) + "\n\n" +\
        "Distance: " + str(m_dist)

        print_gui_msg(result)
    except:
        printError_msg(error_msg)


def line_length():
    """
    Check for Line Length:
        Length measurement and Delta values (on main Axes) for a Line
        - Select the Line

    """
    msg = verbose

    error_msg = "INCORRECT Object(s) Selection:\n\nYou Must Select One Line !"
    m_length = None

    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))

        if Number_of_Edges != 1:
            printError_msg(error_msg)
            return

        Edge_List = SelectedObjects[4]
        edge = Edge_List[0]

        pos_X1 = edge.Vertexes[0].Point.x
        pos_Y1 = edge.Vertexes[0].Point.y
        pos_Z1 = edge.Vertexes[0].Point.z
        if msg != 0:
            print_point(edge.Vertexes[0].Point, msg="First Point: ")

        pos_X2 = edge.Vertexes[-1].Point.x
        pos_Y2 = edge.Vertexes[-1].Point.y
        pos_Z2 = edge.Vertexes[-1].Point.z
        if msg != 0:
            print_point(edge.Vertexes[-1].Point, msg="Last Point: ")

        m_dist = distanceBetween(edge.Vertexes[0].Point, edge.Vertexes[-1].Point)
        if msg != 0:
            print_msg("Distance is: " + str(m_dist))

        if hasattr(edge, 'Length'):
            m_length = edge.Length

        result =\
        "Begin: \n X1 " + str(pos_X1) + " \n Y1: " + str(pos_Y1) + " \n Z1: " + str(pos_Z1) + "\n" +\
        "End: \n X2 " + str(pos_X2) + " \n Y2: " + str(pos_Y2) + " \n Z2: " + str(pos_Z2) + "\n" +\
        "Delta X: " + str(abs(pos_X1-pos_X2)) + "\n" +\
        "Delta Y: " + str(abs(pos_Y1-pos_Y2)) + "\n" +\
        "Delta Z: " + str(abs(pos_Z1-pos_Z2)) + "\n\n" +\
        "Distance: " + str(m_dist) + "\n"

        if m_length:
            result += "Length along edge/arc: " + str(m_length)


        print_gui_msg(result)
    except:
        printError_msg(error_msg)


def object_radius():
    """
    Check for Radius:

    """
    error_msg = "INCORRECT Object(s) Selection:\n\nYou Must Select One Arc!"

    Selection = Gui.Selection.getSelectionEx()

    try:
        result = "Radius:"
        m_found = False
        for m_sel in Selection:
            m_name = m_sel.ObjectName
            if hasattr(m_sel, 'SubObjects'):
                for m_sub, m_sub_name in zip(m_sel.SubObjects, m_sel.SubElementNames):
                    if hasattr(m_sub, 'Curve'):
                        r = m_sub.Curve
                        if hasattr(r, 'Radius'):
                            m_radius = r.Radius
                            result += "\nObject: " + str(m_name) + "." + str(m_sub_name)
                            result += "\nRadius is " + str(m_radius)
                            m_found = True
            else:
                if hasattr(m_sel, 'Curve'):
                    r = m_sel.Curve
                    if hasattr(r, 'Radius'):
                        m_radius = r.Radius
                        result += "\nObject: " + str(m_name)
                        result += "\nRadius is " + str(m_radius)
                        m_found = True


        if m_found:
            print_gui_msg(result)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def plane_area():
    """
    Check for surface Area:
        Area measurement for a Plane or a set of Planes.
        - Select One or several Face(s)

    """
    msg = verbose

    # Lets define 2 lists; one for units and the second for corresponding
    # magnitude of the unit:
    unit_list = ["mm2", "cm2", "dm2", "m2"  , "are"   , "hectare" , "km2"]
    unit_mag = [1   , 100 , 10000, 1000000, 100000000, 10000000000, 1000000000000]
    # Lets make a dictionary of these 2 lists: unit_div
    # (for dividing/rounding the value)
    unit_div =  dict(zip(unit_list, unit_mag))
    # And a second dictionary to define ranges of the number of digits
    # regarding the corresponding unit:
    unit_dict = dict.fromkeys(range(0, 3), "mm2")
    unit_dict.update(dict.fromkeys(range(3, 5), "cm2"))
    unit_dict.update(dict.fromkeys(range(5, 7), "dm2"))
    unit_dict.update(dict.fromkeys(range(7, 9), "m2"))
    unit_dict.update(dict.fromkeys(range(9, 11), "are"))
    unit_dict.update(dict.fromkeys(range(11, 13), "hectare"))
    unit_dict.update(dict.fromkeys(range(13, 15), "km2"))

    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select Face(s) !"
    Selection = get_SelectedObjects(info=msg, printError=False)
    try:
        SelectedObjects = Selection
        Number_of_Planes = SelectedObjects[2]
        if msg != 0:
            print_msg("Number_of_Planes=" + str(Number_of_Planes))

        if Number_of_Planes >= 1:
            Plane_List = SelectedObjects[5]
            if msg != 0:
                print_msg(" Plane_List=" + str(Plane_List))
            m_areas = []
            result = ""
            for m_plane in Plane_List:
                m_areas.append(m_plane.Area)
            result = "Area(s):"
            a = 0.0
            for m_a in m_areas:
                a += m_a
                m_value = math.ceil(m_a*1000)/1000
                #result += str(m_value) + " mm2"
                if digitsNumber(m_value) > 15:
                    result += "\n" + str(format(float(m_value)/1000000000000, '.2f')) + " " + "km2"
                else:
                    result += "\n" + str(format(float(m_value)/unit_div[unit_dict[digitsNumber(m_value)]], '.2f')) + " " + str(unit_dict[digitsNumber(m_value)])

            m_value = math.ceil(a*1000)/1000
            #result += "Total of areas is " + str(m_value) + " mm2"
            if digitsNumber(m_value) > 15:
                result += "\n" + "Total of areas is \n" + str(format(float(m_value)/1000000000000, '.2f')) + " " + "km2"
            else:
                result += "\n" + "Total of areas is \n" + str(format(float(m_value)/unit_div[unit_dict[digitsNumber(m_value)]], '.2f')) + " " + str(unit_dict[digitsNumber(m_value)])

            print_gui_msg(result)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def camera_orientation():
    """ Detect the position of the camera.
    The returned value is the value provided 
    by the function getCameraOrientation().
    """
    msg = verbose

    pl = App.Placement()
    pl.Rotation = Gui.ActiveDocument.ActiveView.getCameraOrientation()

    xP = pl.Rotation.Q[0]
    yP = pl.Rotation.Q[1]
    zP = pl.Rotation.Q[2]
    qP = pl.Rotation.Q[3]

    cam = Gui.ActiveDocument.ActiveView.getCameraNode()
    direction = cam.orientation.getValue().multVec(coin.SbVec3f(0, 0, 1)).getValue()

    result =\
    "___Camera_Orientation____________________" + "\n" +\
    "Radians XYZ Q : " + str(pl.Rotation.Q) + "\n" +\
    "Degrees XYZ   : " + str(math.degrees(xP)) + ", " + str(math.degrees(yP)) + ", " + str(math.degrees(zP)) + "\n" +\
    "Degrees Q     : " + str(math.degrees(qP)) + "\n" +\
    "Radians Axis.xyz A: " + str(pl.Rotation.Axis) + ", " + str(pl.Rotation.Angle) + "\n" +\
    "Degrees Axis.x: " + str(math.degrees(pl.Rotation.Axis.x)) + "\n" +\
    "Degrees Axis.y: " + str(math.degrees(pl.Rotation.Axis.y)) + "\n" +\
    "Degrees Axis.z: " + str(math.degrees(pl.Rotation.Axis.z)) + "\n" +\
    "Degrees Angle : " + str(math.degrees(pl.Rotation.Angle)) + "\n" +\
    "Direction Vector: " + str (direction)

    print_gui_msg(result)


def object_common():
    """Compute the common parts between selected shapes.
    - Select at least two objects.
        
    Original code from HighlightCommon.FCMacro
    https://github.com/FreeCAD/FreeCAD-macros/blob/master/Utility/HighlightCommon.FCMacro
    Authors = 2015 Javier Martinez Garcia
    """
    global verbose
    msg = verbose

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    createFolders('WorkObjects')
    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select at least Two(2) Objects !"
    result_msg = ": Common object created into WorkFeatures/WorkObjects/"
    name = "Part"
    part = "Part::Feature"
    grp = "WorkObjects"

    try:
        selectionObjects = Gui.Selection.getSelection()
        if len(selectionObjects) < 2:
            printError_msg(error_msg)
            return
        object_list = []
        for obj in selectionObjects:
            object_list.append(obj)
        for i, object_a in enumerate(object_list):
            shape_a = object_a.Shape
            label_a = object_a.Label
            for object_b in object_list[(i + 1):]:
                shape_b = object_b.Shape
                label_b = object_b.Label
                common = shape_a.common(shape_b)
                if common.Volume > 1e-6:
                    if not(App.ActiveDocument.getObject(grp)):
                        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
                    intersection_object = FreeCAD.ActiveDocument.addObject(part)
                    intersection_object.Label = "Common (" +\
                         str(label_a.encode('utf-8')) +\
                         "-" +\
                         str(label_b.encode('utf-8')) +\
                         ")"
                    intersection_object.Shape = common
                    App.ActiveDocument.getObject(grp).addObject(intersection_object)
                    intersection_object.ViewObject.ShapeColor = (1.0, 0.0, 0.0, 1.0)
                    object_a.ViewObject.Transparency = 80
                    object_b.ViewObject.Transparency = 80

                    print_msg(str(intersection_object.Label.encode('utf-8')) + result_msg)
                    print_msg("Volume of the intersection between " +\
                        str(label_a.encode('utf-8')) +\
                        " and " +\
                        str(label_b.encode('utf-8')) +\
                        ": " +\
                        str(common.Volume) + "\n")
                else:
                    print_gui_msg("No intersection between " +\
                        str(label_a.encode('utf-8')) +\
                        " and " +\
                        str(label_b.encode('utf-8')))
    except:
        printError_msg(error_msg)


def object_difference():
    """Compute the difference parts between selected shapes.
    - Select two objects.

    Original code from HighlightDifference.FCMacro
    https://github.com/FreeCAD/FreeCAD-macros/blob/master/Utility/HighlightDifference.FCMacro
    Authors = 2015 Gaël Ecorchard (Galou)
    """
    global verbose
    msg = verbose

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None

    createFolders('WorkObjects')
    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select Two(2) Objects !"
    result_msg = ": Difference object created into WorkFeatures/WorkObjects/"
    name = "Part"
    part = "Part::Feature"
    grp = "WorkObjects"

    try:
        selectionObjects = Gui.Selection.getSelection()

        if len(selectionObjects) < 2:
            printError_msg(error_msg)
            return
        object_list = []
        for obj in selectionObjects:
            object_list.append(obj)
        for i, object_a in enumerate(object_list):
            shape_a = object_a.Shape
            label_a = object_a.Label
            for object_b in object_list[(i + 1):]:
                shape_b = object_b.Shape
                label_b = object_b.Label
                shape_addition = shape_a.cut(shape_b)
                if shape_addition.Volume < 1e-6:
                    print_gui_msg("No Cut of " +\
                        str(label_a.encode('utf-8')) +\
                        " by " +\
                        str(label_b.encode('utf-8')))
                else:
                    print_msg("Volume of the red " +\
                        str(label_a.encode('utf-8')) +\
                        " Cut by " +\
                        str(label_b.encode('utf-8')) +\
                        ": " +\
                        str(shape_addition.Volume) + "\n")
                    if not(App.ActiveDocument.getObject(grp)):
                        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)

                    added = FreeCAD.ActiveDocument.addObject(part)
                    added.Label = "Cut red (" +\
                         str(label_a.encode('utf-8')) +\
                         "-" +\
                         str(label_b.encode('utf-8')) +\
                         ")"
                    added.Shape = shape_addition
                    App.ActiveDocument.getObject(grp).addObject(added)
                    added.ViewObject.ShapeColor = (1.0, 0.0, 0.0, 1.0)

                shape_removal = shape_b.cut(shape_a)
                if shape_removal.Volume < 1e-6:
                    print_gui_msg("No Cut of " +\
                        str(label_b.encode('utf-8')) +\
                        " by " +\
                        str(label_a.encode('utf-8')))
                else:
                    print_msg("Volume of the green " +\
                        str(label_b.encode('utf-8')) +\
                        " Cut by " +\
                        str(label_a.encode('utf-8')) +\
                        ": " +\
                        str(shape_removal.Volume) + "\n")

                    if not(App.ActiveDocument.getObject(grp)):
                        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)

                    removed = FreeCAD.ActiveDocument.addObject(part)
                    removed.Label = "Cut green (" +\
                         str(label_b.encode('utf-8')) +\
                         "-" +\
                         str(label_a.encode('utf-8')) +\
                         ")"
                    removed.Shape = shape_removal
                    App.ActiveDocument.getObject(grp).addObject(removed)
                    removed.ViewObject.ShapeColor = (0.0, 0.5, 0.0, 1.0)

                object_a.ViewObject.Transparency = 80
                object_b.ViewObject.Transparency = 80
    except:
        printError_msg(error_msg)


# object_a = FreeCAD.Gui.Selection.getSelectionEx()[0].Object
# object_b = FreeCAD.Gui.Selection.getSelectionEx()[1].Object
# shape_a = object_a.Shape
# shape_b = object_b.Shape
# label_a = object_a.Label
# label_b = object_b.Label
# shape_addition = shape_a.cut(shape_b)
# if shape_addition.Volume < 1e-6:
#     FreeCAD.Console.PrintMessage('No addition from {} to {}\n'.format(
#         label_a, label_b))
# else:
#     FreeCAD.Console.PrintMessage(
#         'Volume of the addition from {} to {}: {}\n'.format(
#             label_a, label_b, shape_addition.Volume))
#
# shape_removal = shape_b.cut(shape_a)
# if shape_removal.Volume < 1e-6:
#     FreeCAD.Console.PrintMessage('No removal from {} to {}\n'.format(
#         label_a, label_b))
# else:
#     FreeCAD.Console.PrintMessage(
#         'Volume of the removal from {} to {}: {}\n'.format(
#             label_a, label_b, shape_removal.Volume))
#
# if (shape_addition.Volume < 1e-6) and (shape_removal.Volume < 1e-6):
#     FreeCAD.Console.PrintMessage('{} and {} have the same shape\n'.format(
#         label_a, label_b))
#
# added = FreeCAD.ActiveDocument.addObject('Part::Feature')
# added.Label = 'Addition ({} − {})'.format(label_a, label_b)
# added.Shape = shape_addition
# added.ViewObject.ShapeColor = (1.0, 0.0, 0.0, 1.0)
# removed = FreeCAD.ActiveDocument.addObject('Part::Feature')
# removed.Label = 'Removal ({} − {})'.format(label_b, label_a)
# removed.Shape = shape_removal
# removed.ViewObject.ShapeColor = (0.0, 0.5, 0.0, 1.0)
#
# object_a.ViewObject.Transparency = 80
# object_b.ViewObject.Transparency = 80

def object_align2view_old():
    """ Align the object(s) selected to the actual view.
    - Click first to select a Face of an object.

    The changed values are: Rotation Axis((X, Y, Z), Angle) 
    Same Euler angles: Yaw, Pitch, Roll
    The Translation is not modifylace your object selected to the position ActiveView (camera)
    
    Original Code from Mario52
    """
    # revoir le point de rotation
    msg = verbose

    error_msg = "INCORRECT Object(s) Selection:\n\nYou Must at least one object !"

    try:
        m_sel_list = Gui.Selection.getSelection()
        pl = App.Placement()
        pl.Rotation = Gui.ActiveDocument.ActiveView.getCameraOrientation()
        for m_sel in m_sel_list:
            m_Nameelement = m_sel.Name
            if msg != 0:
                print_msg("Object selected =" + str(m_Nameelement))
            pl.Base = m_sel.Placement.Base
            App.ActiveDocument.getObject(m_Nameelement).Placement = pl
    except:
        printError_msg(error_msg)


def object_align2view():
    """
    Align the face of selected object(s)  to the actual view Plane.
    - Click first to select a Face of one or several objects.

    NB:
      The center of rotation is the center of the bounbing box if possible or 
      the center of the Face.
     
      if the Face of the object selected is already aligned to the  view Plane,
      a rotation of 180 deg is applied to the object.
      In this case the Axis of rotation is Z vector: Base.Vector(0, 0, 1)
      
      Two clicks will rotate by 180 deg.
    """
    msg = verbose

    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select at least one Face of one Object !\n" +\
    "All Face(s) will be aligned to the actual view Plane!"

    Selection = get_SelectedObjectsWithParent(info=msg, printError=False)
    m_actDoc = get_ActiveDocument(info=1)
    Selection2 = Gui.Selection.getSelectionEx(m_actDoc.Name)

    try:
        SelectedObjects = Selection
        Number_of_Planes = SelectedObjects[2]
        if msg != 0:
            print_msg("Number_of_Planes=" + str(Number_of_Planes))
        if Number_of_Planes >= 1:
            Plane_List = SelectedObjects[5]
            if msg != 0:
                print_msg(" Plane_List=" + str(Plane_List))

            Origin = Base.Vector(0, 0, 0)

            Plane_Normal_ref = Gui.ActiveDocument.ActiveView.getViewDirection()
            if msg != 0:
                print_point(Plane_Normal_ref, msg="Reference Plane_Normal = ")

            for Selected_Plane_dict in Plane_List:
                if msg != 0:
                    print_msg("Selected_Plane_dict = " + str(Selected_Plane_dict))
                for Selected_Plane, Parent_Plane in Selected_Plane_dict.iteritems():
                    if msg != 0:
                        print_msg("Selected_Plane = " + str(Selected_Plane))
                        print_msg("Parent = " + str(Parent_Plane))
                    try:
                        Plane_Point = Parent_Plane.Shape.BoundBox.Center
                    except:
                        Plane_Point = Selected_Plane.CenterOfMass

                    Plane_Normal = Selected_Plane.normalAt(0, 0)
                    if msg != 0:
                        print_point(Plane_Point, msg="Plane_Point = ")
                        print_point(Plane_Normal, msg="Plane_Normal = ")
                    if colinearVectors(Plane_Normal, Origin, Plane_Normal_ref, info=0, tolerance=1e-12):
                        rot_axis = Base.Vector(0, 0, 1).cross(Plane_Normal)
                        rot_center = Plane_Point
                        rot_angle = 180.
                        Draft.rotate(Parent_Plane, rot_angle, rot_center, rot_axis)
                    else:
                        m_angle, m_angle_rad = angleBetween(Plane_Normal, Plane_Normal_ref)
                        rot_axis = Plane_Normal.cross(Plane_Normal_ref)
                        rot_center = Plane_Point
                        rot_angle = m_angle
                        Draft.rotate(Parent_Plane, rot_angle, rot_center, rot_axis)
            # Reset the selection changed by Draft.rotate
            reset_SelectedObjects(Selection2, info=0)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def angleAlignFaces(value):
    """ Respond to the change in angle value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_angleAlignFaces
        if str(value) == '-':
            return
        m_angleAlignFaces = float(value)
        print_msg("New angle in degrees is:" + str(m_angleAlignFaces))
    except ValueError:
        printError_msg("Angle must be valid number !")


def object_copy():
    """
    Duplicate:
    Make a copy of an object or a selected subObject part:
    - Select one or several object(s) or subobject(s)
       
    Original code from Macro_ReproWire
    Authors = 2015 Mario52
    """
    msg = verbose

    error_msg = "INCORRECT Object(s) Selection:\n\nYou Must Select at least one Object !"

    sel = Gui.Selection.getSelection()
    s = Gui.Selection.getSelectionEx()

    try:
        if len(sel) != 0:
            # print "Object(s): ", len(sel), ", SubObject(s): ", len(s)
            i2 = ii2 = -1
            for i in s:
                i2 += 1
                ii2 = -1
                try:
                    Gui.Selection.getSelectionEx()[i2].SubObjects[ii2]
                    for ii in i.SubElementNames:
                        # print "SubObject"
                        ii2 += 1
                        # create repro shape subObject
                        Part.show(Gui.Selection.getSelectionEx()[i2].SubObjects[ii2].copy())
                        # display the info SubObject
                        print(i2 + 1, "/", ii2 + 1, "/", len(s), " ", i.ObjectName, " ", ii)

                        a = App.ActiveDocument.ActiveObject
                        # Label for the repro shape
                        #          object Name  / original object Name / SubObject Name
                        a.Label = a.Name + " " + i.ObjectName + " " + ii
                        try:
                            # give LineColor
                            Gui.activeDocument().activeObject().LineColor = (1.0, 0.0, 0.0)
                            # give PointColor
                            Gui.activeDocument().activeObject().PointColor = (1.0, 0.0, 0.0)
                            # give ShapeColor
                            Gui.activeDocument().activeObject().ShapeColor = (1.0, 0.0, 0.0)

                        except Exception:
                            None
                except Exception:
                    # print "Not SubObject"
                    # create repro shape object
                    Part.show(sel[i2].Shape)
                    # display the info SubObject
                    print(i2 + 1, "/", ii2 + 1, "/", len(s), " ", sel[i2].Name)

                    a = App.ActiveDocument.ActiveObject
                    # Label for the repro shape
                    #        object Name  /  original object Name
                    a.Label = a.Name + " " + sel[i2].Name

                    try:
                        # give LineColor
                        Gui.activeDocument().activeObject().LineColor = (1.0, 0.0, 0.0)
                        # give PointColor
                        Gui.activeDocument().activeObject().PointColor = (1.0, 0.0, 0.0)
                        # give ShapeColor
                        Gui.activeDocument().activeObject().ShapeColor = (1.0, 0.0, 0.0)

                    except Exception:
                        None
        else:
            printError_msg(error_msg)
        pass
    except:
        printError_msg(error_msg)

# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# import codecs   #https://docs.python.org/2/howto/unicode.html
# import Part,Draft
# #
# #__title__="Macro_ReproWire"
# #__author__ = "Mario52"
# #__url__    = "http://www.freecadweb.org/index-fr.html"
# #__version__ = "00.01"
# #__date__   = "24/10/2015"
# #
#
# sel = Gui.Selection.getSelection()
# s  = Gui.Selection.getSelectionEx()
#
# try:
#     if len(sel) != 0:
#             print "Object(s): ", len(sel), ", SubObject(s): ", len(s)
#             i2 = ii2 = -1
#             for i in s:
#                 i2 += 1
#                 ii2 = -1
#                 try:
#                     Gui.Selection.getSelectionEx()[i2].SubObjects[ii2]
#                     for ii in i.SubElementNames:
# #                        print "SubObject"
#                         ii2 += 1
#                         Part.show(Gui.Selection.getSelectionEx()[i2].SubObjects[ii2].copy())   # create repro shape subObject
#                         print i2+1,"/", ii2+1,"/", len(s)," ", i.ObjectName," ", ii               # display the info SubObject
#                         a = App.ActiveDocument.ActiveObject
#                         #    object Name  / original object Name / SubObject Name
#                         a.Label = a.Name + " " + i.ObjectName + " " + ii                              # Label for the repro shape
#                         try:
#                             Gui.activeDocument().activeObject().LineColor = (1.0,0.0,0.0)     # give LineColor
#                             Gui.activeDocument().activeObject().PointColor = (1.0,0.0,0.0)     # give PointColor
#                             Gui.activeDocument().activeObject().ShapeColor = (1.0,0.0,0.0)     # give ShapeColor
#                         except Exception:
#                             None
#                 except Exception:
# #                    print "Not SubObject"
#                     Part.show(sel[i2].Shape)                                                          # create repro shape object
#                     print i2+1,"/", ii2+1,"/", len(s)," ", sel[i2].Name                            # display the info SubObject
#                     a = App.ActiveDocument.ActiveObject
#                     #        object Name  /  original object Name
#                     a.Label =a.Name + " " +  sel[i2].Name                                             # Label for the repro shape
#                     try:
#                         Gui.activeDocument().activeObject().LineColor = (1.0,0.0,0.0)         # give LineColor
#                         Gui.activeDocument().activeObject().PointColor = (1.0,0.0,0.0)         # give PointColor
#                         Gui.activeDocument().activeObject().ShapeColor = (1.0,0.0,0.0)         # give ShapeColor
#                     except Exception:
#                         None
#     else:
#         print "Select one object"
# except Exception:
#     print "Unexpected error"


def object_alignFaces():
    """
    Align the Face(s) from selected object(s) to the last Face selected.
     - Click first to select a Face of an object or several Faces from several objects. 
     - Click second to select a Face to align to.
    
    NB:
      The center of rotation is the center of the bounbing box if possible or 
      the center of the Face.
     
      if the Face of the object selected is already aligned to the last one,
      a rotation of 180 deg is applied to the object.
      In this case the Axis of rotation is Z vector: Base.Vector(0, 0, 1)  
      
      Two clicks will rotate by 180 deg.
    """
    msg = verbose

    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select at least two(2) Faces (from two objects) !\n" +\
    "All Faces will be aligned to the last one !"

    Selection = get_SelectedObjectsWithParent(info=msg, printError=False)
    m_actDoc = get_ActiveDocument(info=1)
    Selection2 = Gui.Selection.getSelectionEx(m_actDoc.Name)

    try:
        SelectedObjects = Selection
        Number_of_Planes = SelectedObjects[2]
        if msg != 0:
            print_msg("Number_of_Planes=" + str(Number_of_Planes))

        if Number_of_Planes >= 2:
            Plane_List = SelectedObjects[5]
            if msg != 0:
                print_msg(" Plane_List=" + str(Plane_List))

            Origin = Base.Vector(0, 0, 0)
            # Get the Reference Plane: last of the selected
            Ref_Plane_dict = Plane_List[-1]
            for Selected_Plane, Parent_Plane in Ref_Plane_dict.iteritems():
                Plane_Point_ref = Selected_Plane.CenterOfMass
                Plane_Normal_ref = Selected_Plane.normalAt(0, 0)
            if msg != 0:
                print_point(Plane_Point_ref, msg="Reference Plane_Point = ")
                print_point(Plane_Normal_ref, msg="Reference Plane_Normal = ")
            del Plane_List[-1]

            for Selected_Plane_dict in Plane_List:
                if msg != 0:
                    print_msg("Selected_Plane_dict = " + str(Selected_Plane_dict))
                for Selected_Plane, Parent_Plane in Selected_Plane_dict.iteritems():
                    if msg != 0:
                        print_msg("Selected_Plane = " + str(Selected_Plane))
                        print_msg("Parent = " + str(Parent_Plane))
                    try:
                        Plane_Point = Parent_Plane.Shape.BoundBox.Center
                    except:
                        Plane_Point = Selected_Plane.CenterOfMass

                    Plane_Normal = Selected_Plane.normalAt(0, 0)
                    if msg != 0:
                        print_point(Plane_Point, msg="Plane_Point = ")
                        print_point(Plane_Normal, msg="Plane_Normal = ")

                    if colinearVectors(Plane_Normal, Origin, Plane_Normal_ref, info=0, tolerance=1e-12):
                        rot_axis = Base.Vector(0, 0, 1).cross(Plane_Normal)
                        rot_center = Plane_Point
                        rot_angle = 180. + m_angleAlignFaces
                        Draft.rotate(Parent_Plane, rot_angle, rot_center, rot_axis)
                    else:
                        m_angle, m_angle_rad = angleBetween(Plane_Normal, Plane_Normal_ref)
                        rot_axis = Plane_Normal.cross(Plane_Normal_ref)
                        rot_center = Plane_Point
                        rot_angle = m_angle + m_angleAlignFaces
                        Draft.rotate(Parent_Plane, rot_angle, rot_center, rot_axis)

            # Reset the selection changed by Draft.rotate
            reset_SelectedObjects(Selection2, info=0)

        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def angleAlignEdges(value):
    """ Respond to the change in angle value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_angleAlignEdges
        if str(value) == '-':
            return
        m_angleAlignEdges = float(value)
        print_msg("New angle in degrees is:" + str(m_angleAlignEdges))
    except ValueError:
        printError_msg("Angle must be valid number !")


def object_alignEdges():
    """ 
    Align the Edge(s) from selected object(s) to the last Edge selected.
    - Click first to select an Edge of an object or several Edges from several objects. 
    - Click second to select an Edge to align to.

    NB:
      The center of rotation is the center of the bounbing box if possible or 
      the center of the Edge.
     
      if the Edge of the object selected is already aligned to the last one,
      a rotation of 180 deg is applied to the object.
      In this case the Axis of rotation is Z vector: Base.Vector(0, 0, 1)
      
      Two clicks will rotate by 180 deg.
    """
    msg = verbose

    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select at least two(2) Edges (from two objects) !\n" +\
    "All Edges will be aligned to the last one !"

    Selection = get_SelectedObjectsWithParent(info=msg, printError=False)
    m_actDoc = get_ActiveDocument(info=1)
    Selection2 = Gui.Selection.getSelectionEx(m_actDoc.Name)

    try:
        SelectedObjects = Selection
        Number_of_Edges = SelectedObjects[1]
        if msg != 0:
            print_msg("Number_of_Edges=" + str(Number_of_Edges))

        if Number_of_Edges >= 2:
            Edge_List = SelectedObjects[4]
            if msg != 0:
                print_msg(" Edge_List=" + str(Edge_List))

            # Get the Reference Edge: last of the selected
            Ref_Edge_dict = Edge_List[-1]
            for Selected_Edge, Parent_Edge in Ref_Edge_dict.iteritems():
                Edge_ref = Selected_Edge

            del Edge_List[-1]

            for Selected_Edge_dict in Edge_List:
                if msg != 0:
                    print_msg("Selected_Edge_dict = " + str(Selected_Edge_dict))
                for Selected_Edge, Parent_Edge in Selected_Edge_dict.iteritems():
                    if msg != 0:
                        print_msg("Selected_Edge = " + str(Selected_Edge))
                        print_msg("Parent = " + str(Parent_Edge))
                    try:
                        Edge_Point = Parent_Edge.Shape.BoundBox.Center
                    except:
                        Edge_Point = centerLinePoint(Selected_Edge, info=0)

                    if msg != 0:
                        print_point(Edge_Point, msg="Edge_Point = ")
                    Edge = Selected_Edge

                    if colinearEdges(Edge, Edge_ref, info=msg, tolerance=1e-12):
                        rot_axis = Base.Vector(0, 0, 1).cross(edgeToVector(Edge))
                        rot_center = Edge_Point
                        rot_angle = 180. + m_angleAlignEdges
                        Draft.rotate(Parent_Edge, rot_angle, rot_center, rot_axis)
                    else:
                        m_angle, m_angle_rad = angleBetween(Edge, Edge_ref)
                        print_msg("m_angle = " + str(m_angle))
                        rot_axis = edgeToVector(Edge).cross(edgeToVector(Edge_ref))
                        print_msg("rot_axis = " + str(rot_axis))
                        rot_center = Edge_Point
                        rot_angle = m_angle + m_angleAlignEdges
                        Draft.rotate(Parent_Edge, rot_angle, rot_center, rot_axis)
            # Reset the selection changed by Draft.rotate
            reset_SelectedObjects(Selection2, info=0)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def angleAlignMainAxis(value):
    """ Respond to the change in angle value from the text box.
    """
    try:
        # First we check if a valid number have been entered
        global m_angleAlignMainAxis
        if str(value) == '-':
            return
        m_angleAlignMainAxis = float(value)
        print_msg("New angle in degrees is:" + str(m_angleAlignMainAxis))
    except ValueError:
        printError_msg("Angle must be valid number !")


def object_alignMainAxis():
    """Align the main Axis (first of the 2 axis set) from selected object(s) to the last Edge (or 2 main Axis from an object) selected.
     - Click first to select at least one object! 
    This or These first object(s) will be rotated.
     - Click last to select an Edge (or an Object) to align to (this last object is fixed and will never move).
    Then Click the button.
    
    NB:
      The 2 main first axis are calculated using scan and sort from all axis of the object.
      The center of rotation is at center mass location of each selected object.

      In case of several objects selection: 
        The 2 main Axis of the first object(s) will be aligned on the 2 main Axis of the last one.
      In case of several objects selection plus one Edge:
         The first main Axis of the object(s) will be aligned on the Edge.
     -  One click will align first main Axes.
     -  Second click will also align the second main Axes if exists on last object or
      will rotate by 180 deg the moving objects on first main axes.
     -  Third and following clicks will rotate by 180 deg the moving objects on first main axes. 
    """
    msg = verbose

    try:
        import numpy as np
    except:
        error_msg = "Unable to import numpy !\n" +\
        "You MUSt install numpy to use this function !"
        printError_msg(error_msg)

    m_actDoc = get_ActiveDocument(info=msg)
    if m_actDoc is None:
        return None


    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select at least one object and one object (or one Edge)!\n" +\
    "In case of several objects selection:\n" +\
    "  The 2 main Axis of the first object(s) will be aligned on the 2 main Axis of the last one.\n" +\
    "In case of several objects selection plus one Edge:\n" +\
    "  The first main Axis of the object(s) will be aligned on the Edge."

    Selection2 = Gui.Selection.getSelectionEx(m_actDoc.Name)

    SelectedObjects = get_SelectedObjects(info=msg, printError=False)


    try:
        Selected_Axes = []
        Ref_Edge1 = None
        Ref_Edge2 = None
        Edge1 = None
        Edge2 = None

        Number_of_Edges = SelectedObjects[1]
        Number_of_Faces = SelectedObjects[2]
        Number_of_Objects = len(SelectedObjects[6])
        if msg != 0:
            print_msg("Number_of_Edges = " + str(Number_of_Edges))
            print_msg("Number_of_Faces = " + str(Number_of_Faces))
            print_msg("Number_of_Objects = " + str(Number_of_Objects))

        # Get the Reference Edge: last of the selected or main axes of last object
        if Number_of_Edges >= 1:
            Edge_List = SelectedObjects[4]
            # Get the Reference Edge: last of the selected
            Ref_Edge1 = (Edge_List[-1].Vertexes[0].Point, Edge_List[-1].Vertexes[-1].Point)
            # del Edge_List[-1]
        else:
            if Number_of_Objects > 1:
                Ref_object = SelectedObjects[6][-1]
                Selected_Axes = []
                for m_edge in Ref_object.Shape.Edges:
                    Selected_Axes.append(m_edge)
                Number_of_Axes = len(Selected_Axes)
                if Number_of_Axes == 0:
                    printError_msg(error_msg)
                    return
                Selected_AxesWithLength, Selected_Points =  get_mainAxesFromSelectedAxes(Selected_Axes, info=0)
                if Selected_AxesWithLength:
                    m_new_dim = len(Selected_AxesWithLength)
                    Vector_Center = meanVectorsPoint(Selected_Points, info=0)
                    if m_new_dim >= 1:
                        # Get the first main axis
                        m_axiswithlength = Selected_AxesWithLength[-1]
                        m_p1 = m_axiswithlength[0].Vertexes[0].Point
                        m_p2 = m_axiswithlength[0].Vertexes[-1].Point
                        m_c = centerLinePoint(m_axiswithlength[0])
                        m_mv = Vector_Center.sub(m_c)
                        Vector = m_p2.sub(m_p1).normalize().multiply(m_axiswithlength[1]/2)

                        m_c.add(Vector.multiply(-1)).add(m_mv)
                        Ref_Edge1 = (m_c.add(Vector).add(m_mv), m_c.add(Vector.multiply(-1)).add(m_mv))
                        if m_new_dim >= 2:
                            # Get the second main axis
                            m_axiswithlength = Selected_AxesWithLength[-2]
                            m_p1 = m_axiswithlength[0].Vertexes[0].Point
                            m_p2 = m_axiswithlength[0].Vertexes[-1].Point
                            m_c = centerLinePoint(m_axiswithlength[0])
                            m_mv = Vector_Center.sub(m_c)
                            Vector = m_p2.sub(m_p1).normalize().multiply(m_axiswithlength[1]/2)

                            m_c.add(Vector.multiply(-1)).add(m_mv)
                            Ref_Edge2 = (m_c.add(Vector).add(m_mv), m_c.add(Vector.multiply(-1)).add(m_mv))
                    else:
                        printError_msg(error_msg)
                        return
                # del SelectedObjects[6][-1]
            else:
                printError_msg(error_msg)

        if not Ref_Edge1:
            printError_msg(error_msg)
            return
        if msg != 0:
            print_msg("Ref_Edge = " + str(Ref_Edge1))

        Number_of_Objects = len(SelectedObjects[6])
        if msg != 0:
            print_msg("Number_of_Objects to move = " + str(Number_of_Objects - 1))
        if Number_of_Objects > 0:
            Object_List = SelectedObjects[6]
            for m_object in Object_List[:-1]:
                if msg != 0:
                    print_msg("m_object = " + str(m_object))
                Selected_Axes = []
                for m_edge in m_object.Shape.Edges:
                    Selected_Axes.append(m_edge)

                Number_of_Axes = len(Selected_Axes)
                if msg != 0:
                    print_msg("Number_of_Axes = " + str(Number_of_Axes))
                if Number_of_Axes == 0:
                    continue

                Selected_AxesWithLength, Selected_Points =  get_mainAxesFromSelectedAxes(Selected_Axes, info=0)
                if not Selected_AxesWithLength:
                    continue
                m_new_dim = len(Selected_AxesWithLength)
                if msg != 0:
                    print_msg("New Number_of_Axes = " + str(m_new_dim))
                Vector_Center = m_object.Shape.CenterOfMass
                if not Vector_Center:
                    Vector_Center = meanVectorsPoint(Selected_Points, info=0)
                if m_new_dim >= 1:
                    # Get the first main axis
                    m_axiswithlength = Selected_AxesWithLength[-1]
                    m_p1 = m_axiswithlength[0].Vertexes[0].Point
                    m_p2 = m_axiswithlength[0].Vertexes[-1].Point
                    m_c = centerLinePoint(m_axiswithlength[0])
                    m_mv = Vector_Center.sub(m_c)
                    Vector = m_p2.sub(m_p1).normalize().multiply(m_axiswithlength[1]/2)

                    m_c.add(Vector.multiply(-1)).add(m_mv)
                    Selected_Edge1 = (m_c.add(Vector).add(m_mv), m_c.add(Vector.multiply(-1)).add(m_mv))
                    if m_new_dim >= 2:
                        # Get the second main axis
                        m_axiswithlength = Selected_AxesWithLength[-2]
                        m_p1 = m_axiswithlength[0].Vertexes[0].Point
                        m_p2 = m_axiswithlength[0].Vertexes[-1].Point
                        m_c = centerLinePoint(m_axiswithlength[0])
                        m_mv = Vector_Center.sub(m_c)
                        Vector = m_p2.sub(m_p1).normalize().multiply(m_axiswithlength[1] / 2)

                        m_c.add(Vector.multiply(-1)).add(m_mv)
                        Selected_Edge2 = (m_c.add(Vector).add(m_mv), m_c.add(Vector.multiply(-1)).add(m_mv))
                else:
                    printError_msg(error_msg)
                    return

                Edge1 = Selected_Edge1
                if Selected_Edge2:
                    Edge2 = Selected_Edge2
                if msg != 0:
                    print_msg("Selected_Edge1 = " + str(Edge1))
                    if Selected_Edge2:
                        print_msg("Selected_Edge2 = " + str(Edge2))
                A = Base.Vector(Ref_Edge1[-1]).sub(Base.Vector(Ref_Edge1[0]))
                if Ref_Edge2:
                    B = Base.Vector(Ref_Edge2[-1]).sub(Base.Vector(Ref_Edge2[0]))
                Z = Base.Vector(0, 0, 0)
                C = Base.Vector(Edge1[-1]).sub(Base.Vector(Edge1[0]))
                if Selected_Edge2:
                    D = Base.Vector(Edge2[-1]).sub(Base.Vector(Edge2[0]))

                # if angleBetween(C,A) == 0.0 or angleBetween(C,A) == 180.0:
                if colinearVectors(A, Z, C, info=msg, tolerance=1e-7):
                    if msg != 0:
                        print_msg("First main axis are colinear!")
                    if Selected_Edge2 and Ref_Edge2:
                        # if angleBetween(D,B) == 0.0 or angleBetween(D,B) == 180.0:
                        if colinearVectors(B, Z, D, info=msg, tolerance=1e-7):
                            if msg != 0:
                                print_msg("Second main axis are colinear!")
                            rot_axis = Base.Vector(0, 0, 1).cross(D)
                            rot_center = Vector_Center
                            rot_angle = 180. + m_angleAlignMainAxis
                            if msg != 0:
                                print_msg("rot_axis = " + str(rot_axis))
                                print_msg("rot_center = " + str(rot_center))
                                print_msg("rot_angle = " + str(rot_angle))
                            Draft.rotate(m_object, rot_angle, rot_center, rot_axis)
                        else:
                            if msg != 0:
                                print_msg("Second main axis are Not colinear!")
                            m_angle, _ = angleBetween(D, B)
                            rot_axis = D.cross(B)
                            print_msg("rot_axis = " + str(rot_axis))
                            rot_center = Vector_Center
                            rot_angle = m_angle + m_angleAlignMainAxis
                            if msg != 0:
                                print_msg("rot_axis = " + str(rot_axis))
                                print_msg("rot_center = " + str(rot_center))
                                print_msg("rot_angle = " + str(rot_angle))
                            Draft.rotate(m_object, rot_angle, rot_center, rot_axis)
                    else:
                        rot_axis = Base.Vector(0, 0, 1).cross(C)
                        rot_center = Vector_Center
                        rot_angle = 180. + m_angleAlignMainAxis
                        if msg != 0:
                            print_msg("rot_axis = " + str(rot_axis))
                            print_msg("rot_center = " + str(rot_center))
                            print_msg("rot_angle = " + str(rot_angle))
                        Draft.rotate(m_object, rot_angle, rot_center, rot_axis)
                else:
                    if msg != 0:
                        print_msg("First main axis are Not colinear!")
                    m_angle, _ = angleBetween(C, A)
                    rot_axis = C.cross(A)
                    print_msg("rot_axis = " + str(rot_axis))
                    rot_center = Vector_Center
                    rot_angle = m_angle + m_angleAlignMainAxis
                    if msg != 0:
                        print_msg("rot_axis = " + str(rot_axis))
                        print_msg("rot_center = " + str(rot_center))
                        print_msg("rot_angle = " + str(rot_angle))
                    Draft.rotate(m_object, rot_angle, rot_center, rot_axis)
        # Case of Cube
        # case of Sphere
        # case of Tore
        # Case of Cylinder
        # Case of Cone
        # Case of other objects
            # Reset the selection changed by Draft.rotate
            reset_SelectedObjects(Selection2, info=0)
        else:
            printError_msg(error_msg)
    except:
        printError_msg(error_msg)


def object_jointPoints():
    """
    Joint Point(s) from selected object(s) to the last Point selected.
    - Click first to select a Point of an object or several Points from several objects. 
    - Click second to select an Point to joint to.
    """
    msg = verbose

    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select at least two(2) Points (from two different objects) !\n" +\
    "All Points will be displaced onto the last one !"

    Selection = get_SelectedObjectsWithParent(info=msg, printError=False)

    try:
        SelectedObjects = Selection
        Number_of_Points = SelectedObjects[0]
        if msg != 0:
            print_msg("Number_of_Points=" + str(Number_of_Points))

        if Number_of_Points >= 2:
            Point_List = SelectedObjects[3]
            if msg != 0:
                print_msg(" Point_List=" + str(Point_List))

            # Get the Reference Point: last of the selected
            Ref_Point_dict = Point_List[-1]
            for Selected_Point, Parent_Point in Ref_Point_dict.iteritems():
                Point_ref = Selected_Point
                Parent_ref = Parent_Point
            if msg != 0:
                print_point(Point_ref, msg="Reference Point_ref = ")
            del Point_List[-1]

            for Selected_Point_dict in Point_List:
                if msg != 0:
                    print_msg("Selected_Point_dict = " + str(Selected_Point_dict))
                for Selected_Point, Parent_Point in Selected_Point_dict.iteritems():
                    if msg != 0:
                        print_msg("Selected_Point = " + str(Selected_Point))
                        print_msg("Parent_Point = " + str(Parent_Point))
                    m_move = Point_ref.Point.sub(Selected_Point.Point)
                    if msg != 0:
                        print_msg("m_move = " + str(m_move))
                    m_rot = Parent_Point.Placement.Rotation
                    m_base = Parent_Point.Placement.Base
                    m_newplace = App.Placement(m_base.add(m_move), m_rot)
                    Parent_Point.Placement = m_newplace

        else:
            printError_msg(error_msg)

    except:
        printError_msg(error_msg)


def object_jointFaces():
    """Joint Face(s) from selected object(s) to the last Face selected.
    - Click first to select a Face of an object or several Faces from several objects. 
    - Click second to select an Face to joint to.
    """
    msg = verbose

    createFolders('WorkPoints')
    error_msg =\
    "INCORRECT Object(s) Selection:\n" +\
    "You Must Select at least two(2) Faces (from two different objects) !\n" +\
    "All Faces will be displaced onto the last one !"

    Selection = get_SelectedObjectsWithParent(info=msg, printError=False)
    m_actDoc = get_ActiveDocument(info=1)
    Selection2 = Gui.Selection.getSelectionEx(m_actDoc.Name)

    try:
        SelectedObjects = Selection
        Number_of_Planes = SelectedObjects[2]
        if msg != 0:
            print_msg("Number_of_Planes=" + str(Number_of_Planes))

        if Number_of_Planes >= 2:
            Plane_List = SelectedObjects[5]
            if msg != 0:
                print_msg(" Plane_List=" + str(Plane_List))

            Origin = Base.Vector(0, 0, 0)
            # Get the Reference Plane: last of the selected
            Ref_Plane_dict = Plane_List[-1]
            for Selected_Plane, Parent_Plane in Ref_Plane_dict.iteritems():
                Plane_Point_ref = Selected_Plane.CenterOfMass
                Plane_Normal_ref = Selected_Plane.normalAt(0, 0)
            if msg != 0:
                print_point(Plane_Point_ref, msg="Reference Plane_Point = ")
                print_point(Plane_Normal_ref, msg="Reference Plane_Normal = ")
                point_User_Name = plot_point(Plane_Point_ref, part="Part::Feature", name="End", grp="WorkPoints")
                Gui.ActiveDocument.getObject(point_User_Name).PointColor = (1.0, 1.0, 1.0)

            del Plane_List[-1]

            for Selected_Plane_dict in Plane_List:
                if msg != 0:
                    print_msg("Selected_Plane_dict = " + str(Selected_Plane_dict))
                for Selected_Plane, Parent_Plane in Selected_Plane_dict.iteritems():
                    if msg != 0:
                        print_msg("Selected_Plane = " + str(Selected_Plane))
                        print_msg("Parent = " + str(Parent_Plane))
                    try:
                        Plane_Point = Parent_Plane.Shape.BoundBox.Center
                    except:
                        Plane_Point = Selected_Plane.CenterOfMass

                    Plane_Normal = Selected_Plane.normalAt(0, 0)
                    Plane_Center = Selected_Plane.CenterOfMass
                    point = App.ActiveDocument.addObject("Part::Feature", "Start")
                    point.Shape = Part.Vertex(Plane_Center)

                    if msg != 0:
                        print_point(Plane_Point, msg="Plane_Point = ")
                        print_point(Plane_Normal, msg="Plane_Normal = ")
                        point_User_Name = plot_point(Plane_Point, part="Part::Feature", name="Center_Rot", grp="WorkPoints")
                        Gui.ActiveDocument.getObject(point_User_Name).PointColor = (0.0, 0.0, 1.0)
# ==============================================================================
#             # First align Faces
# ==============================================================================
                    if colinearVectors(Plane_Normal, Origin, Plane_Normal_ref, info=msg, tolerance=1e-12):
                        if Plane_Normal == Plane_Normal_ref.multiply(-1):
                            Plane_Center = Selected_Plane.CenterOfMass
                        # else:
                        rot_axis = Base.Vector(0, 0, 1).cross(Plane_Normal)
                        rot_center = Plane_Point
                        rot_angle = 180.
                        Draft.rotate(Parent_Plane, rot_angle, rot_center, rot_axis)
                        Draft.rotate(point, rot_angle, rot_center, rot_axis)
                        Plane_Center = point.Shape.Point
                    else:
                        m_angle, m_angle_rad = angleBetween(Plane_Normal, Plane_Normal_ref)
                        rot_axis = Plane_Normal.cross(Plane_Normal_ref)
                        rot_center = Plane_Point
                        rot_angle = m_angle
                        Draft.rotate(Parent_Plane, rot_angle, rot_center, rot_axis)
                        Draft.rotate(point, rot_angle, rot_center, rot_axis)
                        Plane_Center = point.Shape.Point
                    if msg != 0:
                        print_msg("rotation done !")
                    # Reset the selection changed by Draft.rotate
                    reset_SelectedObjects(Selection2, info=0)

                    if msg != 0:
                        point_User_Name = plot_point(Plane_Center, part="Part::Feature", name="Start", grp="WorkPoints")
                        Gui.ActiveDocument.getObject(point_User_Name).PointColor = (0.0, 0.0, 1.0)

# ==============================================================================
#             # Then Joint Faces
# ==============================================================================
                    m_move = Plane_Point_ref.sub(Plane_Center)
                    m_oldplace = Parent_Plane.Placement
                    m_rot = m_oldplace.Rotation
                    m_base = m_oldplace.Base
                    m_newplace = App.Placement(m_base.add(m_move), m_rot)
                    Parent_Plane.Placement = m_newplace
                    App.getDocument(str(App.activeDocument().Name)).removeObject(point.Label)
                    if msg != 0:
                        print_msg("move done !")

    except:
        printError_msg(error_msg)


####################################################################################
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

####################################################################################
# ==============================================================================
# App.newDocument()
# v=Gui.activeDocument().activeView()
#
# #This class logs any mouse button events. As the registered callback function fires twice for 'down' and
# # 'up' events we need a boolean flag to handle this.
# class ViewObserver:
#    def logPosition(self, info):
#        down = (info["State"] == "DOWN")
#        pos = info["Position"]
#        if (down):
#            App.Console.PrintMessage("Clicked on position: (" + str(pos[0]) + ", " + str(pos[1]) + ")\n")
#
# o = ViewObserver()
# c = v.addEventCallback("SoMouseButtonEvent",o.logPosition)

# Quit Observer
# v.removeEventCallback("SoMouseButtonEvent",c)
# ==============================================================================


class ViewObserver:
    """ This class logs any mouse button events.
    """
    def __init__(self, view):
        """view=Gui.activeDocument().activeView()
        """
        self.view = view

    def logPosition(self, info):
        # As the registered callback function fires twice for 'down' and
        # 'up' events we need a test to handle this
        down = (info["State"] == "DOWN")
        # if info["State"] == "DOWN":
        if (down):
            # 2D position X,Y
            # 0,0 = bottom left of the FreeCAD work window
            # Xmax,Ymax = top right of the FreeCAD work window
            pos = info["Position"]
            print_msg("Clicked on position: (" + str(pos[0]) + ", " + str(pos[1]) + ")\n")
            # 3D position X,Y,Z anywhere in the work window and on top of an object
            pnt = self.view.getPoint(pos)
            print_msg("World coordinates: " + str(pnt) + "\n")
            # Object info or None
            Object_info = self.view.getObjectInfo(pos)
            print_msg("Object info: " + str(Object_info) + "\n")

    def getObjectInfo(self, info):
        global myObject
        myObject = None
        down = (info["State"] == "DOWN")
        pos = info["Position"]
        if (down):
            myObject = self.view.getObjectInfo(pos)


class WorkFeatureTab():
    def __init__(self, movable=True):

        self.movable = movable
        if self.movable:
            # Look if WF movable tab already exists
            m_mvtab = Gui.getMainWindow().findChild(QtGui.QDockWidget, "WorkFeatures")
            if m_mvtab:
                m_mvtab.show()
                m_mvtab.raise_()
                return

        # Get main window
        self.m_main = self.getMainWindow()

        # Get Tab panel
        if self.movable:
            self.m_tab = self.getComboViewMv(self.m_main)

            self.m_dialog = QtGui.QWidget()
            self.m_tab.addWidget(self.m_dialog)
            self.ui = WFGui.Ui_Form()
            self.ui.setupUi(self.m_dialog)
            self.m_dialog.setMaximumWidth(400)
        else:
            self.m_tab = self.getComboView(self.m_main)

            if self.m_tab.count() == 2:
                # Create a new fake dialog
                self.m_fake_dialog = QtGui.QDialog()
                self.m_tab.addTab(self.m_fake_dialog, "")

            # Create a new dialog for WorkFeatureTab
            self.m_dialog = QtGui.QDialog()
            # Add the dialog in a new tab or focus on it if already exists
            if self.m_tab.count() >= 2:
                for i in range(2, self.m_tab.count()):
                    # print_msg (str(isinstance(self.m_tab.tabText(i), unicode)))
                    # print_msg (str(unicode(self.m_tab.tabText(i), 'utf-8')))
                    # if "Work Features" == str(unicode(self.m_tab.tabText(i), 'utf-8')):
                    if "Work Features" == str(_fromUtf8(self.m_tab.tabText(i))):
                        self.m_tab.removeTab(int(i))
                        break

            self.m_tab.addTab(self.m_dialog, "Work Features")

            self.ui = WFGui.Ui_Form()
            self.ui.setupUi(self.m_dialog)
            self.m_tab.setCurrentIndex(3)

# ----------------------------------------------------------------
        # Create a Rotation object and connect
        self.eventsRot = RotationEvents(self.ui)
        # Create a Translation object and connect
        self.eventsTrans = TranslationEvents(self.ui)

        # #Create a Parametric 2D Curve object and connect
        # self.events2D = ParametricCurve2DEvents(self.ui)
        # # Create a Parametric 3D Curve object and connect
        # self.events3D = ParametricCurve3DEvents(self.ui)

        # ## Connect to functions
        self.connections_for_checkbox_toggled = {
                             "checkBox_object_center"      : "bBox_toggled",
                             "checkBox_solid"              : "solid_toggled",
                             "checkBox_allsubselect"       : "subselect_toggled",
                             "checkBox_volumBB"            : "volumBBox_toggled",
                             "checkBox_infoBB"             : "infoBBox_toggled"
                            }
        self.connections_for_button_clicked = {
                             "button_WF_quit"              : "quit_clicked",
                             "button_curves_and_surfaces"  : "launch_curvesAndSurfaces",
                            }
                #self.PB_Quit.clicked.connect(self.on_PB_Quit_clicked) # quit

        self.connections_for_button_pressed = {
                             "button_origin"              : "plot_originObject",

                             "button_object_center"       : "plot_centerObjectPoint",
                             "button_Npoints_center"      : "plot_NpointsPoint",
                             "button_line_center"         : "plot_centerLinePoint",
                             "button_line_extrema"        : "plot_extremaLinePoint",
                             "button_circle_center"       : "plot_centerCirclePoint",
                             "button_point_on_line"       : "plot_alongLinePoint",
                             "button_face_center"         : "plot_centerFacePoint",
                             "button_line_face_point"     : "plot_lineFacePoint",
                             "button_points_projection"   : "plot_projected_points",

                             "button_point_face_point"    : "plot_pointFacePoint",
                             "button_twolines_point"      : "plot_2LinesPoint",
                             "button_point_line_point"    : "plot_pointLinePoint",
                             "button_distPoint"           : "plot_distPoint",
                             "button_cut_wire_point"      : "plot_cutWirePoint",
                             "button_click_for_point"     : "plot_clickForPoint",
                             "button_object_base_point"   : "plot_baseObjectPoint",
                             "button_object_center_mass_point": "plot_centerMassObjectPoint",
                             "button_object_Npoint"       : "plot_objectNPoints",

                             "button_points_load"         : "point_toLoad",
                             "button_points_save"         : "point_toSave",
                             "button_points_random"       : "plot_points_random",
                             "button_point_to_sketch"     : "point_toSketch",

                             "button_object_axis"         : "plot_centerObjectAxes",
                             "button_twopoints_axis"      : "plot_2PointsAxis",
                             "button_Npoints_axis"        : "plot_NPointsAxis",
                             "button_cylinder_axis"       : "plot_cylinderAxis",
                             "button_plane_axis"          : "plot_planeAxis",
                             "button_face_normal"         : "plot_faceNormal",
                             "button_point_line_axis"     : "plot_pointLineAxis",
                             "button_line_point_axis"     : "plot_linePointAxis",
                             "button_twolines_axis"       : "plot_2LinesAxis",
                             "button_plane_point_line_axis": "plot_planeLinePointAxis",
                             "button_line_plane_axis"     : "plot_linePlaneAxis",
                             "button_twoplanes_axis"      : "plot_2PlanesAxis",

                             "button_distLine"            : "plot_distLine",
                             "button_angleLine"           : "plot_angleLine",
                             "button_cut_axis"            : "plot_cutAxis",
                             "button_cut_wire_axis"       : "plot_cutWireAxis",
                             "button_extension_axis"      : "plot_extensionAxis",
                             "button_click_for_axis"      : "plot_clickForAxis",
                             "button_object_base_axes"    : "plot_baseObjectAxes",
                             "button_object_Naxes"        : "plot_objectNAxes",
                             "button_object_3axes"        : "plot_object3Axes",
                             "button_line_to_sketch"      : "line_toSketch",

                             "button_points_to_polygon"   : "points_toPolygon",
                             # "button_wire_on_plane"       : "plot_wire_on_plane",
                             "button_points_to_convex_2Dpolygon": "Plot_convex2Dpolygon",
                             "button_4points_bezier"      : "plot_4points_bezier",

                             "button_linecenter_circle"   : "plot_linecenterCircle",
                             "button_linepoint_circle"    : "plot_linepointCircle",
                             "button_3points_circle"      : "plot_3pointsCircle",
                             "button_3points_ellipse"     : "plot_3pointsEllipse",
                             "button_3points_arc"         : "plot_3pointsArc",
                             "button_cut_circle"          : "plot_cutCircle",
                             "button_circle_to_sketch"    : "circle_toSketch",

                             "button_threepoints_plane"   : "plot_3PointsPlane",
                             "button_twopoints_plane"     : "plot_2PointsPlane",
                             "button_Npoints_plane"       : "plot_NPointsPlane",
                             "button_axisandpoint_plane"  : "plot_axisPointPlane",
                             "button_axis_point_plane"    : "plot_perpendicularAxisPointPlane",
                             "button_planeandpoint_plane" : "plot_planePointPlane",
                             "button_planeandaxis_plane"  : "plot_planeAxisPlane",
                             "button_distPlane"           : "plot_distPlane",
                             "button_face_tangent"        : "plot_faceTangentPlane",
                             "button_click_for_plane"     : "plot_clickForPlane",

                             "button_extension_plane"     : "plot_extensionPlane",
                             # "button_click_for_plane2"    : "plot_clickForPlane2",
                             "button_object_center_planes": "plot_centerObjectPlanes",

                             "button_boundingboxes"       : "plot_boundingBoxes",
                             "button_boundingbox"         : "plot_boundingBox",
                             "button_cylinder_create"     : "plot_axisPointCylinder",
                             "button_cube_create"         : "plot_axisPointCube",
                             "button_sphere_create"       : "plot_centerSphere",
                             "button_dome_create"         : "plot_centerDome",
                             "button_letter"              : "plot_letter",
                             "button_revolve"             : "plot_revolution",
                             "button_common"              : "object_common",
                             "button_difference"          : "object_difference",
                             "button_copy_objects"        : "object_copy",
                             "button_sweep"               : "plot_sectionSweep",
                             "button_beam"                : "plot_sectionBeam",

                             # "button_rotate_image"        : "rotate_image",
                             "button_scale_image"         : "scale_image",

                             "button_alignview"           : "view_align",
                             "button_trackcamera"         : "view_trackCamera",

                             "button_cut_select_object"   : "cut_selectObject",
                             "button_cut_select_line"     : "cut_selectLine",
                             "button_cut_select_plane"    : "cut_selectPlane",
                             "button_cut_reset"           : "cut_reset",
                             "button_cut_apply"           : "plot_cutObject",

                             "button_isParallel"          : "object_parallel",
                             "button_isPerpendicular"     : "object_perpendicular",
                             "button_isCoplanar"          : "object_coplanar",
                             "button_isClearance"         : "object_clearance",
                             "button_isAngle"             : "object_angle",
                             "button_isDistance"          : "points_distance",
                             "button_isLength"            : "line_length",
                             "button_isRadius"            : "object_radius",
                             "button_isArea"              : "plane_area",
                             "button_isView"              : "camera_orientation",

                             "button_alignface2view"      : "object_align2view",
                             "button_align_faces"         : "object_alignFaces",
                             "button_align_edges"         : "object_alignEdges",
                             "button_align_main_axis"     : "object_alignMainAxis",
                             "button_joint_points"        : "object_jointPoints",
                             "button_joint_faces"         : "object_jointFaces",
                            }

        self.connections_for_text_changed = {
                             "tolerance_edit"           : "setTolerance",
                             "distance_point_on_line"   : "distanceLinePoint",
                             "distance_random_points"   : "distanceRandomPoints",

                             "extension_twopoints_axis" : "extensionTwoPointsAxis",
                             "extension_face_normal"    : "extensionFaceNormal",
                             "extension_line_point_axis": "extensionLinePointAxis",
                             "extension_line"           : "extensionLine",

                             "radius_circle"            : "radiusCircle",

                             "extension_planePointPlane": "extensionPlanePointPlane",
                             "angle_planeandaxis_plane" : "anglePlaneAxisPlane",

                             "diameter_cylinder"        : "diameterCylinder",
                             "length_cylinder"          : "lengthCylinder",
                             "section_cube"             : "sectionCube",
                             "height_cube"              : "heightCube",
                             "diameter_sphere"          : "diameterSphere",
                             "diameter_dome"            : "diameterDome",

                             "angle_cut_object"         : "angleCutObject",
                             "thickness_cut_object"     : "thicknessCutObject",

                             "length_plane"             : "lengthPlane",
                             "width_plane"              : "widthPlane",
                             "length_plane_2"           : "lengthPlane",
                             "width_plane_2"            : "widthPlane",
                             "extension_plane"          : "extensionPlane",
                             "extension_axis"           : "extensionAxis",
                             "dist_plane"               : "distPlane",
                             "dist_line"                : "distLine",
                             "dist_point"               : "distPoint",
                             "length_image"             : "lengthImage",
                             "angle_align_faces"        : "angleAlignFaces",
                             "angle_align_edges"        : "angleAlignEdges",
                             "angle_align_main_axis"    : "angleAlignMainAxis",
                             "angle_revolve"            : "angleRevolve",
                             "size_letter"              : "sizeLetter",
                             "letter"                   : "letter",
                            }

        self.connections_for_spin_changed = {
                             "spin_line_center"         : "numberLinePart",
                             "spin_axis_cut"            : "numberLineCut",
                             "spin_wire_cut_point"      : "numberPointCutWire",
                             "spin_wire_cut_axis"       : "numberAxisCutWire",
                             "spin_random_points"       : "numberRandomPoint",
                             "spin_circle_cut"          : "numberCircleCut",
                             "spin_dist_plane"          : "numberPlane",
                             "spin_dist_line"           : "numberLine",
                             "spin_angle_line"          : "numberLine2",
                             "spin_dist_point"          : "numberPoint",
                             "spin_frequency_dome"      : "frequencyDome",
                            }

        self.connections_for_radiobutton_clicked = {
                             "radioButton_verbose"      : "verbose_toggled",
                             "radioButton_biColor"      : "biColor_toggled",
                             "radioButton_copy"         : "copy_toggled",
                             "radioButton_Frenet"       : "frenet_toggled",
                            }

        self.connections_for_combobox_changed = {
                             "point_loc_comboBox"       : "sel_attachPoint",
                             "transition_comboBox"      : "sel_transition",
                             "Image_comboBox_axis_scale": "sel_imageAxisScale",
                             "point_proj_comboBox"      : "sel_projection",
                             "point_proj_comboBox_2"    : "sel_projection2",
                            }

        for m_key, m_val in self.connections_for_button_clicked.items():
            # print_msg( "Connecting: " + str(m_key) + " and " + str(m_val) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("clicked()"),
                                   getattr(self, str(m_val)))

        for m_key, m_val in self.connections_for_button_pressed.items():
            # print_msg( "Connecting: " + str(m_key) + " and " + str(m_val) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("pressed()"),
                                   globals()[str(m_val)])

        for m_key, m_val in self.connections_for_text_changed.items():
            # print_msg( "Connecting: " + str(m_key) + " and " + str(m_val) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("textChanged(QString)")),
                                   globals()[str(m_val)])
            # QtCore.SIGNAL(QtCore.QString.fromUtf8("textChanged(QString)")),globals()[str(m_val)])

        for m_key, m_val in self.connections_for_spin_changed.items():
            # print_msg( "Connecting: " + str(m_key) + " and " + str(m_val) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("valueChanged(int)"),
                                   globals()[str(m_val)])

        for m_key, m_val in self.connections_for_checkbox_toggled.items():
            # print_msg( "Connecting: " + str(m_key) + " and " + str(m_val) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("toggled(bool)")),
                                   globals()[str(m_val)])

        for m_key, m_val in self.connections_for_radiobutton_clicked.items():
            # print_msg( "Connecting: " + str(m_key) + " and " + str(m_val) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("clicked(bool)")),
                                   globals()[str(m_val)])

        for m_key, m_val in self.connections_for_combobox_changed.items():
            # print_msg( "Connecting: " + str(m_key) + " and " + str(m_val) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")),
                                   globals()[str(m_val)])

        self.m_dialog.show()
        m_text = str(myRelease)
        # self.ui.label_release.setText(_translate("Form", m_text, None))
        self.ui.label_release.setText(m_text)

# ----------------------------------------------------------------
        if self.movable:
            t = Gui.getMainWindow()
            wf = t.findChild(QtGui.QDockWidget, "WorkFeatures")
            cv = t.findChild(QtGui.QDockWidget, "Combo View")
            print_msg("Combo View" + str(cv))
            print_msg("WorkFeatures" + str(wf))
            cv.setFeatures(QtGui.QDockWidget.DockWidgetMovable | QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetClosable)
            wf.setFeatures(QtGui.QDockWidget.DockWidgetMovable | QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetClosable)
            if wf and cv:
                t.tabifyDockWidget(cv, wf)
                print_msg("Tabified done !")
                wf.activateWindow()
                wf.raise_()

        print_msg("icons path = " + str(WF_ICONS_PATH))

    def quit_clicked(self):
        print_msg("Quit requested !")
        if self.movable:
            self.dw.close()
            # self.close()
            # self.m_dialog.close()
            if self.m_tab.count() >= 2:
                for i in range(2, self.m_tab.count()):
                    if "Work Features" == str(_fromUtf8(self.m_tab.tabText(i))):
                        self.m_tab.removeTab(int(i))
                        break
        else:
            self.m_dialog.close()
            if self.m_tab.count() >= 2:
                for i in range(2, self.m_tab.count()):
                    if "Work Features" == str(_fromUtf8(self.m_tab.tabText(i))):
                        self.m_tab.removeTab(int(i))
                        break
        print_msg("Close done !")
        return

    def launch_curvesAndSurfaces(self):
        myObject = ParametricTab(ParCurveGui)

        # Create a Regression 2D Curve object and connect
        self.reg_events2D = RegressionCurve2DEvents(myObject.ui)
        # Create a Parametric 2D Curve object and connect
        self.events2D = ParametricCurve2DEvents(myObject.ui)
        # Create a Parametric 3D Curve object and connect
        self.events3D = ParametricCurve3DEvents(myObject.ui)
        # Create a Surface object and connect
        self.surface = SurfaceEvents(myObject.ui)

        # QtCore.QObject.connect(myObject.ui.button_quit, QtCore.SIGNAL ('clicked()'), myObject.quit_clicked)

    def getMainWindow(self):
        """ Returns the main window
        """
        # using QtGui.qApp.activeWindow() isn't very reliable because if another
        # widget than the mainwindow is active (e.g. a dialog) the wrong widget
        # is returned
        # toplevel = QtGui.qApp.topLevelWidgets()
        toplevel = QtGui.QApplication.topLevelWidgets()
        for i in toplevel:
            if i.metaObject().className() == "Gui::MainWindow":
                return i
        raise Exception("No main window found")

    def getComboView(self, window):
        """ Returns the main Tab.
        """
        dw = window.findChildren(QtGui.QDockWidget)
        for i in dw:
            if str(i.objectName()) == "Combo View":
                return i.findChild(QtGui.QTabWidget)
        raise Exception("No tab widget found")

    def getComboViewMv(self, window):
        """ Returns the main Tab.
        """
        import FreeCAD
        mw = FreeCAD.Gui.getMainWindow()
        layout = QtGui.QVBoxLayout()
        myw = QtGui.QWidget()
        myw.setLayout(layout)

        dw1 = QtGui.QDockWidget(mw)
        dw1.setWindowTitle("Work Features")
        dw1.setObjectName('WorkFeatures')
        dw1.setWidget(myw)

        mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, dw1)
        self.myw = myw
        self.dw = dw1
        layout.mw = mw
        return layout


if __name__ == '__main__':
    myDialog = WorkFeatureTab()
