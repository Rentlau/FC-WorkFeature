# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

import FreeCAD as App


def print_msg(message):
    """ Print a message on console.
    """
    print(message)
    App.Console.PrintMessage(message + "\n")


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
            # print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("valueChanged(int)"), getattr(self.obj, str(m_val)))

        for m_key, m_val in self.connections_for_button_pressed.items():
            # print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("pressed()"), getattr(self.obj, str(m_val)))

        for m_key, m_val in self.connections_for_combobox_changed.items():
            # print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), getattr(self.obj, str(m_val)))

        for m_key, m_val in self.connections_for_checkbox_toggled.items():
            # print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL(_fromUtf8("toggled(bool)")), getattr(self.obj, str(m_val)))

        for m_key, m_val in self.connections_for_spin_changed.items():
            # print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("valueChanged(int)"), getattr(self.obj, str(m_val)))

        for m_key, m_val in self.connections_for_return_pressed.items():
            # print_msg( "Connecting : " + str(getattr(self.ui, str(m_key))) + " and " + str(getattr(self.obj, str(m_val))) )
            QtCore.QObject.connect(getattr(self.ui, str(m_key)),
                                   QtCore.SIGNAL("returnPressed()"), getattr(self.obj, str(m_val)))
