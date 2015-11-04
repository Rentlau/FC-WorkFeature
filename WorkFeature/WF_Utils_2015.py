# -*- coding: utf-8 -*-
"""
"""
import os.path

from PySide import QtCore
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


###############################################################################
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


def  write_text(filename=None, text=None):
    """
    Write the text into an ASCII file.
    
    Return True if success, false if not.
    
    *filename* : (string) full path name.
    
    *text* : (string) the text to write.
    """
    if filename != None and text != None:
        try:
            __m_f=open(filename,'w')
            __m_f.write(text)
            __m_f.close()
            return True
        except:
            print "\nERROR : The file " + str(filename) + \
              " cannot be opened in write mode !"
            return False
    else:
        return False
    
    
def append_text(filename=None,  text=""  ):
    """
    Print/Add text either on screen or on at the end of an existing ASCII text file.
    
    *filename* : (string) full path name.

    *text*  : (string) the text to add at the end of the file.
    """
    if text.__class__.__name__ != 'str': 
        return None
    if filename and os.path.exists(filename):
        try:
            __m_f=open(filename,'r+')
            __m_f.readlines()
            __m_f.write(text+'\n')
            __m_f.close()
        except:
            print "\nERROR : The file " + str(filename) + \
              " can not be opened for append mode !"
            return False
    else:
        print text +'\n'

def read_text_into_list(filename):
    """
    Read the complete ASCII file *filename* (if possible) into a unique 
    list of strings and return the list 
    (or None in case of error).

    Controls are done on *filename*.
    
    *filename* : (string) full path name.
    """         
    if filename and os.path.exists(filename):
        try:
            __m_f=open(filename,'r')
            # read the complete ASCII file if possible into a unique list of strings
            try:
                #m_strings = __m_f.readlines()
                m_strings = __m_f.read().splitlines()
            except:
                __m_f.close()
                print "\nERROR : The file " + str(filename) + \
                  " cannot be fully read !"                    
                return None
            finally:
                __m_f.close()
            __m_f.close()
            return m_strings
        except:
            print "\nERROR : The file " + str(filename) + \
              " cannot be opened in read mode !"
            return None
    else:
        if os.path.exists(filename) == False:
            print "\nERROR : " + str(filename) + " not a valid file !"                  
        return None
    
    
def read_text(filename):
    """
    Read the complete ASCII file *filename* (if possible) into a unique 
    string and return the string 
    (or None in case of error).

    Controls are done on *filename*.
    
    *filename* : (string) full path name.
    """         
    if filename and os.path.exists(filename):
        try:
            __m_f=open(filename,'r')
            # read the complete ASCII file if possible into a unique string
            try:
                m_string = __m_f.read()
            except:
                __m_f.close()
                print "\nERROR : The file " + str(filename) + \
                  " cannot be fully read !"                    
                return None
            finally:
                __m_f.close()
            __m_f.close()
            return m_string
        except:
            print "\nERROR : The file " + str(filename) + \
              " cannot be opened in read mode !"
            return None
    else:
        if os.path.exists(filename) == False:
            print "\nERROR : " + str(filename) + " not a valid file !"                  
        return None

              
###############################################################################                
# Classes
class DefineAndConnectEvents():
    def __init__(self, ui, obj):
        """
        Definition of communications between a Gui and an python Object.
        This class is a base class and must be derived like :
        
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
                                    "ParCurve_button_edit_2"           : "edit",
                                    "ParCurve_button_apply_2"          : "draw",
                                    "ParCurve_button_store_2"          : "store",
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
            #print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("valueChanged(int)"),getattr(self.obj, str(m_val)))
                                   
        for m_key, m_val in self.connections_for_button_pressed.items():
            #print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("pressed()"),getattr(self.obj, str(m_val)))
                    
        for m_key, m_val in self.connections_for_combobox_changed.items():
            #print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )                            
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")),getattr(self.obj, str(m_val)))     

        for m_key, m_val in self.connections_for_checkbox_toggled.items():
            #print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) ) 
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("toggled(bool)")),getattr(self.obj, str(m_val)))  
              
        for m_key, m_val in self.connections_for_spin_changed.items():
            #print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) ) 
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("valueChanged(int)"),getattr(self.obj, str(m_val))) 

        for m_key, m_val in self.connections_for_return_pressed.items():
            #print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("returnPressed()"),getattr(self.obj, str(m_val)))

if __name__ == '__main__':
    myObject = DefineAndConnectEvents(None, None)