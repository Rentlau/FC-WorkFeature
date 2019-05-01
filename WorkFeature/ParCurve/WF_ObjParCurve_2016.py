# -*- coding:utf-8 -*-
"""
To execute the MACRO in FreeCAD python console:
  execfile("/home/laurent/Develop/Workspaces/Python/WF_test/WorkFeature/ParCurve/WF_ObjParCurve_2016.py")
"""
import sys
import os.path

from WorkFeature.Utils.WF_translate import _translate
import WorkFeature.ParCurve.WF_ObjParCurveEdit_2016 as ParCurveEdit
import WorkFeature.ParCurve.Ui.WF_ParCurveGui_2016 as ParCurveGui

from ParCurve.Utils.Gui import DefineAndConnectEvents
from ParCurve.Utils.Gui import print_msg

import FreeCAD
import FreeCADGui
import Draft
import Part
# import Part.BSplineSurface
# import Part.OCCError
# import Part.makePolygon

from PySide import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s:s

from math import *

# Get the path of the current python script
m_current_path = os.path.realpath(__file__)
# Update paths
if not sys.path.__contains__(m_current_path):
    sys.path.append(m_current_path)

App = FreeCAD
global myTabName
myTabName = "Parametric Curves"
global myObjName
myObjName = "ParametricCurves"
global ParametricRelease
ParametricRelease = "2019_05"
global f2
global f2b
global f3
global f3b


def f2(fa, fb, fx, fy, t, i):
    pass


def f2b(fa, fb, fx, fy, t, i, msgBox):
    pass


def f3(fa, fb, fc, fx, fy, fz, t):
    pass


def f3b(fa, fb, fc, fx, fy, fz, u, v, msgBox):
    pass


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
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Warning,
                             'Error in ' + str(m_script), msg)
    diag.setWindowModality(QtCore.Qt.ApplicationModal)
    diag.exec_()


def print_msg(message):
    """ Print a message on console.
    """
    print(message)
    FreeCAD.Console.PrintMessage(message + "\n")


def printError_msg(message):
    """ Print a ERROR message on console.
    """
    print(message)
    FreeCAD.Console.PrintError("\nERROR: " + message)
    try:
        gui_errorDialog(message)
    except Exception as inst:
        print(inst.args)
        FreeCAD.Console.PrintError("\nERROR: Not able to launch a QT dialog !")
        raise(Exception(message))


def get_ActiveDocument(info=0):
    """ Return the active document
    """
    m_actDoc = FreeCAD.activeDocument()
    if m_actDoc is None:
        printError_msg("No Active document selected !")
        return None
    if info != 0:
        message = "Active Document is:" + str(m_actDoc.Name)
        print_msg(message)
    return m_actDoc


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
        m_selEx = FreeCADGui.Selection.getSelectionEx(m_actDoc.Name)

        m_num = len(m_selEx)
        if info != 0:
            print_msg("m_selEx:" + str(m_selEx))
            print_msg("m_num  :" + str(m_num))

        if m_num >= 1:
            Selected_Points = []
            Selected_Edges = []
            Selected_Planes = []
            Selected_Objects = []
            for Sel_i_Object in m_selEx:
                if info != 0:
                    print_msg("Processing:" + str(Sel_i_Object.ObjectName))
                if Sel_i_Object.HasSubObjects:
                    for Object in Sel_i_Object.SubObjects:
                        if info != 0:
                            print_msg("SubObject:" + str(Object))
                        if hasattr(Object, 'ShapeType'):
                            storeShapeType(Object, Selected_Points, Selected_Edges, Selected_Planes)
                        if hasattr(Object, 'Shape'):
                            Selected_Objects.append(Object)
                else:
                    if info != 0:
                        print_msg("Object:" + str(Sel_i_Object))
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
                          "Selected_Points, Selected_Edges, Selected_Planes , Selected_Objects = " + str(Selection))
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

####################################################################################
# Classes:Regression, Parametric


class Regression():
    def __init__(self, gui):
        """ A Regression object
        """
        self.debug = 1
        self.degree = 2
        self.gui = gui
        self.data = []
        self.x = []
        self.y = []

    def updateOptions(self):
        pass

    def setDegree(self, value):
        """ Respond to a change in Degree
        """
        try:
            self.degree = int(value)
            if self.debug != 0:
                print_msg("New degree is:" + str(self.degree))
        except ValueError:
            print_msg("Degree must be valid !")


class Parametric():
    def __init__(self, gui):
        """ A Parametric object
        """
        self.debug = 1

        self.close = False
        self.face = False

        self.points = False
        self.poly = True
        self.bspline = False
        self.bezier = False
        self.nurbs = False
        self.meshes = False

        self.polar = False
        self.cylind = False
        self.spheri = False

        self.dialog = None
        self.combox = None

        self.gui = gui
        self.msgBox = QtGui.QMessageBox()
        self.pbar = None

        self.setGuiStuff()

        self.ox, self.oy, self.oz = 0.0, 0.0, 0.0

        try:
            import numpy as np
        except ImportError:
            print_msg("Impossible to load Module numpy !")
            return

    def setGuiStuff(self):
        self.pbar = self.gui.progressBar
        self.pbar.setValue(0)

        self.x_ref = self.gui.Par_x_ref
        self.y_ref = self.gui.Par_y_ref
        self.z_ref = self.gui.Par_z_ref

    def updateOptions(self):
        pass

    def resetOrigin(self):
        self.x_ref.setText("0.0")
        self.y_ref.setText("0.0")
        self.z_ref.setText("0.0")

    def getOrigin(self):
        msg = self.debug

        error_msg = """Select at one points !"""
        Selection = get_SelectedObjects(info=msg, printError=False)

        try:
            SelectedObjects = Selection
            Number_of_Points = SelectedObjects[0]
            if msg != 0:
                print_msg("Number_of_Points=" + str(Number_of_Points))
            if Number_of_Points == 1:
                m_x = 0.0
                m_y = 0.0
                m_z = 0.0
                Point_List = SelectedObjects[3]
                for Selected_Point in Point_List:
                    m_point = Selected_Point.Point
                    m_x = m_point.x
                    m_y = m_point.y
                    m_z = m_point.z
            if Number_of_Points > 1:
                m_x = ""
                m_y = ""
                m_z = ""
                Point_List = SelectedObjects[3]
                for Selected_Point in Point_List:
                    m_point = Selected_Point.Point
                    m_x += str(m_point.x) + ", "
                    m_y += str(m_point.y) + ", "
                    m_z += str(m_point.z) + ", "
            self.x_ref.setText(str(m_x))
            self.y_ref.setText(str(m_y))
            self.z_ref.setText(str(m_z))
        except Exception as inst:
            print(inst.args)
            printError_msg(error_msg)

    def ccloseState(self, flag):
        if self.debug != 0:
            print(self.ccloseState.__name__)
        self.close = flag
        self.updateOptions()

    def cfaceState(self, flag):
        if self.debug != 0:
            print(self.cfaceState.__name__)
        self.face = flag
        self.updateOptions()

    def cpointsState(self, flag):
        if self.debug != 0:
            print(self.cpointsState.__name__)
        self.points = flag
        self.updateOptions()

    def cpolyState(self, flag):
        if self.debug != 0:
            print(self.cpolyState.__name__)
        self.poly = flag
        self.updateOptions()

    def cbsplineState(self, flag):
        if self.debug != 0:
            print(self.cbsplineState.__name__)
        self.bspline = flag
        self.updateOptions()

    def cbezierState(self, flag):
        if self.debug != 0:
            print(self.cbezierState.__name__)
        self.bezier = flag
        self.updateOptions()

    def cnurbsState(self, flag):
        if self.debug != 0:
            print(self.cnurbsState.__name__)
        self.nurbs = flag
        self.updateOptions()

    def cmeshesState(self, flag):
        if self.debug != 0:
            print(self.cmeshesState.__name__)
        self.meshes = flag
        self.updateOptions()

    def cpolarState(self, flag):
        if self.debug != 0:
            print(self.cpolarState.__name__)
        self.polar = flag
        self.updateOptions()

    def ccylindState(self, flag):
        if self.debug != 0:
            print(self.ccylindState.__name__)
        self.cylind = flag
        self.updateOptions()

    def csphericState(self, flag):
        if self.debug != 0:
            print(self.csphericState.__name__)
        self.spheri = flag
        self.updateOptions()

    def plot_matriz_old(self, matriz):
        """ Plot the dataset with different options.
        """
        if self.debug != 0:
            print(self.plot_matriz.__name__)

        if self.points is True:
            for point in matriz:
                Draft.makePoint(point)
        else:
            curva = Part.makePolygon(matriz)
            if self.bspline is True:
                Draft.makeBSpline(curva, closed=self.close, face=False)
                # Draft.makeBSpline(Draft.makeWire(curva,closed=self.close,face=False),closed=self.close,face=False)
            if self.bezier is True:
                Draft.makeBezCurve(curva, closed=self.close, face=False)
            if self.poly is True:
                Draft.makeWire(curva, closed=self.close, face=False)
                if self.close is True and self.face is True:
                    Draft.upgrade(FreeCADGui.Selection.getSelection(), delete=True)
                    FreeCAD.ActiveDocument.recompute()

    def plot_matriz(self, matriz, text="matriz"):
        """ Plot the dataset with different options.
        """
        if self.debug != 0:
            print(self.plot_matriz.__name__)

        doc = FreeCAD.ActiveDocument
        if doc is None:
            doc = FreeCAD.newDocument()

        if len(matriz) == 0:
            self.msgBox.setText("Error:No point to show !")
            self.msgBox.exec_()
            return
        if len(matriz) == 1:
            for point in matriz:
                a = Draft.makePoint(point)
                FreeCAD.ActiveDocument.ActiveObject.Label = str(a.Name) + "_Point_" + str(text)
        else:
            if self.points is True:
                # self.onShowQuestion(self.gui)
                i = 0
                self.pbar.setValue(i)
                number = len(matriz)
                for point in matriz:
                    i += 1
                    if not i % 20:
                        step = int((i * 100) / number)
                        self.pbar.setValue(step)
                        # FreeCAD.ActiveDocument.recompute()
                    a = Draft.makePoint(point)
                    FreeCAD.ActiveDocument.ActiveObject.Label = str(a.Name) + "_Point_" + str(text)
            else:
                try:
                    curva = Part.makePolygon(matriz)
                except Part.OCCError:
                    self.msgBox.setText("Error:Not able to make a polygon...check your parameters !")
                    self.msgBox.exec_()
                    return
                if self.bspline is True:
                    a = Draft.makeBSpline(curva, closed=self.close, face=False)
                    FreeCAD.ActiveDocument.ActiveObject.Label = str(a.Name) + "_BSpline_" + str(text)
                if self.bezier is True:
                    a = Draft.makeBezCurve(curva, closed=self.close, face=False)
                    FreeCAD.ActiveDocument.ActiveObject.Label = str(a.Name) + "_BezCurve_" + str(text)
                if self.poly is True:
                    a = Draft.makeWire(curva, closed=self.close, face=False)
                    FreeCAD.ActiveDocument.ActiveObject.Label = str(a.Name) + "_Wire_" + str(text)
#             if self.arcs is True:
#                 s=Part.BSplineCurve()
#                 s.interpolate(matriz, True)
#                 s.buildFromPoles(matriz)
#                 #Part.show(s.toShape())
#                 arcs=s.toBiArcs(0.1)
#                 wire=Part.Wire([Part.Edge(i) for i in arcs])
#                 Part.show(wire)
        if self.close is True and self.face is True:
            Draft.upgrade(FreeCADGui.Selection.getSelection(), delete=True)
        FreeCAD.ActiveDocument.recompute()
        # FreeCADGui.ActiveDocument.ActiveView.fitAll()

    def edit(self):
        """ Launch the edit panel curve.
        """
        if self.debug != 0:
            print(self.edit.__name__)

        self.dialog.show()
#        self.dialog.exec_()

    def onShowQuestion(self, gui, question="Do you really want to continue ?"):
        """ Show the question message
        """
        flags = QtGui.QMessageBox.StandardButton.Yes
        flags |= QtGui.QMessageBox.StandardButton.No
        response = QtGui.QMessageBox.question(gui, "Question",
                                              question,
                                              flags)
        if response == QtGui.QMessageBox.Yes:
            return True
        else:
            return False


class RegressionCurve2D(Regression, Parametric):
    """ A RegressionCurve2D object
    """
    def __init__(self, gui):
        # Parent1
        Regression.__init__(self, gui)
        # Parent2
        Parametric.__init__(self, gui)

        self.input_textEdit = self.gui.Reg2DCurve_input_textEdit
        # Reg2DCurve_button_select_points
        self.function_textEdit = self.gui.Reg2DCurve_function_textEdit
        self.degree_select = self.gui.Reg2DCurve_degree_select

        self.lmin = self.gui.Reg2DCurve_min
        self.lmax = self.gui.Reg2DCurve_max
        self.lstep = self.gui.Reg2DCurve_step
        self.lz = self.gui.Reg2DCurve_z

        infinity = float("inf")
        self.maxx = self.maxy = -1 * infinity
        self.minx = self.miny = infinity
        self.stepx = 0.1
        self.constz = 0.0

        self.coef_poly = None
        self.name = "RegressionCurve2D"

    def get_points(self):
        msg = self.debug
        error_msg = """Select at least two points !"""
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
                text = ""
                Point_List = SelectedObjects[3]
                for Selected_Point in Point_List:
                    m_point = Selected_Point.Point
                    m_x = m_point.x
                    m_y = m_point.y
                    m_z = m_point.z
                    text += str(m_x) + "  " + str(m_y) + "  " + str(m_z) + str('\n')
                self.input_textEdit.setText(text)
        except Exception as inst:
            print(inst.args)
            printError_msg(error_msg)

    def get_input_data(self):
        """ Recover the data from the input Qtextedit and
        feed the self.data and self.x and self.y arrays
        """
        if self.debug != 0:
            print(str(self.input_textEdit.toPlainText()))
        self.data = []
        self.x = []
        self.y = []
        self.data = self.input_textEdit.toPlainText().splitlines()
        if self.data in [None]:
            return
        for item in self.data:
            if self.debug != 0:
                print("item = " + str(item))
            values = item.split()

            try:
                self.x.append(float(values[0].strip()))
                self.y.append(float(values[1].strip()))
            except ValueError:
                print_msg("Value " + str(values[0].strip()) + " must be a valid Float!")
                print_msg("Value " + str(values[1].strip()) + " must be a valid Float!")
                continue

        if self.debug != 0:
            print("X = " + str(self.x))
            print("Y = " + str(self.y))

    def poly_estimate(self):
        """ Estimate a 2D polynom by Least squares polynomial fit.
        """
        if len(self.x) != len(self.y):
            print_msg("Length of the 2 arrays X and Y are not the same !")
            return

        import numpy as np

        datasize = len(self.x)
        xdata = np.array(self.x)
        ydata = np.array(self.y)

        # Get min max limits
        self.minx, self.maxx = min(self.x), max(self.x)
        self.miny, self.maxy = min(self.y), max(self.y)

        # Adjust the max degree
        max_degree = datasize - 1
        if self.degree < 0:
            self.degree = 0
        if self.degree > max_degree:
            self.degree = max_degree
        # Need to update the Reg2DCurve_degree_select
        self.degree_select.setValue(self.degree)

        # Least squares polynomial fit.
        # Fit a polynomial p(x) = p[0] * x**deg + ... + p[deg] of degree deg to points (x, y).
        # Returns a vector of coefficients p that minimises the squared error.
        self.coef_poly = np.polyfit(xdata, ydata, self.degree)

    def print_function(self):
        import numpy as np

        datasize = len(self.x)
        xdata = np.array(self.x)
        ydata = np.array(self.y)

        # Evaluate a polynomial at specific values.
        ya = np.polyval(self.coef_poly, xdata)
        yb = sum(ydata) / datasize
        sr = sum([(yi - yb)**2 for yi in ya])
        st = sum([(yi - yb)**2 for yi in ydata])
        corr_coeff = sr / st
        stderr = 0
        if(datasize > 2):
            a = 0
            for i, x in enumerate(xdata):
                a += (ya[i] - ydata[i])**2
            stderr = np.sqrt(a / (datasize - 2))

        text = "Degree %d, %d x,y pairs" % (self.degree, datasize)
        text += "\nCorr. coeff. (r^2) = %+.16e" % corr_coeff
        text += "\nStandard Error     = %+.16e" % stderr
        text += "\n\nf(x) = "
        a = []
        for n, v in enumerate(self.coef_poly[::-1]):
            s = "%+.16e" % v
            a.append("%s * x^%02d" % (s, n))
        text += "\n       ".join(a) + "\n"
        self.function_textEdit.setText(text)

    def draw(self):
        if self.debug != 0:
            print(self.draw.__name__)

        import numpy as np

        self.get_input_data()
        self.poly_estimate()

        matriz = []

        try:
            minx = float(eval(str(self.lmin.text())))
        except Exception as inst:
            print(inst.args)
            minx = self.minx
        try:
            maxx = float(eval(str(self.lmax.text())))
        except Exception as inst:
            print(inst.args)
            maxx = self.maxx
        try:
            step = float(eval(str(self.lstep.text())))
        except Exception as inst:
            print(inst.args)
            step = self.stepx
        try:
            z = float(eval(str(self.lz.text())))
        except Exception as inst:
            print(inst.args)
            z = self.constz

        for x in np.arange(minx, maxx, step):
            y = np.polyval(self.coef_poly, x)
            matriz.append(FreeCAD.Vector(x, y, z))

        self.plot_matriz(matriz, self.name)

        self.print_function()


class ParametricCurve2D(Parametric):
    """ A ParametricCurve2D object
    """
    def __init__(self, gui):
        Parametric.__init__(self, gui)

        self.name = self.gui.ParCurve_name_2
        self.la = self.gui.ParCurve_a_2
        self.lb = self.gui.ParCurve_b_2
        self.label_x = self.gui.label_x_2
        self.lx = self.gui.ParCurve_x_2
        self.label_y = self.gui.label_y_2
        self.ly = self.gui.ParCurve_y_2
        self.ltmin = self.gui.ParCurve_tmin_2
        self.ltmax = self.gui.ParCurve_tmax_2
        self.ltstep = self.gui.ParCurve_tstep_2
        # self.label_z  = self.gui.label_z_5
        # self.lz       = self.gui.ParCurve_z_2

        self.lpolar = self.gui.checkBox_polar_2
        self.cb_points = self.gui.checkBox_points_2
        self.cb_polyline = self.gui.checkBox_polyline_2
        self.cb_bspline = self.gui.checkBox_bspline_2
        self.cb_bezier = self.gui.checkBox_bezier_2

        self.cb_close = self.gui.checkBox_close_2
        self.cb_face = self.gui.checkBox_face_2

        self.cb_face.setEnabled(False)
        self.close = False
        self.face = False

        self.combox = self.gui.ParCurve_comboBox_2

        self.dialog = QtGui.QDialog()
        self.dialog.resize(280, 110)
        self.dialog.setWindowTitle("2D Parametric Curve Editor")
        self.dialog.ui = ParCurveEdit.tableWidget2D(database="Parametric2D.dat")
        self.dialog.ui.setupUi(self.dialog, self.combox)

    def updateOptions(self):
        if self.lpolar.isChecked():
            self.label_x.setText("Rho (a,b,t)")
            self.label_y.setText("Phi (a,b,t)")
        else:
            self.label_x.setText("X (a,b,t)")
            self.label_y.setText("Y (a,b,t)")

        if self.points:
            self.cb_close.setEnabled(False)
            self.cb_face.setEnabled(False)
            self.cb_close.setChecked(False)
            self.cb_face.setChecked(False)
            self.close = False
            self.face = False
        else:
            self.cb_close.setEnabled(True)
            if self.poly and self.close:
                self.cb_face.setEnabled(True)
            else:
                self.cb_face.setEnabled(False)
                self.cb_face.setChecked(False)
                self.face = False

    def select_curve(self, *argc):
        """ Selection of Curve by combo box.
        """
        if self.debug != 0:
            print(self.select_curve.__name__)

        m_line = self.dialog.ui.selectCurve(*argc)
        if self.debug != 0:
            print(str(m_line))
        self.name.setText(str(m_line[0]))
        self.la.setText(str(m_line[1]))
        self.lb.setText(str(m_line[2]))
        self.lx.setText(str(m_line[3]))
        self.ly.setText(str(m_line[4]))
        # self.lz.setText("0.0")
        self.resetOrigin()
        self.ltmin.setText(str(m_line[5]))
        self.ltmax.setText(str(m_line[6]))
        self.ltstep.setText(str(m_line[7]))
        m_polar = int(str(m_line[8]))
        if self.debug != 0:
            print(str(m_polar))
            print(str(self.lpolar))
        self.polar = False
        if m_polar == 1:
            print(str(m_polar))
            self.polar = True
        if self.polar:
            self.label_x.setText("Rho (a,b,t)")
            self.label_y.setText("Phi (a,b,t)")
        else:
            self.label_x.setText("X (a,b,t)")
            self.label_y.setText("Y (a,b,t)")
        self.lpolar.setChecked(self.polar)

    def draw(self):
        if self.debug != 0:
            print(self.draw.__name__)

        import numpy as np
        t = 0.

        fa = str(self.la.text())
        fb = str(self.lb.text())

        a = eval(fa)
        b = eval(fb)

        def iterate():
            if hasattr(a, '__iter__') and hasattr(b, '__iter__'):
                for m_a in a:
                    for m_b in b:
                        if self.debug != 0:
                            print("a=" + str(m_a))
                            print("b=" + str(m_b))
                        self.draw_par_function(m_a, m_b)
            elif hasattr(a, '__iter__') and not hasattr(b, '__iter__'):
                for m_a in a:
                    if self.debug != 0:
                        print("a=" + str(m_a))
                        print("b=" + str(b))
                    self.draw_par_function(m_a, b)
            elif not hasattr(a, '__iter__') and hasattr(b, '__iter__'):
                for m_b in b:
                    if self.debug != 0:
                        print("a=" + str(a))
                        print("b=" + str(m_b))
                    self.draw_par_function(a, m_b)
            else:
                if self.debug != 0:
                    print("a=" + str(a))
                    print("b=" + str(b))
                self.draw_par_function(a, b)

        oxs = eval(str(self.x_ref.text()))
        oys = eval(str(self.y_ref.text()))
        ozs = eval(str(self.z_ref.text()))
        if hasattr(oxs, '__iter__'):
            for m_ox, m_oy, m_oz in zip(oxs, oys, ozs):
                self.ox = float(m_ox)
                self.oy = float(m_oy)
                self.oz = float(m_oz)
                iterate()
        else:
            self.ox = float(eval(str(self.x_ref.text())))
            self.oy = float(eval(str(self.y_ref.text())))
            self.oz = float(eval(str(self.z_ref.text())))
            iterate()

    def draw_par_function(self, fa, fb):
        if self.debug != 0:
            print(self.draw_par_function.__name__)

        fx = str(self.lx.text())
        fy = str(self.ly.text())
        t = float(eval(str(self.ltmin.text())))
        tf = float(eval(str(self.ltmax.text())))
        intt = float(eval(str(self.ltstep.text())))
        # fz   = float(eval(str(self.lz.text())))

        ox, oy, oz = self.ox, self.oy, self.oz

        if intt != 0.:
            d = (tf + intt - t) / intt
        else:
            d = 1
        dmax = int(d)
        matriz = []

        if self.debug != 0:
            print("t=" + str(t) + " to " + str(tf) + " with step of " + str(intt))
            print("d=" + str(d))
            print("a=" + str(fa))
            print("b=" + str(fb))
            print("x=" + str(fx))
            print("y=" + str(fy))
            print("Ref Point:")
            print("x_ref=" + str(ox))
            print("y_ref=" + str(oy))
            print("z_ref=" + str(oz))

        code = """
def f2b(fa,fb,fx,fy,t,i,msgBox):
    value=""
    #msgBox = QtGui.QMessageBox()
    try:
        value="a() = """ + str(fa) + """"
        a=""" + str(fa) + """
        value="b() = """ + str(fb) + """"
        b=""" + str(fb) + """
        value="X() = """ + str(fx) + """"
        fxx=""" + str(fx) + """
        value="Y() = """ + str(fy) + """"
        fyy=""" + str(fy) + """
    except ZeroDivisionError:
        msgBox.setText("Error division by zero in calculus of " +value+" for (t) = " + str(t) + " at " + str(i) +"!")
        msgBox.exec_()
        return
    except Exception as inst:
        print(inst.args)
        msgBox.setText("Error in the formula of " +value+" for (t) = " + str(t) + " at " + str(i) +"!")
        msgBox.exec_()
        return

    return fxx, fyy
        """
        if self.debug != 0:
            print(code)
        try:
            exec(code, globals())
        except Exception as inst:
            print(inst.args)
            import traceback
            var = traceback.format_exc()
            self.msgBox.setText("Error in the code:\n" +
                                str(var)
                                )
            self.msgBox.exec_()
            return

        NbPoles = len(range(dmax))

        x, y, z = 0.0, 0.0, 0.0

        for i in range(dmax):
            step = int((i * 100) / NbPoles)
            self.pbar.setValue(step)

            fxx, fyy = f2b(fa, fb, fx, fy, t, i, self.msgBox)

            if self.polar is True:
                x, y, z = ox + (fxx * cos(fyy)), oy + (fxx * sin(fyy)), oz
                # matriz.append(FreeCAD.Vector(fxx*cos(fyy),fxx*sin(fyy),fz))
            else:
                x, y, z = ox + fxx, oy + fyy, oz
                # matriz.append(FreeCAD.Vector(fxx,fxx,fz))

            matriz.append(FreeCAD.Vector(x, y, z))
            t += intt

        self.plot_matriz(matriz, self.name.text())

    def draw_old(self):
        if self.debug != 0:
            print(self.draw_old.__name__)

        fa = str(self.la.text())
        fb = str(self.lb.text())
        fx = str(self.lx.text())
        fy = str(self.ly.text())
        t = float(eval(str(self.ltmin.text())))
        tf = float(eval(str(self.ltmax.text())))
        intt = float(eval(str(self.ltstep.text())))

        if intt != 0.:
            d = (tf + intt - t) / intt
        else:
            d = 1
        dmax = int(d)
        matriz = []

        if self.debug != 0:
            print("t=" + str(t) + " to " + str(tf) + " with step of " + str(intt))
            print("d=" + str(d))
            print("a=" + str(fa))
            print("b=" + str(fb))
            print("x=" + str(fx))
            print("y=" + str(fy))

        code = """
def f2(fa,fb,fx,fy,t,i):
    value=""
    msgBox = QtGui.QMessageBox()
    try:
        value="a() = """ + str(fa) + """"
        a=""" + str(fa) + """
        value="b() = """ + str(fb) + """"
        b=""" + str(fb) + """
        value="X() = """ + str(fx) + """"
        fxx=""" + str(fx) + """
        value="Y() = """ + str(fy) + """"
        fyy=""" + str(fy) + """
    except ZeroDivisionError:
        msgBox.setText("Error division by zero in calculus of " +value+" for (t) = " + str(t) + " at " + str(i) +"!")
        msgBox.exec_()
        return
    except Exception as inst:
        print(inst.args)
        msgBox.setText("Error in the formula of " +value+" for (t) = " + str(t) + " at " + str(i) +"!")
        msgBox.exec_()
        return

    return fxx, fyy
        """

        if self.debug != 0:
            print(code)

        exec(code, globals())

        for i in range(dmax):
            fxx, fyy = f2(fa, fb, fx, fy, t, i)
            if self.polar is True:
                matriz.append(FreeCAD.Vector(fxx * cos(fyy), fxx * sin(fyy), 0.0))
            else:
                matriz.append(FreeCAD.Vector(fxx, fyy, 0.0))
            t += intt

        self.plot_matriz(matriz, self.name.text())

# ==============================================================================
#         for i in range(int(d)):
#             try:
#                 value="a"
#                 a=eval(fa)
#                 value="b"
#                 b=eval(fb)
#                 value="X"
#                 fxx=eval(fx)
#                 value="Y"
#                 fyy=eval(fy)
#                 #print fxx,fyy
#             except ZeroDivisionError:
#                 msgBox.setText("Error division by zero in calculus of " +value+"() for t=" + str(t) + " !")
#                 msgBox.exec_()
#             except:
#                 msgBox.setText("Error in the formula of " +value+"() !")
#                 msgBox.exec_()
#
#             if self.polar is True:
#                 matriz.append(FreeCAD.Vector(fxx*cos(fyy),fxx*sin(fyy),0.0))
#             else:
#                 matriz.append(FreeCAD.Vector(fxx,fyy,0.0))
#             t+=intt
# ==============================================================================

    def store(self):
        """ Store the parametric curve.
        """
        if self.debug != 0:
            print(self.store.__name__)
        m_line = []
        m_items = [self.name, self.la, self.lb, self.lx, self.ly,
                   self.ltmin, self.ltmax, self.ltstep, ]

        for m_item in m_items:
            m_val = ""
            m_val = m_item.text()
            m_line.append(str(m_val))
        if self.polar:
            m_line.append("1")
        else:
            m_line.append("0")
        # append comment
        m_line.append("")
        print(str(m_line))
        self.dialog.ui.addCurveData(m_line)


class ParametricCurve3D(Parametric):
    """ A ParametricCurve3D object
    """
    def __init__(self, gui):
        Parametric.__init__(self, gui)

        self.name = self.gui.ParCurve_name_3
        self.la = self.gui.ParCurve_a_3
        self.lb = self.gui.ParCurve_b_3
        self.lc = self.gui.ParCurve_c_3
        self.label_x = self.gui.label_x_3
        self.lx = self.gui.ParCurve_x_3
        self.label_y = self.gui.label_y_3
        self.ly = self.gui.ParCurve_y_3
        self.label_z = self.gui.label_z_3
        self.lz = self.gui.ParCurve_z_3
        self.ltmin = self.gui.ParCurve_tmin_3
        self.ltmax = self.gui.ParCurve_tmax_3
        self.ltstep = self.gui.ParCurve_tstep_3

        self.lcylind = self.gui.checkBox_cylind_3
        self.lspheri = self.gui.checkBox_spheric_3

        self.combox = self.gui.ParCurve_comboBox_3

        self.dialog = QtGui.QDialog()
        self.dialog.resize(280, 110)
        self.dialog.setWindowTitle("3D Parametric Curve Editor")
        self.dialog.ui = ParCurveEdit.tableWidget3D(database="Parametric3D.dat")
        self.dialog.ui.setupUi(self.dialog, self.combox)

    def updateOptions(self):
        if self.cylind:
            self.spheri = False

            self.label_x.setText("Rho (a,b,c,t)")
            self.label_y.setText("Phi (a,b,c,t)")
            self.label_z.setText("Z (a,b,c,t)")
        elif self.spheri:
            self.cylind = False

            self.label_x.setText("Rho (a,b,c,t)")
            self.label_y.setText("Theta (a,b,c,t)")
            self.label_z.setText("Phi (a,b,c,t)")
        else:
            self.cylind = False
            self.spheri = False
            self.label_x.setText("X (a,b,c,t)")
            self.label_y.setText("Y (a,b,c,t)")
            self.label_z.setText("Z (a,b,c,t)")

        self.lcylind.setChecked(self.cylind)
        self.lspheri.setChecked(self.spheri)

    def select_curve(self, *argc):
        """ Selection of Curve by combo box.
        """
        if self.debug != 0:
            print(self.select_curve.__name__)

        m_line = self.dialog.ui.selectCurve(*argc)
        if self.debug != 0:
            print(str(m_line))
        self.name.setText(str(m_line[0]))
        self.la.setText(str(m_line[1]))
        self.lb.setText(str(m_line[2]))
        self.lc.setText(str(m_line[3]))
        self.lx.setText(str(m_line[4]))
        self.ly.setText(str(m_line[5]))
        self.lz.setText(str(m_line[6]))
        self.ltmin.setText(str(m_line[7]))
        self.ltmax.setText(str(m_line[8]))
        self.ltstep.setText(str(m_line[9]))
        self.resetOrigin()
        m_cartcylindspheric = int(str(m_line[10]))

        self.cylind = False
        self.spheri = False
        if m_cartcylindspheric == 1:
            print(str(m_cartcylindspheric))
            self.cylind = True
            self.spheri = False
        if m_cartcylindspheric == 2:
            print(str(m_cartcylindspheric))
            self.cylind = False
            self.spheri = True

        if self.cylind:
            self.label_x.setText("Rho (a,b,c,t)")
            self.label_y.setText("Phi (a,b,c,t)")
            self.label_z.setText("Z (a,b,c,t)")
        else:
            self.label_x.setText("X (a,b,c,t)")
            self.label_y.setText("Y (a,b,c,t)")
            self.label_z.setText("Z (a,b,c,t)")

        if self.spheri:
            self.label_x.setText("Rho (a,b,c,t)")
            self.label_y.setText("Theta (a,b,c,t)")
            self.label_z.setText("Phi (a,b,c,t)")
        else:
            self.label_x.setText("X (a,b,c,t)")
            self.label_y.setText("Y (a,b,c,t)")
            self.label_z.setText("Z (a,b,c,t)")

        self.lcylind.setChecked(self.cylind)
        self.lspheri.setChecked(self.spheri)

    def draw(self):
        if self.debug != 0:
            print(self.draw.__name__)

        import numpy as np
        t = 0.

        fa = str(self.la.text())
        fb = str(self.lb.text())
        fc = str(self.lc.text())

        a = eval(fa)
        b = eval(fb)
        c = eval(fc)

        def iterate():
            def printABC(m_a, m_b, m_c):
                print("a=" + str(m_a))
                print("b=" + str(m_b))
                print("c=" + str(m_c))

            if hasattr(a, '__iter__') and hasattr(b, '__iter__') and hasattr(c, '__iter__'):
                for m_a in a:
                    for m_b in b:
                        for m_c in c:
                            if self.debug != 0:
                                printABC(m_a, m_b, m_c)
                            self.draw_par_function(m_a, m_b, m_c)
            elif hasattr(a, '__iter__') and hasattr(b, '__iter__') and not hasattr(c, '__iter__'):
                for m_a in a:
                    for m_b in b:
                        if self.debug != 0:
                            printABC(m_a, m_b, c)
                        self.draw_par_function(m_a, m_b, c)
            elif hasattr(a, '__iter__') and not hasattr(b, '__iter__') and hasattr(c, '__iter__'):
                for m_a in a:
                    for m_c in c:
                        if self.debug != 0:
                            printABC(m_a, b, m_c)
                        self.draw_par_function(m_a, b, m_c)
            elif not hasattr(a, '__iter__') and hasattr(b, '__iter__') and hasattr(c, '__iter__'):
                for m_b in b:
                    for m_c in c:
                        if self.debug != 0:
                            printABC(a, m_b, m_c)
                        self.draw_par_function(a, m_b, m_c)
            elif not hasattr(a, '__iter__') and not hasattr(b, '__iter__') and hasattr(c, '__iter__'):
                for m_c in c:
                    if self.debug != 0:
                        printABC(a, b, m_c)
                    self.draw_par_function(a, b, m_c)
            elif hasattr(a, '__iter__') and not hasattr(b, '__iter__') and not hasattr(c, '__iter__'):
                for m_a in a:
                    if self.debug != 0:
                        printABC(m_a, b, c)
                    self.draw_par_function(m_a, b, c)
            elif not hasattr(a, '__iter__') and hasattr(b, '__iter__') and not hasattr(c, '__iter__'):
                for m_b in b:
                    if self.debug != 0:
                        printABC(a, m_b, c)
                    self.draw_par_function(a, m_b, c)
            else:
                if self.debug != 0:
                    printABC(a, b, c)
                self.draw_par_function(a, b, c)

        oxs = eval(str(self.x_ref.text()))
        oys = eval(str(self.y_ref.text()))
        ozs = eval(str(self.z_ref.text()))
        if hasattr(oxs, '__iter__'):
            for m_ox, m_oy, m_oz in zip(oxs, oys, ozs):
                self.ox = float(m_ox)
                self.oy = float(m_oy)
                self.oz = float(m_oz)
                iterate()
        else:
            self.ox = float(eval(str(self.x_ref.text())))
            self.oy = float(eval(str(self.y_ref.text())))
            self.oz = float(eval(str(self.z_ref.text())))
            iterate()

    def draw_par_function(self, fa, fb, fc):
        if self.debug != 0:
            print(self.draw.__name__)

        fx = str(self.lx.text())
        fy = str(self.ly.text())
        fz = str(self.lz.text())
        t = float(eval(str(self.ltmin.text())))
        tf = float(eval(str(self.ltmax.text())))
        intt = float(eval(str(self.ltstep.text())))

        ox, oy, oz = self.ox, self.oy, self.oz

        d = (tf + intt - t) / intt
        dmax = int(d)
        matriz = []

        if self.debug != 0:
            print("t=" + str(t) + " to " + str(tf) + " with step of " + str(intt))
            print("d=" + str(d))
            print("a=" + str(fa))
            print("b=" + str(fb))
            print("c=" + str(fc))
            print("x=" + str(fx))
            print("y=" + str(fy))
            print("z=" + str(fz))
            print("Ref Point:")
            print("x_ref=" + str(ox))
            print("y_ref=" + str(oy))
            print("z_ref=" + str(oz))

        code = """
def f3b(fa,fb,fc,fx,fy,fz,t,i,msgBox):
    value=""
    #msgBox = QtGui.QMessageBox()
    try:
        value="a() = """ + str(fa) + """"
        a=""" + str(fa) + """
        value="b() = """ + str(fb) + """"
        b=""" + str(fb) + """
        value="c() = """ + str(fc) + """"
        c=""" + str(fc) + """
        value="X() = """ + str(fx) + """"
        fxx=""" + str(fx) + """
        value="Y() = """ + str(fy) + """"
        fyy=""" + str(fy) + """
        value="Z() = """ + str(fz) + """"
        fzz=""" + str(fz) + """
    except ZeroDivisionError:
        msgBox.setText("Error division by zero in calculus of " +value+" for (t) = " + str(t) + " !")
        msgBox.exec_()
        return
    except Exception as inst:
        print(inst.args)
        msgBox.setText("Error in the formula of " +value+" for (t) = " + str(t) + " !")
        msgBox.exec_()
        return
    return fxx, fyy, fzz
        """
        if self.debug != 0:
            print(code)
        try:
            exec(code, globals())
        except Exception as inst:
            print(inst.args)
            import traceback
            var = traceback.format_exc()
            self.msgBox.setText("Error in the code:\n" +
                                str(var)
                                )
            self.msgBox.exec_()
            return

        NbPoles = len(range(dmax))

        x, y, z = 0.0, 0.0, 0.0

        for i in range(dmax):
            step = int((i * 100) / NbPoles)
            self.pbar.setValue(step)

            fxx, fyy, fzz = f3b(fa, fb, fc, fx, fy, fz, t, i, self.msgBox)

            if self.cylind is True:
                x, y, z = ox + (fxx * cos(fyy)), oy + (fxx * sin(fyy)), oz + fzz
                # matriz.append(FreeCAD.Vector(fxx*cos(fyy),fxx*sin(fyy),fzz))
            if self.spheri is True:
                x, y, z = ox + (fxx * sin(fyy) * cos(fzz)), oy + (fxx * sin(fyy) * sin(fzz)), oz + (fxx * cos(fyy))
                # matriz.append(FreeCAD.Vector(fxx*sin(fyy)*cos(fzz),fxx*sin(fyy)*sin(fzz),fxx*cos(fyy)))
            else:
                x, y, z = ox + fxx, oy + fyy, oz + fzz
                # matriz.append(FreeCAD.Vector(fxx,fyy,fzz))

            matriz.append(FreeCAD.Vector(x, y, z))

            t += intt
        self.plot_matriz(matriz, self.name.text())

    def draw_old(self):
        if self.debug != 0:
            print(self.draw.__name__)
        msgBox = QtGui.QMessageBox()
        fa = str(self.la.text())
        fb = str(self.lb.text())
        fc = str(self.lc.text())
        fx = str(self.lx.text())
        fy = str(self.ly.text())
        fz = str(self.lz.text())
        t = float(eval(str(self.ltmin.text())))
        tf = float(eval(str(self.ltmax.text())))
        intt = float(eval(str(self.ltstep.text())))

        d = (tf + intt - t) / intt
        dmax = int(d)
        matriz = []

        if self.debug != 0:
            print("t=" + str(t) + " to " + str(tf) + " with step of " + str(intt))
            print("d=" + str(d))
            print("a=" + str(fa))
            print("b=" + str(fb))
            print("c=" + str(fc))
            print("x=" + str(fx))
            print("y=" + str(fy))
            print("z=" + str(fz))

        code = """
def f3(fa,fb,fc,fx,fy,fz,t,i):
    value=""
    msgBox = QtGui.QMessageBox()
    try:
        value="a() = """ + str(fa) + """"
        a=""" + str(fa) + """
        value="b() = """ + str(fb) + """"
        b=""" + str(fb) + """
        value="c() = """ + str(fc) + """"
        c=""" + str(fc) + """
        value="X() = """ + str(fx) + """"
        fxx=""" + str(fx) + """
        value="Y() = """ + str(fy) + """"
        fyy=""" + str(fy) + """
        value="Z() = """ + str(fz) + """"
        fzz=""" + str(fz) + """
    except ZeroDivisionError:
        msgBox.setText("Error division by zero in calculus of " +value+" for (t) = " + str(t) + " !")
        msgBox.exec_()
        return
    except Exception as inst:
        print(inst.args)
        msgBox.setText("Error in the formula of " +value+" for (t) = " + str(t) + " !")
        msgBox.exec_()
        return
    return fxx, fyy, fzz
        """
# ==============================================================================
#         for i in range(int(d)):
#             try:
#               value="a"
#               a=eval(fa)
#               value="b"
#               b=eval(fb)
#               value="c"
#               c=eval(fc)
#               value="X"
#               fxx=eval(fx)
#               value="Y"
#               fyy=eval(fy)
#               value="Z"
#               fzz=eval(fz)
#             except ZeroDivisionError:
#               msgBox.setText("Error division by zero in calculus of " +value+"() for t=" + str(t) + " !")
#               msgBox.exec_()
#             except:
#               msgBox.setText("Error in the formula of " +value+"() !")
#               msgBox.exec_()
#             matriz.append(FreeCAD.Vector(fxx,fyy,fzz))
#             t+=intv
# ==============================================================================

        if self.debug != 0:
            print(code)
        exec(code, globals())
        for i in range(dmax):
            fxx, fyy, fzz = f3(fa, fb, fc, fx, fy, fz, t, i)

            if self.cylind is True:
                matriz.append(FreeCAD.Vector(fxx * cos(fyy), fxx * sin(fyy), fzz))
            if self.spheri is True:
                matriz.append(FreeCAD.Vector(fxx * sin(fyy) * cos(fzz), fxx * sin(fyy) * sin(fzz), fxx * cos(fyy)))
            else:
                matriz.append(FreeCAD.Vector(fxx, fyy, fzz))
            t += intt
        self.plot_matriz(matriz, self.name.text())

    def store(self):
        """ Store the parametric curve.
        """
        if self.debug != 0:
            print(self.store.__name__)
        m_line = []
        m_cartesian = 0
        if self.cylind is True:
            m_cartesian = 1
        if self.spheri is True:
            m_cartesian = 2

        m_items = [self.name, self.la, self.lb, self.lc, self.lx, self.ly, self.lz,
                   self.ltmin, self.ltmax, self.ltstep]
        for m_item in m_items:
            m_val = ""
            m_val = m_item.text()
            m_line.append(str(m_val))
        # cartesian append
        m_line.append(str(m_cartesian))
        # append comment
        m_line.append("")
        print(str(m_line))
        self.dialog.ui.addCurveData(m_line)


class Surface(Parametric):
    """ A Surface object
    """
    def __init__(self, gui):
        # Parent
        Parametric.__init__(self, gui)

        self.debug = 1

        self.nurbs = True

        self.name = "Surface"
        self.name = self.gui.Surf_name
        self.la = self.gui.Surf_a
        self.lb = self.gui.Surf_b
        self.lc = self.gui.Surf_c
        self.lx = self.gui.Surf_x
        self.ly = self.gui.Surf_y
        self.lz = self.gui.Surf_z

        self.lumin = self.gui.Surf_umin
        self.lumax = self.gui.Surf_umax
        self.lustep = self.gui.Surf_ustep
        self.lvmin = self.gui.Surf_vmin
        self.lvmax = self.gui.Surf_vmax
        self.lvstep = self.gui.Surf_vstep

        self.cb_points = self.gui.Surf_points
        self.cb_polyline = self.gui.Surf_polyline
        self.cb_bspline = self.gui.Surf_bspline
        self.cb_bspline_surf = self.gui.Surf_bspline_surf
        self.cb_meshes = self.gui.Surf_meshes
#
#         self.cb_close    = self.gui.checkBox_close_2
#         self.cb_face     = self.gui.checkBox_face_2
#
#         self.cb_face.setEnabled(False)
#         self.close  = False
#         self.face   = False
#
        self.combox = self.gui.Surf_comboBox

        self.dialog = QtGui.QDialog()
        self.dialog.resize(280, 110)
        self.dialog.setWindowTitle("Parametric Surface Editor")
        self.dialog.ui = ParCurveEdit.tableWidgetSurf(database="ParametricSurf.dat")
        self.dialog.ui.setupUi(self.dialog, self.combox)

    def select_surface(self, *argc):
        """ Selection of Surface by combo box.
        """
        if self.debug != 0:
            print(self.select_surface.__name__)
        # Name, a , b (a),c (a,b), X (a,b,c,U,V), Y (a,b,c,U,V), Z (a,b,c,U,V), U min, U max, U step, V min, V max, V step, Comment
        m_line = self.dialog.ui.selectCurve(*argc)
        if self.debug != 0:
            print(str(m_line))
        self.name.setText(str(m_line[0]))
        self.la.setText(str(m_line[1]))
        self.lb.setText(str(m_line[2]))
        self.lc.setText(str(m_line[3]))
        self.lx.setText(str(m_line[4]))
        self.ly.setText(str(m_line[5]))
        self.lz.setText(str(m_line[6]))
        self.resetOrigin()
        self.lumin.setText(str(m_line[7]))
        self.lumax.setText(str(m_line[8]))
        self.lustep.setText(str(m_line[9]))
        self.lvmin.setText(str(m_line[10]))
        self.lvmax.setText(str(m_line[11]))
        self.lvstep.setText(str(m_line[12]))

    def draw(self):
        if self.debug != 0:
            print(self.draw.__name__)

        import numpy as np
        u = 0.
        v = 0.

        fa = str(self.la.text())
        fb = str(self.lb.text())
        fc = str(self.lc.text())
        a = eval(fa)
        b = eval(fb)
        c = eval(fc)

        def iterate():
            def printABC(m_a, m_b, m_c):
                print("a=" + str(m_a))
                print("b=" + str(m_b))
                print("c=" + str(m_c))
            if hasattr(a, '__iter__') and hasattr(b, '__iter__') and hasattr(c, '__iter__'):
                for m_a in a:
                    for m_b in b:
                        for m_c in c:
                            if self.debug != 0:
                                printABC(m_a, m_b, m_c)
                            self.draw_par_function(m_a, m_b, m_c)
            elif hasattr(a, '__iter__') and hasattr(b, '__iter__') and not hasattr(c, '__iter__'):
                for m_a in a:
                    for m_b in b:
                        if self.debug != 0:
                            printABC(m_a, m_b, c)
                        self.draw_par_function(m_a, m_b, c)
            elif hasattr(a, '__iter__') and not hasattr(b, '__iter__') and hasattr(c, '__iter__'):
                for m_a in a:
                    for m_c in c:
                        if self.debug != 0:
                            printABC(m_a, b, m_c)
                        self.draw_par_function(m_a, b, m_c)
            elif not hasattr(a, '__iter__') and hasattr(b, '__iter__') and hasattr(c, '__iter__'):
                for m_b in b:
                    for m_c in c:
                        if self.debug != 0:
                            printABC(a, m_b, m_c)
                        self.draw_par_function(a, m_b, m_c)
            elif not hasattr(a, '__iter__') and not hasattr(b, '__iter__') and hasattr(c, '__iter__'):
                for m_c in c:
                    if self.debug != 0:
                        printABC(a, b, m_c)
                    self.draw_par_function(a, b, m_c)
            elif hasattr(a, '__iter__') and not hasattr(b, '__iter__') and not hasattr(c, '__iter__'):
                for m_a in a:
                    if self.debug != 0:
                        printABC(m_a, b, c)
                    self.draw_par_function(m_a, b, c)
            elif not hasattr(a, '__iter__') and hasattr(b, '__iter__') and not hasattr(c, '__iter__'):
                for m_b in b:
                    if self.debug != 0:
                        printABC(a, m_b, c)
                    self.draw_par_function(a, m_b, c)
            else:
                if self.debug != 0:
                    printABC(a, b, c)
                self.draw_par_function(a, b, c)

        oxs = eval(self.x_ref.text())
        oys = eval(self.y_ref.text())
        ozs = eval(self.z_ref.text())
        if self.debug != 0:
            print(oxs)
            print("oxs=" + str(oxs))
            print("oys=" + str(oys))
            print("ozs=" + str(ozs))

        import collections
        # if hasattr(oxs, '__iter__'):
        if isinstance(oxs, collections.Iterable):
            for m_ox, m_oy, m_oz in zip(oxs, oys, ozs):
                self.ox = float(m_ox)
                self.oy = float(m_oy)
                self.oz = float(m_oz)
                iterate()
        else:
            self.ox = float(eval(str(self.x_ref.text())))
            self.oy = float(eval(str(self.y_ref.text())))
            self.oz = float(eval(str(self.z_ref.text())))
            iterate()

    def draw_par_function(self, fa, fb, fc):
        if self.debug != 0:
            print(self.draw_par_function.__name__)

        import numpy as np

        fx = str(self.lx.text())
        fy = str(self.ly.text())
        fz = str(self.lz.text())

        umin = float(eval(str(self.lumin.text())))
        umax = float(eval(str(self.lumax.text())))
        ustep = float(eval(str(self.lustep.text())))

        vmin = float(eval(str(self.lvmin.text())))
        vmax = float(eval(str(self.lvmax.text())))
        vstep = float(eval(str(self.lvstep.text())))

        ox, oy, oz = self.ox, self.oy, self.oz

        matriz = []

        if self.debug != 0:
            print("umin=" + str(umin) + " to " + str(umax) + " with step of " + str(ustep))
            print("vmin=" + str(vmin) + " to " + str(vmax) + " with step of " + str(vstep))
            print("a=" + str(fa))
            print("b=" + str(fb))
            print("c=" + str(fc))
            print("x=" + str(fx))
            print("y=" + str(fy))
            print("z=" + str(fz))

        code = """
def f3b(fa,fb,fc,fx,fy,fz,u,v,msgBox):
    value=""
    try:
        value="a() = """ + str(fa) + """"
        a=""" + str(fa) + """
        value="b() = """ + str(fb) + """"
        b=""" + str(fb) + """
        value="c() = """ + str(fc) + """"
        c=""" + str(fc) + """
        value="X() = """ + str(fx) + """"
        fxx=""" + str(fx) + """
        value="Y() = """ + str(fy) + """"
        fyy=""" + str(fy) + """
        value="Z() = """ + str(fz) + """"
        fzz=""" + str(fz) + """
    except ZeroDivisionError:
        msgBox.setText("Error division by zero in calculus of " +value+" for (u,v) = " + str(u) + "," + str(v) + " !")
        msgBox.exec_()
        return
    except Exception as inst:
        print(inst.args)
        msgBox.setText("Error in the formula of " +value+" for (u,v) = " + str(u) + "," + str(v) + " !")
        msgBox.exec_()
        return
    return fxx, fyy, fzz
        """

        if self.debug != 0:
            print(code)
        try:
            exec(code, globals())
        except Exception as inst:
            print(inst.args)
            import traceback
            var = traceback.format_exc()
            self.msgBox.setText("Error in the code:\n" +
                                str(var)
                                )
            self.msgBox.exec_()
            return

        x, y, z = 0.0, 0.0, 0.0

        NbUPoles = len(np.arange(umin, umax, ustep))
        NbVPoles = len(np.arange(vmin, vmax, vstep))
        step = 0
        i = 0

        if self.debug != 0:
            print("Step = " + str(step))
            print("NbVPoles = " + str(NbUPoles))
            print("NbVPoles = " + str(NbVPoles))

        ps = []
        # for u in np.arange(umin,umax,ustep):
        for v in np.arange(vmin, vmax, vstep):
            i += 1
            step = int((i * 100) / NbVPoles)
            # print str(step)
            self.pbar.setValue(step)
            psl = []
            # for v in np.arange(vmin,vmax,vstep):
            for u in np.arange(umin, umax, ustep):
                fxx, fyy, fzz = f3b(fa, fb, fc, fx, fy, fz, u, v, self.msgBox)
                x, y, z = ox + fxx, oy + fyy, oz + fzz
                matriz.append(FreeCAD.Vector(x, y, z))
                psl.append(FreeCAD.Vector(x, y, z))
            ps.append(psl)

        if not (self.nurbs or self.meshes):
            self.plot_matriz(matriz, self.name.text())

        else:
            bs = Part.BSplineSurface()

            kv = [1.0 / (NbVPoles - 1) * i for i in range(NbVPoles)]
            ku = [1.0 / (NbUPoles - 1) * i for i in range(NbUPoles)]

            bs.buildFromPolesMultsKnots(ps,
                                        [3] + [1] * (NbVPoles - 2) + [3],
                                        [3] + [1] * (NbUPoles - 2) + [3],
                                        kv,
                                        ku,
                                        False,
                                        False,
                                        3, 3)

            sha = bs.toShape()
            label = str(self.name.text()) + "_Nurbs"
            sp = App.ActiveDocument.addObject("Part::Spline", label)
            sp.Shape = sha
            sp.ViewObject.ControlPoints = False
            sp.ViewObject.ShapeColor = (1.00, 0.67, 0.00)

    def draw_old(self):
        if self.debug != 0:
            print(self.draw.__name__)

        import numpy as np
        u = 0.
        v = 0.

        fa = str(self.la.text())
        fb = str(self.lb.text())
        fc = str(self.lc.text())

        fx = str(self.lx.text())
        fy = str(self.ly.text())
        fz = str(self.lz.text())

        a = eval(fa)
        b = eval(fb)
        c = eval(fc)

        umin = float(eval(str(self.lumin.text())))
        umax = float(eval(str(self.lumax.text())))
        ustep = float(eval(str(self.lustep.text())))

        vmin = float(eval(str(self.lvmin.text())))
        vmax = float(eval(str(self.lvmax.text())))
        vstep = float(eval(str(self.lvstep.text())))

        ox = float(eval(str(self.x_ref.text())))
        oy = float(eval(str(self.y_ref.text())))
        oz = float(eval(str(self.z_ref.text())))

        matriz = []

        if self.debug != 0:
            print("umin=" + str(umin) + " to " + str(umax) + " with step of " + str(ustep))
            print("vmin=" + str(vmin) + " to " + str(vmax) + " with step of " + str(vstep))
            print("a=" + str(fa))
            print("b=" + str(fb))
            print("c=" + str(fc))
            print("x=" + str(fx))
            print("y=" + str(fy))
            print("z=" + str(fz))

        code = """
def f3b(fa,fb,fc,fx,fy,fz,u,v,msgBox):
    value=""
    try:
        value="a() = """ + str(fa) + """"
        a=""" + str(fa) + """
        value="b() = """ + str(fb) + """"
        b=""" + str(fb) + """
        value="c() = """ + str(fc) + """"
        c=""" + str(fc) + """
        value="X() = """ + str(fx) + """"
        fxx=""" + str(fx) + """
        value="Y() = """ + str(fy) + """"
        fyy=""" + str(fy) + """
        value="Z() = """ + str(fz) + """"
        fzz=""" + str(fz) + """
    except ZeroDivisionError:
        msgBox.setText("Error division by zero in calculus of " +value+" for (u,v) = " + str(u) + "," + str(v) + " !")
        msgBox.exec_()
        return
    except Exception as inst:
        print(inst.args)
        msgBox.setText("Error in the formula of " +value+" for (u,v) = " + str(u) + "," + str(v) + " !")
        msgBox.exec_()
        return
    return fxx, fyy, fzz
        """

        if self.debug != 0:
            print(code)
        try:
            exec(code, globals())
        except Exception as inst:
            print(inst.args)
            import traceback
            var = traceback.format_exc()
            self.msgBox.setText("Error in the code:\n" +
                                str(var)
                                )
            self.msgBox.exec_()
            return

        x, y, z = 0.0, 0.0, 0.0

        NbUPoles = len(np.arange(umin, umax, ustep))
        NbVPoles = len(np.arange(vmin, vmax, vstep))
        step = 0
        i = 0

        if self.debug != 0:
            print("Step = " + str(step))
            print("NbVPoles = " + str(NbUPoles))
            print("NbVPoles = " + str(NbVPoles))

        ps = []
        # for u in np.arange(umin,umax,ustep):
        for v in np.arange(vmin, vmax, vstep):
            i += 1
            step = int((i * 100) / NbVPoles)
            # print str(step)
            self.pbar.setValue(step)
            psl = []
            # for v in np.arange(vmin, vmax, vstep):
            for u in np.arange(umin, umax, ustep):
                fxx, fyy, fzz = f3b(fa, fb, fc, fx, fy, fz, u, v, self.msgBox)
                x, y, z = ox + fxx, oy + fyy, oz + fzz
                matriz.append(FreeCAD.Vector(x, y, z))
                psl.append(FreeCAD.Vector(x, y, z))
            ps.append(psl)

        if not (self.nurbs or self.meshes):
            self.plot_matriz(matriz, self.name.text())

        else:
            bs = Part.BSplineSurface()

            kv = [1.0 / (NbVPoles - 1) * i for i in range(NbVPoles)]
            ku = [1.0 / (NbUPoles - 1) * i for i in range(NbUPoles)]

            bs.buildFromPolesMultsKnots(ps,
                                        [3] + [1] * (NbVPoles - 2) + [3],
                                        [3] + [1] * (NbUPoles - 2) + [3],
                                        kv,
                                        ku,
                                        False,
                                        False,
                                        3, 3)

            sha = bs.toShape()
            label = str(self.name.text()) + "_Nurbs"
            sp = App.ActiveDocument.addObject("Part::Spline", label)
            sp.Shape = sha
            sp.ViewObject.ControlPoints = False
            sp.ViewObject.ShapeColor = (1.00, 0.67, 0.00)

# >>> import nurbswb.spreadsheet_lib as ns
# >>> import numpy as np
# >>> x = np.arange(-5.00, 5.00, 0.5)
# >>> y = np.arange(-5.00, 5.00, 0.5)
# >>> xx, yy = np.meshgrid(x, y)
# >>> z = np.sin(xx**2+yy**2)
# >>> ss1=ns.createSpreadsheet(label='MySpreadsheet')
# >>> ns.setSpreadsheet(ss1,x,y,z)
# >>> ns.table2Nurbs(ss1,"waves")

    def store(self):
        """ Store the parametric surface.
        """
        if self.debug != 0:
            print(self.store.__name__)
        m_line = []

        # Name, a , b (a),c (a,b), X (a,b,c,U,V), Y (a,b,c,U,V), Z (a,b,c,U,V), U min, U max, U step, V min, V max, V step, Comment
        m_items = [self.name, self.la, self.lb, self.lc, self.lx, self.ly, self.lz,
                   self.lumin, self.lumax, self.lustep, self.lvmin, self.lvmax, self.lvstep]
        for m_item in m_items:
            m_val = ""
            m_val = m_item.text()
            m_line.append(str(m_val))

        # append comment
        m_line.append("")
        print(str(m_line))
        self.dialog.ui.addCurveData(m_line)


class SurfaceEvents(DefineAndConnectEvents):
    def __init__(self, ui):
        self.ui = ui
        # Create Surface object
        self.surface = Surface(self.ui)
        DefineAndConnectEvents.__init__(self, self.ui, self.surface)

    def defineEvents(self):
        # ======================================================================
        # Connect to 2D functions
        # ======================================================================
        self.connections_for_slider_changed = {}
        self.connections_for_button_pressed = {"Surf_button_edit": "edit",
                                               "Surf_button_apply": "draw",
                                               "Surf_button_store": "store",
                                               "button_select_point": "getOrigin",
                                               }
        self.connections_for_combobox_changed = {"Surf_comboBox": "select_surface",
                                                 }
        self.connections_for_checkbox_toggled = {"Surf_points": "cpointsState",
                                                 "Surf_polyline": "cpolyState",
                                                 "Surf_bspline": "cbsplineState",
                                                 "Surf_bspline_surf": "cnurbsState",
                                                 "Surf_meshes": "cmeshesState",
                                                 }
        self.connections_for_spin_changed = {}  # "Reg2DCurve_degree_select"         :"setDegree"
        self.connections_for_return_pressed = {}


class RegressionCurve2DEvents(DefineAndConnectEvents):
    def __init__(self, ui):
        self.ui = ui
        # Create Regression Curve 2D object
        self.regcurv2D = RegressionCurve2D(self.ui)
        DefineAndConnectEvents.__init__(self, self.ui, self.regcurv2D)

    def defineEvents(self):
        # ======================================================================
        # Connect to 2D functions
        # ======================================================================
        self.connections_for_slider_changed = {}
        self.connections_for_button_pressed = {
                            "Reg2DCurve_button_apply"         :"draw",
                            "Reg2DCurve_button_select_points" :"get_points",
                            }
        self.connections_for_combobox_changed = {
                            #"ParCurve_comboBox_2"            :"select_curve",
                            }
        self.connections_for_checkbox_toggled = {
                            "checkBox_points_reg1"             :"cpointsState",
                            "checkBox_polyline_reg1"           :"cpolyState",
                            "checkBox_bspline_reg1"            :"cbsplineState",
                            "checkBox_bezier_reg1"             :"cbezierState",
                            }
        self.connections_for_spin_changed = {
                            "Reg2DCurve_degree_select"         :"setDegree"}
        self.connections_for_return_pressed = {}


class ParametricCurve2DEvents(DefineAndConnectEvents):
    def __init__(self, ui):
        self.ui = ui
        # Create Parametric Curve 2D object
        self.parcurv2D = ParametricCurve2D(self.ui)
        DefineAndConnectEvents.__init__(self, self.ui, self.parcurv2D)

    def defineEvents(self):
        # ======================================================================
        # Connect to 2D functions
        # ======================================================================
        self.connections_for_slider_changed = {}
        self.connections_for_button_pressed = {
                            "ParCurve_button_edit_2"        :"edit",
                            "ParCurve_button_apply_2"       :"draw",
                            "ParCurve_button_store_2"       :"store",
                            "button_select_point"           :"getOrigin",
                            }
        self.connections_for_combobox_changed = {
                            "ParCurve_comboBox_2"           :"select_curve",
                            }
        self.connections_for_checkbox_toggled = {
                            "checkBox_close_2"              :"ccloseState",
                            "checkBox_face_2"               :"cfaceState",
                            "checkBox_points_2"             :"cpointsState",
                            "checkBox_polyline_2"           :"cpolyState",
                            "checkBox_bspline_2"            :"cbsplineState",
                            "checkBox_bezier_2"             :"cbezierState",
                            "checkBox_polar_2"              :"cpolarState",
                            }
        self.connections_for_spin_changed = {}
        self.connections_for_return_pressed = {}


class ParametricCurve3DEvents(DefineAndConnectEvents):
    def __init__(self, ui):
        self.ui = ui
        # Create Parametric Curve 3D object
        self.parcurv3D = ParametricCurve3D(self.ui)
        DefineAndConnectEvents.__init__(self, self.ui, self.parcurv3D)

    def defineEvents(self):
        # ======================================================================
        # Connect to 3D functions
        # ======================================================================
        self.connections_for_slider_changed = {}
        self.connections_for_button_pressed = {
                            "ParCurve_button_edit_3"          :"edit",
                            "ParCurve_button_apply_3"         :"draw",
                            "ParCurve_button_store_3"         :"store",
                            "button_select_point"             :"getOrigin",
                            }
        self.connections_for_combobox_changed = {
                            "ParCurve_comboBox_3"            :"select_curve",
                            }
        self.connections_for_checkbox_toggled = {
                            "checkBox_close_3"              :"ccloseState",
                            "checkBox_points_3"             :"cpointsState",
                            "checkBox_polyline_3"           :"cpolyState",
                            "checkBox_bspline_3"            :"cbsplineState",
                            "checkBox_bezier_3"             :"cbezierState",
                            "checkBox_cylind_3"             :"ccylindState",
                            "checkBox_spheric_3"            :"csphericState",
                            }
        self.connections_for_spin_changed = {}
        self.connections_for_return_pressed = {}


class ParametricTab():
    def __init__(self, gui, movable=True):
        self.gui = gui
        self.title = myTabName
        self.objname = myObjName

        self.movable = movable
        if self.movable:
            # Look if WF movable tab already exists
            m_mvtab = FreeCADGui.getMainWindow().findChild(QtGui.QDockWidget, str(self.title))
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
            self.ui = self.gui.Ui_Form()
            self.ui.setupUi(self.m_dialog)
            self.m_dialog.setMaximumWidth(400)
        else:
            self.m_tab = self.getComboView(self.m_main)

            if self.m_tab.count() == 2:
                # Create a new fake dialog
                self.m_fake_dialog = QtGui.QDialog()
                self.m_tab.addTab(self.m_fake_dialog, "")
            # Create a new dialog for ParametricTabTab
            self.m_dialog = QtGui.QDialog()
            # Add the dialog in a new tab or focus on it if already exists
            if self.m_tab.count() >= 2:
                for i in range(2, self.m_tab.count()):
                    # if str(self.title) == str(unicode(self.m_tab.tabText(i), 'utf-8')):
                    if str(self.title) == str(_fromUtf8(self.m_tab.tabText(i))):
                        self.m_tab.removeTab(int(i))
                        break

            self.m_tab.addTab(self.m_dialog, str(self.title))

            self.ui = self.gui.Ui_Form()
            self.ui.setupUi(self.m_dialog)
            self.m_tab.setCurrentIndex(3)

        self.connections_for_button_clicked = {"button_quit": "quit_clicked",
                                               }

        for m_key, m_val in self.connections_for_button_clicked.items():
            print_msg("Connecting:" + str(m_key) + " and " + str(m_val))
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("clicked()"), getattr(self, str(m_val)))

        # Create a Regression 2D Curve object and connect
        self.reg_events2D = RegressionCurve2DEvents(self.ui)
        # Create a Parametric 2D Curve object and connect
        self.events2D = ParametricCurve2DEvents(self.ui)
        # Create a Parametric 3D Curve object and connect
        self.events3D = ParametricCurve3DEvents(self.ui)
        # Create a Surface object and connect
        self.surface = SurfaceEvents(self.ui)

        m_text = str(ParametricRelease)
        self.ui.label_release.setText(_translate("Form", m_text, None))

        if self.movable:
            t = FreeCADGui.getMainWindow()
            wf = t.findChild(QtGui.QDockWidget, str(self.objname))
            cv = t.findChild(QtGui.QDockWidget, "Combo View")
            cv.setFeatures(QtGui.QDockWidget.DockWidgetMovable | QtGui.QDockWidget.DockWidgetFloatable | QtGui.QDockWidget.DockWidgetClosable)
            wf.setFeatures(QtGui.QDockWidget.DockWidgetMovable | QtGui.QDockWidget.DockWidgetFloatable | QtGui.QDockWidget.DockWidgetClosable)
            if wf and cv:
                t.tabifyDockWidget(cv, wf)
                print_msg("Tabified done !")
                wf.activateWindow()
                wf.raise_()

        QtCore.QObject.connect(self.ui.button_quit, QtCore.SIGNAL('clicked()'), self.quit_clicked)

    def quit_clicked(self):
        print_msg("quit_clicked !")
        if self.movable:
            self.dw.close()
            self.close()
            print_msg("Close done !")
            return
        else:
            self.m_dialog.close()
            if self.m_tab.count() >= 2:
                for i in range(2, self.m_tab.count()):
                    if str(self.title) == str(_fromUtf8(self.m_tab.tabText(i))):
                        self.m_tab.removeTab(int(i))
                        break

    def getMainWindow(self):
        """ Returns the main window
        """
        # using QtGui.qApp.activeWindow() isn't very reliable because if another
        # widget than the mainwindow is active (e.g. a dialog) the wrong widget
        # is returned
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
        mw = FreeCAD.Gui.getMainWindow()
        layout = QtGui.QVBoxLayout()
        myw = QtGui.QWidget()
        myw.setLayout(layout)

        dw1 = QtGui.QDockWidget(mw)
        dw1.setWindowTitle(str(self.title))
        dw1.setObjectName(str(self.objname))
        dw1.setWidget(myw)

        mw.addDockWidget(QtCore.Qt.RightDockWidgetArea, dw1)
        self.myw = myw
        self.dw = dw1
        layout.mw = mw
        return layout

if __name__ == '__main__':
    myObject = ParametricTab(ParCurveGui)
