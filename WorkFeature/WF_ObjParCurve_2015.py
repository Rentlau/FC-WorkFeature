# -*- coding: utf-8 -*-
"""
"""
from WorkFeature.WF_Utils_2015 import DefineAndConnectEvents
import WorkFeature.WF_ObjParCurveEdit_2015 as ParCurveEdit

import FreeCAD
import FreeCADGui
import Draft
import Part

from PySide import QtGui
from math import *

####################################################################################
# Classes            
class Parametric():
    def __init__(self, gui):
        """ A Parametric object
        """
        self.debug  = 1
        self.close  = False
        self.face   = False
        self.points = False
        self.poly   = True
        self.bspline = False
        self.bezier = False
        self.meshes = False
        self.polar  = False
        
        self.dialog = None
        self.combox = None

        self.gui    = gui


    def updateOptions(self):
        pass        

            
    def ccloseState(self, flag):
        if self.debug != 0:
            print self.ccloseState.__name__
        self.close = flag
        self.updateOptions()
        
        
    def cfaceState(self, flag):
        if self.debug != 0:
            print self.cfaceState.__name__
        self.face = flag
        self.updateOptions()

    
    def cpointsState(self, flag):
        if self.debug != 0:
            print self.cpointsState.__name__
        self.points = flag
        self.updateOptions()
        
            
    def cpolyState(self, flag):
        if self.debug != 0:
            print self.cpolyState.__name__
        self.poly = flag
        self.updateOptions()    

   
    def cbsplineState(self, flag):
        if self.debug != 0:
            print self.cbsplineState.__name__
        self.bspline = flag
        self.updateOptions()
    
    
    def cbezierState(self, flag):
        if self.debug != 0:
            print self.cbezierState.__name__
        self.bezier = flag
        self.updateOptions()   
          

    def cmeshesState (self, flag):
        if self.debug != 0:
            print self.cmeshesState.__name__
        self.meshes = flag
        self.updateOptions()
        
        
    def cpolarState(self, flag):
        if self.debug != 0:
            print self.ccloseState.__name__
        self.polar = flag
        self.updateOptions()


    def plot_matriz_old(self, matriz):
        """ Plot the dataset with different options.
        """
        if self.debug != 0:
            print self.plot_matriz.__name__        
         
        if self.points == True:
            for point in matriz:
                Draft.makePoint(point)
        else:
            curva = Part.makePolygon(matriz)
            if self.bspline == True:
                Draft.makeBSpline(curva,closed=self.close,face=False)
                #Draft.makeBSpline(Draft.makeWire(curva,closed=self.close,face=False),closed=self.close,face=False)
            if self.bezier == True:
                Draft.makeBezCurve(curva,closed=self.close,face=False)
            if self.poly == True:
                Draft.makeWire(curva,closed=self.close,face=False)
                if self.close == True and self.face == True:
                    Draft.upgrade(FreeCADGui.Selection.getSelection(),delete=True)
                    FreeCAD.ActiveDocument.recompute() 
 
    def plot_matriz(self, matriz):
        """ Plot the dataset with different options.
        """
        if self.debug != 0:
            print self.plot_matriz.__name__       
               
        doc = FreeCAD.ActiveDocument
        if doc == None:
            doc = FreeCAD.newDocument()
 
        if self.points == True:
            for point in matriz:
                a = Draft.makePoint(point)
                FreeCAD.ActiveDocument.ActiveObject.Label = str(a.Name)+"_Point_"+str(self.name.text())
        else:
            curva = Part.makePolygon(matriz)
            if self.bspline == True:
                a = Draft.makeBSpline(curva,closed=self.close,face=False)
                FreeCAD.ActiveDocument.ActiveObject.Label = str(a.Name)+"_BSpline_"+str(self.name.text())
            if self.bezier == True:
                a = Draft.makeBezCurve(curva,closed=self.close,face=False)
                FreeCAD.ActiveDocument.ActiveObject.Label = str(a.Name)+"_BezCurve_"+str(self.name.text())
            if self.poly == True:
                a = Draft.makeWire(curva,closed=self.close,face=False)
                FreeCAD.ActiveDocument.ActiveObject.Label = str(a.Name)+"_Wire_"+str(self.name.text())
#             if self.arcs == True:
#                 s=Part.BSplineCurve()
#                 s.interpolate(matriz, True)
#                 s.buildFromPoles(matriz)
#                 #Part.show(s.toShape())
#                 arcs=s.toBiArcs(0.1)
#                 wire=Part.Wire([Part.Edge(i) for i in arcs])
#                 Part.show(wire)
        if self.close == True and self.face == True:
            Draft.upgrade(FreeCADGui.Selection.getSelection(),delete=True)
        FreeCAD.ActiveDocument.recompute()
        FreeCADGui.ActiveDocument.ActiveView.fitAll()
               
    def edit(self):
        """ Launch the edit panel curve.
        """
        if self.debug != 0:
            print self.edit.__name__
    
        self.dialog.show()
#        self.dialog.exec_()

class ParametricCurve2D(Parametric):
    """ A ParametricCurve2D object
    """
    def __init__(self, gui):
        Parametric.__init__(self, gui)        
        
        self.name     = self.gui.ParCurve_name_2
        self.la       = self.gui.ParCurve_a_2
        self.lb       = self.gui.ParCurve_b_2
        self.lx       = self.gui.ParCurve_x_2
        self.ly       = self.gui.ParCurve_y_2
        self.ltmin    = self.gui.ParCurve_tmin_2
        self.ltmax    = self.gui.ParCurve_tmax_2
        self.ltstep   = self.gui.ParCurve_tstep_2
        
        self.lpolar      = self.gui.checkBox_polar_2
        self.cb_points   = self.gui.checkBox_points_2       
        self.cb_polyline = self.gui.checkBox_polyline_2
        self.cb_bspline  = self.gui.checkBox_bspline_2
        self.cb_bezier   = self.gui.checkBox_bezier_2
        
        self.cb_close    = self.gui.checkBox_close_2
        self.cb_face     = self.gui.checkBox_face_2

        self.cb_face.setEnabled(False) 
        self.close  = False
        self.face   = False

        self.combox = self.gui.ParCurve_comboBox_2
        
        self.dialog = QtGui.QDialog()
        self.dialog.resize(280,110)
        self.dialog.setWindowTitle("2D Parametric Curve Editor") 
        self.dialog.ui = ParCurveEdit.tableWidget2D(database="Parametric2D.dat")
        self.dialog.ui.setupUi(self.dialog, self.combox)
    
    
    def updateOptions(self):
        if self.points:
            self.cb_close.setEnabled(False)
            self.cb_face.setEnabled(False)
            self.cb_close.setChecked(False)
            self.cb_face.setChecked(False) 
            self.close  = False
            self.face   = False
        else:
            self.cb_close.setEnabled(True)
            if self.poly and self.close:
                self.cb_face.setEnabled(True)
            else:
                self.cb_face.setEnabled(False)
                self.cb_face.setChecked(False) 
                self.face   = False
                            
       
    def select_curve(self, *argc):
        """ Selection of Curve by combo box.
        """
        if self.debug != 0:
            print self.select_curve.__name__
            
        m_line = self.dialog.ui.selectCurve(*argc)
        if self.debug != 0:
            print str(m_line)
        self.name.setText(str(m_line[0]))   
        self.la.setText(str(m_line[1])) 
        self.lb.setText(str(m_line[2])) 
        self.lx.setText(str(m_line[3])) 
        self.ly.setText(str(m_line[4])) 
        self.ltmin.setText(str(m_line[5])) 
        self.ltmax.setText(str(m_line[6])) 
        self.ltstep.setText(str(m_line[7]))
        m_polar = int(str(m_line[8]))
        if self.debug != 0:
            print str(m_polar)
            print str(self.lpolar)
        self.polar = False
        if m_polar == 1:
            print str(m_polar)
            self.polar = True
        self.lpolar.setChecked(self.polar)
        
    def draw(self):
        if self.debug != 0:
            print self.draw.__name__
            
        msgBox = QtGui.QMessageBox()

        fa = str(self.la.text())
        fb = str(self.lb.text())
        fx = str(self.lx.text())
        fy = str(self.ly.text())
        t    = float(eval(str(self.ltmin.text())))
        tf   = float(eval(str(self.ltmax.text())))
        intt = float(eval(str(self.ltstep.text())))
        
        d = (tf + intt -t)/intt
        dmax = int(d)
        matriz = []
        
        if self.debug != 0:
            print "t=" + str(t) +" to " + str(tf) + " with step of " + str(intt)
            print "d=" + str(d)
            print "a=" + str(fa)
            print "b=" + str(fb)
            print "x=" + str(fx)
            print "y=" + str(fy)
        
        code = """
def f(fa,fb,fx,fy,t):
    value=""
    msgBox = QtGui.QMessageBox()
    try:
        value="a() = """+str(fa)+""""
        a="""+str(fa)+"""
        value="b() = """+str(fb)+""""  
        b="""+str(fb)+"""
        value="X() = """+str(fx)+"""" 
        fxx="""+str(fx)+"""
        value="Y() = """+str(fy)+"""" 
        fyy="""+str(fy)+"""
    except ZeroDivisionError:
        msgBox.setText("Error division by zero in calculus of "+value+" for (t) = "+str(t)+" !")
        msgBox.exec_()
        return
    except:
        msgBox.setText("Error in the formula of "+value+" for (t) = "+str(t)+" !")
        msgBox.exec_()
        return
        
    return fxx, fyy        
        """    
#==============================================================================
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
#                 msgBox.setText("Error division by zero in calculus of "+value+"() for t="+str(t)+" !")
#                 msgBox.exec_()
#             except:
#                 msgBox.setText("Error in the formula of "+value+"() !")
#                 msgBox.exec_()
#                 
#             if self.polar == True:
#                 matriz.append(FreeCAD.Vector(fxx*cos(fyy),fxx*sin(fyy),0.0))
#             else:                
#                 matriz.append(FreeCAD.Vector(fxx,fyy,0.0))
#             t+=intt
#==============================================================================
            
        if self.debug != 0:
            print code
        exec code
        
        for i in range(dmax):
            fxx, fyy = f(fa,fb,fx,fy,t)
            if self.polar == True:
                matriz.append(FreeCAD.Vector(fxx*cos(fyy),fxx*sin(fyy),0.0))
            else:                
                matriz.append(FreeCAD.Vector(fxx,fyy,0.0))
            t+=intt
            
        self.plot_matriz(matriz)


    def store(self):
        """ Store the parametric curve.
        """
        if self.debug != 0:
            print self.store.__name__
        m_line = []
        m_items = [self.name, self.la, self.lb,self.lx, self.ly,
               self.ltmin, self.ltmax, self.ltstep,]

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
        print str(m_line)
        self.dialog.ui.addCurveData(m_line)            


class ParametricCurve3D(Parametric):
    """ A ParametricCurve3D object
    """
    def __init__(self, gui):
        Parametric.__init__(self, gui)

        self.name   = self.gui.ParCurve_name_3
        self.la     = self.gui.ParCurve_a_3
        self.lb     = self.gui.ParCurve_b_3
        self.lc     = self.gui.ParCurve_c_3
        self.lx     = self.gui.ParCurve_x_3
        self.ly     = self.gui.ParCurve_y_3
        self.lz     = self.gui.ParCurve_z_3
        self.ltmin  = self.gui.ParCurve_tmin_3
        self.ltmax  = self.gui.ParCurve_tmax_3
        self.ltstep = self.gui.ParCurve_tstep_3
        
        self.combox = self.gui.ParCurve_comboBox_3

        self.dialog = QtGui.QDialog()
        self.dialog.resize(280,110)
        self.dialog.setWindowTitle("3D Parametric Curve Editor") 
        self.dialog.ui = ParCurveEdit.tableWidget3D(database="Parametric3D.dat")
        self.dialog.ui.setupUi(self.dialog, self.combox)
    

    def select_curve(self, *argc):
        """ Selection of Curve by combo box.
        """
        if self.debug != 0:
            print self.select_curve.__name__
            
        m_line = self.dialog.ui.selectCurve(*argc)
        if self.debug != 0:
            print str(m_line)
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
        

    def draw(self):
        if self.debug != 0:
            print self.draw.__name__
        msgBox = QtGui.QMessageBox()
        fa = str(self.la.text())
        fb = str(self.lb.text())
        fc = str(self.lc.text())
        fx = str(self.lx.text())
        fy = str(self.ly.text())
        fz = str(self.lz.text())
        t    = float(eval(str(self.ltmin.text())))
        tf   = float(eval(str(self.ltmax.text())))
        intt = float(eval(str(self.ltstep.text())))
        
        d = (tf + intt -t)/intt
        dmax = int(d)
        matriz = []

        if self.debug != 0:
            print "t=" + str(t) +" to " + str(tf) + " with step of " + str(intt)
            print "d=" + str(d)
            print "a=" + str(fa)
            print "b=" + str(fb)
            print "c=" + str(fc)
            print "x=" + str(fx)
            print "y=" + str(fy)
            print "z=" + str(fz)
            
        code = """
def f(fa,fb,fc,fx,fy,fz,t):
    value=""
    msgBox = QtGui.QMessageBox()
    try: 
        value="a() = """+str(fa)+""""
        a="""+str(fa)+"""
        value="b() = """+str(fb)+""""  
        b="""+str(fb)+"""
        value="c() = """+str(fc)+""""  
        c="""+str(fc)+"""
        value="X() = """+str(fx)+"""" 
        fxx="""+str(fx)+"""
        value="Y() = """+str(fy)+"""" 
        fyy="""+str(fy)+"""
        value="Z() = """+str(fz)+"""" 
        fzz="""+str(fz)+"""
    except ZeroDivisionError:
        msgBox.setText("Error division by zero in calculus of "+value+" for (t) = "+str(t)+" !")
        msgBox.exec_()
        return  
    except:
        msgBox.setText("Error in the formula of "+value+" for (t) = "+str(t)+" !")
        msgBox.exec_()
        return
    return fxx, fyy, fzz       
        """            
#==============================================================================
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
#               msgBox.setText("Error division by zero in calculus of "+value+"() for t="+str(t)+" !")
#               msgBox.exec_()
#             except:
#               msgBox.setText("Error in the formula of "+value+"() !")
#               msgBox.exec_()
#             matriz.append(FreeCAD.Vector(fxx,fyy,fzz))
#             t+=intv
#==============================================================================            
                
        if self.debug != 0:
            print code
        exec code
        for i in range(dmax):
            fxx, fyy, fzz = f(fa,fb,fc,fx,fy,fz,t)            
            matriz.append(FreeCAD.Vector(fxx,fyy,fzz))
            t+=intt
        self.plot_matriz(matriz)
        
            
    def store(self):
        """ Store the parametric curve.
        """
        if self.debug != 0:
            print self.store.__name__
        m_line = []
        m_items = [self.name, self.la, self.lb, self.lc, self.lx, self.ly, self.lz,
                   self.ltmin, self.ltmax, self.ltstep,]
        for m_item in m_items:
            m_val = ""
            m_val = m_item.text()
            m_line.append(str(m_val))
        # append comment
        m_line.append("") 
        print str(m_line)
        self.dialog.ui.addCurveData(m_line)


class ParametricCurve2DEvents(DefineAndConnectEvents):
    def __init__(self,ui):
        self.ui = ui
        # Create Parametric Curve 2D object
        self.parcurv2D = ParametricCurve2D(self.ui)
        DefineAndConnectEvents.__init__(self, self.ui, self.parcurv2D)

    def defineEvents(self):                               
        #======================================================================
        # Connect to 2D functions
        #======================================================================
        self.connections_for_slider_changed = {}
        self.connections_for_button_pressed = {
                            "ParCurve_button_edit_2"           : "edit",
                            "ParCurve_button_apply_2"          : "draw",
                            "ParCurve_button_store_2"          : "store",
                            }
        self.connections_for_combobox_changed = {
                            "ParCurve_comboBox_2"             : "select_curve",
                            }
        self.connections_for_checkbox_toggled = {
                            "checkBox_close_2"               : "ccloseState",
                            "checkBox_face_2"                : "cfaceState",
                            "checkBox_points_2"              : "cpointsState",
                            "checkBox_polyline_2"            : "cpolyState",
                            "checkBox_bspline_2"             : "cbsplineState",
                            "checkBox_bezier_2"              : "cbezierState",
                            "checkBox_polar_2"               : "cpolarState",
                            }
        self.connections_for_spin_changed = {}
        self.connections_for_return_pressed = {}
        
        
class ParametricCurve3DEvents(DefineAndConnectEvents):
    def __init__(self,ui):
        self.ui = ui
        # Create Parametric Curve 3D object
        self.parcurv3D = ParametricCurve3D(self.ui)
        DefineAndConnectEvents.__init__(self, self.ui, self.parcurv3D)

    def defineEvents(self):                               
        #======================================================================
        # Connect to 3D functions
        #======================================================================
        self.connections_for_slider_changed = {}
        self.connections_for_button_pressed = {
                            "ParCurve_button_edit_3"           : "edit",
                            "ParCurve_button_apply_3"          : "draw",
                            "ParCurve_button_store_3"          : "store",
                            }
        self.connections_for_combobox_changed = {
                            "ParCurve_comboBox_3"             : "select_curve",
                            }
        self.connections_for_checkbox_toggled = {
                            "checkBox_close_3"               : "ccloseState",
                            "checkBox_points_3"              : "cpointsState",
                            "checkBox_polyline_3"            : "cpolyState",
                            "checkBox_bspline_3"             : "cbsplineState",
                            "checkBox_bezier_3"              : "cbezierState",
                            }
        self.connections_for_spin_changed = {}
        self.connections_for_return_pressed = {}

        
if __name__ == '__main__':
    myObject = Parametric(None)