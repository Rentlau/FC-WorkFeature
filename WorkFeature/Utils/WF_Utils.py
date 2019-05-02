# -*- coding: utf-8 -*-
"""
"""
import os.path
from PySide import QtCore, QtGui
import FreeCAD as App

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


error_msg_not_yet = "Not yet Developed !"


def gui_infoDialog(msg):
    """ Create a simple QMessageBox dialog for info messages.
    """
    # The first argument indicates the icon used:
    # one of QtGui.QMessageBox.{NoIcon,Information,Warning Critical,Question}
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Information, 'Info:', msg)
    diag.setWindowModality(QtCore.Qt.ApplicationModal)
    diag.exec_()


def gui_errorDialog(msg):
    """ Create a simple QMessageBox dialog for error messages.
    """
    m_script = os.path.basename(os.path.realpath(__file__))
    # The first argument indicates the icon used:
    # one of QtGui.QMessageBox.{NoIcon,Information,Warning Critical,Question}
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Warning, 'Error in ' + str(m_script), msg)
    diag.setWindowModality(QtCore.Qt.ApplicationModal)
    diag.exec_()


def print_msg(message):
    """ Print a message on console.
    """
    print(message)
    App.Console.PrintMessage(message + "\n")


def print_gui_msg(message):
    """ Print a message on console.
    """
    print(message)
    App.Console.PrintMessage(message + "\n")
    try:
        gui_infoDialog(message)
    except Exception as inst:
        print(inst.args)
        App.Console.PrintError("\nERROR: Not able to launch a QT dialog !")
        raise(Exception(message))


def printError_msg(message):
    """ Print a ERROR message on console.
    """
    print(message)
    App.Console.PrintError("\nERROR: " + message)
    try:
        gui_errorDialog(message)
    except Exception as inst:
        print(inst.args)
        App.Console.PrintError("\nERROR: Not able to launch a QT dialog !")
        raise(Exception(message))


def print_not_yet():
    printError_msg(error_msg_not_yet)


def print_attributes(obj, doc=False):
    """ Print all the attributes of this object and their value """
    __m_type = obj.__class__.__name__
    print('* Attributes print for ' + str(__m_type) + '*')
    for names in dir(obj):
        attr = getattr(obj, names)
        if not callable(attr):
            if doc:
                print(names, ':', attr)
            else:
                print(names)


def print_methods(obj, doc=False):
    """ Print all the methods of this object and their doc string"""
    __m_type = obj.__class__.__name__
    print('\n* Methods print for ' + str(__m_type) + '*')
    for names in dir(obj):
        attr = getattr(obj, names)
        if callable(attr):
            if doc:
                print(names, ':', attr.__doc__)
            else:
                print(names)


def write_text(filename=None, text=None):
    """
    Write the text into an ASCII file.

    Return True if success, false if not.

    *filename*: (string) full path name.

    *text*: (string) the text to write.
    """
    if filename is not None and text is not None:
        try:
            __m_f = open(filename, 'w')
            __m_f.write(text)
            __m_f.close()
            return True
        except Exception as inst:
            print(inst.args)
            print("\nERROR: The file " + str(filename) + " cannot be opened in write mode !")
            return False
    else:
        return False


def append_text(filename=None, text=""):
    """
    Print/Add text either on screen or on at the end of an existing ASCII text file.

    *filename*: (string) full path name.

    *text* : (string) the text to add at the end of the file.
    """
    if text.__class__.__name__ != 'str':
        return None
    if filename and os.path.exists(filename):
        try:
            __m_f = open(filename, 'r+')
            __m_f.readlines()
            __m_f.write(text + '\n')
            __m_f.close()
        except Exception as inst:
            print(inst.args)
            print("\nERROR: The file " + str(filename) + " can not be opened for append mode !")
            return False
    else:
        print(text + '\n')


def read_text_into_list(filename):
    """
    Read the complete ASCII file *filename* (if possible) into a unique
    list of strings and return the list
    (or None in case of error).

    Controls are done on *filename*.

    *filename*: (string) full path name.
    """
    if filename and os.path.exists(filename):
        try:
            __m_f = open(filename, 'r')
            # read the complete ASCII file if possible into a unique list of strings
            try:
                # m_strings = __m_f.readlines()
                m_strings = __m_f.read().splitlines()
            except Exception as inst:
                print(inst.args)
                __m_f.close()
                print("\nERROR: The file " + str(filename) + " cannot be fully read !")
                return None
            finally:
                __m_f.close()
            __m_f.close()
            return m_strings
        except Exception as inst:
            print(inst.args)
            print("\nERROR: The file " + str(filename) + " cannot be opened in read mode !")
            return None
    else:
        if os.path.exists(filename) is False:
            print("\nERROR: " + str(filename) + " not a valid file !")
        return None


def read_text(filename):
    """
    Read the complete ASCII file *filename* (if possible) into a unique
    string and return the string
    (or None in case of error).

    Controls are done on *filename*.

    *filename*: (string) full path name.
    """
    if filename and os.path.exists(filename):
        try:
            __m_f = open(filename, 'r')
            # read the complete ASCII file if possible into a unique string
            try:
                m_string = __m_f.read()
            except Exception as inst:
                print(inst.args)
                __m_f.close()
                print("\nERROR: The file " + str(filename) + " cannot be fully read !")
                return None
            finally:
                __m_f.close()
            __m_f.close()
            return m_string
        except Exception as inst:
            print(inst.args)
            print("\nERROR: The file " + str(filename) + " cannot be opened in read mode !")
            return None
    else:
        if os.path.exists(filename) is False:
            print("\nERROR: " + str(filename) + " not a valid file !")
        return None


class Selection():
    """
    Create a Selection Object

    *Gui_Selection*: selected object from GUI.

        m_activeDoc = App.activeDocument()
        if m_activeDoc is None:
            message = "No Active document selected !"
            return (None, message)

        if m_activeDoc.Name:
            m_selEx = Gui.Selection.getSelectionEx(m_activeDoc.Name)
            m_sel = Selection(m_selEx)
    """
    def __init__(self, Gui_Selection):
        self.__numberOfEntities = 0
        self.__numberOfVertexes = 0
        self.__numberOfEdges = 0
        self.__numberOfWires = 0
        self.__numberOfFaces = 0
        self.__numberOfObjects = 0
        self.__numberOfImages = 0
        self.__selectedVertices = []
        self.__selectedEdges = []
        self.__selectedWires = []
        self.__selectedFaces = []
        self.__selectedObjects = []
        self.__selectedImages = []
        self.__selEx = None
        if Gui_Selection is None:
            message = "No Selection from Active document passed !"
            return (None, message)
        self.__selEx = Gui_Selection

        self.initialize()

    def storeShapeType(self, Object):
        if Object.ShapeType == "Vertex":
            self.__selectedVertices.append(Object)
            return True
        if Object.ShapeType == "Edge":
            self.__selectedEdges.append(Object)
            return True
        if Object.ShapeType == "Wire":
            self.__selectedWires.append(Object)
            return True
        if Object.ShapeType == "Face":
            self.__selectedFaces.append(Object)
            return True
        return False

    def initialize(self):
        self.__numberOfEntities = len(self.__selEx)

        if self.__numberOfEntities >= 1:
            for m_Sel_i_Object in self.__selEx:
                if not m_Sel_i_Object.HasSubObjects:
                    if hasattr(m_Sel_i_Object, 'Object'):
                        m_Object = m_Sel_i_Object.Object
                        if hasattr(m_Object, 'ShapeType'):
                            self.storeShapeType(m_Object)
                        if hasattr(m_Object, 'Shape'):
                            self.__selectedObjects.append(m_Object)
                        if hasattr(m_Object, 'ImageFile'):
                            self.__selectedImages.append(m_Object)
#                         if hasattr(m_Sel_i_Object.Object, 'Shape'):
# #                             if hasattr(m_Sel_i_Object.Object.Shape, 'ShapeType'):
# #                                 if not self.storeShapeType(m_Sel_i_Object.Object.Shape):
# #                                     self.__selectedObjects.append(m_Sel_i_Object.Object)
                else:
                    for m_Object in m_Sel_i_Object.SubObjects:
                        if hasattr(m_Object, 'ShapeType'):
                            self.storeShapeType(m_Object)
                        if hasattr(m_Object, 'Shape'):
                            self.__selectedObjects.append(m_Object)
                        if hasattr(m_Object, 'ImageFile'):
                            self.__selectedImages.append(m_Object)

            self.__numberOfVertexes = len(self.__selectedVertices)
            self.__numberOfEdges = len(self.__selectedEdges)
            self.__numberOfWires = len(self.__selectedWires)
            self.__numberOfFaces = len(self.__selectedFaces)
            self.__numberOfObjects = len(self.__selectedObjects)
            self.__numberOfImages = len(self.__selectedImages)
            message = "Initialization done !"
            return message
        else:
            message = "No Object selected !"
            return (None, message)

        message = ""
        return (None, message)

    def __getNumberOfEntities(self):
        return self.__numberOfEntities

    def __setNumberOfEntities(self, val):
        self.__numberOfEntities = val

    numberOfEntities = property(__getNumberOfEntities, __setNumberOfEntities)

    def __getNumberOfPoints(self):
        return self.__numberOfVertexes

    def __setNumberOfPoints(self, val):
        self.__numberOfVertexes = val

    numberOfPoints = property(__getNumberOfPoints, __setNumberOfPoints)

    def __getNumberOfSegments(self):
        return self.__numberOfEdges

    def __setNumberOfSegments(self, val):
        self.__numberOfEdges = val

    numberOfSegments = property(__getNumberOfSegments, __setNumberOfSegments)

    def __getNumberOfCurves(self):
        return self.__numberOfWires

    def __setNumberOfCurves(self, val):
        self.__numberOfWires = val

    numberOfCurves = property(__getNumberOfCurves, __setNumberOfCurves)

    def __getNumberOfPlanes(self):
        return self.__numberOfFaces

    def __setNumberOfPlanes(self, val):
        self.__numberOfFaces = val

    numberOfPlanes = property(__getNumberOfPlanes, __setNumberOfPlanes)

    def __getNumberOfObjects(self):
        return self.__numberOfObjects

    def __setNumberOfObjects(self, val):
        self.__numberOfObjects = val

    numberOfObjects = property(__getNumberOfObjects, __setNumberOfObjects)

    def __getNumberOfImages(self):
        return self.__numberOfImages

    def __setNumberOfImages(self, val):
        self.__numberOfImages = val

    numberOfImages = property(__getNumberOfImages, __setNumberOfImages)

    def __str__(self):
        message = "Gui_Selection     : " + str(self.__selEx)
        message += "\nNumberOfImages    : " + str(self.__numberOfImages)
        message += "\nNumberOfObjects   : " + str(self.__numberOfObjects)
        message += "\nNumberOfPlanes    : " + str(self.__numberOfFaces)
        message += "\nNumberOfCurves    : " + str(self.__numberOfWires)
        message += "\nNumberOfSegments  : " + str(self.__numberOfEdges)
        message += "\nNumberOfPoints    : " + str(self.__numberOfVertexes)
        message += "\nNumberOfEntities  : " + str(self.__numberOfEntities)
        return (message)

    def get_points(self, getfrom=["Points", "Segments", "Curves", "Planes", "Objects"]):
        """ Return all Points found in selection including the Points from objects as
        (Number of Points, list of Vertexes)
        Return None if no Point detected
        """
        Selected_Entities = []

        if self.numberOfEntities == 0:
            return None

        if self.numberOfPoints > 0 and "Points" in getfrom:
            for m_point in self.__selectedVertices:
                Selected_Entities.append(m_point)

        if self.numberOfSegments > 0 and "Segments" in getfrom:
            for m_edge in self.__selectedEdges:
                Selected_Entities.append(m_edge.Vertexes[0])
                Selected_Entities.append(m_edge.Vertexes[-1])
        # TOCOMPLETE
        if self.numberOfCurves > 0 and "Curves" in getfrom:
            pass

        if self.numberOfPlanes > 0 and "Planes" in getfrom:
            for m_face in self.__selectedFaces:
                m_edges_list = m_face.Edges
                for m_edge in m_edges_list:
                    Selected_Entities.append(m_edge.Vertexes[0])
                    Selected_Entities.append(m_edge.Vertexes[-1])

        if self.numberOfObjects > 0 and "Objects" in getfrom:
            for m_object in self.__selectedObjects:
                for m_vertex in m_object.Shape.Vertexes:
                    Selected_Entities.append(m_vertex)

        if len(Selected_Entities) != 0:
            return (len(Selected_Entities), Selected_Entities)
        else:
            return (0, None)

    def get_segments(self, getfrom=["Points", "Segments", "Curves", "Planes", "Objects"]):
        """ Return all Segments found in selection including the Segments from objects as
        (Number of Segments, list of Edges)
        In case of at least 2 points selected it will create a line from these 2 points
        Return None if no Segment detected
        """
        Selected_Entities = []

        if self.numberOfEntities == 0:
            return None

        if self.numberOfPoints >= 2 and "Points" in getfrom:
            import Part
            for m_p1, m_p2 in zip(self.__selectedVertices, self.__selectedVertices[1:]):
                m_diff = m_p2.Point.sub(m_p1.Point)
                tolerance = 1e-10
                if abs(m_diff.x) <= tolerance and abs(m_diff.y) <= tolerance and abs(m_diff.z) <= tolerance:
                    continue
                Selected_Entities.append(Part.makeLine(m_p2.Point, m_p1.Point))

        if self.numberOfSegments > 0 and "Segments" in getfrom:
            for m_edge in self.__selectedEdges:
                Selected_Entities.append(m_edge)
        # TOCOMPLETE
        if self.numberOfCurves > 0 and "Curves" in getfrom:
            for m_wire in self.__selectedWires:
                Selected_Entities.append(m_wire)

        if self.numberOfPlanes > 0 and "Planes" in getfrom:
            for m_face in self.__selectedFaces:
                m_edges_list = m_face.Edges
                for m_edge in m_edges_list:
                    Selected_Entities.append(m_edge)

        if self.numberOfObjects > 0 and "Objects" in getfrom:
            for m_object in self.__selectedObjects:
                for m_edge in m_object.Shape.Edges:
                    Selected_Entities.append(m_edge)

        if len(Selected_Entities) != 0:
            return (len(Selected_Entities), Selected_Entities)
        else:
            return (0, None)

    def get_curves(self, getfrom=["Points", "Segments", "Curves", "Planes", "Objects"]):
        Selected_Entities = []

        if self.numberOfEntities == 0:
            return None

        if self.numberOfCurves > 0 and "Curves" in getfrom:
            for m_wire in self.__selectedWires:
                Selected_Entities.append(m_wire)

        if self.numberOfPlanes > 0 and "Planes" in getfrom:
            for m_face in self.__selectedFaces:
                m_wires_list = m_face.Wires
                for m_wire in m_wires_list:
                    Selected_Entities.append(m_wire)

        if self.numberOfObjects > 0 and "Objects" in getfrom:
            for m_object in self.__selectedObjects:
                for m_wire in m_object.Shape.Wires:
                    Selected_Entities.append(m_wire)

        if len(Selected_Entities) != 0:
            return (len(Selected_Entities), Selected_Entities)
        else:
            return (0, None)

    def get_planes(self, getfrom=["Points", "Segments", "Curves", "Planes", "Objects"]):
        Selected_Entities = []

        if self.numberOfEntities == 0:
            return None

        # TOCOMPLETE
#         if self.numberOfPoints >= 3 and "Points" in getfrom:
#             import Part
#             for m_p1,m_p2 in zip(self.__selectedVertices, self.__selectedVertices[1:]):
#                 m_diff = m_p2.Point.sub(m_p1.Point)
#                 tolerance = 1e-10
#                 if abs(m_diff.x) <= tolerance and abs(m_diff.y) <= tolerance and abs(m_diff.z) <= tolerance:
#                     continue
#                 Selected_Entities.append(Part.makeLine(m_p2.Point, m_p1.Point))
#
#         # TOCOMPLETE
#         if self.numberOfSegments >= 2 and "Segments" in getfrom:
#             import Part
#             for m_l1,m_l2 in zip(self.__selectedEdges, self.__selectedEdges[1:]):
#             for m_edge in self.__selectedEdges
#                 Selected_Entities.append(m_edge)

        if self.numberOfPlanes > 0 and "Planes" in getfrom:
            for m_face in self.__selectedFaces:
                Selected_Entities.append(m_face)

        if self.numberOfObjects > 0 and "Objects" in getfrom:
            for m_object in self.__selectedObjects:
                for m_face in m_object.Shape.Faces:
                    Selected_Entities.append(m_face)

        if len(Selected_Entities) != 0:
            return (len(Selected_Entities), Selected_Entities)
        else:
            return (0, None)

    def get_objects(self):
        Selected_Entities = []
        pass

    def get_primer_selected_entities(self, selection_type):
        Selected_Entities = selection_type
        if len(Selected_Entities) != 0:
            return (len(Selected_Entities), Selected_Entities)
        else:
            return (0, None)

    def get_primerPoints(self):
        return self.get_primer_selected_entities(self.__selectedVertices)

    def get_primerSegments(self):
        return self.get_primer_selected_entities(self.__selectedEdges)

    def get_primerCurves(self):
        return self.get_primer_selected_entities(self.__selectedWires)

    def get_primerPlanes(self):
        return self.get_primer_selected_entities(self.__selectedFaces)

    def get_primerObjects(self):
        return self.get_primer_selected_entities(self.__selectedObjects)

    def get_primerImages(self):
        return self.get_primer_selected_entities(self.__selectedImages)


class DefineAndConnectEvents():
    def __init__(self, ui, obj):
        """
        Definition of communications between a Gui and an python Object.
        This class is a base class and must be derived like:

        class ParametricCurve2DEvents(DefineAndConnectEvents):
            def __init__(self,ui):
                self.ui = ui
                # Create Parametric Curve objects
                self.parcurv2D = ParametricCurve2D(self.ui)
                DefineAndConnectEvents.__init__(self, self.ui, self.parcurv2D)

            def defineEvents(self):
                #==============================

                # Definition of connections

                # by type of actions on widgets of the Gui.
                #==============================
                self.connections_for_button_pressed = {
                                    "ParCurve_button_edit_2"          : "edit",
                                    "ParCurve_button_apply_2"         : "draw",
                                    "ParCurve_button_store_2"         : "store",
                                    }
                ...
        """
        if self.__class__ is DefineAndConnectEvents:
            raise Exception("Direct construction not allowed !\nSee doc of the Class.")
        self.ui = ui
        self.obj = obj
        self.defineEvents()
        self.connectEvents()

    def defineEvents(self):
        """
        Definition of connections by type of actions on widgets of the Gui.
        """
        self.connections_for_slider_changed = {}
        self.connections_for_button_pressed = {}
        self.connections_for_combobox_changed = {}
        self.connections_for_checkbox_toggled = {}
        self.connections_for_spin_changed = {}
        self.connections_for_return_pressed = {}

    def connectEvents(self):
        for m_key, m_val in self.connections_for_slider_changed.items():
            # print_msg( "Connecting: " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("valueChanged(int)"), getattr(self.obj, str(m_val)))

        for m_key, m_val in self.connections_for_button_pressed.items():
            # print_msg( "Connecting: " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("pressed()"), getattr(self.obj, str(m_val)))

        for m_key, m_val in self.connections_for_combobox_changed.items():
            # print_msg( "Connecting: " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), getattr(self.obj, str(m_val)))

        for m_key, m_val in self.connections_for_checkbox_toggled.items():
            # print_msg( "Connecting: " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("toggled(bool)")), getattr(self.obj, str(m_val)))

        for m_key, m_val in self.connections_for_spin_changed.items():
            # print_msg( "Connecting: " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("valueChanged(int)"), getattr(self.obj, str(m_val)))

        for m_key, m_val in self.connections_for_return_pressed.items():
            # print_msg( "Connecting: " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("returnPressed()"), getattr(self.obj, str(m_val)))

        for m_key, m_val in self.connections_for_return_pressed.items():
            # print_msg( "Connecting: " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("editingFinished()"), getattr(self.obj, str(m_val)))


if __name__ == '__main__':
    myObject = DefineAndConnectEvents(None, None)
