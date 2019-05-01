# -*- coding: utf-8 -*-
from PySide import QtGui


def translate(str1, str2):
    """ function to fix compatibility for
    Macros to be Py3/Qt5 compatible with 0.18 and beyond.
    """
    try:
        QtGui.QApplication.translate(str1, str2, None, QtGui.QApplication.UnicodeUTF8)
    except AttributeError:
        QtGui.QApplication.translate(str1, str2, None, 0)


try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        """ function to fix compatibility for
        Macros to be Py3/Qt5 compatible with 0.18 and beyond.
        """
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:

    def _translate(context, text, disambig):
        """ function to fix compatibility for
        Macros to be Py3/Qt5 compatible with 0.18 and beyond.
        """
        return QtGui.QApplication.translate(context, text, disambig)
