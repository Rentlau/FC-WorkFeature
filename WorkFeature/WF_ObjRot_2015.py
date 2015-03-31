# -*- coding: utf-8 -*-
# First two lines to be able to launch with python
import sys
# change this by your own FreeCAD lib path import FreeCAD
if not sys.path.__contains__("/usr/lib/freecad/lib"): 
    sys.path.append("/usr/lib/freecad/lib") 
    
import ObjRotGui_2015 as ObjRotGui
import MY_Functions  as func
global myRelease
myRelease = "2105_02"

import os.path
import math
    
import FreeCAD as App
import FreeCADGui as Gui
from pivy.coin import *
import Part
import Draft
from FreeCAD import Base 

from PySide import QtCore, QtGui

####################################################################################
# Functions
def print_attributes(obj, doc=False):
    """ Print all the attributes of this object and their value """
    __m_type = obj.__class__.__name__
    print '* Attributes print for '+ str(__m_type) + '*'
    for names in dir(obj):
        attr = getattr(obj,names)
        if not callable(attr):
            if doc:
                print names,':',attr
            else:
                print names
                

def print_methods(obj, doc=False):
    """ Print all the methods of this object and their doc string"""
    __m_type = obj.__class__.__name__
    print '\n* Methods print for '+ str(__m_type) + '*'
    for names in dir(obj):
        attr = getattr(obj,names)
        if callable(attr):
            if doc:
                print names,':',attr.__doc__
            else:
                print names
                

def plot_point(Vector_point, part= "Part::Feature", name= "CenterObjects", grp="Rot_Trans"):
    if not(App.ActiveDocument.getObject( grp )):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    point = App.ActiveDocument.addObject( part, name )
    point.Shape = Part.Vertex( Vector_point )
    App.ActiveDocument.getObject( grp ).addObject(point)
    point_User_Name = point.Label                
    Gui.ActiveDocument.getObject( point_User_Name ).PointColor = (1.00,0.67,0.00)
    Gui.ActiveDocument.getObject( point_User_Name ).PointSize = 10.00
    return point_User_Name, point
    
def plot_axis(Vector_A, Vector_B, part= "Part::Feature", name= "Line", grp="Rot_Trans"):
    if not(App.ActiveDocument.getObject( grp )):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)
    axis = App.ActiveDocument.addObject(part, name)
    axis.Shape = Part.makeLine(Vector_A, Vector_B)
    App.ActiveDocument.getObject( grp ).addObject(axis)
    axis_User_Name = axis.Label
    Gui.ActiveDocument.getObject(axis_User_Name).LineColor = (1.00,0.67,0.00)
    Gui.ActiveDocument.getObject(axis_User_Name).PointColor = (1.00,0.67,0.00)    
    return axis_User_Name, axis 

def plot_circle(Radius, Position, Direction, part= "Part::Feature", name= "Line", grp="Rot_Trans"):
    if not(App.ActiveDocument.getObject( grp )):
        App.ActiveDocument.addObject("App::DocumentObjectGroup", grp)    
    circle = App.ActiveDocument.addObject(part, name)
    circle.Shape = Part.makeCircle(Radius, Position, Direction)
    App.ActiveDocument.getObject( grp ).addObject(circle)
    circle_User_Name = circle.Label
    Gui.ActiveDocument.getObject(circle_User_Name).LineColor = (1.00,0.67,0.00)  
    return circle_User_Name, circle     
    

#Print a message on console.   
def print_msg(message):
    """ Print a message on console.
    """
    print message
    App.Console.PrintMessage( message + "\n")    


def minMaxObjectsLimits(objs,info=0):
    """ Return the min and max limits along the 3 Axis for all selected objects
    """
    xmax = xmin = ymax = ymin = zmax = zmin = 0
    if objs == None:
        print_msg("ERROR : objs=None, leaving minMaxObjectsLimits()")
        return xmax, xmin, ymax, ymin, zmax, zmin
        
    m_objs = objs
    m_num = len(m_objs)
    if m_num < 1:
        print_msg("ERROR : len(m_objs) <1 , leaving minMaxObjectsLimits()")
        return xmax, xmin, ymax, ymin, zmax, zmin

    import sys
    if sys.version < '3.0.0':    
        max_val = sys.maxint
        min_val = -sys.maxint - 1
    else:# for python 3.0 use sys.maxsize
        max_val = sys.maxsize
        min_val = -sys.maxsize - 1        
    xmin = ymin = zmin = max_val
    xmax = ymax = zmax = min_val 
    #print_msg(str(xmin))
    #print_msg(str(xmax))
    m_doc=App.activeDocument()
    
    for m_obj in m_objs:
        if hasattr(m_obj, 'TypeId'):
            m_type = m_obj.TypeId
        else:
            m_type = m_obj.Type
        #pm_type = m_obj.TypeId        
        if info != 0:
            print_msg("m_obj        : " + str(m_obj))
            #print_msg("m_obj.Type   : " + str(m_obj.Type))
            #print_msg("m_obj.TypeId : " + str(m_obj.TypeId))
            print_msg("m_obj.TypeId : " + str(m_type))

        #if m_obj.TypeId[:6] == "Length":
        if m_type[:6] == "Length":
            if info != 0:
                print_msg("Found a Length object!")
            box = m_obj.Shape.BoundBox
        #elif m_obj.TypeId[:4] == "Mesh":
        elif m_type[:4] == "Mesh":
            if info != 0:
                print_msg("Found a Mesh object!")
            box = m_obj.Mesh.BoundBox
        #elif m_obj.TypeId[:6] == "Points":
        elif m_type[:6] == "Points":
            if info != 0:
                print_msg("Found a Points object!")
            box = m_obj.Points.BoundBox
        #elif m_obj.TypeId[:4] == "Part":
        elif m_type[:4] == "Part":
            if info != 0:
                print_msg("Found a Part object!")
            box = m_obj.Shape.BoundBox
        #elif m_obj.TypeId[:6] == "Sketch":
        elif m_type[:6] == "Sketch":
            if info != 0:
                print_msg("Found a Sketch object!")
            #box = Draft.draftify(m_obj,delete=False).Shape.BoundBox    
            m_wire = Draft.draftify(m_obj,delete=False)
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
        print_msg("Limits of all objects selected are :")    
        print_msg("xmax =" + str(xmax) + ", "
                  "xmin =" + str(xmin) + ", "
                  "ymax =" + str(ymax) + ", "
                  "ymin =" + str(ymin) + ", "
                  "zmax =" + str(zmax) + ", "
                  "zmin =" + str(zmin))               
    return xmax, xmin, ymax, ymin, zmax, zmin    
    
####################################################################################
# Classes
class Translation():
    """ A translation object
    """
    def __init__(self, gui):
        self.msg        = 1
        self.applied    = False
        self.m_num_obj  = 0
        self.m_selEx    = None
        self.m_objs     = None
        self.m_objs_dup = []
        self.m_transp_dup = []
        self.m_objNames = None
        self.placement0 = []
        self.placement1 = []
        self.names      = []
        self.transparency = []         
        self.center     = None
        self.base       = None
        self.origin     = App.Vector(0,0,0)
        self.gui        = gui
        self.start      = self.origin
        self.end        = []
        self.m_num_end  = 0
        self.end.append(self.origin)
        self.but_select = self.gui.ObjTrans_button_select
        self.but_start  = self.gui.ObjTrans_button_select_start
        self.but_end    = self.gui.ObjTrans_button_select_end

        self.but_reset  = self.gui.ObjTrans_button_reset
        self.but_apply  = self.gui.ObjTrans_button_apply
        
        self.comb_start = self.gui.ObjTrans_comboBox_start
        self.comb_end   = self.gui.ObjTrans_comboBox_end
        self.start_x    = self.gui.ObjTrans_start_x
        self.start_y    = self.gui.ObjTrans_start_y
        self.start_z    = self.gui.ObjTrans_start_z
        self.end_x      = self.gui.ObjTrans_end_x
        self.end_y      = self.gui.ObjTrans_end_y
        self.end_z      = self.gui.ObjTrans_end_z
        self.dupli      = self.gui.ObjTrans_duplicate
        self.dup_num    = self.gui.ObjTrans_spin


        self.valid_start = {  "Origin" : "origin",
                              "Base Obj." : "base",
                              "Center Obj.(s)" : "center",
                              "To select" : "select",
                              "To define" : "define",
                            }
        
        self.visuObjects = []
        
        self.duplicate = False
        self.m_num_cpy = 1
        self.dup_num.setValue(self.m_num_cpy)
        self.dup_num.setEnabled(self.duplicate)
        self.dupli.setCheckState(QtCore.Qt.Unchecked)
        
        self.enable(False)

                
    def enable(self, flag=True):
        """ Enable or not most of the buttons.
        """
        self.comb_start.setEnabled(flag)
        self.but_start.setEnabled(flag)
        self.comb_end.setEnabled(flag)      
        self.but_end.setEnabled(flag)
        self.dupli.setEnabled(flag)
        self.but_reset.setEnabled(flag)
        self.but_apply.setEnabled(flag)
   

    def setEnabledStartInput(self, flag=True):
        """ Enable or not the input boxes for start point.
        """        
        self.start_x.setEnabled(flag)
        self.start_y.setEnabled(flag)
        self.start_z.setEnabled(flag)
        

    def setEnabledEndInput(self, flag=True):
        """ Enable or not the input boxes for end point.
        """ 
        self.end_x.setEnabled(flag)
        self.end_y.setEnabled(flag)
        self.end_z.setEnabled(flag)

    
    def numberCopies(self,value):
        """ Respond to the change in number of part value from the spin box.
        """            
        try:
            # First we check if a valid number have been entered
            if str(value) == '-':
                return
            self.m_num_cpy  = int(value)
        except ValueError:
           func. printError_msg("Number must be valid !")
           
        if self.msg != 0:
            func.print_msg("New copy number is :" + str(self.m_num_cpy))   
        
        if self.m_num_obj >= 1 and self.m_num_cpy >= 1:
            self.reset()
            self.preview()
 
       
    def copyFlag(self, flag):
        """ Respond to the change of duplicate flag.
        """
        if self.msg != 0:
            func.print_msg("copyFlag !")        
        if flag == False:
            self.m_num_cpy = 1
            self.dup_num.setValue(self.m_num_cpy)
        self.duplicate = flag
        self.dup_num.setEnabled(self.duplicate)

        if self.m_num_obj >= 1 and self.m_num_cpy >= 1:
            self.reset()
            self.preview()             

        
    def selection(self):
        """ Check if one object at least is selected.
        """
        if self.m_num_obj < 1:
            func.printError_msg("Select at least one object and click on 'Select Object(s)' button!")
            return False
        return True

        
    def cleanDuplication(self):
        """ Clean the list of Duplicated objects.
        """
        if self.msg != 0:
            func.print_msg("cleanDuplication !")
            
        for m_objdup in self.m_objs_dup:
            if self.msg != 0:
                func.print_msg("Object duplique : " + str(m_objdup))
            App.getDocument(str(App.activeDocument().Name)).removeObject(m_objdup.Name)
        del self.m_objs_dup[:]
        del self.m_transp_dup[:]  
        
        
    def resetDuplication(self):  
        """ Reset the list of Duplicated objects.
        """
        if self.msg != 0:
            func.print_msg("resetDuplication !")
        
        self.cleanDuplication()
        
        self.duplicate = False
        self.m_num_cpy = 1
        self.dup_num.setValue(self.m_num_cpy)
        self.dup_num.setEnabled(self.duplicate)
        self.dupli.setCheckState(QtCore.Qt.Unchecked)

           
    def initialize(self):
        """ Store a copy of original placements for all selected objects
        into internal placement lists.
        """
        if self.msg != 0:
            func.print_msg("initialize !")
            
        if not(App.ActiveDocument.getObject("Rot_Trans")):   
            try:
                App.ActiveDocument.addObject("App::DocumentObjectGroup","Rot_Trans")    
            except:
                printError_msg("Could not Create 'Rot_Trans' Objects Group!")
                    
        # Mimic behavior of toggle button
        # Here we have at least an existing object selected and we clean and unselect
        if self.m_num_obj >= 1:
            #self.set_zero()
            if not self.applied:
                self.reset()
            self.m_num_obj=0           
            button_text = "Select Object(s)"
            self.but_select.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
            self.enable(False)
            self.resetDuplication()
            for m_i in range(len(self.names)):
                Gui.ActiveDocument.getObject( self.names[m_i]).Transparency = self.transparency[m_i]
            self.removeVisu()
            del self.names[:]
            del self.end[:] 
            return
        
        # Here is the normal entrance after objects selection
        self.m_num_obj=0     
        # Get the selected Objects
        self.m_num_obj, self.m_selEx, self.m_objs, self.m_objNames = func.get_InfoObjects(info=0, printError=True)
            
        # Houps! nothing is selected
        if self.m_num_obj < 1:
            #self.set_zero()
            #self.reset()        
            self.m_num_obj=0
            button_text = "Select Object(s)"
            self.but_select.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
            self.enable(False)
            self.resetDuplication()
            for m_i in range(len(self.names)):
                Gui.ActiveDocument.getObject( self.names[m_i]).Transparency = self.transparency[m_i]
            self.removeVisu()
            del self.names[:]
            del self.end[:] 
            return
            
        # Ok some objects are selected let's go
        self.applied = False
        del self.placement0[:]
        del self.placement1[:]
        del self.transparency[:]
        del self.names[:]
        del self.end[:]
        self.m_num_end = 0  
        
        button_text = str(self.m_num_obj) + " Object(s) selected"
        self.enable(True)   
        self.but_select.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
        
        # get placement and transparency for all objects             
        # Placement [Pos=(0,0,0), Yaw-Pitch-Roll=(0,0,0)]
        for m_i in range(self.m_num_obj):            
            self.placement0.append(App.Placement(self.m_objs[m_i].Placement))
            self.placement1.append(App.Placement(self.m_objs[m_i].Placement))
            self.names.append(self.m_objNames[m_i])
            self.transparency.append(Gui.ActiveDocument.getObject( self.names[m_i] ).Transparency)
            # set new transparency
            Gui.ActiveDocument.getObject( self.names[m_i] ).Transparency = 75
        
        if self.msg != 0:   
            func.print_msg("self.placement0[" + str(m_i) + "]=" + str(self.placement0[m_i] ))
            func.print_msg("self.placement0[" + str(m_i) + "].Base=" + str(self.placement0[m_i].Base ))
            func.print_msg("self.placement0[" + str(m_i) + "].Rotation=" + str(self.placement0[m_i].Rotation ))
        
        self.base = self.placement0[0].Base
        self.center = func.centerObjectsPoint(self.m_objs, info=0)
        self.origin = App.Vector(0,0,0)
        
        self.start = None
        self.comb_start.setCurrentIndex(3)
        self.comb_end.setCurrentIndex(3)       

              
        self.visu()
        
        button_text = "Select"
        self.but_start.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
        self.but_end.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
        self.but_start.setEnabled(True)
        self.but_end.setEnabled(True)
        
        self.setEnabledStartInput(False)
        self.setEnabledEndInput(False)
        Gui.Selection.clearSelection()


    def removeVisu(self):
        """ Remove the visualization object.
        """ 
        if self.msg != 0:
            func.print_msg("removeVisu !")
            
        for i in range(len(self.visuObjects)):
            App.getDocument(str(App.activeDocument().Name)).removeObject(self.visuObjects[i])        
        del self.visuObjects[:]

     
    def visu(self):
        """ Set the visualization objects.
        """
        if self.msg != 0:
            func.print_msg("Visu !") 
        
        m_start  = self.start        
        m_base   = self.base
        m_center = self.center
               
        self.removeVisu() 
        if m_start != None:
            point_User_Name, point = plot_point(m_start, name= "Start", grp="Rot_Trans")
            Gui.ActiveDocument.getObject( point_User_Name ).PointColor = (0.0,0.0,1.0)
            Gui.ActiveDocument.getObject( point_User_Name ).PointSize = 10.00
            self.visuObjects.append(point_User_Name)
        if m_base != None:   
            point_User_Name, point = plot_point(m_base, name= "Base", grp="Rot_Trans")
            Gui.ActiveDocument.getObject( point_User_Name ).PointColor = (1.0,0.0,0.0)
            Gui.ActiveDocument.getObject( point_User_Name ).PointSize = 3.00
            self.visuObjects.append(point_User_Name)
        if m_center != None:   
            point_User_Name, point = plot_point(m_center, name= "Base", grp="Rot_Trans")
            Gui.ActiveDocument.getObject( point_User_Name ).PointColor = (0.0,1.0,0.0)
            Gui.ActiveDocument.getObject( point_User_Name ).PointSize = 3.00
            self.visuObjects.append(point_User_Name)
        if self.m_num_end != 0:
            for m_i_end in range(self.m_num_end): 
                point_User_Name, point = plot_point(self.end[m_i_end], name= "End", grp="Rot_Trans")
                Gui.ActiveDocument.getObject( point_User_Name ).PointColor = (1.0,1.0,1.0)
                Gui.ActiveDocument.getObject( point_User_Name ).PointSize = 10.00
                self.visuObjects.append(point_User_Name)
        
        if self.msg != 0:
            self.info()

        
    def info(self):                
        func.print_msg("translation start = " + str(self.start))
        func.print_msg("translation end   = " + str(self.end))

        
    def select_start(self):
        """ Selection of Start point of translation by button.
        """
        if self.msg != 0:
            func.print_msg("Selection of Start point of translation by button !")  
        
        error_msg = "Select one point !"
        
        # Get the selected Objects
        SelectedObjects = func.get_SelectedObjects()
        if SelectedObjects == None:
            func.printError_msg(error_msg)
            return         
        Number_of_Points = SelectedObjects[0]
        if Number_of_Points != 1:
            func.printError_msg(error_msg)
            return
        else:
            Point_List = SelectedObjects[3]
            self.start = Point_List[0].Point
            button_text = "Selected !"
            self.but_start.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))        
            self.visu()

             
    def start_value(self, *argc):
        """ Start point of translation by combo box.
        """
        if self.msg != 0:
            func.print_msg("Start point of translation by combo box !") 
            
        # DeActivate select button 
        self.but_start.setEnabled(False)
        button_text = "Select"
        self.but_start.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
        
        self.setEnabledStartInput(False)        
        if str(*argc) == "To select":
            # Activate select button and wait for selection
            self.but_start.setEnabled(True)
            self.start = None
        elif str(*argc) == "To define":
            # Activate define input boxes and wait for entering values
            self.setEnabledStartInput(True)
            self.start = None
        else:
            button_text = "Select"
            self.but_start.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
            self.but_start.setEnabled(False)
            self.start = getattr(self, str(self.valid_start[str(*argc)]))
            
        self.visu()
   
    def end_value(self, *argc):
        """ End point of translation by combo box.
        """
        if self.msg != 0:
            func.print_msg("End point of translation by combo box !")
        
        # DeActivate select button 
        self.but_end.setEnabled(False)
        button_text = "Select"
        self.but_end.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))             
        
        self.setEnabledEndInput(False)
        del self.end[:]
        self.m_num_end = 0  
        if str(*argc) == "To select":
            # Activate select button and wait for selection
            self.but_end.setEnabled(True)
        elif str(*argc) == "To define":
            # Activate define input boxes and wait for entering values
            self.setEnabledEndInput(True)
        else:
            button_text = "Select"
            self.but_end.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
            self.but_end.setEnabled(False)
            self.end.append(getattr(self, str(self.valid_start[str(*argc)])))
            self.m_num_end = 1
            
        self.visu()
        
    def select_end(self):
        """ Selection of End point(s) of translation by button.
        """
        if self.msg != 0:
            func.print_msg("Selection of End point(s) of translation by button !")
            
        error_msg = "Select at least one point !"
        
        # Get the selected Objects
        SelectedObjects = func.get_SelectedObjects()
        if SelectedObjects == None:
            func.printError_msg(error_msg)
            return        
        Number_of_Points = SelectedObjects[0]
        self.m_num_end = Number_of_Points
        if Number_of_Points == 0:
            func.printError_msg(error_msg)
            return
        else:
            Point_List = SelectedObjects[3]
            # For all the end points
            for m_i_end in range(Number_of_Points):
                self.end.append(Point_List[m_i_end].Point)
            if Number_of_Points == 1:
                button_text = "Selected !"
            else:
                button_text = "Multi Sel !"
            self.but_end.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
            self.visu()
            self.preview()

    
    def preview(self):
        """ Preview the placement.
        """
        if self.msg != 0:
            func.print_msg("Preview the placement !")
            
        if self.selection() == False:
            return
        
        if self.start != None:
            # Possible several end points
            if len(self.end) != 0:
                self.cleanDuplication()
                if self.msg != 0:
                    func.print_msg("Preview the placement of " + str(self.m_num_obj) + " objects !") 
                # loop on the selected objects
                for m_i_obj in range(self.m_num_obj):
                    

                    base1 = self.placement1[m_i_obj].Base
                    rot1 = self.placement1[m_i_obj].Rotation
                    # For all the end points
                    if self.msg != 0:
                        func.print_msg("on " + str(self.m_num_end) + " end pointss !")
                    for m_i_end in range(self.m_num_end):
                        m_move = self.end[m_i_end].sub(self.start)
                        if m_i_end == 0:
                            # First end point
                            if self.duplicate:
                                for m_copy in range(self.m_num_cpy):
                                    # Let's duplicate the Object
                                    m_obj2 = App.activeDocument().copyObject(self.m_objs[m_i_obj])
                                    self.m_objs_dup.append(m_obj2)
                                    self.m_transp_dup.append(self.transparency[m_i_obj])
                                    App.ActiveDocument.getObject("Rot_Trans").addObject(m_obj2)
                                    newplace1 = App.Placement(base1.add(m_move), rot1 )
                                    m_obj2.Placement = newplace1
                                    # Update the move
                                    m_move = m_move.add(self.end[m_i_end].sub(self.start))
                            else:
                                newplace1 = App.Placement(base1.add(m_move), rot1 )
                                self.m_objs[m_i_obj].Placement = newplace1
                                
                        else:
                            # At least a second end point exists so duplication
                            m_obj3 = App.activeDocument().copyObject(self.m_objs[m_i_obj])
                            self.m_objs_dup.append(m_obj3)
                            self.m_transp_dup.append(self.transparency[m_i_obj])
                            if self.duplicate:
                                for m_copy in range(self.m_num_cpy):
                                    # Let's duplicate the Object
                                    m_obj4 = App.activeDocument().copyObject(m_obj3)
                                    self.m_objs_dup.append(m_obj4)
                                    self.m_transp_dup.append(self.transparency[m_i_obj])
                                    App.ActiveDocument.getObject("Rot_Trans").addObject(m_obj4)
                                    newplace1 = App.Placement(base1.add(m_move), rot1 )
                                    m_obj4.Placement = newplace1
                                    # Update the move
                                    m_move = m_move.add(self.end[m_i_end].sub(self.start))
                            else:                                
                                newplace2 = App.Placement(base1.add(m_move), rot1 )
                                m_obj3.Placement = newplace2
                Gui.updateGui()
                if self.msg != 0:
                    func.print_msg("Number of Object dup : " + str(len(self.m_objs_dup)))

        
    def application(self):
        """ Application by saving into internal placements list.
        """
        if self.msg != 0:
            func.print_msg("Apply button pressed !")
        
        if self.selection() == False:
            if self.msg != 0:
                func.print_msg("No selection detected !")
            return
            
        for m_i in range(self.m_num_obj):
            if self.msg != 0:
                self.info()
                func.print_msg("placement old   = " + str(self.placement1[m_i]))
                func.print_msg("base1   = " + str(self.placement1[m_i].Base))
                func.print_msg("placement new   = " + str(self.m_objs[m_i].Placement))
                func.print_msg("base2   = " + str(self.m_objs[m_i].Placement.Base))
            self.placement1[m_i]    = self.m_objs[m_i].Placement
            
        for m_i_dup in range(len(self.m_objs_dup)):
            Gui.ActiveDocument.getObject(self.m_objs_dup[m_i_dup].Name).Transparency = self.m_transp_dup[m_i_dup]
        
        del self.m_objs_dup[:]
        del self.m_transp_dup[:]
        self.applied = True
        self.initialize()

    def reset(self):
        """ Reset to original placement.
        """
        if self.msg != 0:
            func.print_msg("Reset button pressed !")
            
        if self.selection() == False:
            if self.msg != 0:
                func.print_msg("No selection detected !")
            return
                     
        if self.msg != 0:
             func.print_msg("Selection detected !")
             
        for m_i_obj in range(self.m_num_obj):
            self.m_objs[m_i_obj].Placement     = self.placement0[m_i_obj]
        
        self.cleanDuplication()

#==============================================================================
#         self.duplicate = False
#         self.m_num_cpy = 1
#         self.dup_num.setValue(self.m_num_cpy)
#         self.dup_num.setEnabled(self.duplicate)
#         self.dupli.setCheckState(QtCore.Qt.Unchecked)
#         self.end_value("To select") 
#==============================================================================

            
class Rotation():
    """ A rotation object
    """
    def __init__(self, gui):
        self.msg        = 1
        self.m_num      = None
        self.m_selEx    = None
        self.m_objs     = None
        self.m_objNames = None
        # self.placement0 = None Initial Placement
        # Store a copy of the original placement for each object
        self.placement0 = []
        self.placement1 = []
        self.names      = []         
        self.center     = None
        self.base       = None
        self.origin     = App.Vector(0,0,0)
        self.gui        = gui
        #func.print_msg("gui=" + str(self.gui))
        self.but_select = self.gui.ObjRot_button_select
        self.but_center = self.gui.ObjRot_button_select_center
        self.but_axis   = self.gui.ObjRot_button_select_axis
        
        self.but_reset  = self.gui.ObjRot_button_reset
        self.but_apply  = self.gui.ObjRot_button_apply
        
        self.comb_center= self.gui.ObjRot_comboBox_center
        self.comb_axis  = self.gui.ObjRot_comboBox_axis
        
        self.slider     = self.gui.ObjRot_horizontalSlider
        self.angle_edit = self.gui.ObjRot_lineEdit_angle 
        
        self.internal = False
        
        self.valid_center = { "Origin" : "origin",
                              "Base Obj." : "base",
                              "Center Obj.(s)" : "center",
                              "To select" : "select",
                            }

        self.valid_axis = { "X" : App.Vector(1,0,0),
                            "Y" : App.Vector(0,1,0),
                            "Z" : App.Vector(0,0,1),
                            "To select" : "select",
                          }
        self.enable(False)
        self.visuObjects = []

                          
    def enable(self, flag=True):
        self.but_center.setEnabled(flag)
        self.but_reset.setEnabled(flag)
        self.but_apply.setEnabled(flag)
        self.comb_center.setEnabled(flag)
        self.comb_axis.setEnabled(flag)
        self.slider.setEnabled(flag)
        self.angle_edit.setEnabled(flag)

        
    def selection(self):
        """ Check if one object at least is selected.
        """
        if self.m_num < 1:
            func.printError_msg("Select at least one object and click on 'Select Object(s)' button!")
            return False
        return True


    def initialize(self):
        """ Store a copy of original placements for all selected objects
        into internal placements list.
        """
        if self.msg != 0:
            func.print_msg("initialize !")
            
        if not(App.ActiveDocument.getObject("Rot_Trans")):   
            try:
                App.ActiveDocument.addObject("App::DocumentObjectGroup","Rot_Trans")    
            except:
                printError_msg("Could not Create 'Rot_Trans' Objects Group!")
        del self.placement0[:]
        del self.placement1[:]
        
        # Mimic behavior of toggle button
        if self.m_num >= 1:
            self.set_zero()
            self.m_num=0            
            button_text = "Select Object(s)"
            self.but_select.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
            self.enable(False)
            for m_i in range(len(self.names)):
                Gui.ActiveDocument.getObject( self.names[m_i]).Transparency = 0
            self.removeVisu()
            del self.names[:] 
            return
        
        # Get the selected Objects
        self.m_num, self.m_selEx, self.m_objs, self.m_objNames = func.get_InfoObjects()
        button_text = str(self.m_num) + " Object(s) selected"
        self.enable(True)
        xmax, xmin, ymax, ymin, zmax, zmin = minMaxObjectsLimits(self.m_objs,info=0)
        wides = [xmax - xmin,ymax - ymin,zmax - zmin]
        self.wide = max(wides)        
        
        if self.m_num < 1:
            self.set_zero()
            button_text = "Select Object(s)"
            self.but_select.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
            self.enable(False)
            self.removeVisu()
            return
            
        self.but_select.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
                       
        # Placement [Pos=(0,0,0), Yaw-Pitch-Roll=(0,0,0)]
        for m_i in range(self.m_num):
            self.placement0.append(App.Placement(self.m_objs[m_i].Placement))
            self.placement1.append(App.Placement(self.m_objs[m_i].Placement))
            self.names.append(self.m_objNames[m_i])
            Gui.ActiveDocument.getObject( self.names[m_i] ).Transparency = 75
            
        if self.msg != 0:   
            func.print_msg("self.placement0[" + str(m_i) + "]=" + str(self.placement0[m_i] ))
            func.print_msg("self.placement0[" + str(m_i) + "].Base=" + str(self.placement0[m_i].Base ))
            func.print_msg("self.placement0[" + str(m_i) + "].Rotation=" + str(self.placement0[m_i].Rotation ))
        
        self.base = self.placement0[0].Base
        self.center = func.centerObjectsPoint(self.m_objs, info=0)
        self.origin = App.Vector(0,0,0)
        
        self.rot_center = self.center
        self.comb_center.setCurrentIndex(2)
        
        self.rot_axis = App.Vector(1,0,0)
        self.comb_axis.setCurrentIndex(0)

        self.rot_angle = 0.0
        self.set_zero()
        self.visu()
        
        self.but_center.setEnabled(False)
        self.but_axis.setEnabled(False)
        if self.msg != 0:
            self.info()
            
        Gui.Selection.clearSelection()
            
    def removeVisu(self):
        for i in range(len(self.visuObjects)):
            App.getDocument(str(App.activeDocument().Name)).removeObject(self.visuObjects[i])        
        del self.visuObjects[:]
        
   
    def visu(self):
        m_axis = self.rot_axis 
        m_center = self.rot_center
        m_base = self.placement0[0].Base
        pt_A = m_center    
        #pt_B = m_axis.projectToLine(m_center,m_axis).normalize().multiply(10)
        pt_B = m_center + m_axis.normalize().multiply(self.wide*1.2)
        #pt_C = m_axis.projectToLine(m_center,m_axis.negative()).normalize().multiply(10)
        pt_C = m_center - m_axis.normalize().multiply(self.wide*1.2)
        
        
        self.removeVisu()
        if pt_A != pt_B: 
            axis_User_Name, axis = plot_axis(pt_A, pt_B , name= "Axis1", grp="Rot_Trans")
            self.visuObjects.append(axis_User_Name)
            Gui.ActiveDocument.getObject(axis_User_Name).LineColor = (0.0,0.0,1.0)
        if pt_A != pt_C:
            axis_User_Name, axis = plot_axis(pt_A, pt_C , name= "Axis2", grp="Rot_Trans")
            self.visuObjects.append(axis_User_Name)
            Gui.ActiveDocument.getObject(axis_User_Name).LineColor = (0.0,0.0,1.0)
        if m_center != None and m_axis != None:   
            circle_User_Name, circle = plot_circle(self.wide*1.2, m_center, m_axis)
            self.visuObjects.append(circle_User_Name)
            Gui.ActiveDocument.getObject(circle_User_Name).LineColor = (0.0,0.0,1.0)
        if m_center != None:
            point_User_Name, point = plot_point(m_center, name= "Center", grp="Rot_Trans")
            Gui.ActiveDocument.getObject( point_User_Name ).PointColor = (0.0,1.0,0.0)
            Gui.ActiveDocument.getObject( point_User_Name ).PointSize = 3.00
            self.visuObjects.append(point_User_Name)
        if m_base != None:    
            point_User_Name, point = plot_point(m_base, name= "Base", grp="Rot_Trans")
            Gui.ActiveDocument.getObject( point_User_Name ).PointColor = (1.0,0.0,0.0)
            Gui.ActiveDocument.getObject( point_User_Name ).PointSize = 3.00
            self.visuObjects.append(point_User_Name)
        if m_base != m_center:
            axis_User_Name, axis = plot_axis(m_center, m_base)
            self.visuObjects.append(axis_User_Name)
        if m_base != App.Vector(0,0,0):
            axis_User_Name, axis = plot_axis(App.Vector(0,0,0), m_base)
            self.visuObjects.append(axis_User_Name)
        if m_center != App.Vector(0,0,0):
            axis_User_Name, axis = plot_axis(App.Vector(0,0,0), m_center)
            self.visuObjects.append(axis_User_Name)
        
    def info(self):                
        func.print_msg("rotation        = " + str(App.Rotation(self.rot_axis,self.rot_angle)))
        func.print_msg("rotation center = " + str(self.rot_center))
        func.print_msg("rotation axis   = " + str(self.rot_axis))
        func.print_msg("rotation angle  = " + str(self.rot_angle))

                    
    def select_center(self):
        """ Selection of Center of rotation by button.
        """
        # Get the selected Objects
        Selection = func.get_SelectedObjects()
        error_msg = "Select one point !"

        SelectedObjects = Selection        
        Number_of_Points = SelectedObjects[0]
        if Number_of_Points < 1:
            func.printError_msg(error_msg)
            return
        else:
            Point_List = SelectedObjects[3]
            self.rot_center = Point_List[0].Point
            button_text = "Selected !"
            self.but_center.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
        
        self.visu()
        if self.msg != 0:
            self.info()
        

    def select_axis(self):
        """ Selection of Axis of rotation by button.
        """
        # Get the selected Objects
        Selection = func.get_SelectedObjects()
        error_msg = "Select one axis !"
        
        SelectedObjects = Selection        
        Number_of_Edges = SelectedObjects[1]
        if Number_of_Edges != 1:
            func.printError_msg(error_msg)
        else:
            num, selEx, objs, objNames = func.get_InfoObjects()
            Edge_List = SelectedObjects[4]
            Point_A = Edge_List[0].valueAt(0.0)
            Point_B = Edge_List[0].valueAt(Edge_List[0].Length)
            self.rot_axis = Point_B - Point_A
        
            button_text = "Selected !"
            self.but_axis.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))

        self.visu()
        if self.msg != 0:
            self.info()

        
    def set_zero(self):
        """ Put zero into edit box and on slider.
        """
        self.internal = True
        self.slider.setValue(0.0)
        self.angle_edit.setText(str(0.0))
        self.internal = False

        
    def center_value(self, *argc):
        """ Center of rotation selection by combo box.
        """
        #func.print_msg("New center selected : " + str(*argc))
        # DeActivate select button 
        self.but_center.setEnabled(False)
        button_text = "Select"
        self.but_center.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
        # Reset to zero
        self.set_zero()
        
        if str(*argc) == "To select":
            # Activate select button and wait for selection
            self.but_center.setEnabled(True)
            self.rot_center = None
        else:
            button_text = "Select"
            self.but_center.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
            self.but_center.setEnabled(False)
            self.rot_center = getattr(self, str(self.valid_center[str(*argc)]))
            self.visu()
            
        if self.msg != 0:
            self.info()

        
    def axis_value(self, *argc):
        """ Axis of rotation selection by combo box.
        """
        #func.print_msg("New axis selected : " + str(*argc))
        # DeActivate select button
        self.but_axis.setEnabled(False)
        button_text = "Select"
        self.but_axis.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
        # Reset to zero
        self.set_zero()     
        
        if str(*argc) == "To select":
            # Activate select button and wait for selection
            self.but_axis.setEnabled(True)
            self.rot_axis = None 
        else:
            button_text = "Select"
            self.but_axis.setText(QtGui.QApplication.translate("Form", button_text, None, QtGui.QApplication.UnicodeUTF8))
            self.but_axis.setEnabled(False)
            self.rot_axis = self.valid_axis[str(*argc)]
            self.visu()
            
        if self.msg != 0:
            self.info()

    
    def angle_value_changed(self, value):
        """ Respond to the change in value of a slider, update the text box
        """
        # If the value was changed internally, ignore event.
        if self.internal:
            return
        
        self.angle_edit.setText(str(value))
        self.angle_value_entered()
            
               
    def angle_value_entered(self):
        #if self.msg != 0:
            #func.print_msg("angle_value_entered entered!")       
        try:
            # First we check if a valid number have been entered
            self.rot_angle = float(self.angle_edit.text())
            # Update the slider by internal update
            self.internal = True
            self.slider.setValue(self.rot_angle)
            self.internal = False           
            # Update the view
            self.preview()
        except ValueError:
            func.printError_msg("Angle must be valid number in degrees !")    

               
    def preview(self):
        """ Preview the placement
        """

        if self.selection() == False:return
                
        if self.rot_center != None:
            if self.rot_axis != None:                                  
                for m_i in range(self.m_num):
                    
                    # Resest to original placement
                    self.m_objs[m_i].Placement = self.placement0[m_i]
                                        
                    Draft.rotate(self.m_objs[m_i],self.rot_angle,self.rot_center,self.rot_axis)

            else:
                func.printError_msg("Select an axis of rotation first!")
        else:
            func.printError_msg("Select a center of rotation first!")

                
    def application(self):
        """ Application by saving into internal placements list
        """
        if self.msg != 0:
            func.print_msg("Apply button pressed!")
        if self.selection() == False:return
            
        for m_i in range(self.m_num):
            if self.msg != 0:
                self.info()
                func.print_msg("placement old   = " + str(self.placement1[m_i]))
                func.print_msg("base1   = " + str(self.placement1[m_i].Base))
                func.print_msg("rot1    = " + str(self.placement1[m_i].Rotation))
                func.print_msg("placement new   = " + str(self.m_objs[m_i].Placement))
                func.print_msg("base2   = " + str(self.m_objs[m_i].Placement.Base))
                func.print_msg("rot2   = " + str(self.m_objs[m_i].Placement.Rotation))
            self.placement1[m_i].Base     = self.m_objs[m_i].Placement.Base
            self.placement1[m_i].Rotation = self.m_objs[m_i].Placement.Rotation
        self.set_zero()
            
        
    def reset(self):
        if self.selection() == False:return
            
        if self.msg != 0:
            func.print_msg("Reset button pressed!")
        self.set_zero()
        for m_i in range(self.m_num):
            self.m_objs[m_i].Placement.Base     = self.placement0[m_i].Base
            self.m_objs[m_i].Placement.Rotation = self.placement0[m_i].Rotation


####################################################################################
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

####################################################################################
class ObjectRotationTab():
    def __init__(self):
        # Get main window
        self.m_main = self.getMainWindow()
        
        # Get Tab panel
        self.m_tab = self.getComboView(self.m_main)

        if self.m_tab.count() == 2:
            # Create a new fake dialog
            self.m_fake_dialog = QtGui.QDialog()
            self.m_tab.addTab(self.m_fake_dialog,"")
            
        # Create a new dialog for ObjectRotationTab
        self.m_dialog = QtGui.QDialog()
        # Add the dialog in a new tab or focus on it if already exists
        if self.m_tab.count() >= 2:
            for i in range(2,self.m_tab.count()):
                #func.print_msg (str(isinstance(self.m_tab.tabText(i), unicode)))
                #func.print_msg (str(unicode(self.m_tab.tabText(i), 'utf-8')))
                if "Displacements" == str(_fromUtf8(self.m_tab.tabText(i))):
                    self.m_tab.removeTab(int(i))
                    break
  
        self.m_tab.addTab(self.m_dialog,"Displacements")
        
        self.ui = ObjRotGui.Ui_Form()
        self.ui.setupUi(self.m_dialog)
        self.m_tab.setCurrentIndex(i+1)
        
        # Create a Rotation object
        self.rot = Rotation(self.ui)
        # Create a Translation object
        self.trans = Translation(self.ui)
        
        # Connect to functions
 
                            
        self.connections_for_ObjTrans_button_pressed = {                        
                             "ObjTrans_button_select"         : "initialize",
                             "ObjTrans_button_select_start"   : "select_start",
                             "ObjTrans_button_select_end"     : "select_end",
                             "ObjTrans_button_reset"          : "reset",
                             "ObjTrans_button_apply"          : "application",
                             } 
                                   
        self.connections_for_ObjTrans_combobox_changed = {
                             "ObjTrans_comboBox_start"        : "start_value",
                             "ObjTrans_comboBox_end"          : "end_value",
                            }
                            
        self.connections_for_ObjTrans_checkbox_toggled = { 
                            "ObjTrans_duplicate"              : "copyFlag",
                            }
                
        self.connections_for_ObjTrans_spin_changed = {
                             "ObjTrans_spin"                  : "numberCopies",
                            }
                                           
        self.connections_for_ObjRot_slider_changed = {                    
                             "ObjRot_horizontalSlider"    : "angle_value_changed",
                             }
                             
        self.connections_for_ObjRot_button_pressed = { 
                             "ObjRot_button_select"           : "initialize",
                             "ObjRot_button_select_center"    : "select_center",
                             "ObjRot_button_select_axis"      : "select_axis",
                             "ObjRot_button_reset"            : "reset",
                             "ObjRot_button_apply"            : "application",
                             }
                             
        self.connections_for_ObjRot_combobox_changed = {
                             "ObjRot_comboBox_center"        : "center_value",
                             "ObjRot_comboBox_axis"          : "axis_value",
                            }
                              
        self.connections_for_ObjRot_return_pressed = { 
                             "ObjRot_lineEdit_angle"           : "angle_value_entered",
                             }
                             
        self.connections_for_button_clicked = {
                             "button_quit"               : "quit_clicked", 
                            }
                            
        for m_key, m_val in self.connections_for_button_clicked.items():
            #print_msg( "Connecting : " + str(m_key) + " and " + str(m_val) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("clicked()"),getattr(self,str(m_val))) 
       
        # Connect to Rotation functions 
        for m_key, m_val in self.connections_for_ObjRot_button_pressed.items():
            func.print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.rot, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("pressed()"),getattr(self.rot, str(m_val)))                   
                                           
        for m_key, m_val in self.connections_for_ObjRot_combobox_changed.items():
            print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.rot, str(m_val))) )                            
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")),getattr(self.rot, str(m_val)))     
        
        for m_key, m_val in self.connections_for_ObjRot_slider_changed.items():
            func.print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.rot, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("valueChanged(int)"),getattr(self.rot, str(m_val)))        
        
        for m_key, m_val in self.connections_for_ObjRot_return_pressed.items():
            func.print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.rot, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("returnPressed()"),getattr(self.rot, str(m_val)))
                                   
        # Connect to Translation functions
        for m_key, m_val in self.connections_for_ObjTrans_button_pressed.items():
            func.print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.trans, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("pressed()"),getattr(self.trans, str(m_val)))
                                        
        for m_key, m_val in self.connections_for_ObjTrans_combobox_changed.items():
            print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.trans, str(m_val))) )                            
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")),getattr(self.trans, str(m_val)))     

        for m_key, m_val in self.connections_for_ObjTrans_checkbox_toggled.items():
            #print_msg( "Connecting : " + str(m_key) + " and " + str(m_val) )
            print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.trans, str(m_val))) ) 
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("toggled(bool)")),getattr(self.trans, str(m_val)))  
              

        for m_key, m_val in self.connections_for_ObjTrans_spin_changed.items():
            print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.trans, str(m_val))) ) 
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("valueChanged(int)"),getattr(self.trans, str(m_val))) 

                                   
        self.m_dialog.show()
        m_text=str(myRelease)
        self.ui.label_release.setText(QtGui.QApplication.translate("Form", m_text, None, QtGui.QApplication.UnicodeUTF8))

    def quit_clicked(self): # quit
        #self.m_dialog.hide()
        self.m_dialog.close()
        if self.m_tab.count() >= 2:
            for i in range(2,self.m_tab.count()):
                if "Displacements" == str(_fromUtf8(self.m_tab.tabText(i))):
                    self.m_tab.removeTab(int(i))
                    break 
                
    def getMainWindow(self):
       """ Returns the main window.
       """
       # using QtGui.qApp.activeWindow() isn't very reliable because if another
       # widget than the mainwindow is active (e.g. a dialog) the wrong widget
       # is returned
       toplevel = QtGui.qApp.topLevelWidgets()
       for i in toplevel:
           if i.metaObject().className() == "Gui::MainWindow":
               return i
       raise Exception("No main window found")
       

    def getComboView(self,window):
        """ Returns the main Tab.
        """
        dw=window.findChildren(QtGui.QDockWidget)
        for i in dw:
            if str(i.objectName()) == "Combo View":
                return i.findChild(QtGui.QTabWidget)
        raise Exception("No tab widget found")

       
if __name__ == '__main__':
    myDialog = ObjectRotationTab()
    