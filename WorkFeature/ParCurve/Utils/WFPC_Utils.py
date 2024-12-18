#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 07:45:00 2024

@author: laurent
"""
import os
from PySide import QtCore, QtGui
import FreeCAD as App


def gui_infoDialog(msg):
    """Create a simple QMessageBox dialog for info messages."""
    # The first argument indicates the icon used:
    # one of QtGui.QMessageBox.{NoIcon,Information,Warning Critical,Question}
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Information, 'Info:', msg)
    diag.setWindowModality(QtCore.Qt.ApplicationModal)
    diag.exec_()


def gui_errorDialog(msg):
    """Create a simple QMessageBox dialog for error messages."""
    m_script = os.path.basename(os.path.realpath(__file__))
    # The first argument indicates the icon used:
    # one of QtGui.QMessageBox.{NoIcon,Information,Warning Critical,Question}
    diag = QtGui.QMessageBox(QtGui.QMessageBox.Warning,
                             'Error in ' + str(m_script), msg)
    diag.setWindowModality(QtCore.Qt.ApplicationModal)
    diag.exec_()


def print_msg(message):
    """Print a message on console."""
    print(message)
    App.Console.PrintMessage(message + "\n")


def printError_msg(message):
    """Print a ERROR message on console."""
    print(message)
    App.Console.PrintError("\nERROR: " + message)
    try:
        gui_errorDialog(message)
    except Exception as inst:
        print(inst.args)
        App.Console.PrintError("\nERROR: Not able to launch a QT dialog !")
        raise (Exception(message))
