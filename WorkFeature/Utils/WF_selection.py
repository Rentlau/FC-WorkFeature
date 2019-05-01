# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui as Gui
from WorkFeature.Utils.WF_Utils import *


def get_ActiveDocument(info=0):
    """ Return the active document
    """
    m_actDoc = App.activeDocument()
    if m_actDoc is None:
        printError_msg("No Active document selected !")
        return None
    if info != 0:
        message = "Active Document is: " + str(m_actDoc.Name)
        print_msg(message)
    return m_actDoc


def get_ActiveView(info=0):
    """ Return the active View of active Document
    """
    m_actView = Gui.activeDocument().activeView()
    if m_actView is None:
        printError_msg("No Active view selected !")
        return None
    if info != 0:
        message = "Active View is: " + str(m_actView)
        print_msg(message)
    return m_actView


def get_SelectedObjectsWithParent(info=0, printError=True):
    """ Return selected objects as
        Selection = (Number_of_Points, Number_of_Edges, Number_of_Planes,
                    Selected_Points, Selected_Edges, Selected_Planes)
        but each subObject is then returned with its parent
    """
    m_actDoc = get_ActiveDocument(info=1)

    if m_actDoc.Name:
        # Return a list of SelectionObjects for a given document name.
        # "getSelectionEx" Used for selecting subobjects
        m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
        m_objs = [selobj.Object for selobj in m_selEx]
        m_objNames = [selobj.ObjectName for selobj in m_selEx]
        m_num = len(m_objs)
        m_num = len(m_selEx)
        if m_num >= 1:
            Selected_Points = []
            Selected_Edges = []
            Selected_Planes = []
            for m_i in range(m_num):
                Sel_i_Object = m_selEx[m_i]
                Parent = Sel_i_Object.Object
                SubObjects_Inside = Sel_i_Object.SubObjects
                for n in range(len(SubObjects_Inside)):
                    SubObject = SubObjects_Inside[n]
                    if info != 0:
                        message = "Processing: " + str(m_objNames[m_i]) + ": " + str(SubObject.ShapeType)
                        print_msg(message)
                    if SubObject.ShapeType == "Vertex":
                        Selected_Points.append({SubObject: Parent})
                    if SubObject.ShapeType == "Edge":
                        Selected_Edges.append({SubObject: Parent})
                    if SubObject.ShapeType == "Face":
                        Selected_Planes.append({SubObject: Parent})
            Number_of_Points = len(Selected_Points)
            Number_of_Edges = len(Selected_Edges)
            Number_of_Planes = len(Selected_Planes)
            Selection = (Number_of_Points,
                         Number_of_Edges,
                         Number_of_Planes,
                         Selected_Points,
                         Selected_Edges,
                         Selected_Planes)
            if info != 0:
                print_msg("Number_of_Points, Number_of_Edges, Number_of_Planes," +
                          "Selected_Points, Selected_Edges, Selected_Planes = " + str(Selection))
            return Selection
        else:
            if printError:
                printError_msg("Select at least one object !")
            return None
    else:
        printError_msg("No active document !")
    return


def get_SelectedObjects(info=0, printError=True):
    """ Return selected objects as
        Selection = (Number_of_Points, Number_of_Edges, Number_of_Planes,
                    Selected_Points, Selected_Edges, Selected_Planes)
    """
    def storeShapeType(Object, Selected_Points, Selected_Edges, Selected_Planes):
        if Object.ShapeType == "Vertex":
            Selected_Points.append(Object)
            return True
        if Object.ShapeType == "Edge":
            Selected_Edges.append(Object)
            return True
        if Object.ShapeType == "Face":
            Selected_Planes.append(Object)
            return True
        return False

    m_actDoc = get_ActiveDocument(info=0)

    if m_actDoc.Name:
        # Return a list of SelectionObjects for a given document name.
        # "getSelectionEx" Used for selecting subobjects
        m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)

        m_num = len(m_selEx)
        if info != 0:
            print_msg("m_selEx: " + str(m_selEx))
            print_msg("m_num  : " + str(m_num))

        if m_num >= 1:
            Selected_Points = []
            Selected_Edges = []
            Selected_Planes = []
            Selected_Objects = []
            for Sel_i_Object in m_selEx:
                if info != 0:
                    print_msg("Processing: " + str(Sel_i_Object.ObjectName))

                if Sel_i_Object.HasSubObjects:
                    for Object in Sel_i_Object.SubObjects:
                        if info != 0:
                            print_msg("SubObject: " + str(Object))
                        if hasattr(Object, 'ShapeType'):
                            storeShapeType(Object, Selected_Points, Selected_Edges, Selected_Planes)
                        if hasattr(Object, 'Shape'):
                            Selected_Objects.append(Object)
                else:
                    if info != 0:
                        print_msg("Object: " + str(Sel_i_Object))
                    if hasattr(Sel_i_Object, 'Object'):
                        if hasattr(Sel_i_Object.Object, 'ShapeType'):
                            storeShapeType(Sel_i_Object.Object, Selected_Points, Selected_Edges, Selected_Planes)
                        if hasattr(Sel_i_Object.Object, 'Shape'):
                            if hasattr(Sel_i_Object.Object.Shape, 'ShapeType'):
                                if not storeShapeType(Sel_i_Object.Object.Shape, Selected_Points, Selected_Edges, Selected_Planes):
                                    Selected_Objects.append(Sel_i_Object.Object)
            Number_of_Points = len(Selected_Points)
            Number_of_Edges = len(Selected_Edges)
            Number_of_Planes = len(Selected_Planes)
            Selection = (Number_of_Points,
                         Number_of_Edges,
                         Number_of_Planes,
                         Selected_Points,
                         Selected_Edges,
                         Selected_Planes,
                         Selected_Objects)
            if info != 0:
                print_msg("Number_of_Points, Number_of_Edges, Number_of_Planes," +
                          "Selected_Points, Selected_Edges, Selected_Planes, Selected_Objects = " + str(Selection))
            return Selection
        else:
            if info != 0:
                print_msg("No Object selected !")
            if printError:
                printError_msg("Select at least one object !")
            return None
    else:
        printError_msg("No active document !")
    return


def createFolders(folder=None):
    """ Create WorkFeatures folders if needed.
    """
    if App.ActiveDocument is None:
        gui_errorDialog("Create a document first !")
        return False
    if not(App.ActiveDocument.getObject("WorkFeatures")):
        try:
            App.ActiveDocument.addObject("App::DocumentObjectGroup", "WorkFeatures")
        except Exception as inst:
            print(inst.args)
            printError_msg("Could not Create 'WorkFeatures' Objects Group!")
    m_list_dirs = ['Origin',
                   'WorkPoints',
                   'WorkAxis',
                   'WorkPlanes',
                   'WorkCircles',
                   'WorkArcs',
                   'WorkBoxes',
                   'WorkWires',
                   'WorkImages',
                   'WorkObjects',
                   'Rot_Trans']
    for m_dir in m_list_dirs:
        if folder == m_dir:
            if not(App.ActiveDocument.getObject(str(m_dir))):
                try:
                    App.ActiveDocument.getObject("WorkFeatures").newObject("App::DocumentObjectGroup", str(m_dir))
                except Exception as inst:
                    print(inst.args)
                    printError_msg("Could not Create '" + str(m_dir) + "' Objects Group!")
    return True


def get_InfoObjects(info=0, printError=True):
    """ Return info on objects selected:
    num, selEx, objs, objNames
    num    : number of objects
    selEx  : a list of Selected Objects
    objs   : a list of the .Object
    objNames: a list of the .ObjectName
    """
    m_actDoc = get_ActiveDocument()
    if m_actDoc is None:
        if printError:
            printError_msg("No active document !")
        return 0, 0, 0, 0
    # Return a list of Selected Objects for a given document name.
    m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
    m_objs = [selobj.Object for selobj in m_selEx]
    m_objNames = [selobj.ObjectName for selobj in m_selEx]
    m_num = len(m_objs)
    if m_num < 1:
        if printError:
            printError_msg("Select at least one object !")
        return 0, 0, 0, 0
    if info != 0:
        print_msg("m_num=" + str(m_num) +
                  ", m_selEx=" + str(m_selEx) +
                  ", m_objs=" + str(m_objs) +
                  ", m_objNames=" + str(m_objNames))
    return m_num, m_selEx, m_objs, m_objNames



def get_SelectedObjects_old(info=0, printError=True):
    """ Return selected objects as
        Selection = (Number_of_Points, Number_of_Edges, Number_of_Planes,
                    Selected_Points, Selected_Edges, Selected_Planes)
    """
    m_actDoc = get_ActiveDocument(info=0)

    if m_actDoc.Name:
        # Return a list of SelectionObjects for a given document name.
        # "getSelectionEx" Used for selecting subobjects
        m_selEx = Gui.Selection.getSelectionEx(m_actDoc.Name)
        m_objs = [selobj.Object for selobj in m_selEx]
        m_objNames = [selobj.ObjectName for selobj in m_selEx]
        m_num = len(m_objs)
        m_num = len(m_selEx)
        if m_num >= 1:
            Selected_Points = []
            Selected_Edges = []
            Selected_Planes = []
            for m_i in range(m_num):
                Sel_i_Object = m_selEx[m_i]
                SubObjects_Inside = Sel_i_Object.SubObjects
                for n in range(len(SubObjects_Inside)):
                    SubObject = SubObjects_Inside[n]
                    if info != 0:
                        message = "Processing: " + str(m_objNames[m_i]) + ": " + str(SubObject.ShapeType)
                        print_msg(message)
                    if SubObject.ShapeType == "Vertex":
                        Selected_Points.append(SubObject)
                    if SubObject.ShapeType == "Edge":
                        Selected_Edges.append(SubObject)
                    if SubObject.ShapeType == "Face":
                        Selected_Planes.append(SubObject)
            Number_of_Points = len(Selected_Points)
            Number_of_Edges = len(Selected_Edges)
            Number_of_Planes = len(Selected_Planes)
            Selection = (Number_of_Points,
                         Number_of_Edges,
                         Number_of_Planes,
                         Selected_Points,
                         Selected_Edges,
                         Selected_Planes)
            if info != 0:
                print_msg("Number_of_Points, Number_of_Edges, Number_of_Planes," +
                          "Selected_Points, Selected_Edges, Selected_Planes = " + str(Selection))
            return Selection
        else:
            if info != 0:
                print_msg("No Object selected !")
            if printError:
                printError_msg("Select at least one object !")
            return None
    else:
        printError_msg("No active document !")
    return
