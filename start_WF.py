# -*- coding: utf-8 -*-
import sys
import os.path

# Change this by your own FreeCAD lib path to import FreeCAD
if not sys.path.__contains__("/usr/lib/freecad/lib"): 
    sys.path.append("/usr/lib/freecad/lib")

try:
    # try import
    import WorkFeature.WF_2015 as WF
except:
    try:
        import FreeCAD            
        # first check if the path to WorkFeature was set in the preferences
        param = FreeCAD.ParamGet('User parameter:Plugins/workfeature')
        m_current_path = param.GetString('destination','')
        if not m_current_path:
            # get the path of the current python script    
            m_current_path = os.path.realpath(__file__)
            m_current_path = os.path.dirname(m_current_path)
        # check if this path belongs to the PYTHONPATH variable and if not add it
        if not sys.path.__contains__(str(m_current_path)):
            sys.path.append(str(m_current_path))
        # retry import now
        try:
            import WorkFeature.WF_2015 as WF
        except:
            # we still cannot find WorkFeature. Ask the user
            from PySide import QtGui
            folderDialog = QtGui.QFileDialog.getExistingDirectory(None,QtGui.QApplication.translate("WorkFeature", "Location of your WorkFeature folder", None, QtGui.QApplication.UnicodeUTF8))
            param.SetString('destination',folderDialog)
            m_current_path = param.GetString('destination')
            sys.path.append(str(m_current_path))
            # retry import
            import WorkFeature.WF_2015 as WF
    except:
        print "ERROR:cannot load FreeCAD module...modify line 6 and 7 of this script !!"
        sys.exit(1)
        
WF.myDialog = WF.WorkFeatureTab()
