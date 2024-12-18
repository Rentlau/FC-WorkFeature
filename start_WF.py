# -*- coding: utf-8 -*-
import sys
import os

# Change this by your own FreeCAD lib path to import FreeCAD
if not sys.path.__contains__("/usr/lib/freecad/lib"):
    sys.path.append("/usr/lib/freecad/lib")


def launchWorkFeature():
    """
    Launch GUI.

    Returns
    -------
    None.

    """
    import WorkFeature.WF as WF
    print()
    print("INFO: WF module path is\n{0:s}".format(os.path.abspath(WF.__file__)))
    print("INFO: WF release is\n{0:s}".format(str(WF.myRelease)))
    WF.myDialog = WF.WorkFeatureTab()


def updatePYTHONPATH(current_path):
    """
    Update PYTHONPATH id needed.

    Parameters
    ----------
    current_path : String
        A path to workfeature directory.

    Returns
    -------
    None.

    """
    # remove file name from the full path name
    m_current_path = os.path.dirname(current_path)
    # check if this path belongs to the PYTHONPATH variable and if not add it
    if not sys.path.__contains__(str(m_current_path)):
        sys.path.append(str(m_current_path))
    if not sys.path.__contains__(str(m_current_path) + os.sep + "WorkFeature"):
        sys.path.append(str(m_current_path) + os.sep + "WorkFeature")


try:
    m_current_path = os.path.realpath(__file__)
    if os.path.islink(m_current_path):
        m_current_path = os.path.realpath(m_current_path)
    updatePYTHONPATH(m_current_path)
    launchWorkFeature()
except ImportError as error:
    print(sys.path)
    print(error.__class__.__name__ + ": " + error.msg)
    try:
        import FreeCAD
        # first check if the path to WorkFeature was set in the preferences
        param = FreeCAD.ParamGet('User parameter:Plugins/workfeature')
        m_current_path = param.GetString('destination', '')
        if not m_current_path:
            # get the path of the current python script
            m_current_path = os.path.realpath(__file__)
            if os.path.islink(m_current_path):
                m_current_path = os.path.realpath(m_current_path)
            m_current_path = os.path.dirname(m_current_path)

        updatePYTHONPATH(m_current_path)
        # retry import now
        try:
            launchWorkFeature()
        except ImportError:
            # we still cannot find WorkFeature. Inform the user
            from PySide import QtGui
            msgBox = QtGui.QMessageBox()
            msgBox.setText("ERROR: Cannot load FreeCAD WorkFeature macro path ! \nCheck the installation !")
            msgBox.exec_()
            print("ERROR:cannot load FreeCAD WorkFeature macro path !")
            print("Check the installation !")

    except ImportError:
        print("ERROR: Cannot load FreeCAD WorkFeature macro path !")
        print("Check the installation !")
